---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-30T05:40:07.146917Z  
**Evidence through:** 2026-09-29T23:44:28Z  
**Source revision:** `08d7fd3bae206f93550d57eacebecfff4fa21800` · **Collection run:** `36674318465` · **Publication state:** `workflow-generated`  
**Change units:** 899 · **Material:** 305  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 67
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 97

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 171 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 75 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 5 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 20 | 5 |
| Governed action | **Advancing strongly** | 275 | 75 |
| Implementation and interoperability | **Advancing strongly** | 364 | 171 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 5 material specification change unit(s) and 140 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 71 material specification change unit(s) and 169 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 169 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-0D6D37C2F91D4D87` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-B01FBC49BF654996` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-06B2F7C8FCCA240B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E8B39D0EF0A8E3EB` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-0B2EE21302D6F008` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-2551D4E24E77535C` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B525881D5BE24FEE` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-78D09E7BC516E0ED` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-BF8A3FDA17393985` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
