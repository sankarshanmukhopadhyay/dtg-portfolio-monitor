---
title: Release notes v0.5.1
nav_exclude: true
---
# v0.5.1 — Operational Validation Patch

v0.5.1 fixes the first end-to-end operational defect found after v0.5.0 and makes substantive monitor changes automatically exercise the real collection pipeline on `main`.

## Fixed

- Direct execution of `scripts/prune_evidence.py` now bootstraps the repository root before importing `dtg_monitor`, matching the invocation used by GitHub Actions.
- Regression coverage now verifies that the pruning script can be loaded in direct-script mode with no externally supplied `PYTHONPATH`.

## Operational assurance

The collection workflow now also runs on `main` pushes that modify monitor source, scripts, configuration, requirements, or the collection workflow. Generated evidence commits do not match these paths, preventing recursion.

The required acceptance path is:

**collect → reports → retention → tests → persist evidence → build Pages → validate routes → deploy**

## Governance boundary

RAHP/external assurance execution remains deferred. This patch changes only the monitor's own operational validation and release reliability.
