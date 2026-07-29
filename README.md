# DTG Portfolio Monitor

> An independent, evidence-backed observatory for change across the Decentralized Trust Graph ecosystem.

[![Validate](https://github.com/OWNER/dtg-portfolio-monitor/actions/workflows/validate.yml/badge.svg)](https://github.com/OWNER/dtg-portfolio-monitor/actions/workflows/validate.yml)
[![Collect and report](https://github.com/OWNER/dtg-portfolio-monitor/actions/workflows/collect.yml/badge.svg)](https://github.com/OWNER/dtg-portfolio-monitor/actions/workflows/collect.yml)

## Purpose

GitHub already records repository activity. This project adds the missing portfolio layer: it collects activity across related ToIP and OpenVTC repositories, normalises it into an auditable event model, applies transparent significance rules, and produces reports that explain what changed, why it may matter, and where cross-repository review may be required.

This repository is independently maintained and is not an official Trust over IP Foundation or OpenVTC publication.

## What v0.2.0 provides

- configuration-driven monitoring of 13 repositories;
- collection of commits, pull requests, issues, releases, and repository metadata;
- incremental checkpoints to avoid repeatedly reporting old activity;
- resilient per-stream collection so empty repositories and isolated API failures do not abort the portfolio run;
- deterministic change-significance scoring;
- detection of explicit references to other monitored repositories;
- portfolio findings for empty, stale, cross-referenced, and incompletely collected repositories;
- repository-health reporting with configured and observed lifecycle states;
- daily and weekly Markdown reports;
- machine-readable JSON event and finding stores;
- scheduled GitHub Actions;
- GitHub Pages documentation;
- schema and configuration validation tests.

## Start here

1. Create a repository named `dtg-portfolio-monitor`.
2. Replace `OWNER` in badges and `_config.yml` with your GitHub username.
3. Commit this payload to the default branch.
4. Enable **Settings → Pages → Source: GitHub Actions**.
5. Run **Collect DTG portfolio activity** manually once.
6. Review the generated `reports/`, `data/`, and `docs/portfolio-status.md` changes.
7. Optionally enable the workflow's automatic commit step by leaving `persist_changes` set to `true`.

The workflow uses the built-in `GITHUB_TOKEN` for public GitHub API access. No additional secret is required for the initial deployment.

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

The monitor separates four concerns:

1. **Collection** records source activity without interpretation.
2. **Normalisation** maps GitHub objects into a stable local event schema.
3. **Classification** applies visible, deterministic significance rules.
4. **Reporting** groups events by workstream, repository, and implication.

Automated narrative should remain subordinate to traceable evidence. Every report item links to its source.

## Tracked scope

The complete registry is maintained in [`config/repositories.yaml`](config/repositories.yaml). It includes ToIP DTG coordination, specification, and task-force repositories, together with OpenVTC implementation and credential repositories.

## Governance boundary

The monitor may create findings in this repository, but it does not automatically open issues, submit comments, or modify content in upstream repositories. Upstream engagement remains a human decision.

## Licence

Apache-2.0. See [LICENSE](LICENSE).
