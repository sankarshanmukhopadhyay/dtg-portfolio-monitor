---
title: Tracked repositories
nav_order: 4
permalink: /repositories/
---
# Tracked repositories

The effective monitoring scope combines the curated registry with repositories admitted by the deterministic discovery policy. Curated metadata always overrides discovered defaults.

**Discovery evidence generated:** 2026-08-26T07:01:42.097333Z  
**Policy:** `config/repository-discovery.yaml`

| Repository | Workstream | Role | Lifecycle | Weight | Admission |
|---|---|---|---|---|---|
| [`OpenVTC/dtg-credentials`](https://github.com/OpenVTC/dtg-credentials) | credentials | implementation-and-examples | active | high | curated |
| [`OpenVTC/openvtc`](https://github.com/OpenVTC/openvtc) | community-platform | implementation | active | high | curated |
| [`OpenVTC/verifiable-trust-infrastructure`](https://github.com/OpenVTC/verifiable-trust-infrastructure) | verifiable-trust-infrastructure | reference-implementation | active | critical | curated |
| [`trustoverip/dtgwg-agent-names-tf`](https://github.com/trustoverip/dtgwg-agent-names-tf) | agent-names | task-force-workspace | active | high | curated |
| [`trustoverip/dtgwg-cred-spec`](https://github.com/trustoverip/dtgwg-cred-spec) | credentials | normative-specification | active | critical | curated |
| [`trustoverip/dtgwg-cred-tf`](https://github.com/trustoverip/dtgwg-cred-tf) | credentials | task-force-workspace | active | high | curated |
| [`trustoverip/dtgwg-general`](https://github.com/trustoverip/dtgwg-general) | coordination | coordination | active | high | curated |
| [`trustoverip/dtgwg-htx-tf`](https://github.com/trustoverip/dtgwg-htx-tf) | human-trust-experience | task-force-workspace | active | high | curated |
| [`trustoverip/dtgwg-rahp-tf`](https://github.com/trustoverip/dtgwg-rahp-tf) | rahp | task-force-workspace | active | high | curated |
| [`trustoverip/dtgwg-rcards-tf`](https://github.com/trustoverip/dtgwg-rcards-tf) | relationship-cards | legacy-or-transition | transitional | low | curated |
| [`trustoverip/dtgwg-trust-tasks-spec`](https://github.com/trustoverip/dtgwg-trust-tasks-spec) | trust-tasks | normative-specification | active | critical | curated |
| [`trustoverip/dtgwg-trust-tasks-tf`](https://github.com/trustoverip/dtgwg-trust-tasks-tf) | trust-tasks | protocol-and-task-specification | active | critical | curated |
| [`trustoverip/dtgwg-ux-tf`](https://github.com/trustoverip/dtgwg-ux-tf) | human-trust-experience | legacy-or-transition | transitional | low | curated |
| [`trustoverip/dtgwg-vds-tf`](https://github.com/trustoverip/dtgwg-vds-tf) | verifiable-data-structures | normative-specification | active | critical | curated |
| [`trustoverip/dtgwg-zkp-tf`](https://github.com/trustoverip/dtgwg-zkp-tf) | zero-knowledge-proofs | implementation-guidance | active | critical | curated |

## Governance boundary

Dynamic discovery is an admission mechanism, not an authority override. `config/repositories.yaml` remains authoritative for explicitly curated metadata. `config/repository-discovery.yaml` defines who may be discovered, naming scope, exclusions, fork policy, and defaults. Removing a source, adding an exclusion, or archiving a repository revokes automatic admission on the next collection run.

Forks are excluded by default to avoid duplicate observation of upstream DTG repositories. A fork must be explicitly allowlisted before it can enter dynamic scope.

## Discovery decisions

Current run: **12 admitted candidate(s)** and **0 rejected candidate(s)**. The full machine-readable decision record is persisted at `data/repository-discovery.json`.

## Cross-specification assurance seams

Composition boundaries remain governed separately in `config/cross-spec-pressure-tests.yaml`; repository discovery changes observation scope only and does not itself assert assurance or conformance.
