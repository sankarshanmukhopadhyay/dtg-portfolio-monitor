from __future__ import annotations

from typing import Any

PULSE_LABELS = {
    "advancing-strongly": "Advancing strongly",
    "advancing": "Advancing",
    "active": "Active",
    "quiet": "Quiet this window",
}


def _label(snapshot: dict[str, Any], capability_id: str) -> str:
    return snapshot["capabilities"][capability_id]["label"]


def _portfolio_direction(snapshot: dict[str, Any]) -> str:
    dominant = snapshot.get("dominant_capabilities", [])
    if not dominant:
        return "No material portfolio movement is visible in the current observation window."
    labels = [_label(snapshot, capability_id) for capability_id in dominant]
    if len(labels) == 1:
        joined = labels[0]
    elif len(labels) == 2:
        joined = f"{labels[0]} and {labels[1]}"
    else:
        joined = f"{labels[0]}, {labels[1]}, and {labels[2]}"
    return f"The strongest observed movement is currently concentrated in **{joined}**."


def _capability_narrative(snapshot: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    for capability_id in snapshot.get("dominant_capabilities", [])[:3]:
        state = snapshot["capabilities"][capability_id]
        if not state["change_units"]:
            continue
        themes = ", ".join(theme["label"].lower() for theme in state["themes"][:2])
        detail = f"{state['material_change_units']} material change unit{'s' if state['material_change_units'] != 1 else ''}"
        if themes:
            detail += f", led by {themes}"
        lines.append(f"**{state['label']}** — {detail}.")
    return lines


def _convergence_text(snapshot: dict[str, Any], item: dict[str, Any]) -> str:
    left = _label(snapshot, item["from"])
    right = _label(snapshot, item["to"])
    shared = [theme.replace("-", " ") for theme in item.get("shared_themes", [])]
    theme_text = f" around {', '.join(shared[:2])}" if shared else ""
    return (
        f"**{left} ↔ {right}.** Material activity is present on both sides of the declared "
        f"`{item['relationship']}` relationship{theme_text}."
    )


def _alignment_text(snapshot: dict[str, Any], item: dict[str, Any]) -> str:
    label = _label(snapshot, item["capability"])
    state = item["state"]
    if state == "moving-together":
        return (
            f"**{label}: specification and implementation are moving together.** "
            f"The monitor observed {item['specification_material_change_units']} material specification change unit(s) "
            f"and {item['implementation_material_change_units']} material implementation change unit(s)."
        )
    if state == "specification-ahead":
        return f"**{label}: specification movement is ahead of implementation activity in this window.**"
    return f"**{label}: implementation movement is ahead of normative specification activity in this window.**"


def render(snapshot: dict[str, Any], generated_at: str) -> str:
    observation = snapshot.get("observation", {})
    source_revision = observation.get("source_revision") or "local/unknown"
    run_id = observation.get("collection_run_id") or "local/unknown"
    evidence_through = observation.get("evidence_through") or generated_at
    publication_state = observation.get("publication_state") or "generated"
    queue = snapshot.get("decision_queue", {})

    lines = [
        "---",
        "title: DTG Domain Brief",
        "nav_order: 2",
        "permalink: /domain-brief/",
        "---",
        "# DTG Domain Brief",
        "",
        f"**Generated:** {generated_at}  ",
        f"**Evidence through:** {evidence_through}  ",
        f"**Source revision:** `{source_revision}` · **Collection run:** `{run_id}` · **Publication state:** `{publication_state}`  ",
        f"**Change units:** {snapshot['change_units']} · **Material:** {snapshot['material_change_units']}  ",
        "",
        "This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.",
        "",
        "## Review queue",
        "",
        f"- **Decision findings:** {queue.get('decision_findings', 0)}",
        f"- **Review-required assertions:** {queue.get('review_assertions', 0)}",
        f"- **Watch assertions:** {queue.get('watch_assertions', 0)}",
        f"- **Open findings:** {queue.get('open_findings', 0)}",
        "",
        "Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.",
        "",
        "## Where DTG is moving",
        "",
        _portfolio_direction(snapshot),
        "",
    ]
    narratives = _capability_narrative(snapshot)
    lines.extend(narratives or ["_No capability-level movement summary is available for this window._"])

    lines += ["", "## Portfolio pulse", "", "| Capability | Pulse | Change units | Material |", "|---|---|---:|---:|"]
    for capability_id, state in snapshot["capabilities"].items():
        lines.append(
            f"| {state['label']} | **{PULSE_LABELS[state['pulse']]}** | {state['change_units']} | {state['material_change_units']} |"
        )
    lines += [
        "",
        "> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.",
        "",
        "## Cross-workstream convergence",
        "",
    ]
    if snapshot["convergences"]:
        lines.extend(f"- {_convergence_text(snapshot, item)}" for item in snapshot["convergences"][:5])
    else:
        lines.append("_No declared capability relationship had material activity on both sides in this window._")

    lines += ["", "## Specification and implementation alignment", ""]
    if snapshot["implementation_alignment"]:
        lines.extend(f"- {_alignment_text(snapshot, item)}" for item in snapshot["implementation_alignment"])
    else:
        lines.append("_No strong specification/implementation alignment or asymmetry signal was detected._")

    lines += ["", "## Attention signals", ""]
    if snapshot["attention_signals"]:
        for item in snapshot["attention_signals"][:6]:
            lines.append(f"- {item['summary']} This is a coordination signal, not a finding of failure.")
    else:
        lines.append("_No related-capability asymmetry met the current deterministic signal threshold._")

    lines += ["", "## Machine-addressable assertions", ""]
    assertions = snapshot.get("assertions", [])
    if assertions:
        lines += ["| Assertion | Class | State | Statement |", "|---|---|---|---|"]
        for assertion in assertions[:20]:
            lines.append(
                f"| `{assertion['assertion_id']}` | {assertion['review_class']} | {assertion['state']} | {assertion['statement']} |"
            )
    else:
        lines.append("_No deterministic portfolio assertions were produced in this window._")

    lines += ["", "## What to watch next", ""]
    watch: list[str] = []
    for item in snapshot["implementation_alignment"]:
        if item["state"] == "moving-together":
            watch.append(f"Whether **{_label(snapshot, item['capability'])}** implementation experience feeds back into the associated specification work.")
        elif item["state"] == "implementation-ahead":
            watch.append(f"Whether normative work catches up with implementation movement in **{_label(snapshot, item['capability'])}**.")
        elif item["state"] == "specification-ahead":
            watch.append(f"Whether implementations absorb recent normative movement in **{_label(snapshot, item['capability'])}**.")
    for item in snapshot["attention_signals"]:
        watch.append(f"Whether activity resumes or remains intentionally stable in **{_label(snapshot, item['quiet'])}** while related work advances.")
    for item in snapshot["convergences"][:2]:
        watch.append(f"Whether the current convergence between **{_label(snapshot, item['from'])}** and **{_label(snapshot, item['to'])}** creates new cross-repository dependencies or review needs.")
    if not watch:
        watch.append("Whether the next observation window produces new cross-workstream convergence or specification/implementation movement.")
    for index, text in enumerate(dict.fromkeys(watch), start=1):
        if index > 5:
            break
        lines.append(f"{index}. {text}")

    lines += [
        "",
        "## Evidence trail",
        "",
        "Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.",
        "",
        "The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.",
        "",
    ]
    return "\n".join(lines)
