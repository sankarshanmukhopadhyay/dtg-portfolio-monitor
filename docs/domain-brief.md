---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-18T04:41:53.718764Z  
**Evidence through:** 2026-10-18T04:37:33Z  
**Source revision:** `0bd151e88110e70326435d618c7c412446d2ec9f` · **Collection run:** `39097875488` · **Publication state:** `workflow-generated`  
**Change units:** 806 · **Material:** 220  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 48
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 68

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 114 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 60 material change units, led by credentials and proof, delivery and maintenance.
**Human trust and safety** — 6 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 30 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 253 | 60 |
| Implementation and interoperability | **Advancing strongly** | 382 | 114 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 92 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 58 material specification change unit(s) and 113 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-BEEDC453669E40B2` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-1563A48AC0D47E47` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-2138AB8B6885F705` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-6E6C5EF4DDFBAD39` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-0255C8BAABAEFB16` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B02FE8606A1BDD6E` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-AC020C78D457F56B` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-424082CB75A2A614` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-0C7ED502C61DE63D` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
