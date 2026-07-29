from __future__ import annotations
from typing import Any

LEVELS = ("critical", "high", "medium", "low")

def classify(event: dict[str, Any], rule_config: dict[str, Any], repository_weight: str) -> tuple[str, int, list[str]]:
    text = " ".join([
        str(event.get("title", "")),
        str(event.get("body", "")),
        " ".join(event.get("changed_files", []) or []),
    ]).lower()
    score = int(rule_config.get("weights", {}).get(repository_weight, 0))
    reasons: list[str] = []

    for rule in rule_config.get("rules", []):
        event_types = rule.get("event_types")
        if event_types and event.get("event_type") not in event_types:
            continue
        terms = [str(term).lower() for term in rule.get("terms", [])]
        matched = not terms or any(term in text for term in terms)
        if matched:
            score += int(rule.get("score", 0))
            reasons.append(rule.get("description", rule.get("id", "matched rule")))

    thresholds = rule_config.get("thresholds", {})
    for level in LEVELS:
        if score >= int(thresholds.get(level, 0)):
            return level, score, reasons
    return "low", score, reasons
