---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-06T06:29:11.886216Z  
**Evidence through:** 2026-10-06T06:12:33Z  
**Source revision:** `a99277a717aab9795b7a0d545dade82fc8c9a268` · **Collection run:** `37423818485` · **Publication state:** `workflow-generated`  
**Change units:** 797 · **Material:** 173  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 33
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 52

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 100 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 45 material change units, led by credentials and proof, protocol and interoperability.
**Credentials and evidence** — 6 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 5 | 1 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 16 | 6 |
| Governed action | **Advancing strongly** | 195 | 45 |
| Implementation and interoperability | **Advancing strongly** | 465 | 100 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around delivery and maintenance, governance and lifecycle.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around delivery and maintenance, governance and lifecycle.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 74 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 45 material specification change unit(s) and 96 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-B7F4CCEDCB670155` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-D2F9D48B38566A6E` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D26CBD1441E20AF6` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-9F85878F81A2438A` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-646BF105DAF1C46C` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E369CBEE28EEDC86` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F9176A0A3ED5C2D0` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-7F1D354CE04CB69B` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-B86DBA79FC3CCCA0` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
