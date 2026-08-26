---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-08-26T13:20:09.776655Z  
**Evidence through:** 2026-08-26T13:18:46Z  
**Source revision:** `79a0a5657f980acdcec7b044e2d752b28cd8a6e2` · **Collection run:** `32973457480` · **Publication state:** `workflow-generated`  
**Change units:** 321 · **Material:** 147  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 29
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 59

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 95 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 37 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 10 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 16 | 10 |
| Governed action | **Advancing strongly** | 56 | 37 |
| Implementation and interoperability | **Advancing strongly** | 210 | 95 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 78 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 34 material specification change unit(s) and 94 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 3 material specification change unit(s) and 94 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-CCDFD403B0874B3E` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-AB6CC525C36D20FF` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-F26BEAA5FE51F518` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-591A0A59B8EF78BD` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-5EB13EC52A97D7E5` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-A7DFF945900B7A26` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2E431A54A35AF48E` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-26CACA7F1DE160E3` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-670D9A04B3AE5F7B` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
