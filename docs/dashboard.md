---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-05T04:36:54.016429Z  
**Evidence through:** 2026-09-05T01:51:29Z  
**Source revision:** `28d25bff48ad0f3b74bc861f2f42208f76db6813` · **Collection run:** `33944951866`  

## Review now

**15 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/dtg-credentials` | `69521277d5af9e7d8beacc3d` feat: add the VAC and VDC credential types | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/15) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `149a49aa1cb3037f0cfb0f0f` feat(vta): implement vta/credentials/list, and check the vault/credentials family | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1235) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `4c9cc4d721ef21aaed00d14f` feat(vta): discharge the backup family's spec debt, and audit what it was hiding | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1239) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `6bf9515457f4bb0cb381ee0b` feat(rooms): group custody, so a key-holder still has the group tomorrow | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1248) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `9b38c4f3af53eb6f1669b50e` vta-service-v0.23.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-service-v0.23.1) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `b506e3491fe0d4776198a570` feat(rooms): data rooms end to end — storage, dispatch, verification, MLS, and a host | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1237) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `cb2470b45bf486b6af80ecd3` feat(rooms): the presentation oracle, so an agent never holds its human's credentials | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1247) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `e121b18291ff4d8f4d55fd81` chore: release | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1232) |
| **elevated** | `OpenVTC/vta-agent-memory` | `ca518efb8b8085c52b893898` feat(fence): treat recalled memory as untrusted data, not instructions | potentially-breaking | [source](https://github.com/OpenVTC/vta-agent-memory/pull/13) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `8ef75e6e2fa45fa9a9c88ca0` feat(rp-login): add walletProfile — ask who this site knows you as | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/145) |
| **elevated** | `trustoverip/dtgwg-cred-spec` | `a3b65e64b856c9d421a241ce` feat: replace the four VID types with a declared correlation scope (pairwise | directed | public) | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-cred-spec/pull/30) |
| **elevated** | `trustoverip/dtgwg-cred-spec` | `b998f02671f5d76dce3a85be` Name the asymmetric edge: two halves may declare different correlation scopes | potentially-breaking | [source](https://github.com/trustoverip/dtgwg-cred-spec/issues/23) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-9A43C3E5241EAA86` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/273) |

## Watch

**8 deterministic watch assertion(s)** · **7 other finding(s)**

- `DTG-A-5FFCEB6ABFFD6521` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-36789DACC9B77348` — Governed action specification and implementation are moving together in this window.
- `DTG-A-DE5E7693E768570F` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-6E68B24720AEF2CF` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-D60F976DE0D3E723` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-002EC42001184EBB` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-195CC0BE6F3B81E7` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.
- `DTG-A-AF53DC9408F1ADE8` — Governed action has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 285 · **Material:** 99 · **Breaking:** 1 · **Tagged releases:** 57 · **Cross-repository:** 36  
**Duplicate representations consolidated:** 139

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 28 | 15 |
| Governed action | **Advancing strongly** | 62 | 18 |
| Implementation and interoperability | **Advancing strongly** | 83 | 34 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 203
- **Protocol and interoperability:** 118
- **Credentials and proof:** 102
- **Transport and routing:** 83
- **Authority and delegation:** 80

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
