---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-02T05:47:04.292142Z  
**Evidence through:** 2026-10-02T05:46:02Z  
**Source revision:** `ce0213f02e5d95629343cd8d76378a03b5cafbba` · **Collection run:** `36970395743` · **Publication state:** `workflow-generated`  
**Change units:** 827 · **Material:** 269  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 67
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 94

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 156 material change units, led by delivery and maintenance, authority and delegation.
**Governed action** — 64 material change units, led by credentials and proof, delivery and maintenance.
**Credentials and evidence** — 7 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 24 | 7 |
| Governed action | **Advancing strongly** | 247 | 64 |
| Implementation and interoperability | **Advancing strongly** | 383 | 156 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 6 material specification change unit(s) and 125 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 62 material specification change unit(s) and 150 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 150 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F1A2330D7F66D989` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-60C0759728D5CBA8` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-841F395548FD786C` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-88501CD221470336` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-5517B091DA7B19E0` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F4BBFD09CD705FE4` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-BE695EFE211C6D14` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-815DC3D6E2417981` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-1975A42EECFAB6C1` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
