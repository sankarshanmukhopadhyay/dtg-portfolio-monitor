---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-11T05:55:26.162140Z  
**Evidence through:** 2026-10-11T05:53:49Z  
**Source revision:** `6d75222e5bf2dfb399cc0976c6abf28a9a00fa7f` · **Collection run:** `38116285148` · **Publication state:** `workflow-generated`  
**Change units:** 393 · **Material:** 100  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 18
- **Review-required assertions:** 1
- **Watch assertions:** 8
- **Open findings:** 29

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 50 material change units, led by delivery and maintenance, credentials and proof.
**Governed action** — 20 material change units, led by protocol and interoperability, delivery and maintenance.
**Human trust and safety** — 10 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 27 | 10 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Active** | 3 | 2 |
| Governed action | **Advancing strongly** | 54 | 20 |
| Implementation and interoperability | **Advancing strongly** | 237 | 50 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.
- **Credentials and evidence ↔ Governed action.** Material activity is present on both sides of the declared `supplies-evidence-to` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Credentials and evidence.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: specification and implementation are moving together.** The monitor observed 2 material specification change unit(s) and 32 material implementation change unit(s).
- **Governed action: specification and implementation are moving together.** The monitor observed 20 material specification change unit(s) and 49 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-F9EF6F5B1B004531` | watch | moving-together | Credentials and evidence specification and implementation are moving together in this window. |
| `DTG-A-0FA27B139B14CD67` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-E1054C9DCAFD75D2` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-0B272FA02FC83206` | watch | observed | Material movement is present on both sides of the declared supplies-evidence-to relationship. |
| `DTG-A-BA1953D8C54D3118` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-1B3CA741D28A7831` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-C7346CD6487636A6` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-3AC23645D37890FA` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-54283C39ABF6648F` | watch | observed | Credentials and evidence has material activity while related capability Relationships and naming is quiet in this observation window. |

## What to watch next

1. Whether **Credentials and evidence** implementation experience feeds back into the associated specification work.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Relationships and naming** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
