---
title: Methodology
nav_order: 8
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


## Portfolio semantics and situational awareness

`config/portfolio-model.yaml` declares how monitored workstreams are grouped into DTG capabilities and which capability relationships the monitor is allowed to examine. This model is analytical rather than normative: it documents the monitor's interpretation boundary so that portfolio-level conclusions are reviewable rather than implicit.

The awareness engine operates on consolidated change units and produces four classes of signal:

- **Capability pulse** — advancing strongly, advancing, active, or quiet, based on deterministic activity thresholds.
- **Cross-capability convergence** — material activity on both sides of a declared capability relationship.
- **Specification/implementation alignment** — whether declared specification and implementation repositories are moving together or showing a strong asymmetry in the observation window.
- **Attention signals** — related capabilities where one has material movement while the other is quiet.

These are coordination signals, not project-health grades. In particular, **quiet is not treated as failure, dormancy, or blockage**.

Every awareness run is persisted as JSON under `data/awareness/`. The DTG Domain Brief and dashboard are renderings of that machine-readable snapshot; the Portfolio Status remains the canonical event-level evidence view.

## Interpretation boundary

The monitor intentionally does not infer causation, official architectural status, implementation conformance, consensus, or upstream governance decisions from repository activity. A finding such as "moving together" means correlated movement within the declared monitoring model and observation window. It does not assert that one repository caused another to change or that the relevant upstream communities have formally aligned.
