---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-18T15:57:07.565279Z  
**Evidence through:** 2026-10-18T15:51:42Z  
**Source revision:** `01005ec1cd2eddd6e517c6bb3c93d0acf59f94a1` · **Collection run:** `39142627747` · **Publication state:** `workflow-generated`  
**Change units:** 760 · **Material:** 196  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 49
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 68

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 103 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 56 material change units, led by credentials and proof, delivery and maintenance.
**Human trust and safety** — 6 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 30 | 6 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 8 | 4 |
| Governed action | **Advancing strongly** | 234 | 56 |
| Implementation and interoperability | **Advancing strongly** | 379 | 103 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 91 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 54 material specification change unit(s) and 102 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-61ABAB5A2F1534BD` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-989D5130B33CC267` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-AACC79D84B23CA8A` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-42D88FA6AB16CD5C` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-911757E3CC1B4F2A` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-275598E05FBBCE76` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-AC020C78D457F56B` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-8A2EAB094C671A38` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
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
