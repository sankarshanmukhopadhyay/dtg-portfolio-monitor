---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-21T04:58:07.255183Z  
**Evidence through:** 2026-10-21T04:53:31Z  
**Source revision:** `c61173a5c9cdd30e8792f3506708061b7f31938f` · **Collection run:** `39546743697` · **Publication state:** `workflow-generated`  
**Change units:** 780 · **Material:** 219  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 50
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 77

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 105 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 67 material change units, led by credentials and proof, protocol and interoperability.
**Human trust and safety** — 12 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 61 | 12 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 11 | 6 |
| Governed action | **Advancing strongly** | 275 | 67 |
| Implementation and interoperability | **Advancing strongly** | 318 | 105 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 94 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 65 material specification change unit(s) and 104 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-4D001AE994E33673` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-746E79D6A8393F1B` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E4BD97E09AE4522F` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-1CE9710873B1CEFD` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-1C8E311F544533D0` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-30C892BA98A120DB` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-ECF97EFDAC95C068` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-28320435EE09F30D` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-564AE6C4E77A8A6C` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
