---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-20T04:59:55.490214Z  
**Evidence through:** 2026-09-19T20:40:19Z  
**Source revision:** `90740f58a1db1afb51d0353cd3e221a7dbc6c698` · **Collection run:** `35490454684` · **Publication state:** `workflow-generated`  
**Change units:** 561 · **Material:** 108  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 13
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 27

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 72 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 14 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 7 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 16 | 7 |
| Governed action | **Advancing strongly** | 138 | 14 |
| Implementation and interoperability | **Advancing strongly** | 296 | 72 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 38 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 13 material specification change unit(s) and 71 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 71 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-66A879F63413C23F` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-0DF3FFD17996F208` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-C022EFEBA54B0682` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-EB6915721E185F9B` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-8ECB3382997ADAA2` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F4868F4A98DF98E9` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-DCCC0BC15E8B2F1D` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-6FAE79D5061539EC` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-CD1FB6E5E9EC1C7B` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
