from __future__ import annotations
from datetime import datetime, timedelta, timezone
from typing import Any
import hashlib

def _id(kind: str, repository: str, subject: str) -> str:
    return hashlib.sha256(f"{kind}|{repository}|{subject}".encode()).hexdigest()[:20]

def build_findings(
    events: list[dict[str, Any]],
    collection_warnings: list[dict[str, Any]],
    stale_after_days: int = 90,
) -> list[dict[str, Any]]:
    now = datetime.now(timezone.utc)
    findings: list[dict[str, Any]] = []

    snapshots = {e["repository"]: e for e in events if e["event_type"] == "repository_snapshot"}
    activity = [e for e in events if e["event_type"] != "repository_snapshot"]

    for repository, snapshot in snapshots.items():
        if snapshot.get("is_empty"):
            findings.append({
                "finding_id": _id("empty_repository", repository, "repository"),
                "kind": "empty_repository",
                "severity": "informational",
                "repository": repository,
                "title": "Repository has no commits",
                "summary": "GitHub reports that the repository is empty. This is a valid lifecycle condition, not a collection failure.",
                "evidence_urls": [snapshot["url"]],
                "related_repositories": [],
                "review_status": "observed",
            })

        pushed_at = snapshot.get("pushed_at")
        if pushed_at:
            pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            age = (now - pushed).days
            if age >= stale_after_days:
                findings.append({
                    "finding_id": _id("stale_repository", repository, pushed_at),
                    "kind": "stale_repository",
                    "severity": "low",
                    "repository": repository,
                    "title": f"No repository push for {age} days",
                    "summary": f"The latest recorded push is {age} days old. Review whether the repository is dormant, transitional, or simply stable.",
                    "evidence_urls": [snapshot["url"]],
                    "related_repositories": [],
                    "review_status": "needs-review",
                })

    for event in activity:
        if event.get("linked_repositories") and event.get("significance") in {"critical", "high"}:
            findings.append({
                "finding_id": _id("material_cross_reference", event["repository"], event["event_id"]),
                "kind": "material_cross_reference",
                "severity": event["significance"],
                "repository": event["repository"],
                "title": event["title"],
                "summary": "A material event explicitly references another monitored repository and may require cross-workstream examination.",
                "evidence_urls": [event["url"]],
                "related_repositories": event["linked_repositories"],
                "review_status": "needs-review",
            })

    for warning in collection_warnings:
        findings.append({
            "finding_id": _id("collection_warning", warning["repository"], warning["stream"]),
            "kind": "collection_warning",
            "severity": "medium",
            "repository": warning["repository"],
            "title": f"Collection gap in {warning['stream']}",
            "summary": warning["message"],
            "evidence_urls": [warning.get("url")] if warning.get("url") else [],
            "related_repositories": [],
            "review_status": "needs-review",
        })

    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "informational": 4}
    return sorted(findings, key=lambda f: (order.get(f["severity"], 9), f["repository"], f["kind"]))
