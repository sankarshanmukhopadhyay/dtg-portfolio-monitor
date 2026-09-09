---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-09T16:43:52.734424Z  
**Evidence through:** 2026-09-09T16:30:05Z  
**Source revision:** `dd820b728c96c0f2f31fa32ac71fa73c1731d7e2` · **Collection run:** `34378377270` · **Publication state:** `workflow-generated`  
**Change units:** 690 · **Material:** 227  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 58
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 73

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 100 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 50 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 32 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 46 | 32 |
| Governed action | **Advancing strongly** | 208 | 50 |
| Implementation and interoperability | **Advancing strongly** | 227 | 100 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 18 material specification change unit(s) and 85 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 48 material specification change unit(s) and 93 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 93 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F9DB6C919750A1BE` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-8DEA9DC4DA1FD9CB` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-B78E5807F5D68C40` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-AD8AA81D8F7BDFA3` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-9D422C652BB0697D` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-E7A485DAFA2234F8` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-618B9743753B4257` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-DC588D2E5E609776` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-E4755251F5A163ED` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
