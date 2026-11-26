---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-26T21:40:27.209513Z  
**Evidence through:** 2026-11-26T21:39:11Z  
**Source revision:** `51e12bfb79a3e9d524c3af22dd01c86045641b31` · **Collection run:** `45899576532` · **Publication state:** `workflow-generated`  
**Change units:** 466 · **Material:** 92  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 16
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 36

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 34 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 23 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 16 material change units, led by credentials and proof, delivery and maintenance.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Active** | 4 | 2 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 27 | 16 |
| Governed action | **Advancing strongly** | 115 | 23 |
| Implementation and interoperability | **Advancing strongly** | 237 | 34 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, delivery and maintenance.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 12 material specification change unit(s) and 30 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 22 material specification change unit(s) and 33 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 33 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F41E87BE2BDC46F3` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-7B3E52B1BFEEDE3A` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-C32CE88AC1FD56CB` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-28D9D4FE5EDEA590` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-FD4380252489F603` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-FAFAA583424C2F09` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-4A3DD8E5DB79D495` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-4635E3F87E2E7F9E` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-20A48414B95BD91B` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.
5. Whether the current convergence between **Credentials and evidence** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
