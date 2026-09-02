---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-02T04:42:17.398090Z  
**Evidence through:** 2026-09-02T04:40:59Z  
**Source revision:** `6e338802184a815b963a6125a49f2528448b414e` · **Collection run:** `33591724166` · **Publication state:** `workflow-generated`  
**Change units:** 433 · **Material:** 197  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 20
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 47

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 103 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 59 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 12 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 22 | 12 |
| Governed action | **Advancing strongly** | 131 | 59 |
| Implementation and interoperability | **Advancing strongly** | 218 | 103 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 76 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 53 material specification change unit(s) and 98 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 98 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-ED3E0EC9492D3DB3` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-B67D5BD807377FC5` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-7381626219CC2134` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-EC0EE77F8BAFCB13` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-584169B04B46275A` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-BAA05E1A586DCDAE` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-FAA9F76A30B311E9` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-01BEE21CDF532B9F` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-5D2AAFBD36479142` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
