---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-17T15:41:31.527219Z  
**Evidence through:** 2026-10-17T13:00:40Z  
**Source revision:** `dab7a8b5dfac66e2816dabc9621b476cbb6e4140` · **Collection run:** `39046044724`  

## Review now

**44 decision finding(s)** · **1 review-required assertion(s)**

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
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b5cd4abd5496f98503371ec` feat(vtc)!: community-room details administrators can see, edit and track (trust-tasks-tf #805) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2170) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `3b87559a2585b735cd19f588` vta-cli-common-v0.42.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-cli-common-v0.42.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `4117307f07550112138d39fd` feat(rooms): a member's own private name, description, notes and tags for each room they hold | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2167) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `52ca93666c0c60642917b8b8` feat(rooms): a room's own profile — rooms/keys/profile/{read,write}, sealed inside the room | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2171) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `58f3e21a7dd7227a41ab4200` chore(deps): bump the minor-and-patch group with 9 updates | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2070) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-471E42B0359EE9DE` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/484) |

## Watch

**8 deterministic watch assertion(s)** · **20 other finding(s)**

- `DTG-A-996DA96109B10005` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-C6979D573B9F79AA` — Governed action specification and implementation are moving together in this window.
- `DTG-A-C9627328B585B7F4` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-A6A4FECAB73E46FA` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-B1145F63BBD4F380` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-AC020C78D457F56B` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-8E4929C4EFF0F6BE` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-0C7ED502C61DE63D` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 789 · **Material:** 214 · **Breaking:** 52 · **Tagged releases:** 323 · **Cross-repository:** 113  
**Duplicate representations consolidated:** 329

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 30 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 237 | 56 |
| Implementation and interoperability | **Advancing strongly** | 386 | 115 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 466
- **Credentials and proof:** 296
- **Protocol and interoperability:** 285
- **Authority and delegation:** 190
- **Transport and routing:** 164

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
