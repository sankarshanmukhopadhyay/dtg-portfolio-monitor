---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-16T04:39:21.574265Z  
**Evidence through:** 2026-10-16T03:08:38Z  
**Source revision:** `eb9d692136b4a7aaa65eff81811206eff5c34e93` · **Collection run:** `38851594238` · **Publication state:** `workflow-generated`  
**Change units:** 608 · **Material:** 155  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 31
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 49

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 82 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 35 material change units, led by credentials and proof, delivery and maintenance.
**Human trust and safety** — 6 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 27 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 5 | 3 |
| Governed action | **Advancing strongly** | 162 | 35 |
| Implementation and interoperability | **Advancing strongly** | 310 | 82 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 60 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 33 material specification change unit(s) and 81 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-B722343F95631A3B` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-2F7A138417705C58` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-45774A2D2A43FCB5` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-FB3025367AEF990F` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-8D930B04ADC3C793` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-9C26F05D333BD98D` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-A4D8DA89CE2B6753` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-5F864309139C0A41` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-4670F0990C6B60CB` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
