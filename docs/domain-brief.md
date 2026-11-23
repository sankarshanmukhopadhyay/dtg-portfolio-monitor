---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-23T02:36:45.801485Z  
**Evidence through:** 2026-11-22T18:53:21Z  
**Source revision:** `3c17778775ee03d8eab6d6f607c36aa782a47717` · **Collection run:** `45101001926` · **Publication state:** `workflow-generated`  
**Change units:** 214 · **Material:** 54  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 15
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 32

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 21 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 8 material change units, led by delivery and maintenance, credentials and proof.
**Credentials and evidence** — 1 material change unit, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 1 | 1 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 6 | 1 |
| Governed action | **Advancing strongly** | 58 | 8 |
| Implementation and interoperability | **Advancing strongly** | 47 | 21 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 14 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 20 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-01531AE5DA5D65CE` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-2450B11D9D2B67A1` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-4D89766C73E9994C` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-090A64B4389D9A7C` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-008B20EDD00CB2CA` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-36A37E76C5A0AFC8` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-FE19C5CC26F97E12` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-160CE4449BAC0B96` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-D47F11BCCBED72C4` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
