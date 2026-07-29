---
title: Methodology
nav_order: 4
---

# Methodology

## Evidence model

Every observed item is normalised into a local event containing its source repository, type, state, timestamps, actor, URL, workstream, significance score, reasons, and explicit references to other monitored repositories.

## Significance

Classification is deterministic. Repository weight establishes the baseline, while visible rules add or subtract points for normative language, authority semantics, interoperability, security, implementation evidence, releases, and likely editorial-only changes.

Scores are review signals. They do not establish the meaning, validity, acceptance, or governance status of upstream work.

## Cross-repository implications

The initial release detects explicit textual references to another monitored repository. Later versions may add concept-level correlation, but any inferred relationship should remain separately identified from directly observed evidence.

## Governance boundary

The system writes only to this repository. It does not automatically file issues or comments upstream.
