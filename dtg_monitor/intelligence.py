from __future__ import annotations
from collections import Counter
from typing import Any
import re

THEMES = {
    "authority-and-delegation": ("authority", "delegation", "delegate", "approval", "permission", "acl"),
    "credentials-and-proof": ("credential", "issuance", "presentation", "proof", "zkp", "witness"),
    "protocol-and-interoperability": ("protocol", "interoperability", "canonical", "schema", "binding", "conformance"),
    "governance-and-lifecycle": ("governance", "lifecycle", "revocation", "membership", "policy"),
    "security-and-privacy": ("security", "privacy", "threat", "attack", "vulnerability"),
    "human-trust-experience": ("experience", "journey", "screen", "onboarding", "htx", "ux"),
}

def normalise_title(title: str) -> str:
    text=title.lower().strip()
    text=re.sub(r'^(feat|fix|chore|docs|refactor|test|build)(\([^)]*\))?:\s*','',text)
    text=re.sub(r'\s*\(#\d+\)\s*$','',text)
    text=re.sub(r'[^a-z0-9]+',' ',text)
    return ' '.join(text.split())

def consolidate(events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    groups: dict[tuple[str,str], list[dict[str,Any]]] = {}
    passthrough=[]
    for event in events:
        if event.get('event_type') not in {'commit','pull_request'}:
            passthrough.append(event); continue
        key=(event['repository'], normalise_title(event.get('title','')))
        groups.setdefault(key,[]).append(event)
    result=list(passthrough); collapsed=0
    for group in groups.values():
        if len(group)==1:
            result.extend(group); continue
        # Prefer PR as the human review unit, otherwise most recently updated.
        group=sorted(group,key=lambda e:(e.get('event_type')=='pull_request',e.get('updated_at','')),reverse=True)
        primary=dict(group[0])
        primary['correlated_events']=[{'event_type':e['event_type'],'url':e['url'],'item_id':e['item_id']} for e in group[1:]]
        primary['change_unit_size']=len(group)
        result.append(primary); collapsed += len(group)-1
    return result, collapsed

def theme_counts(events: list[dict[str, Any]]) -> list[tuple[str,int]]:
    counts=Counter()
    for event in events:
        text=f"{event.get('title','')} {event.get('body','')}".lower()
        for theme,terms in THEMES.items():
            if any(term in text for term in terms): counts[theme]+=1
    return counts.most_common()
