---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-13T16:24:34.953270Z  
**Evidence through:** 2026-09-13T06:23:55Z  
**Source revision:** `80623801ffa018c1be701b0b602b570ebf37db27` · **Collection run:** `34768430814` · **Publication state:** `workflow-generated`  
**Change units:** 1007 · **Material:** 299  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 61
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 79

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 139 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 60 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 28 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 44 | 28 |
| Governed action | **Advancing strongly** | 251 | 60 |
| Implementation and interoperability | **Advancing strongly** | 364 | 139 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 15 material specification change unit(s) and 112 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 60 material specification change unit(s) and 129 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-7C302A7B8F811590` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-DE2E32FFBCE1C571` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E9B7DC8DB0D02AA4` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-9F5E6411F5258A82` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-7AF32F49FF1EACC2` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-19F5979B3A3B2498` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-290F679B52AB1325` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-0DC65BB6E2A30F60` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
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
