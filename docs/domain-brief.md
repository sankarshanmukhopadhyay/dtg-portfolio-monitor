---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-29T18:09:12.314166Z  
**Evidence through:** 2026-09-29T18:06:31Z  
**Source revision:** `6e45588ad5c6da21b40898d558a0f23e232fda87` · **Collection run:** `36609707915` · **Publication state:** `workflow-generated`  
**Change units:** 942 · **Material:** 314  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 68
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 100

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 175 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 80 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 5 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 21 | 5 |
| Governed action | **Advancing strongly** | 309 | 80 |
| Implementation and interoperability | **Advancing strongly** | 376 | 175 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 143 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 75 material specification change unit(s) and 173 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 173 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-0D6D37C2F91D4D87` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-3E36DBAB3D98A58E` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-F325ACB4E5CB1FB1` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-83C0F9D2B0F95233` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-2AED5ED07C2DA105` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-DCF41EA7648091A1` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B525881D5BE24FEE` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-78D09E7BC516E0ED` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-284A253DDB5D2E8D` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
