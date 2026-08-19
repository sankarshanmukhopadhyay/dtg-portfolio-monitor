---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-08-19T13:12:55.921371Z  
**Change units:** 264 · **Material:** 78  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 43 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 32 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 3 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 3 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 7 | 3 |
| Governed action | **Advancing strongly** | 46 | 32 |
| Implementation and interoperability | **Advancing strongly** | 208 | 43 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 32 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 32 material specification change unit(s) and 43 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.
5. Whether the current convergence between **Credentials and evidence** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/` so that every published interpretation can be reproduced from versioned evidence and configuration.
