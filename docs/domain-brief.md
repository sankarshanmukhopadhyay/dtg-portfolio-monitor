---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-29T05:49:45.952923Z  
**Evidence through:** 2026-09-29T05:37:44Z  
**Source revision:** `c687a6b12b0bfc2d5533d9614af2a20336051f88` · **Collection run:** `36527915612` · **Publication state:** `workflow-generated`  
**Change units:** 1084 · **Material:** 345  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 75
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 113

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 199 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 82 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 6 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 28 | 6 |
| Governed action | **Advancing strongly** | 361 | 82 |
| Implementation and interoperability | **Advancing strongly** | 448 | 199 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 167 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 77 material specification change unit(s) and 197 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 197 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-2EE2F995953AC921` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-C2F4F485BE940B0D` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-F325ACB4E5CB1FB1` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-FEB43896296755C6` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-36E8BD73163AF383` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B24D4026EF148BC3` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-1C59E0BCA26BD678` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-F0F1374C74FC8F0A` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-C7357C8E7914729A` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
