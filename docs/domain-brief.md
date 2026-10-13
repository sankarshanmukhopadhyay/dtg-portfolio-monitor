---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-13T06:52:05.032893Z  
**Evidence through:** 2026-10-13T06:39:52Z  
**Source revision:** `ae69662074de8e06296a8e78c623cec13b935b5b` · **Collection run:** `38359025727` · **Publication state:** `workflow-generated`  
**Change units:** 367 · **Material:** 109  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 17
- **Review-required assertions:** 2
- **Watch assertions:** 7
- **Open findings:** 34

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 52 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 18 material change units, led by credentials and proof, protocol and interoperability.
**Human trust and safety** — 11 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 11 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 3 | 1 |
| Governed action | **Advancing strongly** | 81 | 18 |
| Implementation and interoperability | **Advancing strongly** | 168 | 52 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around delivery and maintenance, security and privacy.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around delivery and maintenance, security and privacy.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around delivery and maintenance, security and privacy.

## Specification and implementation alignment

- **Credentials and evidence: implementation movement is ahead of normative specification activity in this window.**
- **Governed action: specification and implementation are moving together.** The monitor observed 17 material specification change unit(s) and 51 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-4A8A31EADE68BAF5` | review-required | implementation-ahead | Credentials and evidence implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-DA44712FB6AF9D13` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-A2F9513297221EF6` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-81AA26D2DD0DFBD6` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-7787FAF97009248E` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E60672648A0B0295` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-67550203B347EECA` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-F5257F372B21C8D4` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-21DBC23617C63747` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether normative work catches up with implementation movement in **Credentials and evidence**.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
