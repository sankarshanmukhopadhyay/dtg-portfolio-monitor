---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-09-07T04:49:24.819181Z  
**Evidence through:** 2026-09-07T00:23:33Z  
**Source revision:** `c62d97ceea50b5d38929ca2a64dff4c780ac1a45` · **Collection run:** `34084468177` · **Publication state:** `workflow-generated`  
**Change units:** 328 · **Material:** 124  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 29
- **Review-required assertions:** 0
- **Watch assertions:** 9
- **Open findings:** 38

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Credentials and evidence**.

**Implementation and interoperability** — 46 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 34 material change units, led by delivery and maintenance, protocol and interoperability.
**Credentials and evidence** — 17 material change units, led by delivery and maintenance, credentials and proof.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Quiet this window** | 0 | 0 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Advancing strongly** | 29 | 17 |
| Governed action | **Advancing strongly** | 115 | 34 |
| Implementation and interoperability | **Advancing strongly** | 91 | 46 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 12 material specification change unit(s) and 41 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 32 material specification change unit(s) and 40 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 1 material specification change unit(s) and 40 material implementation change unit(s).

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Governed action has material activity while related capability Human trust and safety is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F78201A232A8EEDF` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-36789DACC9B77348` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-A305DADFCFF7702F` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-6CCC0A15F466E6B4` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-560FA044A08ADFF3` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-D60F976DE0D3E723` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-8C015F80B7E6232E` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |
| `DTG-A-7DF0358DB35E53F0` | watch | observed | Credentials and evidence has material activity while related capability Human trust and safety is quiet in this observation window. |
| `DTG-A-AF53DC9408F1ADE8` | watch | observed | Governed action has material activity while related capability Human trust and safety is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
4. Whether activity resumes or remains intentionally stable in **Human trust and safety** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
