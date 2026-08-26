from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any
import json
import yaml

from .config import ROOT, load_yaml
from .github import GitHubClient, utc_now

DISCOVERY_CONFIG = ROOT / "config" / "repository-discovery.yaml"
DISCOVERY_SNAPSHOT = ROOT / "data" / "repository-discovery.json"
EFFECTIVE_REGISTRY = ROOT / "data" / "effective-repositories.yaml"
REPOSITORY_PAGE = ROOT / "docs" / "repositories.md"


def discovery_config() -> dict[str, Any]:
    return load_yaml(DISCOVERY_CONFIG)


def _candidate_config(repo: dict[str, Any], source: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    name = repo["name"]
    prefixes = source.get("prefixes", [])
    prefix = next((value for value in prefixes if name.startswith(value)), "")
    workstream = name[len(prefix):] if prefix else name
    return {
        "repo": repo["full_name"],
        "organisation": source["organisation"],
        "workstream": workstream,
        "role": source["default_role"],
        "lifecycle": "active",
        "reporting_weight": source.get("default_weight", "medium"),
        "default_branch": repo.get("default_branch") or "main",
        "monitor": deepcopy(policy["default_monitor"]),
        "material_paths": deepcopy(policy["default_material_paths"]),
        "notes": "Dynamically admitted by config/repository-discovery.yaml.",
        "discovery": {
            "source_owner": source["owner"],
            "admission": "automatic",
        },
    }


def evaluate_candidate(repo: dict[str, Any], source: dict[str, Any], policy: dict[str, Any]) -> tuple[bool, str]:
    full_name = repo.get("full_name", "")
    name = repo.get("name", "")
    if not any(name.startswith(prefix) for prefix in source.get("prefixes", [])):
        return False, "name-prefix-mismatch"
    if full_name in set(policy.get("exclude_repositories", [])):
        return False, "explicitly-excluded"
    if policy.get("public_only", True) and repo.get("private", False):
        return False, "private-repository"
    if policy.get("exclude_archived", True) and repo.get("archived", False):
        return False, "archived-repository"
    if policy.get("exclude_forks", True) and repo.get("fork", False) and full_name not in set(policy.get("allow_forks", [])):
        return False, "fork-not-allowlisted"
    return True, "policy-match"


def discover(client: GitHubClient) -> dict[str, Any]:
    cfg = discovery_config()
    policy = cfg["policy"]
    admitted: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []

    for source in cfg.get("sources", []):
        owner = source["owner"]
        for repo in client.paged(f"/users/{owner}/repos", {"type": "public", "sort": "full_name"}):
            accepted, reason = evaluate_candidate(repo, source, policy)
            name = repo.get("name", "")
            if not any(name.startswith(prefix) for prefix in source.get("prefixes", [])):
                continue
            decision = {
                "repository": repo.get("full_name"),
                "owner": owner,
                "admitted": accepted,
                "reason": reason,
                "fork": bool(repo.get("fork")),
                "archived": bool(repo.get("archived")),
                "private": bool(repo.get("private")),
            }
            decisions.append(decision)
            if accepted:
                admitted.append(_candidate_config(repo, source, policy))

    admitted.sort(key=lambda item: item["repo"].lower())
    decisions.sort(key=lambda item: item["repository"].lower())
    return {
        "version": 1,
        "generated_at": utc_now(),
        "policy": str(DISCOVERY_CONFIG.relative_to(ROOT)),
        "admitted": admitted,
        "decisions": decisions,
    }


def merge_effective(configured: list[dict[str, Any]], admitted: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_repo = {item["repo"]: deepcopy(item) for item in admitted}
    for item in configured:
        by_repo[item["repo"]] = deepcopy(item)
    return sorted(by_repo.values(), key=lambda item: item["repo"].lower())


def render_repository_page(effective: list[dict[str, Any]], snapshot: dict[str, Any]) -> str:
    lines = [
        "---",
        "title: Tracked repositories",
        "nav_order: 4",
        "permalink: /repositories/",
        "---",
        "# Tracked repositories",
        "",
        "The effective monitoring scope combines the curated registry with repositories admitted by the deterministic discovery policy. Curated metadata always overrides discovered defaults.",
        "",
        f"**Discovery evidence generated:** {snapshot.get('generated_at', 'unknown')}  ",
        f"**Policy:** `{snapshot.get('policy', 'config/repository-discovery.yaml')}`",
        "",
        "| Repository | Workstream | Role | Lifecycle | Weight | Admission |",
        "|---|---|---|---|---|---|",
    ]
    for item in effective:
        admission = "dynamic" if item.get("discovery") else "curated"
        repo = item["repo"]
        lines.append(
            f"| [`{repo}`](https://github.com/{repo}) | {item.get('workstream', '')} | {item.get('role', '')} | {item.get('lifecycle', '')} | {item.get('reporting_weight', '')} | {admission} |"
        )
    rejected = [item for item in snapshot.get("decisions", []) if not item.get("admitted")]
    lines += [
        "",
        "## Governance boundary",
        "",
        "Dynamic discovery is an admission mechanism, not an authority override. `config/repositories.yaml` remains authoritative for explicitly curated metadata. `config/repository-discovery.yaml` defines who may be discovered, naming scope, exclusions, fork policy, and defaults. Removing a source, adding an exclusion, or archiving a repository revokes automatic admission on the next collection run.",
        "",
        "Forks are excluded by default to avoid duplicate observation of upstream DTG repositories. A fork must be explicitly allowlisted before it can enter dynamic scope.",
        "",
        "## Discovery decisions",
        "",
        f"Current run: **{len(snapshot.get('admitted', []))} admitted candidate(s)** and **{len(rejected)} rejected candidate(s)**. The full machine-readable decision record is persisted at `data/repository-discovery.json`.",
        "",
        "## Cross-specification assurance seams",
        "",
        "Composition boundaries remain governed separately in `config/cross-spec-pressure-tests.yaml`; repository discovery changes observation scope only and does not itself assert assurance or conformance.",
        "",
    ]
    return "\n".join(lines)


def run(client: GitHubClient) -> dict[str, Any]:
    snapshot = discover(client)
    configured = load_yaml(ROOT / "config" / "repositories.yaml")["repositories"]
    effective = merge_effective(configured, snapshot["admitted"])

    DISCOVERY_SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    DISCOVERY_SNAPSHOT.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    EFFECTIVE_REGISTRY.write_text(yaml.safe_dump({"version": 1, "repositories": effective}, sort_keys=False), encoding="utf-8")
    REPOSITORY_PAGE.write_text(render_repository_page(effective, snapshot), encoding="utf-8")
    return snapshot
