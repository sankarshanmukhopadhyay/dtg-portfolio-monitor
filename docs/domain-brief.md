---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-08T16:42:29.016403Z  
**Evidence through:** 2026-09-08T16:22:04Z  
**Source revision:** `66657718bb63a55e35f8eaacd7298a706b82da10` · **Collection run:** `34252583834` · **Publication state:** `workflow-generated`  
**Change units:** 597 · **Material:** 201  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 42
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 58

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 83 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 49 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 25 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 44 | 25 |
| Governed action | **Advancing strongly** | 187 | 49 |
| Implementation and interoperability | **Advancing strongly** | 183 | 83 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 18 material specification change unit(s) and 63 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 47 material specification change unit(s) and 77 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 77 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F9DB6C919750A1BE` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-AAD52A989A4D6C96` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-B78E5807F5D68C40` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-5ED8988E95F9F093` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-9446891CEB58AD2B` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-752CD824FEB3905E` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-57A32A41D6B03DBA` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-AECE1E4743621A41` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-D48A6B3D093D04BB` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
