---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-09T18:25:04.322236Z  
**Evidence through:** 2026-10-09T16:57:30Z  
**Source revision:** `b9d88d53e3aa89fae284a03f0cc9d5531804a332` · **Collection run:** `37972914564`  

## Review now

**18 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `18828d1335ff069040c50d46` feat(vtc)!: git-namespace rights are capabilities on the ACL entry — one authority model (VTI-VTC-020, VTI-ACL-035 – 037) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1930) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `529eb5d4991393ffe4741c69` vti-common-v0.37.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vti-common-v0.37.1) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `8d5718ce13e794725aabb9cb` feat(vtc): a subject may relabel its own entry; single-administrator mode is one person under many identifiers (VTI-ACL-052, VTI-APV-022) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1941) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `94d39806fe806db2aa389a10` cnm-cli-v0.27.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/cnm-cli-v0.27.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `a775c9693b223f68a75123e1` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `bb5f4996fef97c4ed846a065` cnm-cli-v0.27.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/cnm-cli-v0.27.1) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `da705532743623e49813e11f` fix(vtc)!: removing an administrator, lowering the consent threshold and changing authority policy take a second party (VTI-APV-019, VTI-APV-020, VTI-VTC-022) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1917) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `f4cdc35d8f2c782f247c295f` feat(vtc): single-administrator mode, set at install, for communities with one administrator (VTI-APV-022) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1925) |
| **elevated** | `trustoverip/dtgwg-trust-tasks-tf` | `09ccb1d242fb33d91c008f6f` feat(vtc): cooling-off actions, a reduction-pending notice and an offline-write record type | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-trust-tasks-tf/pull/719) |
| **elevated** | `trustoverip/dtgwg-trust-tasks-tf` | `1c24693b39b565b29637f2f6` trust-tasks-rs-v0.27.1 | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-trust-tasks-tf/releases/tag/trust-tasks-rs-v0.27.1) |
| **elevated** | `trustoverip/dtgwg-trust-tasks-tf` | `50a540262a1b6fc308cace8f` vtc/members/update/0.1: publishConsent may be withdrawn by an administrator, never granted — add consentGrantForbidden | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/737) |
| **elevated** | `trustoverip/dtgwg-trust-tasks-tf` | `6ec931acd09d29e7f7e0c409` docs(git-ns): single-administrator mode may waive the self-grant rule | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-trust-tasks-tf/pull/725) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-10C75E7EC928C9AD` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/423) |

## Watch

**8 deterministic watch assertion(s)** · **8 other finding(s)**

- `DTG-A-9D46B03854EC677B` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-F29F44311EC1FBCA` — Governed action specification and implementation are moving together in this window.
- `DTG-A-01C6E8EE0F680156` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-D20B840A53756C86` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-A476C87351FD62DA` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-C7346CD6487636A6` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-FBE046FD3ED11A4D` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-54283C39ABF6648F` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 441 · **Material:** 106 · **Breaking:** 10 · **Tagged releases:** 184 · **Cross-repository:** 46  
**Duplicate representations consolidated:** 199

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 5 | 2 |
| Governed action | **Advancing strongly** | 97 | 25 |
| Implementation and interoperability | **Advancing strongly** | 243 | 54 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 252
- **Protocol and interoperability:** 131
- **Credentials and proof:** 122
- **Authority and delegation:** 102
- **Transport and routing:** 81

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
