---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-26T16:29:15.511125Z  
**Evidence through:** 2026-09-26T16:19:59Z  
**Source revision:** `27542d34e9f3dc9404d9b3fa2e621e0fc766e55e` · **Collection run:** `36255524746` · **Publication state:** `workflow-generated`  
**Change units:** 1041 · **Material:** 283  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 57
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 104

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 155 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 74 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 5 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 22 | 5 |
| Governed action | **Advancing strongly** | 379 | 74 |
| Implementation and interoperability | **Advancing strongly** | 429 | 155 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 120 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 66 material specification change unit(s) and 152 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 152 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-DB39C04A3F694C68` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-9160A98CB862621B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-3B495D450A51B4A1` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E0E55D80E6B8D47F` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-694B40A1A6268D84` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2F85A1A3D6740481` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-0B17FC0E4EBA51DA` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-FE85CA9B20F6B085` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-C81FD9B46F907048` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
