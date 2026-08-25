---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-08-25T13:14:39.754576Z  
**Evidence through:** 2026-08-25T13:05:30Z  
**Source revision:** `c865c99093d20514c8a188b38938df1f7b226e9e` · **Collection run:** `32852074670` · **Publication state:** `workflow-generated`  
**Change units:** 247 · **Material:** 100  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 22
- **Review-required assertions:** 1
- **Watch assertions:** 6
- **Open findings:** 39

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 76 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 15 material change units, led by protocol and interoperability, delivery and maintenance.
**Credentials and evidence** — 9 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 3 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 17 | 9 |
| Governed action | **Advancing strongly** | 28 | 15 |
| Implementation and interoperability | **Advancing strongly** | 199 | 76 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 7 material specification change unit(s) and 59 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 15 material specification change unit(s) and 75 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-6BDD81733056244F` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-B6758B19E17E655B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-333822981D4F307A` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-DDB1C874F5EF0584` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-D8E521C68A1076D6` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B897B58CB1ABDE33` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-5B924474BBF6AA6F` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
