---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-21T17:19:18.326513Z  
**Evidence through:** 2026-10-21T17:11:19Z  
**Source revision:** `83de164be660b82e0bde2ef0ee9160d110b45e9c` · **Collection run:** `39642407106`  

## Review now

**49 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/openvtc` | `2a5769f69aaf67636efe156b` fix(vetting)!: say when a vetter credential is refused, not only in the debug log | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/493) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `02cb514c440bf1b3d1fb4ef3` vti-common-v0.45.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vti-common-v0.45.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `03ed5e52452e39afa501e02d` vta-service-v0.61.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-service-v0.61.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `044add6d73492d7afedf368a` vtc-client-v0.24.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vtc-client-v0.24.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `0883f0a9d45e86e0d6742f1c` feat(rooms)!: rooms/revocations/{put,get} — a host refuses what the room withdrew, at once | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2173) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `176fb15f1c0d72e134a30128` cnm-cli-v0.37.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/cnm-cli-v0.37.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1a1152510cfda3e78869be54` feat(vta): rooms/owner/group/renew renews a sealed room; pnm rooms renew refuses a sealed room | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2112) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1d5c7aef616605f3a972dc2e` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `20bc88fe966b21280abf4c1b` feat(rooms)!: rooms/keys/act 0.4 — a member reads each offered room's description (vtc/rooms/offers/list 0.2) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2183) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3474aeed99edbff13c5c4111` feat!: TEE first-boot enrols the claim DID as the bootstrap admin instead of minting a key (#2066) (#2182) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/commit/989c67e6ef8b35cb459aed93f2c2263db511ef83) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b5cd4abd5496f98503371ec` feat(vtc)!: community-room details administrators can see, edit and track (trust-tasks-tf #805) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2170) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b87559a2585b735cd19f588` vta-cli-common-v0.42.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-cli-common-v0.42.0) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-4F18C56F43BD4E65` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/493) |

## Watch

**8 deterministic watch assertion(s)** · **30 other finding(s)**

- `DTG-A-4D001AE994E33673` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-57972AEA42862C96` — Governed action specification and implementation are moving together in this window.
- `DTG-A-D351C323AAAD6732` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-159ADF90CC3DC3C2` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-FE7A477EFDF2CACB` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-559AEBBF375A2419` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-28096280024D8ABB` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-4054472E47F91C94` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 739 · **Material:** 207 · **Breaking:** 39 · **Tagged releases:** 301 · **Cross-repository:** 121  
**Duplicate representations consolidated:** 345

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 53 | 13 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 281 | 62 |
| Implementation and interoperability | **Advancing strongly** | 300 | 102 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 394
- **Credentials and proof:** 274
- **Protocol and interoperability:** 258
- **Authority and delegation:** 196
- **Governance and lifecycle:** 196

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
