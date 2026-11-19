---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-18T20:40:32.444653Z  
**Evidence through:** 2026-11-18T18:09:58Z  
**Source revision:** `7e2813c8daf867a21e4064513cc83612726aeb44` · **Collection run:** `44392990900` · **Publication state:** `workflow-generated`  
**Change units:** 571 · **Material:** 212  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 38
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 61

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Governed action, Implementation and interoperability, and Human trust and safety**.

**Governed action** — 96 material change units, led by delivery and maintenance, protocol and interoperability.
**Implementation and interoperability** — 83 material change units, led by delivery and maintenance, protocol and interoperability.
**Human trust and safety** — 7 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 10 | 7 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 6 | 3 |
| Governed action | **Advancing strongly** | 254 | 96 |
| Implementation and interoperability | **Advancing strongly** | 207 | 83 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around credentials and proof, delivery and maintenance.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around credentials and proof, delivery and maintenance.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around credentials and proof, delivery and maintenance.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 3 material specification change unit(s) and 64 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 93 material specification change unit(s) and 82 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-AE360BEC950B7ECC` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-5AA024448E00C37B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-53414028C18BC6CE` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-080013AD3D896841` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-422CBCDDE749C429` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B9E363CE113932D1` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-098395B618906F2C` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-C05B2848A5AB6085` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-9837A70CA3E3A72A` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
