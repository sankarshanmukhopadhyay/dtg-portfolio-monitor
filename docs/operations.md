---
title: Operations
nav_order: 8
permalink: /operations/
---
# Operations

## Initial activation

1. Replace `OWNER` in `_config.yml` and `README.md`.
2. Enable GitHub Pages with GitHub Actions as the source.
3. Run the collection workflow manually.
4. Confirm that the workflow commits generated state and reports.
5. Confirm that the dependent documentation job builds and deploys Pages from the exact persisted commit SHA.
6. Review the first report before treating classifications as operationally useful.

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

Each successful scheduled or manually dispatched collection performs one ordered chain: collect → report → test → persist → build documentation → validate site → deploy Pages. The persistence step exposes the resulting Git commit SHA as a job output, and the Pages workflow checks out that exact SHA. This avoids relying on a bot-authored `push` event to start another workflow and gives each publication an auditable source revision.

The Actions workflow intentionally does not provide a non-persisting collection mode. A Pages deployment must correspond to version-controlled evidence. For exploratory or dry-run collection, use the local CLI instead of the hosted collection workflow.

## Failure handling

A failed collection does not update the successful checkpoint. API errors fail the workflow rather than silently producing an incomplete report. Documentation deployment is downstream of the collection job, so collection, report-generation, test, persistence, or site-build failures prevent publication of a newer Pages state.
