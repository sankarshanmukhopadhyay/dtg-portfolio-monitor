---
title: Architecture
nav_order: 7
permalink: /architecture/
---
# Architecture

```mermaid
flowchart LR
    A[13 monitored repositories] --> B[Scheduled GitHub collector]
    B --> C[Normalised JSON events]
    C --> D[Deterministic significance rules]
    D --> E[Daily and weekly reports]
    E --> F[GitHub Pages]
    D --> G[Cross-repository findings]
```

The baseline deliberately avoids a database. Version-controlled JSON and Markdown are sufficient for an auditable early-stage monitor and make changes reviewable through ordinary Git workflows.
