---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-14T05:00:38.967333Z  
**Evidence through:** 2026-10-13T17:55:15Z  
**Source revision:** `5a0f42d9470458714483dd688cf077f3d0c29302` · **Collection run:** `38514217382` · **Publication state:** `workflow-generated`  
**Change units:** 396 · **Material:** 112  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 19
- **Review-required assertions:** 2
- **Watch assertions:** 7
- **Open findings:** 36

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 53 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 19 material change units, led by credentials and proof, protocol and interoperability.
**Human trust and safety** — 10 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 18 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 3 | 1 |
| Governed action | **Advancing strongly** | 82 | 19 |
| Implementation and interoperability | **Advancing strongly** | 202 | 53 |
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
- **Governed action: specification and implementation are moving together.** The monitor observed 18 material specification change unit(s) and 52 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-8293FAA608EC8A91` | review-required | implementation-ahead | Credentials and evidence implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-DA44712FB6AF9D13` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-FDC6D632DA7E6316` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-81AA26D2DD0DFBD6` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-7787FAF97009248E` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E60672648A0B0295` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-A6C44A6781A11DF5` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-A2F839CB4427CB3E` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
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
