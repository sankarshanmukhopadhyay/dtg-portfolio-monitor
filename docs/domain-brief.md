---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-21T17:19:18.326513Z  
**Evidence through:** 2026-10-21T17:11:19Z  
**Source revision:** `83de164be660b82e0bde2ef0ee9160d110b45e9c` · **Collection run:** `39642407106` · **Publication state:** `workflow-generated`  
**Change units:** 739 · **Material:** 207  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 49
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 79

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 102 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 62 material change units, led by credentials and proof, protocol and interoperability.
**Human trust and safety** — 13 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 53 | 13 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 281 | 62 |
| Implementation and interoperability | **Advancing strongly** | 300 | 102 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 93 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 62 material specification change unit(s) and 101 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-4D001AE994E33673` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-57972AEA42862C96` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-4F18C56F43BD4E65` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-D351C323AAAD6732` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-159ADF90CC3DC3C2` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-FE7A477EFDF2CACB` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-559AEBBF375A2419` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-28096280024D8ABB` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-4054472E47F91C94` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
