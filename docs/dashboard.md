---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-15T17:07:34.743812Z  
**Evidence through:** 2026-10-15T16:57:51Z  
**Source revision:** `27be452275e00aab4468c7907eff83554044557e` · **Collection run:** `38774480831`  

## Review now

**24 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/openvtc` | `2a5769f69aaf67636efe156b` fix(vetting)!: say when a vetter credential is refused, not only in the debug log | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/493) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1a1152510cfda3e78869be54` feat(vta): rooms/owner/group/renew renews a sealed room; pnm rooms renew refuses a sealed room | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2112) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `1d5c7aef616605f3a972dc2e` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `58f3e21a7dd7227a41ab4200` chore(deps): bump the minor-and-patch group with 9 updates | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2070) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `93176b4d2a918609a33b13f7` vta-sdk-v0.65.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-sdk-v0.65.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `93dc1d4c3ed05d8329360c7a` feat(vta)!: vta/witness/{open,present,accept} — the VTA is its principal's witnessed party, the client carries the documents (#1068) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2123) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `aa28149c7babc678e9e7412c` feat(vta-sdk)!: wallet sign-in with a trigger link: sign auth/oob grants, enrol UV keys, advertise TrustTaskHTTPS and SignInPortal | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1997) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `c114e0f0e370484459c1ba69` vta-sdk-v0.66.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-sdk-v0.66.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `d6f06da6be6c24f2917aa922` feat(vtc): member portal, with wallet sign-in by trigger link | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2007) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `dc0309a730276b1501b7543c` feat(sdk)!: keep a Trust Task rejection's code and details (#1952) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2093) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `e121b18291ff4d8f4d55fd81` chore: release | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2064) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `0ab1aa8e2e70a9099d7354cc` feat: wallet sign-in with a trigger link (VTI 7a, auth/oob) | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/303) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-45774A2D2A43FCB5` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/484) |

## Watch

**8 deterministic watch assertion(s)** · **18 other finding(s)**

- `DTG-A-B722343F95631A3B` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-2F7A138417705C58` — Governed action specification and implementation are moving together in this window.
- `DTG-A-FB3025367AEF990F` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-8D930B04ADC3C793` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-9C26F05D333BD98D` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-A4D8DA89CE2B6753` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-5F864309139C0A41` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-4670F0990C6B60CB` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 575 · **Material:** 147 · **Breaking:** 37 · **Tagged releases:** 225 · **Cross-repository:** 64  
**Duplicate representations consolidated:** 238

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 27 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 5 | 3 |
| Governed action | **Advancing strongly** | 162 | 35 |
| Implementation and interoperability | **Advancing strongly** | 282 | 74 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 338
- **Protocol and interoperability:** 204
- **Credentials and proof:** 202
- **Transport and routing:** 123
- **Authority and delegation:** 121

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
