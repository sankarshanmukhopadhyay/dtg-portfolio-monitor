---
title: Repository discovery
nav_order: 8
permalink: /repository-discovery/
---
# Repository discovery

DTG Portfolio Monitor separates **curated scope authority** from **dynamic scope discovery**.

`config/repositories.yaml` remains the authoritative registry for repositories whose workstream, role, lifecycle, monitoring weight, or paths have been explicitly curated. `config/repository-discovery.yaml` defines deterministic rules that may admit additional repositories at collection time. A discovered repository can extend the effective scope, but it cannot override metadata already declared in the curated registry.

## Admission policy

The scheduled collection run enumerates repositories for each configured source owner and evaluates each repository against machine-readable policy. The initial policy admits public, non-archived repositories whose names match the declared prefixes:

- `trustoverip/dtgwg-*`;
- `OpenVTC/dtg-*`;
- `sankarshanmukhopadhyay/dtg-*`.

Forks are rejected by default unless their full repository name is listed in `policy.allow_forks`. The monitor repository itself is explicitly excluded to prevent self-observation.

## Evidence and auditability

Every discovery run writes:

- `data/repository-discovery.json` — candidate-level admission/rejection decisions and reasons;
- `data/effective-repositories.yaml` — the merged effective registry used by collection and reporting;
- `docs/repositories.md` — the generated human-readable scope page.

This means scope membership is reproducible from policy plus GitHub repository metadata, and each rejection is explainable by a stable reason such as `explicitly-excluded`, `private-repository`, `archived-repository`, or `fork-not-allowlisted`.

## Authority, override, and revocation

Curated entries take precedence over discovered defaults. This is the authority boundary: dynamic discovery may add an observation target, but only a reviewed change to `config/repositories.yaml` may replace its explicit portfolio semantics.

Automatic admission can be revoked by any of the following governed changes:

1. remove or narrow a discovery source/prefix;
2. add the repository to `policy.exclude_repositories`;
3. remove a fork from `policy.allow_forks`;
4. archive or make the repository private upstream.

The next successful discovery run regenerates the effective registry and `/repositories/` page accordingly.

## Operator workflow

Changes to discovery authority or defaults should follow the normal issue → branch → pull request path. Reviewers should verify the policy diff, unit tests, generated discovery evidence, and the resulting effective repository set before merge.

Discovery changes **monitoring scope only**. They do not assert specification status, conformance, assurance, authority, or endorsement for a repository.
