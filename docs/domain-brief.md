---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-06T18:27:34.419716Z  
**Evidence through:** 2026-10-06T17:28:36Z  
**Source revision:** `a5c43fe20d10c6c091c82072b2153d0d7c50157e` · **Collection run:** `37511225167` · **Publication state:** `workflow-generated`  
**Change units:** 807 · **Material:** 173  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 32
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 51

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 99 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 45 material change units, led by credentials and proof, protocol and interoperability.
**Credentials and evidence** — 5 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 10 | 3 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 15 | 5 |
| Governed action | **Advancing strongly** | 195 | 45 |
| Implementation and interoperability | **Advancing strongly** | 468 | 99 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 74 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 45 material specification change unit(s) and 95 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-93567C3482142430` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-D2F9D48B38566A6E` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D26CBD1441E20AF6` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-36F98AF721080E99` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-C8A9E8800AEC0C4F` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E369CBEE28EEDC86` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-4087A5FA3398E00C` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-566D254F576623A3` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-259D4147740B78BC` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
