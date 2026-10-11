---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-10-11T17:43:55.624650Z  
**Evidence through:** 2026-10-11T17:42:44Z  
**Source revision:** `18dfd3c07d1d81cf959389b120cfb02bc39b553e` · **Collection run:** `38160733759`  

## Review now

**22 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `93176b4d2a918609a33b13f7` vta-sdk-v0.65.0 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/releases/tag/vta-sdk-v0.65.0) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `a775c9693b223f68a75123e1` vta-sdk: keep a trust-task rejection's code and details instead of flattening to Protocol(String) | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/issues/1952) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `aa28149c7babc678e9e7412c` feat(vta-sdk)!: wallet sign-in with a trigger link: sign auth/oob grants, enrol UV keys, advertise TrustTaskHTTPS and SignInPortal | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/1997) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `d6f06da6be6c24f2917aa922` feat(vtc): member portal, with wallet sign-in by trigger link | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2007) |
| **elevated** | `OpenVTC/verifiable-trust-infrastructure` | `e121b18291ff4d8f4d55fd81` chore: release | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-trust-infrastructure/pull/2038) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `0ab1aa8e2e70a9099d7354cc` feat: wallet sign-in with a trigger link (VTI 7a, auth/oob) | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/303) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `14345600ab746827b9d8b3ff` fix(links): align the trigger-link parser with VTI-LNK spec d37a675 | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/316) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `3b62b0cd590b9b45b3da0de6` chore(deps): Bump @openvtc/trust-tasks from 0.23.0 to 0.23.1 | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/300) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `5daf04aa9bf26ef415940de1` feat: say "operator console" when a sign-in link asks for the console's session | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/307) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `5f287722cb80cafcb50337ad` feat!: bind every outbound Trust Task to its signer; DIDComm sign-in via challenge and signed authenticate | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/279) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `c15ef701e115583e2756cddd` feat(did): pluggable contact DID methods and domain-linked contacts (route B) | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/317) |
| **elevated** | `OpenVTC/vta-browser-plugin` | `da3e439ebf70650d0c35d412` feat: sender-bound, purpose-checked Trust Tasks and signed DIDComm sign-in | potentially-breaking | [source](https://github.com/OpenVTC/vta-browser-plugin/pull/304) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-0AED82022BC8D0C1` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/439) |

## Watch

**8 deterministic watch assertion(s)** · **15 other finding(s)**

- `DTG-A-B8C09A73A2262E8D` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-0FA27B139B14CD67` — Governed action specification and implementation are moving together in this window.
- `DTG-A-9242BAFD2776727A` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-F718A0405C6206AD` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-1B3CA741D28A7831` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-9BA350F6C1E2702B` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-3AC23645D37890FA` — Material movement is present on both sides of the declared pressure-tests relationship.
- `DTG-A-1B0BB848DF8A2B78` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 467 · **Material:** 127 · **Breaking:** 15 · **Tagged releases:** 168 · **Cross-repository:** 64  
**Duplicate representations consolidated:** 204

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 2 | 1 |
| Governed action | **Advancing strongly** | 92 | 29 |
| Implementation and interoperability | **Advancing strongly** | 260 | 60 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 287
- **Protocol and interoperability:** 169
- **Credentials and proof:** 147
- **Transport and routing:** 101
- **Authority and delegation:** 86

### Portfolio intelligence

- **Cross-capability convergence signals:** 5
- **Specification/implementation signals:** 3
- **Attention signals:** 1
- **Machine-addressable assertions:** 9
