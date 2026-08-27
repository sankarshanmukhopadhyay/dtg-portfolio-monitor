---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-08-27T04:25:12.473832Z  
**Evidence through:** 2026-08-27T04:24:13Z  
**Source revision:** `659be5e092f7cf70457ebaa6d9314031977a7404` · **Collection run:** `33039290908` · **Publication state:** `workflow-generated`  
**Change units:** 361 · **Material:** 169  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 34
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 61

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 97 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 56 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 12 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 17 | 12 |
| Governed action | **Advancing strongly** | 99 | 56 |
| Implementation and interoperability | **Advancing strongly** | 208 | 97 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 10 material specification change unit(s) and 80 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 48 material specification change unit(s) and 96 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 7 material specification change unit(s) and 96 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-D5075E858A37E248` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-576BBE3D6048C32D` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-A010AE56A4977124` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E60878D0206638CD` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-B508B1A3013BB355` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-99B4A3E10A087954` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-7A305195BBF3BC4C` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-80F8046A72E8A750` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-060FDBC18934E07E` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
