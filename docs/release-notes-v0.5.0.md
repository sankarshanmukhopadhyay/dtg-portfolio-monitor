---
title: Release notes v0.5.0
nav_exclude: true
---
# v0.5.0 — Decision-grade Portfolio Review

v0.5.0 advances DTG Portfolio Monitor from evidence-backed observation toward deterministic decision support while preserving its independent, non-authoritative governance boundary.

## Highlights

- **Change-unit findings:** pull requests and their correlated merge commits are consolidated before findings are generated, reducing duplicate review obligations while preserving every source URL.
- **Finding lifecycle:** findings now carry stable fingerprints, lifecycle state, review status, authority, disposition, related findings and successor metadata.
- **Governed disposition ledger:** non-open finding states persist across collection runs only when an authorized decision is recorded in `config/finding-dispositions.yaml` with rationale, timestamp and evidence.
- **Decision semantics:** materiality, review urgency and assurance impact are distinct signals. High materiality no longer automatically means urgent review.
- **Machine-addressable assertions:** specification/implementation alignment, cross-capability convergence and related-capability asymmetry are emitted as deterministic assertions with stable IDs and evidence URLs.
- **Decision-first UX:** the Domain Brief and dashboard lead with decision findings, review-required assertions, watch items and disposed findings before portfolio movement and raw evidence.
- **Observation provenance:** generated awareness now records evidence-through time, source revision, workflow run and publication state.
- **Bounded evidence history:** daily events, findings and awareness snapshots are pruned according to a declared calendar-month retention policy while weekly summaries and upstream source URLs remain available.
- **Release governance:** `VERSION`, Python package metadata and `dtg_monitor.__version__` are required to agree; GitHub Actions validates tests and the built site before tagging and publishing the release.

## Governance boundary

This release does **not** invoke RAHP or any external assurance execution workflow. It does not automatically file issues, comments or changes in monitored upstream repositories. Assertions and findings remain deterministic review signals rather than declarations of upstream consensus, conformance or failure.

## Evidence and validation

The release workflow requires:

- configuration/schema validation;
- the complete Python unit-test suite;
- a successful Jekyll documentation build;
- published-route validation;
- execution from the exact current `main` revision;
- synchronized version declarations;
- absence of a pre-existing release tag.

The workflow then creates the annotated `v0.5.0` tag and GitHub Release from that validated revision.

## Upgrade notes

Existing v0.4 consumers may continue reading `severity`; in v0.5 it is retained as a compatibility alias for finding materiality. New integrations should prefer `materiality`, `urgency`, `assurance_impact`, `fingerprint`, `state`, and the schema-v2 awareness assertion model.
