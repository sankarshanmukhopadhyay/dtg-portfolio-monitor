from __future__ import annotations
from collections import Counter
from typing import Any
import hashlib
import re

THEMES = {
    "authority-and-delegation": ("authority", "delegation", "delegate", "approval", "permission", "acl", "allowedkeys", "step-up"),
    "credentials-and-proof": ("credential", "issuance", "presentation", "proof", "zkp", "witness"),
    "transport-and-routing": ("transport", "routing", "route", "tsp", "join ceremony"),
    "protocol-and-interoperability": ("protocol", "interoperability", "canonical", "schema", "binding", "conformance", "registry", "migration"),
    "governance-and-lifecycle": ("governance", "lifecycle", "revocation", "membership", "policy"),
    "security-and-privacy": ("security", "privacy", "threat", "attack", "vulnerability", "fail closed"),
    "human-trust-experience": ("experience", "journey", "screen", "onboarding", "htx", "ux", "display"),
    "delivery-and-maintenance": ("changelog", "version", "dependency", "bump", "release", "docs", "documentation", "ci", "workflow"),
}

THEME_LABELS = {
    "authority-and-delegation": "Authority and delegation",
    "credentials-and-proof": "Credentials and proof",
    "transport-and-routing": "Transport and routing",
    "protocol-and-interoperability": "Protocol and interoperability",
    "governance-and-lifecycle": "Governance and lifecycle",
    "security-and-privacy": "Security and privacy",
    "human-trust-experience": "Human trust experience",
    "delivery-and-maintenance": "Delivery and maintenance",
}

SIGNIFICANCE_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def normalise_title(title: str) -> str:
    text = title.lower().strip()
    text = re.sub(r'^(feat|fix|chore|docs|refactor|test|build)(\([^)]*\))?!?:\s*', '', text)
    text = re.sub(r'\s*\(#\d+\)\s*$', '', text)
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return ' '.join(text.split())


def _change_unit_key(repository: str, normalised_title: str) -> str:
    return hashlib.sha256(f"{repository}|{normalised_title}".encode()).hexdigest()[:24]


def consolidate(events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    """Collapse commit/PR representations of one semantic change into one unit.

    The primary record preserves all correlated evidence, linked repositories,
    significance reasons and the strongest observed significance. This makes
    downstream findings operate on review obligations rather than API objects.
    """
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    passthrough: list[dict[str, Any]] = []
    for event in events:
        if event.get('event_type') not in {'commit', 'pull_request'}:
            passthrough.append(event)
            continue
        title_key = normalise_title(event.get('title', ''))
        key = (event['repository'], title_key)
        groups.setdefault(key, []).append(event)

    result = list(passthrough)
    collapsed = 0
    for (repository, title_key), group in groups.items():
        group = sorted(
            group,
            key=lambda e: (e.get('event_type') == 'pull_request', e.get('updated_at', '')),
            reverse=True,
        )
        primary = dict(group[0])
        primary['change_unit_key'] = _change_unit_key(repository, title_key)
        primary['change_unit_size'] = len(group)
        primary['correlated_events'] = [
            {
                'event_type': e['event_type'],
                'url': e['url'],
                'item_id': e['item_id'],
                'event_id': e.get('event_id'),
            }
            for e in group[1:]
        ]
        primary['linked_repositories'] = sorted({
            linked
            for event in group
            for linked in event.get('linked_repositories', [])
        })
        primary['significance_reasons'] = sorted({
            reason
            for event in group
            for reason in event.get('significance_reasons', [])
        })
        strongest = max(
            group,
            key=lambda e: SIGNIFICANCE_ORDER.get(e.get('significance', 'low'), 0),
        )
        primary['significance'] = strongest.get('significance', primary.get('significance'))
        primary['significance_score'] = max(e.get('significance_score', 0) for e in group)
        result.append(primary)
        collapsed += len(group) - 1

    return result, collapsed


def event_themes(event: dict[str, Any]) -> list[str]:
    text = f"{event.get('title', '')} {event.get('body', '')}".lower()
    return [theme for theme, terms in THEMES.items() if any(term in text for term in terms)]


def theme_counts(events: list[dict[str, Any]]) -> list[tuple[str, int]]:
    counts = Counter(theme for event in events for theme in event_themes(event))
    return counts.most_common()
