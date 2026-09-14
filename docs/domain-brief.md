---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-14T05:03:30.257228Z  
**Evidence through:** 2026-09-14T01:11:44Z  
**Source revision:** `86e3211b1d9b313a18c4c8fdd0481274bd6b8c62` · **Collection run:** `34808160865` · **Publication state:** `workflow-generated`  
**Change units:** 990 · **Material:** 293  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 56
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 74

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 136 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 57 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 28 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 46 | 28 |
| Governed action | **Advancing strongly** | 240 | 57 |
| Implementation and interoperability | **Advancing strongly** | 356 | 136 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 15 material specification change unit(s) and 110 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 57 material specification change unit(s) and 127 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-C6C43EADAB5E4509` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-1620AD7E3009C8DC` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E9B7DC8DB0D02AA4` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-C217FA5EA56FDFAC` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-9254CDCEA3632798` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F86E55FDD4D2AFCC` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B872692B5B9F9819` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-4D34DA637631BF54` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-88D4EC75099E1F65` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
