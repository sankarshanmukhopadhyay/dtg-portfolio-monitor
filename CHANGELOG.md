# Changelog

## [Unreleased]

### Added

- Add a synchronized cross-specification pressure-test registry that declares runnable and candidate DTG composition seams and points execution to RAHP Toolkit.
- Document the durable RAHP review-issue and upstream-triage governance model on the repository inventory page.
- Add a dedicated cross-repository change register based on explicit references between monitored repositories.
- Add a compact tagged-release activity pulse showing release counts and the latest release per repository.
- Add configurable daily-report retention, keeping the current and previous calendar month by default.

### Fixed

- Enable Just the Docs Mermaid support so diagrams on the domain-model and architecture pages render on GitHub Pages.
- Add a regression test requiring Mermaid configuration whenever diagram sources are present.

### Changed

- Replace the JavaScript-dependent portfolio event filters with a dependency-free canonical event register ordered by date (newest first), then repository.
- Surface tagged-release and cross-repository change counts on the portfolio dashboard.

## [0.4.0] - 2026-08-11

### Added

- Add `trustoverip/dtgwg-vds-tf` as the active, critical-weight repository for the DTG Verifiable Data Structures specification.
- Add a declared DTG portfolio semantic model in `config/portfolio-model.yaml`.
- Add deterministic capability pulse, cross-capability convergence, specification/implementation alignment, and related-capability attention signals.
- Persist machine-readable situational-awareness snapshots under `data/awareness/`.
- Add the generated DTG Domain Brief and capability-oriented dashboard.
- Add documentation for the domain model, awareness methodology, and interpretation boundary.

### Changed

- Reclassify `trustoverip/dtgwg-rcards-tf` as a low-weight transitional lifecycle record so activity is attributed to the active VDS repository.
- Redesign the portfolio-status report around a synthesis-first information architecture.
- Replace repeated material, repository, and cross-workstream renderings with one canonical filterable event register.
- Add explicit breaking-change callouts, leading engineering threads, compact signal tags, significance-band guidance, and a collapsed inactive-repository summary.
- Explain consolidated commit/PR evidence and signal abbreviations in the methodology.
- Expand scheduled persistence so awareness data and the Domain Brief are deployed from the same evidence-pinned commit.

## [0.3.2] - 2026-07-29

### Fixed

- Apply the Just the Docs gem theme explicitly during the GitHub Actions Jekyll build.
- Preserve the previously published `/repositories.md` and `/portfolio-status.md` URLs as compatibility redirects.
- Validate clean routes, legacy routes, and Just the Docs theme assets before deployment.
- Complete the Just the Docs configuration for search, navigation, footer, and back-to-top behaviour.

## [0.3.1] - 2026-07-29

### Fixed

- Replace residual public `.md` links on the documentation homepage with clean, base-path-aware routes.
- Add or preserve explicit permalinks for repository, portfolio-status, report, and dashboard pages.
- Align the committed documentation with the route-validation tests introduced in v0.3.0.
- Restore a green validation workflow before GitHub Pages deployment.

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
