---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-13T16:24:34.953270Z  
**Evidence through:** 2026-09-13T06:23:55Z  
**Source revision:** `80623801ffa018c1be701b0b602b570ebf37db27` · **Collection run:** `34768430814`  

## Review now

**61 decision finding(s)** · **1 review-required assertion(s)**

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
| `DTG-A-E9B7DC8DB0D02AA4` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/283) |

## Watch

**8 deterministic watch assertion(s)** · **18 other finding(s)**

- `DTG-A-7C302A7B8F811590` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-DE2E32FFBCE1C571` — Governed action specification and implementation are moving together in this window.
- `DTG-A-9F5E6411F5258A82` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-7AF32F49FF1EACC2` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-19F5979B3A3B2498` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-290F679B52AB1325` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-0DC65BB6E2A30F60` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.
- `DTG-A-1FBA90DD5A08A845` — Governed action has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 1007 · **Material:** 299 · **Breaking:** 29 · **Tagged releases:** 301 · **Cross-repository:** 112  
**Duplicate representations consolidated:** 457

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 44 | 28 |
| Governed action | **Advancing strongly** | 251 | 60 |
| Implementation and interoperability | **Advancing strongly** | 364 | 139 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 633
- **Protocol and interoperability:** 372
- **Credentials and proof:** 349
- **Authority and delegation:** 294
- **Governance and lifecycle:** 226

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
