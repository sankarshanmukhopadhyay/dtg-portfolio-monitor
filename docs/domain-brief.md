---
title: DTG Domain Brief
nav_order: 2
permalink: /domain-brief/
---
# DTG Domain Brief

**Generated:** 2026-10-12T06:07:28.188270Z  
**Evidence through:** 2026-10-11T23:44:47Z  
**Source revision:** `1ad625b9bd0b72bc2b9ce896ca3c1803396c0b0b` · **Collection run:** `38210839327` · **Publication state:** `workflow-generated`  
**Change units:** 456 · **Material:** 130  

This is the situational-awareness view of the monitored DTG portfolio. It interprets observed GitHub evidence through the declared [DTG domain model]({{ '/domain-model/' | relative_url }}). It is not an official ToIP architectural statement.

## Review queue

- **Decision findings:** 21
- **Review-required assertions:** 2
- **Watch assertions:** 6
- **Open findings:** 36

Review-required items are deterministic coordination or alignment signals. They are not automatic declarations of specification failure.

## Where DTG is moving

The strongest observed movement is currently concentrated in **Implementation and interoperability, Governed action, and Human trust and safety**.

**Implementation and interoperability** — 58 material change units, led by delivery and maintenance, protocol and interoperability.
**Governed action** — 30 material change units, led by protocol and interoperability, delivery and maintenance.
**Human trust and safety** — 12 material change units, led by delivery and maintenance, protocol and interoperability.

## Portfolio pulse

| Capability | Pulse | Change units | Material |
|---|---|---:|---:|
| Human trust and safety | **Advancing strongly** | 29 | 12 |
| Relationships and naming | **Quiet this window** | 0 | 0 |
| Credentials and evidence | **Quiet this window** | 0 | 0 |
| Governed action | **Advancing strongly** | 93 | 30 |
| Implementation and interoperability | **Advancing strongly** | 242 | 58 |
| Portfolio coordination | **Quiet this window** | 0 | 0 |

> **Quiet is not a failure state.** It means no activity was observed in the monitored GitHub streams during this window; the capability may be stable, on a different cadence, or active elsewhere.

## Cross-workstream convergence

- **Governed action ↔ Implementation and interoperability.** Material activity is present on both sides of the declared `exercised-by` relationship around authority and delegation, credentials and proof.
- **Human trust and safety ↔ Governed action.** Material activity is present on both sides of the declared `pressure-tests` relationship around authority and delegation, credentials and proof.

## Specification and implementation alignment

- **Credentials and evidence: implementation movement is ahead of normative specification activity in this window.**
- **Governed action: specification and implementation are moving together.** The monitor observed 30 material specification change unit(s) and 57 material implementation change unit(s).
- **Governed action: implementation movement is ahead of normative specification activity in this window.**

## Attention signals

- Governed action has material activity while related capability Credentials and evidence is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Implementation and interoperability has material activity while related capability Credentials and evidence is quiet in this observation window. This is a coordination signal, not a finding of failure.
- Human trust and safety has material activity while related capability Credentials and evidence is quiet in this observation window. This is a coordination signal, not a finding of failure.

## Machine-addressable assertions

| Assertion | Class | State | Statement |
|---|---|---|---|
| `DTG-A-C4BD09BBE5A2E6AA` | review-required | implementation-ahead | Credentials and evidence implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-0FA27B139B14CD67` | watch | moving-together | Governed action specification and implementation are moving together in this window. |
| `DTG-A-A4963ED5BD4DC680` | review-required | implementation-ahead | Governed action implementation movement is ahead of normative specification activity in this window. |
| `DTG-A-1B3CA741D28A7831` | watch | observed | Material movement is present on both sides of the declared exercised-by relationship. |
| `DTG-A-B2ED127531BE65B5` | watch | observed | Material movement is present on both sides of the declared pressure-tests relationship. |
| `DTG-A-474B8BAA724B4A1D` | watch | observed | Governed action has material activity while related capability Credentials and evidence is quiet in this observation window. |
| `DTG-A-9C487FDC9ACF4249` | watch | observed | Implementation and interoperability has material activity while related capability Credentials and evidence is quiet in this observation window. |
| `DTG-A-3C4D3F040D4548D9` | watch | observed | Human trust and safety has material activity while related capability Credentials and evidence is quiet in this observation window. |

## What to watch next

1. Whether normative work catches up with implementation movement in **Credentials and evidence**.
2. Whether **Governed action** implementation experience feeds back into the associated specification work.
3. Whether normative work catches up with implementation movement in **Governed action**.
4. Whether activity resumes or remains intentionally stable in **Credentials and evidence** while related work advances.
5. Whether the current convergence between **Governed action** and **Implementation and interoperability** creates new cross-repository dependencies or review needs.

## Evidence trail

Use the [Dashboard]({{ '/dashboard/' | relative_url }}) for capability-level indicators and the [Portfolio Status]({{ '/portfolio-status/' | relative_url }}) for the canonical event register and source links.

The machine-readable awareness snapshot is persisted under `data/awareness/`. Assertions carry stable IDs, deterministic confidence and direct evidence URLs so each published interpretation can be reproduced from versioned evidence and configuration.
