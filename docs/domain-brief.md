---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-14T18:13:06.190923Z  
**Evidence through:** 2026-11-14T15:38:35Z  
**Source revision:** `1a1982212bce36d79a5fb9dc6d58bec7b7d9e01a` · **Collection run:** `43625189023` · **Publication state:** `workflow-generated`  
**Change units:** 722 · **Material:** 257  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 67
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 88

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Governed action, Implementation and interoperability, and Credentials and evidence**.

**Governed action** — 116 material change units, led by delivery and maintenance, protocol and interoperability.
**Implementation and interoperability** — 101 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 9 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 13 | 8 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 22 | 9 |
| Governed action | **Advancing strongly** | 303 | 116 |
| Implementation and interoperability | **Advancing strongly** | 278 | 101 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 7 material specification change unit(s) and 77 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 114 material specification change unit(s) and 96 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-2A74E4AC547763B5` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-7020DC73B0A50AFA` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-70969AE0B17C9130` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-9363721E5B0BF3CE` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-599611E49816E4B5` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-0CEFCA361E25CC4D` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-5638763FF9B8E779` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-DA266A145929ACDD` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-90BDC874AE2B4C27` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
