---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-16T16:45:02.271943Z  
**Evidence through:** 2026-10-16T16:40:47Z  
**Source revision:** `60f9f4f88b9ae38c31ff7514686b32458ad080b1` · **Collection run:** `38934157758` · **Publication state:** `workflow-generated`  
**Change units:** 701 · **Material:** 182  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 38
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 58

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 94 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 49 material change units, led by credentials and proof, protocol and interoperability.
**Human trust and safety** — 6 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 30 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 6 | 4 |
| Governed action | **Advancing strongly** | 221 | 49 |
| Implementation and interoperability | **Advancing strongly** | 335 | 94 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 72 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 47 material specification change unit(s) and 93 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-5DAD747906411F38` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-C6979D573B9F79AA` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-45774A2D2A43FCB5` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-C9627328B585B7F4` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-AA0AF2896D95E4DD` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B1145F63BBD4F380` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-AC020C78D457F56B` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-8E4929C4EFF0F6BE` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-0C7ED502C61DE63D` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
