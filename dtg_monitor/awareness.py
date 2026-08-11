from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json

from .config import ROOT, portfolio_model, repositories
from .intelligence import THEME_LABELS, event_themes

MATERIAL_LEVELS = {"critical", "high"}


def _capability_index(model: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    capabilities = {item["id"]: item for item in model["capabilities"]}
    workstream_to_capability = {
        workstream: item["id"]
        for item in model["capabilities"]
        for workstream in item.get("workstreams", [])
    }
    return capabilities, workstream_to_capability


def _pulse(change_units: int, material_changes: int, thresholds: dict[str, int]) -> str:
    if material_changes >= thresholds["advancing_strongly_material"]:
        return "advancing-strongly"
    if material_changes >= thresholds["advancing_material"]:
        return "advancing"
    if change_units >= thresholds["active_changes"]:
        return "active"
    return "quiet"


def _event_repositories(events: list[dict[str, Any]]) -> list[str]:
    return sorted({event["repository"] for event in events})


def _evidence_urls(events: list[dict[str, Any]], limit: int = 12) -> list[str]:
    urls: list[str] = []
    for event in events:
        url = event.get("url")
        if url and url not in urls:
            urls.append(url)
        if len(urls) >= limit:
            break
    return urls


def analyse(
    events: list[dict[str, Any]],
    *,
    model: dict[str, Any] | None = None,
    repository_configs: list[dict[str, Any]] | None = None,
    findings: list[dict[str, Any]] | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Build a deterministic DTG situational-awareness snapshot.

    ``events`` should contain consolidated, non-snapshot change units. The
    function deliberately uses declared portfolio semantics rather than an LLM
    so that every generated signal can be reproduced from configuration and
    GitHub evidence.
    """
    model = model or portfolio_model()
    repository_configs = repository_configs or repositories()
    findings = findings or []
    generated_at = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    capabilities, workstream_to_capability = _capability_index(model)
    repo_to_workstream = {item["repo"]: item["workstream"] for item in repository_configs}
    repo_to_capability = {
        repo: workstream_to_capability.get(workstream)
        for repo, workstream in repo_to_workstream.items()
    }

    by_capability: dict[str, list[dict[str, Any]]] = defaultdict(list)
    unmapped_events: list[dict[str, Any]] = []
    for event in events:
        capability = repo_to_capability.get(event.get("repository"))
        if capability:
            by_capability[capability].append(event)
        else:
            unmapped_events.append(event)

    thresholds = model["pulse_thresholds"]
    capability_states: dict[str, dict[str, Any]] = {}
    portfolio_themes: Counter[str] = Counter()
    for capability_id, definition in capabilities.items():
        cap_events = by_capability.get(capability_id, [])
        material = [e for e in cap_events if e.get("significance") in MATERIAL_LEVELS]
        themes = Counter(theme for event in cap_events for theme in event_themes(event))
        portfolio_themes.update(themes)
        capability_states[capability_id] = {
            "label": definition["label"],
            "purpose": definition.get("purpose", ""),
            "pulse": _pulse(len(cap_events), len(material), thresholds),
            "change_units": len(cap_events),
            "material_change_units": len(material),
            "repositories": _event_repositories(cap_events),
            "themes": [
                {"id": theme, "label": THEME_LABELS.get(theme, theme), "count": count}
                for theme, count in themes.most_common(5)
            ],
            "evidence_urls": _evidence_urls(material or cap_events),
        }

    convergences: list[dict[str, Any]] = []
    asymmetries: list[dict[str, Any]] = []
    for relation in model.get("relationships", []):
        left_id, right_id = relation["from"], relation["to"]
        left_events = by_capability.get(left_id, [])
        right_events = by_capability.get(right_id, [])
        left_material = [e for e in left_events if e.get("significance") in MATERIAL_LEVELS]
        right_material = [e for e in right_events if e.get("significance") in MATERIAL_LEVELS]
        left_themes = {theme for e in left_material for theme in event_themes(e)}
        right_themes = {theme for e in right_material for theme in event_themes(e)}
        shared = sorted(left_themes & right_themes)

        if left_material and right_material:
            evidence = left_material + right_material
            convergences.append({
                "kind": "cross-capability-convergence",
                "from": left_id,
                "to": right_id,
                "relationship": relation["kind"],
                "rationale": relation.get("rationale", ""),
                "shared_themes": shared,
                "material_change_units": len(left_material) + len(right_material),
                "repositories": _event_repositories(evidence),
                "evidence_urls": _evidence_urls(evidence),
            })
        elif (left_material and not right_events) or (right_material and not left_events):
            advancing_id = left_id if left_material else right_id
            quiet_id = right_id if left_material else left_id
            evidence = left_material if left_material else right_material
            asymmetries.append({
                "kind": "related-capability-asymmetry",
                "advancing": advancing_id,
                "quiet": quiet_id,
                "relationship": relation["kind"],
                "summary": (
                    f"{capabilities[advancing_id]['label']} has material activity while "
                    f"related capability {capabilities[quiet_id]['label']} is quiet in this observation window."
                ),
                "evidence_urls": _evidence_urls(evidence),
            })

    implementation_alignment: list[dict[str, Any]] = []
    by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        by_repo[event.get("repository", "")].append(event)
    for link in model.get("implementation_links", []):
        spec_repo = link["specification_repository"]
        impl_repos = link["implementation_repositories"]
        relevant_themes = set(link.get("themes", []))

        def relevant(event: dict[str, Any]) -> bool:
            return not relevant_themes or bool(relevant_themes & set(event_themes(event)))

        spec_material = [
            e for e in by_repo.get(spec_repo, [])
            if e.get("significance") in MATERIAL_LEVELS and relevant(e)
        ]
        impl_material = [
            e for repo in impl_repos for e in by_repo.get(repo, [])
            if e.get("significance") in MATERIAL_LEVELS and relevant(e)
        ]
        if spec_material and impl_material:
            state = "moving-together"
        elif len(spec_material) >= thresholds["advancing_material"] and not impl_material:
            state = "specification-ahead"
        elif len(impl_material) >= thresholds["advancing_material"] and not spec_material:
            state = "implementation-ahead"
        else:
            state = "no-strong-signal"
        if state != "no-strong-signal":
            evidence = spec_material + impl_material
            implementation_alignment.append({
                "kind": "specification-implementation-alignment",
                "capability": link["capability"],
                "state": state,
                "specification_repository": spec_repo,
                "implementation_repositories": sorted({e["repository"] for e in impl_material}),
                "specification_material_change_units": len(spec_material),
                "implementation_material_change_units": len(impl_material),
                "evidence_urls": _evidence_urls(evidence),
            })

    ranked = sorted(
        capability_states.items(),
        key=lambda item: (item[1]["material_change_units"], item[1]["change_units"]),
        reverse=True,
    )
    dominant_capabilities = [capability_id for capability_id, state in ranked if state["change_units"]][:3]
    dominant_themes = [
        {"id": theme, "label": THEME_LABELS.get(theme, theme), "count": count}
        for theme, count in portfolio_themes.most_common(5)
    ]

    material_findings = [f for f in findings if f.get("severity") in {"critical", "high", "medium"}]
    return {
        "schema_version": 1,
        "generated_at": generated_at,
        "model_version": model.get("version", 1),
        "change_units": len(events),
        "material_change_units": sum(e.get("significance") in MATERIAL_LEVELS for e in events),
        "dominant_capabilities": dominant_capabilities,
        "dominant_themes": dominant_themes,
        "capabilities": capability_states,
        "convergences": sorted(convergences, key=lambda item: item["material_change_units"], reverse=True),
        "implementation_alignment": implementation_alignment,
        "attention_signals": asymmetries,
        "review_findings": len(material_findings),
        "unmapped_change_units": len(unmapped_events),
    }


def write_snapshot(snapshot: dict[str, Any], when: datetime | None = None) -> Path:
    when = when or datetime.now(timezone.utc)
    target = ROOT / "data" / "awareness" / when.strftime("%Y/%m/%d.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target
