---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-08-30T05:30:25.128226Z  
**Evidence through:** 2026-08-30T04:38:44Z  
**Source revision:** `3c80e64cdb6f5b5f4ff3087db14b29ab0bc4dfce` · **Collection run:** `33294795128` · **Publication state:** `workflow-generated`  
**Change units:** 436 · **Material:** 217  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 34
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 67

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 131 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 62 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 13 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 24 | 13 |
| Governed action | **Advancing strongly** | 127 | 62 |
| Implementation and interoperability | **Advancing strongly** | 231 | 131 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 9 material specification change unit(s) and 105 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 54 material specification change unit(s) and 127 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 7 material specification change unit(s) and 127 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-EB78CF7BE0FCE369` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-051284A0C0A256DE` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D17E6B375693740B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-FCEDDB78D794C3DE` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-422BEA925CF7638A` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-51BB8675AD8F9FEB` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-C9BF2A3381FCDAD2` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-9EDFFC526DD682F7` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-D33DFB972BC4947B` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
