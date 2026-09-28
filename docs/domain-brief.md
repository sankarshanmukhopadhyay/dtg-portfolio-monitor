---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-28T05:31:23.406091Z  
**Evidence through:** 2026-09-28T05:29:13Z  
**Source revision:** `a3968ddcba2a1c4b42f2275431ee5ca803fb2571` · **Collection run:** `36382165624` · **Publication state:** `workflow-generated`  
**Change units:** 1204 · **Material:** 348  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 74
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 123

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 199 material change units, led by delivery and maintenance, transport and routing.
**Governed action** — 90 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 5 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing** | 24 | 5 |
| Governed action | **Advancing strongly** | 436 | 90 |
| Implementation and interoperability | **Advancing strongly** | 526 | 199 |
| Portfolio coordination | **Active** | 2 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 4 material specification change unit(s) and 165 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 82 material specification change unit(s) and 196 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 8 material specification change unit(s) and 196 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-7BCC026ACE6501A4` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-930DC469C6F35F76` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-72B585E1C7D4B0E7` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-AF5E3E6F67EA44E7` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-EE08A50EFBEC73EF` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-F4DC24457A4E2F7B` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-0B17FC0E4EBA51DA` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-FE85CA9B20F6B085` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-97DC8517284379F8` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
