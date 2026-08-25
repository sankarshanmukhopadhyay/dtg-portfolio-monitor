---
title: Operations
nav_order: 10
permalink: /operations/
---
# Operations

## Initial activation

1. Replace `OWNER` in `_config.yml` and `README.md` if deploying a fork.
2. Enable GitHub Pages with GitHub Actions as the source.
3. Run the collection workflow manually.
4. Confirm that the workflow commits generated state and reports.
5. Confirm that the dependent documentation job builds and deploys Pages from the exact persisted commit SHA.
6. Review the first decision queue and Domain Brief before treating classifications as operationally useful.

## Permissions

The collection workflow persists evidence and directly invokes the reusable Pages deployment workflow. Its workflow-level permissions therefore cover both operations:

```yaml
permissions:
  contents: write
  pages: write
  id-token: write
```

The reusable Pages workflow narrows content access to read-only while retaining Pages and OIDC deployment permissions.

## Collection-to-publication contract

Each successful scheduled or manually dispatched collection performs one ordered chain:

```text
collect → consolidate → findings → reports/assertions → retention → tests → persist → build → site validation → deploy
```

The persistence step exposes the resulting Git commit SHA as a job output, and the Pages workflow checks out that exact SHA. This avoids relying on a bot-authored `push` event to start another workflow and gives each publication an auditable source revision.

The Actions workflow intentionally does not provide a non-persisting collection mode. A Pages deployment must correspond to version-controlled evidence. For exploratory or dry-run collection, use the local CLI instead of the hosted collection workflow.

## Provenance contract

Awareness snapshots persist:

- `generated_at`;
- the latest source-event timestamp observed as `evidence_through`;
- `GITHUB_SHA` as the workflow source revision when running in Actions;
- `GITHUB_RUN_ID` as the collection/report run identifier;
- the generating repository;
- whether the snapshot was workflow-generated or locally generated.

The Domain Brief and dashboard expose the same provenance. A reader should therefore be able to determine both **how fresh the evidence is** and **which monitor revision produced the interpretation**.

## Finding review and disposition

Generated findings remain `open` until an authorized review explicitly disposes them. Supported terminal/non-open states are `resolved`, `superseded`, `duplicate`, `accepted-risk`, and `not-applicable`.

A valid manual disposition should record at least:

```yaml
authority:
  actor: <GitHub identity or governance role>
  basis: <authority basis>
disposition:
  reason: <short rationale>
  recorded_at: <RFC3339 timestamp>
  evidence:
    - <URL or repository path>
```

The monitor must not infer resolution merely because an item disappears from a later observation window.

## Failure handling

A failed collection does not update the successful checkpoint. API errors fail the workflow rather than silently producing an incomplete report. Documentation deployment is downstream of collection, analysis, retention, tests and persistence, so failures prevent publication of a newer Pages state.

Collection warnings that survive resilient per-stream collection are represented as urgent findings with unknown assurance impact so degraded evidence cannot masquerade as a clean observation.

## Generated-evidence retention

Git is an auditable publication channel, not an unbounded event warehouse.

Two controls bound generated material:

- `daily_report_retention_months` controls generated daily Markdown reports;
- `evidence_snapshot_retention_months` controls daily JSON snapshots under `data/events/`, `data/findings/`, and `data/awareness/`.

The scheduled collection workflow runs `scripts/prune_evidence.py` after report generation and before tests/persistence. By default, recent daily evidence remains directly browsable while older daily snapshots are removed from the current tree. Weekly reports remain the longer-horizon human summary, and all deleted versions remain recoverable from Git history. Upstream GitHub URLs remain the external evidence of record.

Retention is calendar-month based and deterministic. A retention value below one disables pruning rather than deleting all data.

## Release operations

v0.5.x releases are intended to be produced by a dedicated GitHub Actions release workflow. The workflow must validate the requested semantic version, verify that the target is the current `main` revision, run the repository validation/tests and site build checks, then create the tag and GitHub Release. Maintainers should not create a parallel manual tag for the same release.

## Mermaid diagrams

Mermaid rendering is provided by Just the Docs and is enabled through the root `_config.yml`. The Mermaid version is pinned so GitHub Pages builds are reproducible. Documentation authors can use fenced `mermaid` blocks directly; do not add page-specific Mermaid scripts or duplicate initialization code.

The documentation test suite verifies that Mermaid remains enabled while Mermaid diagram sources exist. The Pages workflow remains the end-to-end check that the theme loads the renderer and emits the published diagrams.
