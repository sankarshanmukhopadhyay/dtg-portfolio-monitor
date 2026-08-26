# v0.5.2 — Governed Dynamic Repository Discovery

DTG Portfolio Monitor v0.5.2 makes repository scope dynamic while preserving explicit governance over what that scope means.

## Highlights

- Automatically discovers public, non-archived `trustoverip/dtgwg*` repositories.
- Automatically discovers public, non-archived repositories across the `OpenVTC` organization.
- Keeps repositories under `sankarshanmukhopadhyay` and other untrusted owners outside automatic admission, regardless of `dtg*` or `dtgwg*` naming.
- Persists machine-readable discovery decisions in `data/repository-discovery.json`.
- Generates `data/effective-repositories.yaml` as the collection scope and regenerates `/repositories/` from the same evidence.
- Preserves curated repository metadata over discovered defaults.
- Separates dynamic observation authority from curated semantic authority.
- Allows newly discovered repositories to remain intentionally unmapped to portfolio capabilities while retaining their activity through `unmapped_change_units`.

## Governance model

> **Discovery grants observation authority; curation grants semantic authority.**

A trusted discovered repository may be collected and reported immediately, but discovery does not assert specification status, capability membership, assurance, conformance, or endorsement. Those semantics remain governed by reviewed configuration.

## Assurance and evidence

The post-merge integration run for the dynamic-scope work completed the full collection-to-publication chain successfully: configuration validation, discovery, collection, report generation, evidence retention, unit tests, generated-output persistence, documentation build, route validation, and GitHub Pages deployment.

The generated tracked-repositories page records 26 effective repositories at the release baseline, distinguishing curated and dynamically admitted scope.

## Issues and pull requests

- #9 — governed dynamic discovery scope
- #13 — OpenVTC organization-wide discovery
- #14 — observation-versus-semantics runtime correction
- #15 — semantic separation implementation
- #16 — v0.5.2 release
