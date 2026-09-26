---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-26T05:06:40.301416Z  
**Evidence through:** 2026-09-26T04:13:16Z  
**Source revision:** `a3c774d94d874f7db2f68b227ff249ba56773d6c` · **Collection run:** `36219750584` · **Publication state:** `workflow-generated`  
**Change units:** 1051 · **Material:** 280  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 55
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 101

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 154 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 71 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 6 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 23 | 6 |
| Governed action | **Advancing strongly** | 370 | 71 |
| Implementation and interoperability | **Advancing strongly** | 437 | 154 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 121 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 63 material specification change unit(s) and 151 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 151 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-FC788F804581C3E6` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-14BDB29F2E4CB491` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-3B495D450A51B4A1` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-ECB0559319FB8F36` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-9ABFE7DCE0FC7C0B` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-5889930821A34BB1` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-1A27DB3DBDF1D825` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-28ED8ECAB48104C7` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-9E9533C4954ADEBF` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
