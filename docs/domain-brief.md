---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-01T18:28:08.821177Z  
**Evidence through:** 2026-10-01T18:05:47Z  
**Source revision:** `e34187bebe35098578eec2c5c3f18556e8ae4434` · **Collection run:** `36906856420` · **Publication state:** `workflow-generated`  
**Change units:** 802 · **Material:** 272  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 69
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 96

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 156 material change units, led by delivery and maintenance, authority and delegation.
**Governed action** — 67 material change units, led by credentials and proof, delivery and maintenance.
**Credentials and evidence** — 7 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 23 | 7 |
| Governed action | **Advancing strongly** | 257 | 67 |
| Implementation and interoperability | **Advancing strongly** | 351 | 156 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 6 material specification change unit(s) and 128 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 64 material specification change unit(s) and 151 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 3 material specification change unit(s) and 151 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F1A2330D7F66D989` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-7075D0E68C8DC009` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-B31B3B96153DA984` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-3949996A027EDF59` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-A941C4349B9AB12D` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B1B57DA7B8881F37` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-BE695EFE211C6D14` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-815DC3D6E2417981` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-B304870F334F361A` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
