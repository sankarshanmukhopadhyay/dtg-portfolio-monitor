---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-07T06:07:53.041809Z  
**Evidence through:** 2026-10-07T05:37:35Z  
**Source revision:** `1bf6c1c97adb5ddcd73de4ba6e2a2273dc669215` · **Collection run:** `37579727682` · **Publication state:** `workflow-generated`  
**Change units:** 795 · **Material:** 172  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 30
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 48

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 97 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 43 material change units, led by credentials and proof, delivery and maintenance.
**Human trust and safety** — 6 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 14 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 15 | 5 |
| Governed action | **Advancing strongly** | 186 | 43 |
| Implementation and interoperability | **Advancing strongly** | 467 | 97 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 73 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 43 material specification change unit(s) and 93 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-93567C3482142430` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-CF02C8F776E819EE` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D26CBD1441E20AF6` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-864F503DEA19FB60` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-4E95EDBD60A7F921` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E803F39F609D515F` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B14A6E00B093838F` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-886EA01BD7104E83` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
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
