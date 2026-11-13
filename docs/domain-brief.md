---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-11-13T01:59:16.617628Z  
**Evidence through:** 2026-11-13T01:57:41Z  
**Source revision:** `d60f73a7b6f0e0687033177812ba2c19b16f96f9` · **Collection run:** `43348603223` · **Publication state:** `workflow-generated`  
**Change units:** 2099 · **Material:** 628  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 133
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 208

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 334 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 186 material change units, led by delivery and maintenance, protocol and interoperability.
**Human trust and safety** — 20 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 79 | 20 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 32 | 13 |
| Governed action | **Advancing strongly** | 695 | 186 |
| Implementation and interoperability | **Advancing strongly** | 931 | 334 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 9 material specification change unit(s) and 259 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 177 material specification change unit(s) and 325 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 9 material specification change unit(s) and 325 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-C061259BCD690816` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-132949AA12C1F808` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-62B85A5182FC1998` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-000599105C08C3F7` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-826B924096CD5614` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-1BEFC155485CBF5C` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B72981B6FC638342` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-AF9F18842C9B33DF` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-DB96E2F372A025D6` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.
5. Whether the current convergence between **Credentials and evidence** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
