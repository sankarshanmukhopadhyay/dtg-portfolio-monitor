---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-20T04:58:43.944269Z  
**Evidence through:** 2026-10-20T04:54:55Z  
**Source revision:** `7354a7a4172c71851ca71265dd8ff9ebdb8c3a77` · **Collection run:** `39372250544` · **Publication state:** `workflow-generated`  
**Change units:** 772 · **Material:** 207  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 50
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 76

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 103 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 67 material change units, led by credentials and proof, protocol and interoperability.
**Credentials and evidence** — 6 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing** | 49 | 5 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 11 | 6 |
| Governed action | **Advancing strongly** | 254 | 67 |
| Implementation and interoperability | **Advancing strongly** | 346 | 103 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 92 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 65 material specification change unit(s) and 102 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-AAC377ECA1478FED` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-746E79D6A8393F1B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E4BD97E09AE4522F` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-BD9CFA5972970AD4` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-30BCDD7FEE9BB0DC` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-30C892BA98A120DB` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-4660793F7A89C168` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-7539315B82097BB4` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-99B60907FBA17294` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
