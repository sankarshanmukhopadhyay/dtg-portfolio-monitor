---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-15T05:00:31.131182Z  
**Evidence through:** 2026-09-15T04:59:25Z  
**Source revision:** `fc758ffd7466b31e52ba57ddea87fdc5e3de4dc2` · **Collection run:** `34930918273`  

## Review now

**49 decision finding(s)** · **1 review-required assertion(s)**

### Decision findings

| Urgency | Repository | Finding | Impact | Evidence |
|---|---|---|---|---|
| **elevated** | `OpenVTC/dtg-credentials` | `01c0b3e160885ecb9f818a13` feat!: a VAC is not a bearer credential; remove `audience` | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/21) |
| **elevated** | `OpenVTC/dtg-credentials` | `034f21a5e8d61d0592574ad1` feat: set `credentialStatus` on a credential being built; `PartialEq` on the type | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/24) |
| **elevated** | `OpenVTC/dtg-credentials` | `2a53f45ce2cc63e5bd7f9dd5` ci: pin actions to commit SHAs, scope the publish token, add Dependabot | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/27) |
| **elevated** | `OpenVTC/dtg-credentials` | `506f342e3c98d41469c9c2b5` Working Draft 02: digest encoding, VAC parent digests, and the VDC | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/pull/20) |
| **elevated** | `OpenVTC/dtg-credentials` | `70623bd0786b0afdf672cad3` delegation::verify_chain takes no presenter, so a VDC is still a bearer credential | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/issues/23) |
| **elevated** | `OpenVTC/dtg-credentials` | `ef69e5f150b8a98a45231c66` Add the delegation credential (VDC) to the catalog | potentially-breaking | [source](https://github.com/OpenVTC/dtg-credentials/issues/10) |
| **elevated** | `OpenVTC/openvtc` | `5e066277145877762c4ac06d` docs(design): vetted admission via peer identity vetting | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/292) |
| **elevated** | `OpenVTC/openvtc` | `7c6ccc49fc6b4141eb9dd7aa` ci: pin every action to a commit SHA, drop write-all, and add Dependabot | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/310) |
| **elevated** | `OpenVTC/openvtc` | `9ff50bc250c0f83b4002f453` feat(vetting): guided join, vetter directory and profile, QR tickets, grant checks, resend and branding | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/307) |
| **elevated** | `OpenVTC/openvtc` | `bc384e287556c94f131c2c17` ci(deps): Bump the actions group with 3 updates | potentially-breaking | [source](https://github.com/OpenVTC/openvtc/pull/313) |
| **elevated** | `OpenVTC/verifiable-git-infrastructure` | `598764f918b68ff8d3b7f88c` fix(vgi-core): find the Signed-by-DID trailer block the way git does | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-git-infrastructure/pull/47) |
| **elevated** | `OpenVTC/verifiable-git-infrastructure` | `85dce17dfd099feed7bcead6` chore(deps): take vta-sdk 0.38.0 and drop didwebvh-rs 0.6.1 | potentially-breaking | [source](https://github.com/OpenVTC/verifiable-git-infrastructure/pull/51) |

### Review-required assertions

| Assertion | State | Statement | Evidence |
|---|---|---|---|
| `DTG-A-0CBE7A9777E21F5D` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/283) |

## Watch

**8 deterministic watch assertion(s)** · **18 other finding(s)**

- `DTG-A-7C531BDA60354CEE` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-638B74DD6D829473` — Governed action specification and implementation are moving together in this window.
- `DTG-A-EA75C6CA708B3572` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-B2FB95C832F1BF27` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-4FC895F7F830A4B3` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-F3B13DD846F42999` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-3F5BF6EA994AC597` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.
- `DTG-A-00FB108B5D285A9B` — Governed action has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 860 · **Material:** 260 · **Breaking:** 19 · **Tagged releases:** 234 · **Cross-repository:** 104  
**Duplicate representations consolidated:** 386

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 42 | 26 |
| Governed action | **Advancing strongly** | 215 | 52 |
| Implementation and interoperability | **Advancing strongly** | 303 | 120 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 563
- **Credentials and proof:** 323
- **Protocol and interoperability:** 315
- **Authority and delegation:** 247
- **Governance and lifecycle:** 213

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
