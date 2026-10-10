---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-10T05:59:53.685669Z  
**Evidence through:** 2026-10-10T04:14:47Z  
**Source revision:** `ffb4ed9bc9c3b73607c3ef55b965f631a9ccc9a9` · **Collection run:** `38029325373` · **Publication state:** `workflow-generated`  
**Change units:** 410 · **Material:** 94  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 14
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 21

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 50 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 20 material change units, led by protocol and interoperability, delivery and maintenance.
**Human trust and safety** — 10 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 5 | 2 |
| Governed action | **Advancing strongly** | 71 | 20 |
| Implementation and interoperability | **Advancing strongly** | 236 | 50 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 33 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 20 material specification change unit(s) and 49 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-9D46B03854EC677B` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-5094838CF4BB1FF8` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-10C75E7EC928C9AD` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-4AE2C48DAD70CD02` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-E201CCDB23AD8163` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2A826382DEBFAA41` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-C7346CD6487636A6` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-6F5F3C78AAC1EB5E` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-54283C39ABF6648F` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
