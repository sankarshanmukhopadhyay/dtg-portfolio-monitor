---
title: Repository discovery
nav_order: 8
permalink: /repository-discovery/
---
# Repository discovery

DTG Portfolio Monitor separates **curated semantic authority** from **dynamic observation authority**.

`config/repositories.yaml` remains the authoritative registry for repositories whose workstream, role, lifecycle, monitoring weight, paths, and portfolio semantics have been explicitly reviewed. `config/repository-discovery.yaml` defines deterministic rules that may admit additional repositories at collection time. A discovered repository can extend the effective observation scope, but it cannot override curated metadata or acquire a portfolio capability merely by being discovered.

> **Discovery grants observation authority; curation grants semantic authority.**

## Admission policy

The scheduled collection run currently trusts two organizational namespaces.

### Trust over IP DTG

Automatic admission is limited to public, non-archived repositories matching:

- owner: `trustoverip`
- repository-name prefix: `dtgwg`

This covers names such as `dtgwg-general`, `dtgwg-cred-tf`, and future `trustoverip/dtgwg*` repositories without requiring a manual registry edit.

### OpenVTC

All public, non-archived repositories owned by `OpenVTC` are eligible for automatic admission. This is organization-wide by design because OpenVTC contains multiple implementation, SDK, infrastructure, governance, and experimental repositories whose names do not share one stable DTG prefix but can still produce relevant implementation evidence.

Existing curated OpenVTC entries remain authoritative for their explicit role, workstream, lifecycle, weight, branch, material-path, and capability semantics. Newly discovered OpenVTC repositories receive observation defaults until curated metadata is added.

Repositories under other owners are not discovery candidates. In particular, repositories owned by `sankarshanmukhopadhyay` are never dynamically admitted merely because their names begin with `dtg` or `dtgwg`. Personal forks, assurance tooling, implementation profiles, and experiments must be added explicitly to `config/repositories.yaml` if there is a reviewed reason to monitor them.

Forks are rejected by default unless explicitly allowlisted.

## Observation versus semantic mapping

The effective registry may contain more repositories than the curated registry. This is expected and is not a configuration defect.

A dynamically discovered repository may:

- appear on `/repositories/`;
- contribute commits, pull requests, issues, releases, and other enabled evidence streams;
- contribute to daily and weekly reports;
- remain intentionally unmapped to a DTG capability until a reviewed curation decision is made.

Unmapped activity is retained as evidence and counted through `unmapped_change_units` in the awareness snapshot. The monitor must not invent capability membership from an organization name, repository name, or discovery source.

Capability mapping therefore remains a governed assertion. Validation requires curated workstreams to map to the portfolio model, while dynamically discovered workstreams may remain unmapped without invalidating the collection run.

## Evidence and auditability

Every discovery run writes:

- `data/repository-discovery.json` — candidate-level admission/rejection decisions and reasons;
- `data/effective-repositories.yaml` — the merged effective registry used by collection and reporting;
- `docs/repositories.md` — the generated human-readable scope page.

This means scope membership is reproducible from policy plus GitHub repository metadata, while semantic mappings remain reproducible from the reviewed curated registry and portfolio model.

## Authority, override, and revocation

Curated entries take precedence over discovered defaults. Dynamic discovery may add an observation target, but only a reviewed change to `config/repositories.yaml` may replace explicit portfolio semantics.

Automatic admission can be revoked by any of the following governed changes:

1. narrow or remove a trusted source rule;
2. add the repository to `policy.exclude_repositories`;
3. remove a fork from `policy.allow_forks`;
4. archive or make the repository private upstream.

The next successful discovery run regenerates the effective registry and `/repositories/` page accordingly.

## Operator workflow

Changes to discovery authority, defaults, or semantic mappings should follow the normal issue → branch → pull request path. Reviewers should verify the policy diff, unit tests, generated discovery evidence, effective repository set, and any proposed capability mapping before merge.

Discovery changes **monitoring scope only**. They do not assert specification status, conformance, assurance, capability membership, authority, or endorsement for a repository.
