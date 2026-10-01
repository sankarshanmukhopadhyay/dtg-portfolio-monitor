---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-01T06:04:18.867706Z  
**Evidence through:** 2026-10-01T04:20:04Z  
**Source revision:** `21059e92770362ac9eb2957f942130d1e1f21973` · **Collection run:** `36822742530` · **Publication state:** `workflow-generated`  
**Change units:** 772 · **Material:** 270  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 68
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 93

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 161 material change units, led by delivery and maintenance, authority and delegation.
**Governed action** — 64 material change units, led by credentials and proof, delivery and maintenance.
**Credentials and evidence** — 7 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 25 | 7 |
| Governed action | **Advancing strongly** | 242 | 64 |
| Implementation and interoperability | **Advancing strongly** | 341 | 161 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 6 material specification change unit(s) and 128 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 60 material specification change unit(s) and 155 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 155 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-0DE3AE35D85CB3A9` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-3C24FDA4E078E947` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-D75FE75C53548C90` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-F6052257984203B3` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-2522312941E8C96C` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-0F652337371F1038` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-BE695EFE211C6D14` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-815DC3D6E2417981` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-882A01613ECD9A00` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
