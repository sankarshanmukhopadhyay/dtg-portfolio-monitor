---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-25T08:45:38.026244Z  
**Evidence through:** 2026-11-25T07:52:23Z  
**Source revision:** `827a29db3d3d6830fd0553dfaccc813e0030cb55` · **Collection run:** `45578787391` · **Publication state:** `workflow-generated`  
**Change units:** 430 · **Material:** 85  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 14
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 39

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Credentials and evidence, and Governed action**.

**Implementation and interoperability** — 34 material change units, led by delivery and maintenance, credentials and proof.
**Credentials and evidence** — 17 material change units, led by credentials and proof, delivery and maintenance.
**Governed action** — 14 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 3 | 1 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 29 | 17 |
| Governed action | **Advancing strongly** | 91 | 14 |
| Implementation and interoperability | **Advancing strongly** | 221 | 34 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 13 material specification change unit(s) and 28 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 13 material specification change unit(s) and 33 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 33 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-87B846BB50A5CE72` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-57BF69DC4DCAAC19` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-F4C2CE045E57002E` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-33697316E33F0518` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-D8194435C4B06CD0` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F27C3F6F3001CFC4` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2952718401166750` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-A49810F27DD94626` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-25DE470894E89740` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether the current convergence between **Credentials and evidence** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
