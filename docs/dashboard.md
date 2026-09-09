---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-09T16:43:52.734424Z  
**Evidence through:** 2026-09-09T16:30:05Z  
**Source revision:** `dd820b728c96c0f2f31fa32ac71fa73c1731d7e2` · **Collection run:** `34378377270`  

## Review now

**58 decision finding(s)** · **0 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/dtg-credentials` | `01c0b3e160885ecb9f818a13` feat!: a VAC is not a bearer credential; remove `audience` | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/21) |
| **elevated** | `OpenVTC/dtg-credentials` | `034f21a5e8d61d0592574ad1` feat: set `credentialStatus` on a credential being built; `PartialEq` on the type | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/24) |
| **elevated** | `OpenVTC/dtg-credentials` | `506f342e3c98d41469c9c2b5` Working Draft 02: digest encoding, VAC parent digests, and the VDC | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/20) |
| **elevated** | `OpenVTC/dtg-credentials` | `69521277d5af9e7d8beacc3d` feat: add the VAC and VDC credential types | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/15) |
| **elevated** | `OpenVTC/dtg-credentials` | `70623bd0786b0afdf672cad3` delegation::verify_chain takes no presenter, so a VDC is still a bearer credential | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/issues/23) |
| **elevated** | `OpenVTC/dtg-credentials` | `ef69e5f150b8a98a45231c66` Add the delegation credential (VDC) to the catalog | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/issues/10) |
| **elevated** | `OpenVTC/openvtc` | `7ab9b1e08572bb0c2e88b7eb` feat(persona): read what each face presents, and say when we could not ask | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/275) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1419153e5f85cc1bc1cc9c32` feat(provision): let a caller ask for an unrestricted admin, and say what it got | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1303) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `149a49aa1cb3037f0cfb0f0f` feat(vta): implement vta/credentials/list, and check the vault/credentials family | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1235) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `14e6377f4f573da540c8880f` vtc-client-v0.5.2 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vtc-client-v0.5.2) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1564aaed5d45b4de6943beae` fix(rooms)!: a presentation is bound to its presenter — and dtg-credentials 0.6 → 0.9.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1356) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `15a41317f5d207a5f3e820b5` feat(rooms)!: cut over to present/0.2 and issue-authority/0.2 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1365) |

## Watch

**9 deterministic watch assertion(s)** · **15 other finding(s)**

- `DTG-A-F9DB6C919750A1BE` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-8DEA9DC4DA1FD9CB` — Governed action specification and implementation are moving together in this window.
- `DTG-A-B78E5807F5D68C40` — Governed action specification and implementation are moving together in this window.
- `DTG-A-AD8AA81D8F7BDFA3` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-9D422C652BB0697D` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-E7A485DAFA2234F8` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-618B9743753B4257` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-DC588D2E5E609776` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 690 · **Material:** 227 · **Breaking:** 25 · **Tagged releases:** 191 · **Cross-repository:** 100  
**Duplicate representations consolidated:** 315

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 46 | 32 |
| Governed action | **Advancing strongly** | 208 | 50 |
| Implementation and interoperability | **Advancing strongly** | 227 | 100 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 446
- **Protocol and interoperability:** 287
- **Credentials and proof:** 251
- **Authority and delegation:** 213
- **Governance and lifecycle:** 145

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
