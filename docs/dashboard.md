---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-18T04:41:53.718764Z  
**Evidence through:** 2026-10-18T04:37:33Z  
**Source revision:** `0bd151e88110e70326435d618c7c412446d2ec9f` · **Collection run:** `39097875488`  

## Review now

**48 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/openvtc` | `2a5769f69aaf67636efe156b` fix(vetting)!: say when a vetter credential is refused, not only in the debug log | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/493) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `02cb514c440bf1b3d1fb4ef3` vti-common-v0.45.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vti-common-v0.45.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `03ed5e52452e39afa501e02d` vta-service-v0.61.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-service-v0.61.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `044add6d73492d7afedf368a` vtc-client-v0.24.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vtc-client-v0.24.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `0883f0a9d45e86e0d6742f1c` feat(rooms)!: rooms/revocations/{put,get} — a host refuses what the room withdrew, at once | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2173) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1a1152510cfda3e78869be54` feat(vta): rooms/owner/group/renew renews a sealed room; pnm rooms renew refuses a sealed room | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2112) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1d5c7aef616605f3a972dc2e` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `20bc88fe966b21280abf4c1b` feat(rooms)!: rooms/keys/act 0.4 — a member reads each offered room's description (vtc/rooms/offers/list 0.2) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2183) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3474aeed99edbff13c5c4111` feat!: TEE first-boot enrols the claim DID as the bootstrap admin instead of minting a key (#2066) (#2182) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/commit/989c67e6ef8b35cb459aed93f2c2263db511ef83) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b5cd4abd5496f98503371ec` feat(vtc)!: community-room details administrators can see, edit and track (trust-tasks-tf #805) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2170) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b87559a2585b735cd19f588` vta-cli-common-v0.42.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-cli-common-v0.42.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `4117307f07550112138d39fd` feat(rooms): a member's own private name, description, notes and tags for each room they hold | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2167) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-2138AB8B6885F705` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/484) |

## Watch

**8 deterministic watch assertion(s)** · **20 other finding(s)**

- `DTG-A-BEEDC453669E40B2` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-1563A48AC0D47E47` — Governed action specification and implementation are moving together in this window.
- `DTG-A-6E6C5EF4DDFBAD39` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-0255C8BAABAEFB16` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-B02FE8606A1BDD6E` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-AC020C78D457F56B` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-424082CB75A2A614` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-0C7ED502C61DE63D` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 806 · **Material:** 220 · **Breaking:** 52 · **Tagged releases:** 331 · **Cross-repository:** 120  
**Duplicate representations consolidated:** 338

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 30 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 253 | 60 |
| Implementation and interoperability | **Advancing strongly** | 382 | 114 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 478
- **Credentials and proof:** 310
- **Protocol and interoperability:** 297
- **Authority and delegation:** 195
- **Governance and lifecycle:** 168

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
