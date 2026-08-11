from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any
import json
import re

from .config import ROOT, repositories, rules, portfolio_model
from .intelligence import THEME_LABELS, consolidate, event_themes, theme_counts
from .awareness import analyse as analyse_awareness, write_snapshot
from .domain_brief import PULSE_LABELS, render as render_domain_brief

ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
SIGNAL_TAGS = {
    "Normative requirement language changed": "NORM",
    "Authority, delegation, approval, or revocation semantics": "AUTH",
    "Interoperability, canonicalisation, conformance, or protocol behaviour": "INTEROP",
    "Security, privacy, threat, or vulnerability relevance": "SEC",
    "Implementation or production evidence": "IMPL",
    "Published release or tag": "RELEASE",
    "Likely editorial or documentation-only change": "DOCS",
}


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


def _is_breaking(event: dict[str, Any]) -> bool:
    title = event.get("title", "")
    return bool(re.match(r"^(feat|fix|refactor|build|chore)(\([^)]*\))?!:", title, re.I)) or "breaking change" in title.lower()


def _signal_tags(event: dict[str, Any]) -> list[str]:
    return [SIGNAL_TAGS.get(reason, reason[:12].upper()) for reason in event.get("significance_reasons", [])]


def _threshold_legend() -> str:
    thresholds = rules()["thresholds"]
    return (
        f"Critical {thresholds['critical']}+ · High {thresholds['high']}–{thresholds['critical']-1} · "
        f"Medium {thresholds['medium']}–{thresholds['high']-1} · Low <{thresholds['medium']}"
    )


def _thread_summary(theme: str, events: list[dict[str, Any]]) -> str:
    repos = sorted({e["repository"] for e in events})
    breaking = sum(_is_breaking(e) for e in events)
    material = sum(e.get("significance") in {"critical", "high"} for e in events)
    repo_text = ", ".join(f"`{r}`" for r in repos[:3])
    if len(repos) > 3:
        repo_text += f" and {len(repos)-3} more"
    impact = f"{material} material review signal{'s' if material != 1 else ''}"
    if breaking:
        impact += f" and {breaking} breaking change{'s' if breaking != 1 else ''}"
    return f"**{THEME_LABELS.get(theme, theme.replace('-', ' ').title())}** — {len(events)} events across {repo_text}; {impact}."


def _event_table(activity: list[dict[str, Any]]) -> list[str]:
    rows = [
        '<div class="portfolio-filters" role="group" aria-label="Portfolio event filters">',
        '  <label>Repository <select id="portfolio-repo-filter"><option value="">All repositories</option></select></label>',
        '  <label>Significance <select id="portfolio-significance-filter"><option value="">All levels</option><option>critical</option><option>high</option><option>medium</option><option>low</option></select></label>',
        '  <label>Signal <select id="portfolio-signal-filter"><option value="">All signals</option></select></label>',
        '  <label><input id="portfolio-breaking-filter" type="checkbox"> Breaking only</label>',
        '  <button id="portfolio-filter-reset" type="button">Reset</button>',
        '</div>',
        '<p id="portfolio-filter-count" class="portfolio-filter-count"></p>',
        '<div class="table-wrapper"><table id="portfolio-event-table" class="portfolio-event-table">',
        '<thead><tr><th>Significance</th><th>Repository</th><th>Type / state</th><th>Change</th><th>Signals</th><th>Related</th><th>Updated</th></tr></thead>',
        '<tbody>',
    ]
    for event in activity:
        tags = _signal_tags(event)
        tag_html = " ".join(f'<span class="signal-chip" title="{escape(reason)}">{escape(tag)}</span>' for tag, reason in zip(tags, event.get("significance_reasons", []))) or "—"
        related = ", ".join(f"<code>{escape(repo)}</code>" for repo in event.get("linked_repositories", [])) or "—"
        evidence = ""
        if event.get("correlated_events"):
            count = 1 + len(event["correlated_events"])
            evidence = f'<span class="evidence-note" title="A commit and its associated pull request are represented as one change unit.">{count} sources consolidated</span>'
        breaking = _is_breaking(event)
        breaking_badge = '<span class="breaking-chip">BREAKING</span> ' if breaking else ""
        rows.append(
            f'<tr data-repo="{escape(event["repository"])}" data-significance="{escape(event.get("significance", "low"))}" '
            f'data-signals="{escape(" ".join(tags))}" data-breaking="{str(breaking).lower()}">'
            f'<td><strong>{escape(event.get("significance", "low"))}</strong> ({event.get("significance_score", 0)})</td>'
            f'<td><code>{escape(event["repository"])}</code></td>'
            f'<td>{escape(event.get("event_type", ""))} / {escape(event.get("state", ""))}</td>'
            f'<td>{breaking_badge}<a href="{escape(event["url"])}">{escape(" ".join((event.get("title") or "").split()))}</a>{evidence}</td>'
            f'<td>{tag_html}</td><td>{related}</td><td>{escape(event.get("updated_at", "")[:10])}</td></tr>'
        )
    rows += ['</tbody></table></div>', '<script src="{{ \'/assets/js/portfolio-table.js\' | relative_url }}"></script>']
    return rows


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
    raw_activity = [e for e in events if e["event_type"] != "repository_snapshot"]
    activity, collapsed_duplicates = consolidate(raw_activity)
    activity.sort(key=lambda e: (ORDER.get(e.get("significance", "low"), 9), e.get("updated_at", "")), reverse=False)
    counts = Counter(e.get("significance", "low") for e in activity)
    material = [e for e in activity if e.get("significance") in {"critical", "high"}]
    breaking = [e for e in activity if _is_breaking(e)]
    active_repos = {e["repository"] for e in activity}
    inactive_repos = [cfg["repo"] for cfg in repositories() if cfg["repo"] not in active_repos]

    theme_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in activity:
        for theme in event_themes(event):
            theme_groups[theme].append(event)
    leading_threads = sorted(theme_groups.items(), key=lambda item: len(item[1]), reverse=True)[:5]
    generated_at = now.isoformat().replace('+00:00', 'Z')
    awareness = analyse_awareness(
        activity,
        model=portfolio_model(),
        repository_configs=repositories(),
        findings=findings,
        generated_at=generated_at,
    )
    write_snapshot(awareness, when=now)

    lines = [
        f"# {title}", "",
        f"**Generated:** {generated_at}  ",
        f"**Change units:** {len(activity)}  ",
        f"**Duplicate representations consolidated:** {collapsed_duplicates}  ",
        f"**Significance bands:** {_threshold_legend()} ([methodology]({{{{ '/methodology/' | relative_url }}}}))  ",
        f"**Critical:** {counts['critical']} · **High:** {counts['high']} · **Medium:** {counts['medium']} · **Low:** {counts['low']}",
        "", "## Executive summary", "",
    ]
    if material:
        lines.append(f"{len(material)} material change events were detected across {len(set(e['repository'] for e in material))} repositories.")
        links = sum(1 for e in material if e.get("linked_repositories"))
        lines.append(f"{links} material events explicitly reference another monitored repository and may merit coordinated review.")
        if leading_threads:
            names = ", ".join(THEME_LABELS.get(theme, theme) for theme, _ in leading_threads[:3])
            lines.append(f"The dominant portfolio threads were {names}.")
        if breaking:
            lines.append(f"{len(breaking)} changes use an explicit breaking-change marker and should be assessed for migration or deployment impact.")
    else:
        lines.append("No critical or high-significance activity was detected in this collection window.")

    lines += ["", "## Breaking changes this window", ""]
    if not breaking:
        lines.append("_No explicit conventional-commit breaking markers were detected._")
    else:
        for event in breaking:
            lines.append(f"- `{event['repository']}` · [{_clean(event['title'])}]({event['url']}) — {event['event_type']} / {event['state']}; significance {event['significance']} ({event['significance_score']}).")

    lines += ["", "## This window's threads", ""]
    if leading_threads:
        lines.extend(f"- {_thread_summary(theme, thread_events)}" for theme, thread_events in leading_threads)
    else:
        lines.append("_No recurring engineering threads were detected._")

    lines += [
        "", "## Event register", "",
        "This is the canonical detail view. Use the controls to filter the consolidated change units. Signal abbreviations are defined in the [methodology]({{ '/methodology/' | relative_url }}).",
        "",
    ]
    lines += _event_table(activity)

    lines += ["", "## Inactive repositories this window", ""]
    if inactive_repos:
        lines.append("No activity detected: " + ", ".join(f"`{repo}`" for repo in inactive_repos) + ".")
    else:
        lines.append("_All monitored repositories had activity._")

    lines += [
        "", "## Method note", "",
        "Significance is assigned by deterministic rules in `config/significance-rules.yaml`. Scores are review signals, not authoritative judgements. "
        "Duplicate representations means that a commit and its associated pull request were consolidated into one change unit. Source links remain the evidence of record.", "",
    ]

    target = ROOT / "reports" / period / f"{name}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")

    latest = ROOT / "docs" / "portfolio-status.md"
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text("---\ntitle: Portfolio status\nnav_order: 5\npermalink: /portfolio-status/\n---\n\n" + "\n".join(lines), encoding="utf-8")

    domain_brief = ROOT / "docs" / "domain-brief.md"
    domain_brief.write_text(render_domain_brief(awareness, generated_at), encoding="utf-8")

    dashboard = ROOT / "docs" / "dashboard.md"
    dashboard_lines = [
        "---", "title: Dashboard", "nav_order: 3", "permalink: /dashboard/", "---",
        "# Portfolio dashboard", "",
        f"**Generated:** {generated_at}  ",
        f"**Change units:** {len(activity)}  ", f"**Material change units:** {len(material)}  ",
        f"**Breaking changes:** {len(breaking)}  ", f"**Review findings:** {len(findings)}  ",
        f"**Duplicate representations consolidated:** {collapsed_duplicates}", "",
        "[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }", "",
        "## Capability pulse", "",
        "| Capability | Pulse | Change units | Material |", "|---|---|---:|---:|",
    ]
    for state in awareness["capabilities"].values():
        dashboard_lines.append(
            f"| {state['label']} | **{PULSE_LABELS[state['pulse']]}** | {state['change_units']} | {state['material_change_units']} |"
        )
    dashboard_lines += ["", "## Leading themes", ""]
    themes = theme_counts(activity)
    dashboard_lines += [
        f"- **{THEME_LABELS.get(theme, theme.replace('-', ' ').title())}:** {count}"
        for theme, count in themes[:5]
    ] or ["_No themes detected._"]
    dashboard_lines += [
        "", "## Portfolio intelligence", "",
        f"- **Cross-capability convergence signals:** {len(awareness['convergences'])}",
        f"- **Specification/implementation signals:** {len(awareness['implementation_alignment'])}",
        f"- **Attention signals:** {len(awareness['attention_signals'])}",
    ]
    dashboard.write_text("\n".join(dashboard_lines) + "\n", encoding="utf-8")

    report_index = ROOT / "docs" / "reports.md"
    report_index.write_text(
        "---\ntitle: Reports\nnav_order: 6\npermalink: /reports/\n---\n"
        "# Reports\n\n[Open the current portfolio status]({{ \"/portfolio-status/\" | relative_url }}){: .btn .btn-primary }\n\n"
        f"Latest generated **{period}** report: `{target.relative_to(ROOT)}`.\n", encoding="utf-8",
    )
    return target
