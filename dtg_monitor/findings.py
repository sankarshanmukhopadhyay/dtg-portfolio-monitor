from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
import hashlib


LIFECYCLE_STATES = {"open", "resolved", "superseded", "duplicate", "accepted-risk", "not-applicable"}
REVIEW_STATES = {"unreviewed", "triaged", "action-required", "no-action", "observed"}
URGENCY_ORDER = {"urgent": 0, "elevated": 1, "routine": 2, "informational": 3}


def _fingerprint(kind: str, repository: str, subject: str) -> str:
    """Return a stable identity for the semantic finding, independent of observation time."""
    return hashlib.sha256(f"{kind}|{repository}|{subject}".encode()).hexdigest()[:24]


def _finding(
    *,
    kind: str,
    repository: str,
    subject: str,
    title: str,
    summary: str,
    evidence_urls: list[str],
    related_repositories: list[str],
    materiality: str,
    urgency: str,
    assurance_impact: str = "none",
    review_status: str = "unreviewed",
) -> dict[str, Any]:
    fingerprint = _fingerprint(kind, repository, subject)
    return {
        "finding_id": fingerprint[:20],
        "fingerprint": fingerprint,
        "kind": kind,
        # severity is retained for v0.4 consumers; v0.5 consumers should use
        # materiality + urgency + assurance_impact.
        "severity": materiality,
        "materiality": materiality,
        "urgency": urgency,
        "assurance_impact": assurance_impact,
        "repository": repository,
        "title": title,
        "summary": summary,
        "evidence_urls": list(dict.fromkeys(url for url in evidence_urls if url)),
        "related_repositories": sorted(set(related_repositories)),
        "state": "open",
        "review_status": review_status,
        "authority": None,
        "disposition": None,
        "related_findings": [],
        "successor_finding": None,
    }


def _event_evidence(event: dict[str, Any]) -> list[str]:
    urls = [event.get("url")]
    urls.extend(item.get("url") for item in event.get("correlated_events", []))
    return [url for url in urls if url]


def _assurance_impact(event: dict[str, Any]) -> str:
    reasons = set(event.get("significance_reasons", []))
    text = f"{event.get('title', '')} {event.get('body', '')}".lower()
    if any(token in text for token in ("breaking", "must not", "shall not", "revocation", "permission", "authority")):
        return "potentially-breaking"
    if reasons & {"security-privacy", "normative-language", "authority-semantics", "interoperability"}:
        return "unknown"
    return "none"


def build_findings(
    events: list[dict[str, Any]],
    collection_warnings: list[dict[str, Any]],
    stale_after_days: int = 90,
) -> list[dict[str, Any]]:
    """Build decision-grade findings from repository snapshots and consolidated change units.

    Callers should pass consolidated commit/PR change units. Correlated source-event
    URLs are retained as evidence, so duplicate source events do not create duplicate
    review obligations.
    """
    now = datetime.now(timezone.utc)
    findings: list[dict[str, Any]] = []

    snapshots = {e["repository"]: e for e in events if e["event_type"] == "repository_snapshot"}
    activity = [e for e in events if e["event_type"] != "repository_snapshot"]

    for repository, snapshot in snapshots.items():
        if snapshot.get("is_empty"):
            findings.append(_finding(
                kind="empty_repository",
                repository=repository,
                subject="repository",
                title="Repository has no commits",
                summary="GitHub reports that the repository is empty. This is a valid lifecycle condition, not a collection failure.",
                evidence_urls=[snapshot["url"]],
                related_repositories=[],
                materiality="informational",
                urgency="informational",
                review_status="observed",
            ))

        pushed_at = snapshot.get("pushed_at")
        if pushed_at:
            pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            age = (now - pushed).days
            if age >= stale_after_days:
                findings.append(_finding(
                    kind="stale_repository",
                    repository=repository,
                    subject=pushed_at,
                    title=f"No repository push for {age} days",
                    summary=f"The latest recorded push is {age} days old. Review whether the repository is dormant, transitional, or intentionally stable.",
                    evidence_urls=[snapshot["url"]],
                    related_repositories=[],
                    materiality="low",
                    urgency="routine",
                ))

    for event in activity:
        if event.get("linked_repositories") and event.get("significance") in {"critical", "high"}:
            assurance_impact = _assurance_impact(event)
            urgency = "elevated" if assurance_impact in {"unknown", "potentially-breaking"} else "routine"
            findings.append(_finding(
                kind="material_cross_reference",
                repository=event["repository"],
                subject=f"{event.get('repository')}|{event.get('change_unit_key', event.get('event_id'))}",
                title=event["title"],
                summary="A material consolidated change unit explicitly references another monitored repository and may require cross-workstream examination.",
                evidence_urls=_event_evidence(event),
                related_repositories=event["linked_repositories"],
                materiality="high" if event.get("significance") == "critical" else event.get("significance", "medium"),
                urgency=urgency,
                assurance_impact=assurance_impact,
            ))

    for warning in collection_warnings:
        findings.append(_finding(
            kind="collection_warning",
            repository=warning["repository"],
            subject=warning["stream"],
            title=f"Collection gap in {warning['stream']}",
            summary=warning["message"],
            evidence_urls=[warning.get("url")] if warning.get("url") else [],
            related_repositories=[],
            materiality="medium",
            urgency="urgent",
            assurance_impact="unknown",
            review_status="action-required",
        ))

    return sorted(
        findings,
        key=lambda f: (
            URGENCY_ORDER.get(f["urgency"], 9),
            f["repository"],
            f["kind"],
            f["fingerprint"],
        ),
    )
