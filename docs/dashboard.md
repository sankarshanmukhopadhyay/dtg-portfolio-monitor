---
title: Dashboard
nav_order: 3
permalink: /dashboard/
---
# Portfolio dashboard

**Generated:** 2026-09-15T17:05:12.438863Z  
**Evidence through:** 2026-09-15T17:00:45Z  
**Source revision:** `eca28c7e28e8b16dc37cb055e113f93e7cd395d7` · **Collection run:** `34998879990`  

## Review now

**48 decision finding(s)** · **1 review-required assertion(s)**

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
| `DTG-A-B4ADD25116DAF9C1` | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. | [source](https://github.com/OpenVTC/openvtc/pull/290) |

## Watch

**8 deterministic watch assertion(s)** · **13 other finding(s)**

- `DTG-A-7C531BDA60354CEE` — Credentials and evidence specification and implementation are moving together in this window.
- `DTG-A-EC92469A5B6BE225` — Governed action specification and implementation are moving together in this window.
- `DTG-A-65267A53C83BF044` — Material movement is present on both sides of the declared supplies-evidence-to relationship.
- `DTG-A-8B56E10BDC32B8F2` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-B509745340B8DF61` — Material movement is present on both sides of the declared exercised-by relationship.
- `DTG-A-7E6270AF5BD428CD` — Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window.
- `DTG-A-408A4C593402194E` — Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window.
- `DTG-A-7DED86510FEC26D0` — Governed action has material activity while related capability Human trust and safety is quiet in this observation window.

## Recently disposed

_No explicit finding dispositions are represented in the current snapshot._

## Portfolio movement

**Change units:** 810 · **Material:** 237 · **Breaking:** 19 · **Tagged releases:** 226 · **Cross-repository:** 94  
**Duplicate representations consolidated:** 360

[Read the DTG Domain Brief]({{ '/domain-brief/' | relative_url }}){: .btn .btn-primary }

### Capability pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 39 | 23 |
| Governed action | **Advancing strongly** | 192 | 43 |
| Implementation and interoperability | **Advancing strongly** | 305 | 111 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

### Leading themes

- **Delivery and maintenance:** 535
- **Credentials and proof:** 304
- **Protocol and interoperability:** 294
- **Authority and delegation:** 223
- **Governance and lifecycle:** 206

### Portfolio intelligence

- **Cross-capability convergence signals:** 3
- **Specification/implementation signals:** 3
- **Attention signals:** 3
- **Machine-addressable assertions:** 9
