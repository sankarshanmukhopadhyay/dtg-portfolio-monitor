---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-12T15:37:07.878009Z  
**Evidence through:** 2026-09-12T15:35:59Z  
**Source revision:** `6f27ff984082c87d630ab0509b620c4f0fd644d1` · **Collection run:** `34702671076` · **Publication state:** `workflow-generated`  
**Change units:** 1006 · **Material:** 320  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 69
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 91

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 151 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 67 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 33 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 48 | 33 |
| Governed action | **Advancing strongly** | 283 | 67 |
| Implementation and interoperability | **Advancing strongly** | 361 | 151 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 21 material specification change unit(s) and 123 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 67 material specification change unit(s) and 141 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-63837ABB7B84297A` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-DE2E32FFBCE1C571` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D9318D32F5E1BAB0` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-C09DD8688EEFCB1F` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-22D3284785EFBD85` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-19F5979B3A3B2498` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-031EA86CC2EEBB94` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-6EA6DBF98ACE0A53` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-1FBA90DD5A08A845` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
