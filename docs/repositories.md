---
title: Tracked repositories
nav_order: 4
permalink: /repositories/
---
# Tracked repositories

| Repository | Workstream | Role | Lifecycle | Weight |
|---|---|---|---|---|
| [`trustoverip/dtgwg-trust-tasks-tf`](https://github.com/trustoverip/dtgwg-trust-tasks-tf) | trust-tasks | protocol-and-task-specification | active | critical |
| [`trustoverip/dtgwg-trust-tasks-spec`](https://github.com/trustoverip/dtgwg-trust-tasks-spec) | trust-tasks | normative-specification | active | critical |
| [`trustoverip/dtgwg-htx-tf`](https://github.com/trustoverip/dtgwg-htx-tf) | human-trust-experience | task-force-workspace | active | high |
| [`trustoverip/dtgwg-ux-tf`](https://github.com/trustoverip/dtgwg-ux-tf) | human-trust-experience | legacy-or-transition | transitional | low |
| [`trustoverip/dtgwg-general`](https://github.com/trustoverip/dtgwg-general) | coordination | coordination | active | high |
| [`trustoverip/dtgwg-cred-spec`](https://github.com/trustoverip/dtgwg-cred-spec) | credentials | normative-specification | active | critical |
| [`trustoverip/dtgwg-zkp-tf`](https://github.com/trustoverip/dtgwg-zkp-tf) | zero-knowledge-proofs | implementation-guidance | active | critical |
| [`trustoverip/dtgwg-cred-tf`](https://github.com/trustoverip/dtgwg-cred-tf) | credentials | task-force-workspace | active | high |
| [`trustoverip/dtgwg-rahp-tf`](https://github.com/trustoverip/dtgwg-rahp-tf) | rahp | task-force-workspace | active | high |
| [`trustoverip/dtgwg-rcards-tf`](https://github.com/trustoverip/dtgwg-rcards-tf) | relationship-cards | legacy-or-transition | transitional | low |
| [`trustoverip/dtgwg-vds-tf`](https://github.com/trustoverip/dtgwg-vds-tf) | verifiable-data-structures | normative-specification | active | critical |
| [`trustoverip/dtgwg-agent-names-tf`](https://github.com/trustoverip/dtgwg-agent-names-tf) | agent-names | task-force-workspace | active | high |
| [`OpenVTC/dtg-credentials`](https://github.com/OpenVTC/dtg-credentials) | credentials | implementation-and-examples | active | high |
| [`OpenVTC/openvtc`](https://github.com/OpenVTC/openvtc) | community-platform | implementation | active | high |
| [`OpenVTC/verifiable-trust-infrastructure`](https://github.com/OpenVTC/verifiable-trust-infrastructure) | verifiable-trust-infrastructure | reference-implementation | active | critical |

The YAML registry is the source of truth. Changes to monitoring scope should be made in `config/repositories.yaml` and validated before merge.


## Cross-specification assurance seams

The portfolio declares eight runnable composition boundaries in `config/cross-spec-pressure-tests.yaml`. This registry is **discovery metadata**, not assessment evidence. It records the evidence grade and points DTG users to RAHP Toolkit's dedicated DTG launcher while retaining the generic profile-driven workflow as the ecosystem-neutral execution surface. The optional DTG profile owns the composition data; RAHP core remains ecosystem-neutral and RAHP Toolkit remains the execution authority.

| Composition | Priority | Readiness |
|---|---:|---|
| Trust Tasks × Credential Specification | P0 | **Runnable** |
| Credential Specification × ZKP | P0 | Candidate |
| Credential Specification × VDS | P0 | Candidate |
| Trust Tasks × ZKP | P0 | Candidate |
| Trust Tasks × VDS | P1 | Candidate |
| ZKP × VDS | P1 | Candidate |
| Agent Names × Trust Tasks | P1 | Candidate |
| Agent Names × Credential Specification | P1 | Candidate |

A `Runnable` seam has a reviewed composed corpus and durable assessment in RAHP and can be invoked manually through the RAHP GitHub Actions workflow. `Candidate` means the architectural seam is declared but cannot be run until the RAHP corpus and evidence baseline are added. Manual execution publishes a durable RAHP review issue suitable for WG circulation and contains upstream-ready issue candidates for findings that require specification changes.
