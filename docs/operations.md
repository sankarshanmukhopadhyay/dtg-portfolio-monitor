---
title: Operations
nav_order: 6
---

# Operations

## Initial activation

1. Replace `OWNER` in `_config.yml` and `README.md`.
2. Enable GitHub Pages with GitHub Actions as the source.
3. Run the collection workflow manually.
4. Confirm that the workflow commits generated state and reports.
5. Review the first report before treating classifications as operationally useful.

## Permissions

The collection workflow requires:

```yaml
permissions:
  contents: write
```

The Pages workflow requires read access to contents plus Pages and OIDC deployment permissions.

## Failure handling

A failed collection does not update the successful checkpoint. API errors fail the workflow rather than silently producing an incomplete report.
