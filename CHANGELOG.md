# Changelog

## [0.3.0] - 2026-07-29

### Fixed

- Load the root Jekyll configuration when building the `docs/` source tree.
- Attach the `pages` step identifier to `actions/configure-pages`, where `base_path` is produced.
- Replace public links to source `.md` files with stable, base-path-aware clean URLs.
- Configure the actual GitHub Pages owner and repository rather than placeholder values.

### Added

- Build-time validation for required published routes and leaked `.md` links.
- Stable routes for repositories, portfolio status, reports, dashboard, methodology, architecture, and operations.
- Consolidated change units that collapse duplicate commit and pull-request representations.
- Recurring activity-theme analysis.
- Generated portfolio dashboard and report index pages.
- Tests for documentation routes, source links, consolidation, and themes.

### Changed

- Advance package and documentation metadata to v0.3.0.
- Persist generated dashboard and report-navigation artifacts during scheduled collection.

## [0.2.0] - 2026-07-29

### Fixed

- Treat GitHub's `409 Git Repository is empty` response as a valid empty commit stream.
- Prevent one repository stream failure from aborting collection across the whole portfolio.
- Preserve non-ignorable API failures as collection warnings and review findings.

### Added

- Repository health reporting with observed state and latest push date.
- Findings for empty repositories, stale repositories, material cross-repository references, and collection gaps.
- Machine-readable daily finding records under `data/findings/`.
- Tests covering empty-repository handling and finding generation.

### Changed

- Upgrade `actions/checkout` to v5 and `actions/setup-python` to v6 for Node 24 compatibility.
- Identify the empty UX repository as a transitional lifecycle record rather than an operational failure.
- Advance the package and documentation baseline to v0.2.0.

## [0.1.0] - 2026-07-29

### Added

- Initial registry of 13 ToIP DTG and OpenVTC repositories.
- GitHub API collection for metadata, commits, pull requests, issues, and releases.
- Deterministic significance classification.
- Explicit cross-repository reference detection.
- Daily and weekly Markdown report generation.
- JSON event storage and collection checkpoint.
- Validation and unit tests.
- Scheduled collection and GitHub Pages workflows.
- Guided documentation for setup, methodology, architecture, and operations.
