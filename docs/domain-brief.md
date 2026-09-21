---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-21T18:14:24.035722Z  
**Evidence through:** 2026-09-21T18:13:38Z  
**Source revision:** `020aecf77b665dc51e6a42f3efcba1b8ba92e655` · **Collection run:** `35636964135` · **Publication state:** `workflow-generated`  
**Change units:** 774 · **Material:** 146  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 21
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 48

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 96 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 28 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 7 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 18 | 7 |
| Governed action | **Advancing strongly** | 240 | 28 |
| Implementation and interoperability | **Advancing strongly** | 403 | 96 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 53 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 24 material specification change unit(s) and 94 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 94 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-BDA49C6599240053` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-2C6FF0C3BB769DA9` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-7AA3EF3FF31B8FEF` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-44DFC8E3CF4C4041` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-DDA46AD092762103` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-51B606AB5F75596A` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2F7ADD5BD0702746` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-75972C1EE1BAF050` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-6BE687CAD04B5103` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
