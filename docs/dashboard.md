---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-19T18:45:44.334466Z  
**Evidence through:** 2026-10-19T16:17:12Z  
**Source revision:** `c4aaa264bf36a431d84594b289c3290ad1b548ea` · **Collection run:** `39304995755`  

## Review now

**50 decision finding(s)** · **1 review-required assertion(s)**

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
| `DTG-A-1CB79460DC45D417` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/493) |

## Watch

**8 deterministic watch assertion(s)** · **20 other finding(s)**

- `DTG-A-F20B7A337F2CB9BA` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-746E79D6A8393F1B` — Governed action specification and implementation are moving together in this window.
- `DTG-A-738E37012D39E893` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-3D33B40FEBBF2E8C` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-30C892BA98A120DB` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-EA3DF4D203AC20C8` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-7539315B82097BB4` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-AFCEF8D81CCABA50` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 783 · **Material:** 202 · **Breaking:** 44 · **Tagged releases:** 332 · **Cross-repository:** 119  
**Duplicate representations consolidated:** 335

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 49 | 5 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 5 |
| Governed action | **Advancing strongly** | 261 | 66 |
| Implementation and interoperability | **Advancing strongly** | 358 | 103 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 431
- **Credentials and proof:** 283
- **Protocol and interoperability:** 266
- **Authority and delegation:** 185
- **Governance and lifecycle:** 183

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
