# Changelog

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
