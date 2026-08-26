---
title: Repository discovery
nav_order: 8
permalink: /repository-discovery/
---
# Repository discovery

DTG Portfolio Monitor separates **curated scope authority** from **dynamic scope discovery**.

`config/repositories.yaml` remains the authoritative registry for repositories whose workstream, role, lifecycle, monitoring weight, or paths have been explicitly curated. `config/repository-discovery.yaml` defines deterministic rules that may admit additional repositories at collection time. A discovered repository can extend the effective scope, but it cannot override metadata already declared in the curated registry.

## Admission policy

The scheduled collection run enumerates repositories only from the `trustoverip` organization and evaluates repository names against the official DTG working-group namespace. Automatic admission is limited to public, non-archived repositories matching:

- owner: `trustoverip`
- repository-name prefix: `dtgwg`

This intentionally covers names such as `dtgwg-general`, `dtgwg-cred-tf`, and future `trustoverip/dtgwg*` repositories without requiring a manual registry edit.

Repositories under other owners are not discovery candidates. In particular, repositories owned by `sankarshanmukhopadhyay` are never dynamically admitted merely because their names begin with `dtg` or `dtgwg`. Personal forks, assurance tooling, implementation profiles, and experiments must be added explicitly to `config/repositories.yaml` if there is a reviewed reason to monitor them.

Existing OpenVTC repositories remain curated entries. They are not part of automatic discovery.

Forks are rejected by default unless explicitly allowlisted. This is a secondary control; the primary authority boundary is the `trustoverip` owner plus `dtgwg*` namespace.

## Evidence and auditability

Every discovery run writes:

- `data/repository-discovery.json` — candidate-level admission/rejection decisions and reasons;
- `data/effective-repositories.yaml` — the merged effective registry used by collection and reporting;
- `docs/repositories.md` — the generated human-readable scope page.

This means scope membership is reproducible from policy plus GitHub repository metadata.

## Authority, override, and revocation

Curated entries take precedence over discovered defaults. Dynamic discovery may add an observation target, but only a reviewed change to `config/repositories.yaml` may replace explicit portfolio semantics.

Automatic admission can be revoked by any of the following governed changes:

1. narrow or remove the `trustoverip` discovery source/prefix;
2. add the repository to `policy.exclude_repositories`;
3. remove a fork from `policy.allow_forks`;
4. archive or make the repository private upstream.

The next successful discovery run regenerates the effective registry and `/repositories/` page accordingly.

## Operator workflow

Changes to discovery authority or defaults should follow the normal issue → branch → pull request path. Reviewers should verify the policy diff, unit tests, generated discovery evidence, and the resulting effective repository set before merge.

Discovery changes **monitoring scope only**. They do not assert specification status, conformance, assurance, authority, or endorsement for a repository.
