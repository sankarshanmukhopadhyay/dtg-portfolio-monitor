from __future__ import annotations
from datetime import datetime, timedelta, timezone
from typing import Any, Callable
import hashlib
import json

from .classify import classify
from .config import ROOT, repositories, rules, report_settings
from .findings import build_findings
from .github import GitHubAPIError, GitHubClient, utc_now
from .intelligence import consolidate

def _iso_cutoff(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat().replace("+00:00", "Z")

def _event_id(repo: str, event_type: str, number_or_sha: str, updated: str) -> str:
    raw = f"{repo}|{event_type}|{number_or_sha}|{updated}".encode()
    return hashlib.sha256(raw).hexdigest()[:24]

def _references(text: str, monitored: list[str], own_repo: str) -> list[str]:
    low = text.lower()
    return sorted(repo for repo in monitored if repo != own_repo and repo.lower() in low)

def _safe_stream(
    repository: str,
    stream: str,
    url: str,
    operation: Callable[[], list[Any]],
    warnings: list[dict[str, Any]],
    ignored_statuses: set[int] | None = None,
) -> list[Any]:
    try:
        return operation()
    except GitHubAPIError as exc:
        if exc.status in (ignored_statuses or set()):
            return []
        warnings.append({
            "repository": repository,
            "stream": stream,
            "status": exc.status,
            "message": str(exc),
            "url": url,
        })
        return []
    except RuntimeError as exc:
        warnings.append({
            "repository": repository,
            "stream": stream,
            "status": None,
            "message": str(exc),
            "url": url,
        })
        return []

def collect(lookback_days: int = 7, client: GitHubClient | None = None) -> list[dict[str, Any]]:
    client = client or GitHubClient.from_environment()
    repo_configs = repositories()
    rule_config = rules()
    monitored = [item["repo"] for item in repo_configs]
    cutoff = _iso_cutoff(lookback_days)
    collected_at = utc_now()
    events: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    for cfg in repo_configs:
        repo = cfg["repo"]
        owner, name = repo.split("/", 1)
        repo_url = f"https://github.com/{repo}"
        try:
            metadata = client.get(f"/repos/{owner}/{name}")
        except GitHubAPIError as exc:
            warnings.append({
                "repository": repo, "stream": "metadata", "status": exc.status,
                "message": str(exc), "url": repo_url,
            })
            continue

        base = {
            "repository": repo,
            "organisation": cfg["organisation"],
            "workstream": cfg["workstream"],
            "repository_role": cfg["role"],
            "repository_lifecycle": cfg["lifecycle"],
            "collected_at": collected_at,
        }
        is_empty = int(metadata.get("size", 0)) == 0
        meta_event = {
            **base,
            "event_type": "repository_snapshot",
            "item_id": str(metadata["id"]),
            "title": metadata.get("description") or repo,
            "body": "",
            "url": metadata["html_url"],
            "occurred_at": metadata.get("updated_at") or collected_at,
            "updated_at": metadata.get("updated_at") or collected_at,
            "pushed_at": metadata.get("pushed_at"),
            "state": "archived" if metadata.get("archived") else ("empty" if is_empty else "active"),
            "is_empty": is_empty,
            "author": metadata.get("owner", {}).get("login"),
            "changed_files": [],
        }
        meta_event["event_id"] = _event_id(repo, meta_event["event_type"], meta_event["item_id"], meta_event["updated_at"])
        events.append(meta_event)

        commits = [] if is_empty else _safe_stream(
            repo, "commits", repo_url,
            lambda: client.paged(f"/repos/{owner}/{name}/commits", {"since": cutoff}, empty_on_status={409}),
            warnings, ignored_statuses={409},
        )
        for item in commits:
            message = item.get("commit", {}).get("message", "")
            event = {
                **base, "event_type": "commit", "item_id": item["sha"],
                "title": message.splitlines()[0] if message else item["sha"][:12],
                "body": message, "url": item["html_url"],
                "occurred_at": item.get("commit", {}).get("author", {}).get("date") or collected_at,
                "updated_at": item.get("commit", {}).get("committer", {}).get("date") or collected_at,
                "state": "committed",
                "author": (item.get("author") or {}).get("login") or item.get("commit", {}).get("author", {}).get("name"),
                "changed_files": [],
            }
            event["event_id"] = _event_id(repo, "commit", item["sha"], event["updated_at"])
            events.append(event)

        pulls = _safe_stream(
            repo, "pull_requests", repo_url,
            lambda: client.paged(f"/repos/{owner}/{name}/pulls", {"state": "all", "sort": "updated", "direction": "desc"}),
            warnings,
        )
        for item in pulls:
            if item["updated_at"] < cutoff:
                continue
            event = {
                **base, "event_type": "pull_request", "item_id": str(item["number"]),
                "title": item.get("title", ""), "body": item.get("body") or "",
                "url": item["html_url"], "occurred_at": item["created_at"],
                "updated_at": item["updated_at"],
                "state": "merged" if item.get("merged_at") else item["state"],
                "author": (item.get("user") or {}).get("login"),
                "changed_files": [],
            }
            event["event_id"] = _event_id(repo, "pull_request", str(item["number"]), item["updated_at"])
            events.append(event)

        issues = _safe_stream(
            repo, "issues", repo_url,
            lambda: client.paged(f"/repos/{owner}/{name}/issues", {"state": "all", "sort": "updated", "direction": "desc", "since": cutoff}),
            warnings,
        )
        for item in issues:
            if "pull_request" in item:
                continue
            event = {
                **base, "event_type": "issue", "item_id": str(item["number"]),
                "title": item.get("title", ""), "body": item.get("body") or "",
                "url": item["html_url"], "occurred_at": item["created_at"],
                "updated_at": item["updated_at"], "state": item["state"],
                "author": (item.get("user") or {}).get("login"),
                "changed_files": [],
            }
            event["event_id"] = _event_id(repo, "issue", str(item["number"]), item["updated_at"])
            events.append(event)

        releases = _safe_stream(
            repo, "releases", repo_url,
            lambda: client.paged(f"/repos/{owner}/{name}/releases"),
            warnings,
        )
        for item in releases:
            published = item.get("published_at") or item.get("created_at") or collected_at
            if published < cutoff:
                continue
            event = {
                **base, "event_type": "release", "item_id": str(item["id"]),
                "title": item.get("name") or item.get("tag_name", ""),
                "body": item.get("body") or "", "url": item["html_url"],
                "occurred_at": published, "updated_at": published,
                "state": "prerelease" if item.get("prerelease") else "published",
                "author": (item.get("author") or {}).get("login"),
                "changed_files": [],
            }
            event["event_id"] = _event_id(repo, "release", str(item["id"]), published)
            events.append(event)

    unique = {event["event_id"]: event for event in events}
    for event in unique.values():
        cfg = next(c for c in repo_configs if c["repo"] == event["repository"])
        level, score, reasons = classify(event, rule_config, cfg["reporting_weight"])
        combined = f'{event.get("title", "")}\n{event.get("body", "")}'
        event["significance"] = level
        event["significance_score"] = score
        event["significance_reasons"] = reasons
        event["linked_repositories"] = _references(combined, monitored, event["repository"])

    output = sorted(unique.values(), key=lambda x: (x["updated_at"], x["repository"]), reverse=True)
    date_path = datetime.now(timezone.utc).strftime("%Y/%m/%d")
    target = ROOT / "data" / "events" / f"{date_path}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    snapshots = [event for event in output if event.get("event_type") == "repository_snapshot"]
    activity = [event for event in output if event.get("event_type") != "repository_snapshot"]
    consolidated_activity, collapsed_events = consolidate(activity)
    finding_input = snapshots + consolidated_activity
    findings = build_findings(
        finding_input,
        warnings,
        stale_after_days=int(report_settings().get("stale_after_days", 90)),
    )
    finding_path = ROOT / "data" / "findings" / f"{date_path}.json"
    finding_path.parent.mkdir(parents=True, exist_ok=True)
    finding_path.write_text(json.dumps(findings, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    state = {
        "last_successful_collection": collected_at,
        "lookback_days": lookback_days,
        "event_count": len(output),
        "change_unit_count": len(consolidated_activity),
        "collapsed_event_count": collapsed_events,
        "finding_count": len(findings),
        "warning_count": len(warnings),
        "collection_warnings": warnings,
        "repositories": {cfg["repo"]: {"collected_at": collected_at} for cfg in repo_configs},
    }
    state_path = ROOT / "data" / "state" / "collection.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return output
