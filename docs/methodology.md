---
title: Methodology
nav_order: 8
permalink: /methodology/
---
# Methodology

## Evidence model

Every observed item is normalised into a local event containing its source repository, type, state, timestamps, actor, URL, workstream, significance score, reasons, and explicit references to other monitored repositories.

The monitor then consolidates commit and pull-request representations that describe the same logical change. **Findings are generated from these consolidated change units**, not independently from every GitHub API object. Correlated source URLs remain attached as evidence.

## Materiality is not urgency

Classification remains deterministic. Repository weight establishes the baseline, while visible rules add or subtract points for normative language, authority semantics, interoperability, security, implementation evidence, releases, and likely editorial-only changes.

The v0.5 model separates three concepts:

| Field | Question answered |
|---|---|
| `materiality` | How significant is the observed change? |
| `urgency` | How quickly should a reviewer examine it? |
| `assurance_impact` | Does the change potentially affect an assurance or interoperability contract? |

`severity` is retained as a compatibility alias for materiality for v0.4 consumers. A high-materiality event is not automatically urgent, and a collection gap can be urgent without being a critical architectural change.

Scores and bands are review signals. They do not establish the meaning, validity, acceptance, or governance status of upstream work.

## Finding identity and lifecycle

Every finding has a stable `fingerprint` derived from its semantic kind, repository and subject. Observation time is deliberately excluded so that the same unresolved obligation can be recognized across runs.

The lifecycle vocabulary is:

- `open`
- `resolved`
- `superseded`
- `duplicate`
- `accepted-risk`
- `not-applicable`

A disposition is not inferred from inactivity. It requires an explicit review decision with authority, rationale and supporting evidence. The generated finding envelope therefore reserves `authority`, `disposition`, `related_findings`, and `successor_finding` fields even when no human disposition has yet been recorded.

## Cross-repository implications

The monitor detects explicit textual references to another monitored repository and also evaluates declared capability and implementation relationships. Direct references remain distinguishable from higher-level analytical assertions.

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

A single logical change may appear in GitHub as both a commit and a pull request. The monitor consolidates matching representations into one change unit while preserving correlated evidence URLs, the strongest significance level, all significance reasons, and all linked monitored repositories. This prevents activity counts and findings from overstating the amount of distinct change.

## Portfolio semantics and machine-addressable assertions

`config/portfolio-model.yaml` declares how monitored workstreams are grouped into DTG capabilities and which capability relationships the monitor is allowed to examine. This model is analytical rather than normative: it documents the monitor's interpretation boundary so that portfolio-level conclusions are reviewable rather than implicit.

The awareness engine operates on consolidated change units and produces:

- **Capability pulse** — advancing strongly, advancing, active, or quiet, based on deterministic activity thresholds.
- **Cross-capability convergence** — material activity on both sides of a declared capability relationship.
- **Specification/implementation alignment** — whether declared specification and implementation repositories are moving together or showing a strong asymmetry in the observation window.
- **Attention signals** — related capabilities where one has material movement while the other is quiet.

Each material portfolio conclusion is also persisted as a machine-addressable assertion with:

- stable `assertion_id`;
- assertion `kind` and `subject`;
- deterministic `state`;
- `review_class` of `review-required` or `watch`;
- direct evidence URLs;
- quantitative metrics where applicable;
- `confidence: deterministic`.

An implementation-ahead or specification-ahead assertion is review-required because it represents an observable coordination asymmetry. A moving-together assertion is a watch signal. Neither is an automatic finding of failure.

## Decision-first presentation

The generated dashboard and Domain Brief present information in this order:

1. decision findings;
2. review-required assertions;
3. watch assertions;
4. recently disposed findings;
5. portfolio movement;
6. raw event evidence.

This preserves the complete evidence trail while reducing the operator burden of scanning hundreds of source events before discovering what needs attention.

## Provenance and freshness

Every awareness snapshot records the evidence-through timestamp and, when generated in GitHub Actions, the workflow source revision, workflow run identifier and repository. Rendered pages expose this metadata so a reader can determine which code revision produced the interpretation.

Generated snapshots are versioned evidence, but Git is not treated as an unbounded warehouse. `config/report-settings.yaml` defines a calendar-month retention window for daily event, finding and awareness snapshots. Weekly summaries and upstream GitHub source URLs preserve longer-lived navigability.

## Governance boundary

The system writes only to this repository. It does not automatically file issues, comments, or changes upstream. It also does not execute external assurance tooling as part of the v0.5 model.

## Interpretation boundary

The monitor intentionally does not infer causation, official architectural status, implementation conformance, consensus, or upstream governance decisions from repository activity. A finding or assertion means only what its declared deterministic rule and evidence support. **Quiet is not treated as failure, dormancy, or blockage.**
