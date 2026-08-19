# DTG Portfolio Monitor

> An independent, evidence-backed observatory for change across the Decentralized Trust Graph ecosystem.

[![Validate](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/validate.yml)
[![Collect and report](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/collect.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/collect.yml)

## Purpose

GitHub already records repository activity. This project adds the missing portfolio layer: it collects activity across related ToIP and OpenVTC repositories, normalises it into an auditable event model, applies transparent significance rules, and produces reports that explain what changed, why it may matter, and where cross-repository review may be required.

This repository is independently maintained and is not an official Trust over IP Foundation or OpenVTC publication.

## What v0.4.0 provides

- configuration-driven monitoring of 14 repositories;
- collection of commits, pull requests, issues, releases, and repository metadata;
- incremental checkpoints to avoid repeatedly reporting old activity;
- resilient per-stream collection so empty repositories and isolated API failures do not abort the portfolio run;
- deterministic change-significance scoring;
- detection of explicit references to other monitored repositories;
- portfolio findings for empty, stale, cross-referenced, and incompletely collected repositories;
- repository-health reporting with configured and observed lifecycle states;
- consolidated change units that reduce duplicate commit and pull-request reporting;
- recurring-theme analysis and a compact portfolio dashboard;
- a declared DTG portfolio semantic model that maps workstreams to capabilities;
- deterministic capability pulse, convergence, specification/implementation alignment, and attention signals;
- machine-readable situational-awareness snapshots under `data/awareness/`;
- a generated DTG Domain Brief that explains portfolio movement before exposing the detailed evidence register;
- stable clean GitHub Pages routes with build-time route validation;
- dependency-free portfolio status ordered by date then repository;
- dedicated cross-repository change and tagged-release registers;
- bounded daily-report retention (current and previous calendar month by default) plus weekly Markdown reports;
- machine-readable JSON event and finding stores;
- scheduled GitHub Actions;
- GitHub Pages documentation;
- schema and configuration validation tests.

## Start here

1. Create a repository named `dtg-portfolio-monitor`.
2. The GitHub Pages and repository URLs are configured for `sankarshanmukhopadhyay/dtg-portfolio-monitor`.
3. Commit this payload to the default branch.
4. Enable **Settings → Pages → Source: GitHub Actions**.
5. Run **Collect DTG portfolio activity** manually once.
6. Confirm that the run persists the generated `reports/`, `data/`, and documentation outputs.
7. Confirm that the downstream **Build and deploy current documentation** job deploys GitHub Pages from that exact persisted commit.

Every successful Actions-based collection persists its generated evidence before invoking the reusable Pages workflow. The deployment is pinned to the resulting commit SHA, so the published site and version-controlled evidence remain aligned. The workflow uses the built-in `GITHUB_TOKEN` for public GitHub API access and repository persistence; no additional secret is required for the initial deployment.

## Local use

```bash
python -m pip install -r requirements.txt
python -m dtg_monitor validate
GITHUB_TOKEN=... python -m dtg_monitor collect --lookback-days 7
python -m dtg_monitor report --period daily
python -m dtg_monitor report --period weekly
python -m unittest discover -s tests
```

## Reporting model

The monitor separates six concerns:

1. **Collection** records source activity without interpretation.
2. **Normalisation** maps GitHub objects into a stable local event schema.
3. **Classification** applies visible, deterministic significance and theme rules.
4. **Portfolio semantics** declare how workstreams map to DTG capabilities and relationships.
5. **Situational awareness** derives capability movement, convergence, alignment, and attention signals.
6. **Reporting** renders the machine-readable evidence and awareness state for different audiences.

Automated narrative remains subordinate to traceable evidence. The awareness layer is deterministic and does not require an LLM; source events, configuration, and generated snapshots remain the evidence trail.

## Tracked scope

The complete registry is maintained in [`config/repositories.yaml`](config/repositories.yaml). It includes ToIP DTG coordination, specification, and task-force repositories, together with OpenVTC implementation and credential repositories.

## Governance boundary

The monitor may create findings in this repository, but it does not automatically open issues, submit comments, or modify content in upstream repositories. Upstream engagement remains a human decision.

## Licence

Apache-2.0. See [LICENSE](LICENSE).


### Cross-specification assurance coordination

`config/cross-spec-pressure-tests.yaml` declares eight DTG composition seams, all now runnable through RAHP Toolkit. The Portfolio Monitor exposes readiness, evidence grade and relationships; RAHP Toolkit owns manual execution, evidence and durable review issues through the optional `profiles/dtg/` pack. RAHP core remains ecosystem-neutral. Upstream issue filing remains a human governance decision after RAHP findings are triaged.
