---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-10T17:23:51.018098Z  
**Evidence through:** 2026-10-10T17:18:01Z  
**Source revision:** `a56c5a4e4d3c095b9520ab7b1661863c12c179a2` · **Collection run:** `38071428199`  

## Review now

**17 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `18828d1335ff069040c50d46` feat(vtc)!: git-namespace rights are capabilities on the ACL entry — one authority model (VTI-VTC-020, VTI-ACL-035 – 037) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1930) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `529eb5d4991393ffe4741c69` vti-common-v0.37.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vti-common-v0.37.1) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `8d5718ce13e794725aabb9cb` feat(vtc): a subject may relabel its own entry; single-administrator mode is one person under many identifiers (VTI-ACL-052, VTI-APV-022) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1941) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `94d39806fe806db2aa389a10` cnm-cli-v0.27.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/cnm-cli-v0.27.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `a775c9693b223f68a75123e1` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `aa28149c7babc678e9e7412c` feat(vta-sdk)!: wallet sign-in with a trigger link: sign auth/oob grants, enrol UV keys, advertise TrustTaskHTTPS and SignInPortal | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1997) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `bb5f4996fef97c4ed846a065` cnm-cli-v0.27.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/cnm-cli-v0.27.1) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `0ab1aa8e2e70a9099d7354cc` feat: wallet sign-in with a trigger link (VTI 7a, auth/oob) | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/303) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `3b62b0cd590b9b45b3da0de6` chore(deps): Bump @openvtc/trust-tasks from 0.23.0 to 0.23.1 | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/300) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `5f287722cb80cafcb50337ad` feat!: bind every outbound Trust Task to its signer; DIDComm sign-in via challenge and signed authenticate | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/279) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `da3e439ebf70650d0c35d412` feat: sender-bound, purpose-checked Trust Tasks and signed DIDComm sign-in | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/304) |
| **elevated** | `trustoverip/dtgwg-trust-tasks-tf` | `09ccb1d242fb33d91c008f6f` feat(vtc): cooling-off actions, a reduction-pending notice and an offline-write record type | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-trust-tasks-tf/pull/719) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-10C75E7EC928C9AD` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/423) |

## Watch

**8 deterministic watch assertion(s)** · **10 other finding(s)**

- `DTG-A-9D46B03854EC677B` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-5094838CF4BB1FF8` — Governed action specification and implementation are moving together in this window.
- `DTG-A-4AE2C48DAD70CD02` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-F900D8832619A0E1` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-2A826382DEBFAA41` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-C7346CD6487636A6` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-6F5F3C78AAC1EB5E` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-54283C39ABF6648F` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 419 · **Material:** 101 · **Breaking:** 8 · **Tagged releases:** 158 · **Cross-repository:** 52  
**Duplicate representations consolidated:** 178

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 4 | 2 |
| Governed action | **Advancing strongly** | 74 | 22 |
| Implementation and interoperability | **Advancing strongly** | 243 | 52 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 257
- **Protocol and interoperability:** 132
- **Credentials and proof:** 117
- **Authority and delegation:** 90
- **Transport and routing:** 80

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
