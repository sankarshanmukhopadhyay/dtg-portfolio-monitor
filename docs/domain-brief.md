---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-19T18:45:44.334466Z  
**Evidence through:** 2026-10-19T16:17:12Z  
**Source revision:** `c4aaa264bf36a431d84594b289c3290ad1b548ea` · **Collection run:** `39304995755` · **Publication state:** `workflow-generated`  
**Change units:** 783 · **Material:** 202  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 50
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 70

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 103 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 66 material change units, led by credentials and proof, delivery and maintenance.
**Human trust and safety** — 5 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 49 | 5 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 5 |
| Governed action | **Advancing strongly** | 261 | 66 |
| Implementation and interoperability | **Advancing strongly** | 358 | 103 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 91 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 64 material specification change unit(s) and 102 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F20B7A337F2CB9BA` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-746E79D6A8393F1B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-1CB79460DC45D417` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-738E37012D39E893` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-3D33B40FEBBF2E8C` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-30C892BA98A120DB` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-EA3DF4D203AC20C8` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-7539315B82097BB4` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-AFCEF8D81CCABA50` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
