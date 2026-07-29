---
title: Methodology
nav_order: 6
permalink: /methodology/
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
## Significance bands and signal tags

The report displays the configured score bands once near the top of the page. With the current rules, **Critical** is 80 or above, **High** is 55–79, **Medium** is 25–54, and **Low** is below 25. The source of truth remains `config/significance-rules.yaml`.

Compact tags make repeated signals scannable in the event register:

| Tag | Meaning |
|---|---|
| `NORM` | Normative requirement language changed |
| `AUTH` | Authority, delegation, approval, or revocation semantics |
| `INTEROP` | Interoperability, canonicalisation, conformance, or protocol behaviour |
| `SEC` | Security, privacy, threat, or vulnerability relevance |
| `IMPL` | Implementation or production evidence |
| `RELEASE` | Published release or tag |
| `DOCS` | Likely editorial or documentation-only change |

A **BREAKING** marker is derived from the conventional-commit `!` syntax in a change title. It is an implementer-review flag, not proof that upstream maintainers have published a migration requirement.

## Consolidated evidence

A single logical change may appear in GitHub as both a commit and a pull request. The monitor consolidates matching representations into one change unit while preserving source-count evidence. This prevents activity counts and the event register from overstating the amount of distinct change.

