from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json

from .config import ROOT, repositories
from .intelligence import consolidate, theme_counts

ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

def _load_latest_events() -> list[dict[str, Any]]:
    paths = sorted((ROOT / "data" / "events").glob("**/*.json"))
    if not paths:
        return []
    return json.loads(paths[-1].read_text(encoding="utf-8"))

def _load_latest_findings() -> list[dict[str, Any]]:
    paths = sorted((ROOT / "data" / "findings").glob("**/*.json"))
    if not paths:
        return []
    return json.loads(paths[-1].read_text(encoding="utf-8"))

def _clean(text: str) -> str:
    return " ".join((text or "").replace("|", "\\|").split())

def generate(period: str = "daily", events: list[dict[str, Any]] | None = None) -> Path:
    events = events if events is not None else _load_latest_events()
    now = datetime.now(timezone.utc)
    if period == "weekly":
        name = now.strftime("%G-W%V")
        title = "Weekly DTG Portfolio Change Report"
    else:
        name = now.strftime("%Y-%m-%d")
        title = "Daily DTG Portfolio Change Digest"

    findings = _load_latest_findings()
    snapshots = {e["repository"]: e for e in events if e["event_type"] == "repository_snapshot"}
    raw_activity = [e for e in events if e["event_type"] != "repository_snapshot"]
    activity, collapsed_duplicates = consolidate(raw_activity)
    themes = theme_counts(activity)
    activity.sort(key=lambda e: (ORDER.get(e.get("significance", "low"), 9), e.get("updated_at", "")))
    counts = Counter(e.get("significance", "low") for e in activity)
    by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in activity:
        by_repo[event["repository"]].append(event)

    lines = [
        f"# {title}",
        "",
        f"**Generated:** {now.isoformat().replace('+00:00', 'Z')}  ",
        f"**Change units:** {len(activity)}  ",
        f"**Duplicate representations consolidated:** {collapsed_duplicates}  ",
        f"**Critical:** {counts['critical']} · **High:** {counts['high']} · **Medium:** {counts['medium']} · **Low:** {counts['low']}",
        "",
        "## Executive summary",
        "",
    ]
    material = [e for e in activity if e.get("significance") in {"critical", "high"}]
    if material:
        lines.append(f"{len(material)} material change events were detected across {len(set(e['repository'] for e in material))} repositories.")
        links = sum(1 for e in material if e.get("linked_repositories"))
        if links:
            lines.append(f"{links} material events explicitly reference another monitored repository and may merit cross-workstream review.")
    else:
        lines.append("No critical or high-significance activity was detected in this collection window.")

    lines += ["", "## Material developments", ""]
    if not material:
        lines.append("_None detected._")
    for event in material:
        lines += [
            f"### [{_clean(event['title'])}]({event['url']})",
            "",
            f"- **Repository:** `{event['repository']}`",
            f"- **Type/state:** {event['event_type']} / {event['state']}",
            f"- **Significance:** {event['significance']} ({event['significance_score']})",
            f"- **Updated:** {event['updated_at']}",
        ]
        if event.get("significance_reasons"):
            lines.append(f"- **Signals:** {'; '.join(event['significance_reasons'])}")
        if event.get("correlated_events"):
            lines.append(f"- **Consolidated evidence:** {1 + len(event['correlated_events'])} commit/PR representations")
        if event.get("linked_repositories"):
            lines.append(f"- **Potentially related:** {', '.join(f'`{r}`' for r in event['linked_repositories'])}")
        lines.append("")

    lines += ["## Repository-by-repository activity", ""]
    for cfg in repositories():
        repo = cfg["repo"]
        items = by_repo.get(repo, [])
        lines += [f"### {repo}", "", f"Role: **{cfg['role']}** · Workstream: **{cfg['workstream']}** · Lifecycle: **{cfg['lifecycle']}**", ""]
        if not items:
            lines.append("_No activity detected in this collection window._")
            lines.append("")
            continue
        lines += ["| Significance | Type | State | Change | Updated |", "|---|---|---|---|---|"]
        for event in items[:50]:
            lines.append(
                f"| {event['significance']} | {event['event_type']} | {event['state']} | "
                f"[{_clean(event['title'])}]({event['url']}) | {event['updated_at'][:10]} |"
            )
        lines.append("")

    lines += ["## Cross-workstream implications", ""]
    related = [e for e in activity if e.get("linked_repositories")]
    if not related:
        lines.append("_No explicit cross-repository references detected._")
    else:
        for event in related:
            lines.append(f"- [{_clean(event['title'])}]({event['url']}) in `{event['repository']}` references {', '.join(f'`{r}`' for r in event['linked_repositories'])}.")
    lines += [
        "",
        "## Method note",
        "",
        "Significance is assigned by deterministic rules in `config/significance-rules.yaml`. "
        "A high score is a review signal, not an authoritative judgement. Source links remain the evidence of record.",
        "",
    ]

    target = ROOT / "reports" / period / f"{name}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")

    latest = ROOT / "docs" / "portfolio-status.md"
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text("---\ntitle: Portfolio status\nnav_order: 4\npermalink: /portfolio-status/\n---\n\n" + "\n".join(lines), encoding="utf-8")

    dashboard = ROOT / "docs" / "dashboard.md"
    dashboard_lines = [
        "---", "title: Dashboard", "nav_order: 2", "permalink: /dashboard/", "---",
        "# Portfolio dashboard", "",
        f"**Generated:** {now.isoformat().replace('+00:00', 'Z')}  ",
        f"**Change units:** {len(activity)}  ",
        f"**Material change units:** {len(material)}  ",
        f"**Review findings:** {len(findings)}  ",
        f"**Duplicate representations consolidated:** {collapsed_duplicates}", "",
        "## Leading themes", "",
    ]
    dashboard_lines += [f"- **{theme.replace('-', ' ').title()}:** {count}" for theme,count in themes[:5]] or ["_No themes detected._"]
    dashboard.write_text("\n".join(dashboard_lines)+"\n", encoding="utf-8")

    report_index = ROOT / "docs" / "reports.md"
    report_index.write_text(
        "---\ntitle: Reports\nnav_order: 5\npermalink: /reports/\n---\n"
        "# Reports\n\n"
        "[Open the current portfolio status]({{ \"/portfolio-status/\" | relative_url }}){: .btn .btn-primary }\n\n"
        f"Latest generated **{period}** report: `{target.relative_to(ROOT)}`.\n",
        encoding="utf-8",
    )
    return target
