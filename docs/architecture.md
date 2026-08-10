---
title: Architecture
nav_order: 7
permalink: /architecture/
---
# Architecture

```mermaid
flowchart LR
    A[14 monitored repositories] --> B[Scheduled or manual GitHub collector]
    B --> C[Normalised JSON events]
    C --> D[Deterministic significance rules]
    D --> E[Daily and weekly reports]
    D --> G[Cross-repository findings]
    E --> H[Persist generated evidence]
    G --> H
    H --> I[Exact commit SHA]
    I --> J[Reusable Jekyll build and route validation]
    J --> F[GitHub Pages deployment]
```

The baseline deliberately avoids a database. Version-controlled JSON and Markdown are sufficient for an auditable early-stage monitor and make changes reviewable through ordinary Git workflows.

Publication is coupled to evidence persistence: the collection workflow passes the exact resulting commit SHA into the reusable Pages workflow. GitHub Pages therefore publishes the same revision that contains the generated portfolio evidence, rather than depending on a secondary workflow being triggered by the bot-authored commit.
