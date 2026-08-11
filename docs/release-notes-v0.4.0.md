---
title: Release notes v0.4.0
nav_order: 11
permalink: /release-notes-v0.4.0/
---
# v0.4.0 — DTG situational awareness

v0.4.0 expands the DTG Portfolio Monitor from evidence-backed repository monitoring into a deterministic **DTG situational-awareness layer**.

The release preserves the existing event collection, significance scoring, evidence stores, daily/weekly reports, and GitHub Pages deployment model. It adds a declared semantic layer between repository activity and portfolio interpretation so that the monitor can answer not only **what changed**, but also **which DTG capabilities are moving together and where coordination may deserve attention**.

## Highlights

- Add `config/portfolio-model.yaml` to map monitored workstreams into DTG capabilities and declare analytical relationships.
- Add capability pulse states without treating low activity as negative project health.
- Detect cross-capability convergence across declared relationships.
- Detect specification/implementation movement and strong asymmetry signals.
- Persist machine-readable awareness snapshots under `data/awareness/`.
- Add the generated **DTG Domain Brief** as the easy-to-grasp situational-awareness view.
- Expand the dashboard with capability movement and portfolio-intelligence indicators.
- Preserve Portfolio Status as the canonical event register and source-evidence view.
- Document the analytical/non-normative interpretation boundary.
- Add the active Verifiable Data Structures repository and retain Relationship Cards as transitional lifecycle evidence.

## Design principle

The awareness layer is deterministic and auditable. It does not require an LLM. Generated narrative remains a rendering of versioned GitHub evidence, configuration, and awareness JSON.
