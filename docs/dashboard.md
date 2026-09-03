---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-03T04:38:38.284128Z  
**Evidence through:** 2026-09-02T22:08:06Z  
**Source revision:** `3309ad9206e361c9de4d4a1daf09dafb35ab2203` · **Collection run:** `33715737818`  

## Review now

**18 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/dtg-credentials` | `69521277d5af9e7d8beacc3d` feat: add the VAC and VDC credential types | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/15) |
| **elevated** | `OpenVTC/openvtc` | `1424d521e64b748aad17908c` feat(devices): send this install's current name on the heartbeat | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/264) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `149a49aa1cb3037f0cfb0f0f` feat(vta): implement vta/credentials/list, and check the vault/credentials family | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1235) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `4c9cc4d721ef21aaed00d14f` feat(vta): discharge the backup family's spec debt, and audit what it was hiding | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1239) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `50fd344cc3fa0524b54f4368` pnm-cli-v0.14.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/pnm-cli-v0.14.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `9b38c4f3af53eb6f1669b50e` vta-service-v0.23.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-service-v0.23.1) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `b2352b42ce91d91f1375e627` vta-service-v0.22.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-service-v0.22.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `b506e3491fe0d4776198a570` feat(rooms): data rooms end to end — storage, dispatch, verification, MLS, and a host | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1237) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `e121b18291ff4d8f4d55fd81` chore: release | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1232) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `ea833e9560c87a8d01bda08b` vta-sdk-v0.30.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-sdk-v0.30.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `f5a7e52ff8f5d90f5201df6c` vti-common-v0.15.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vti-common-v0.15.0) |
| **elevated** | `OpenVTC/vta-agent-memory` | `ca518efb8b8085c52b893898` feat(fence): treat recalled memory as untrusted data, not instructions | potentially-breaking | [source](https://github.com/OpenVTC/vta-agent-memory/pull/13) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-3962763FA8F79FE7` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/259) |

## Watch

**8 deterministic watch assertion(s)** · **17 other finding(s)**

- `DTG-A-8306AADB72E36FC1` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-DE1B7FA8C16CDFC8` — Governed action specification and implementation are moving together in this window.
- `DTG-A-3E7E1C62DCE2F467` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-73A262ACDCAED52A` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-D46D259537B53EB1` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-1C75653DA0379627` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-DCBB6910817802D1` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.
- `DTG-A-F7B5116F80E82805` — Governed action has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 364 · **Material:** 148 · **Breaking:** 14 · **Tagged releases:** 112 · **Cross-repository:** 46  
**Duplicate representations consolidated:** 199

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 31 | 16 |
| Governed action | **Advancing strongly** | 86 | 24 |
| Implementation and interoperability | **Advancing strongly** | 180 | 86 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 254
- **Protocol and interoperability:** 177
- **Credentials and proof:** 150
- **Transport and routing:** 118
- **Authority and delegation:** 102

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
