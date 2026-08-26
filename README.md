# DTG Portfolio Monitor

> An independent, evidence-backed observatory and decision-support layer for change across the Decentralized Trust Graph ecosystem.

[![Validate](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/validate.yml)
[![Collect and report](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/collect.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/actions/workflows/collect.yml)

## Purpose

GitHub already records repository activity. This project adds the portfolio layer: it collects activity across related ToIP and OpenVTC repositories, normalises it into auditable evidence, consolidates duplicate representations into change units, applies transparent deterministic rules, and surfaces what requires review, what should be watched, and which evidence supports each conclusion.

This repository is independently maintained and is not an official Trust over IP Foundation or OpenVTC publication.

## What v0.5.0 provides

- configuration-driven monitoring of the declared DTG portfolio;
- collection of commits, pull requests, issues, releases, and repository metadata;
- consolidated change units that prevent a PR and correlated merge commit from creating duplicate review obligations;
- stable finding fingerprints and explicit lifecycle/disposition fields;
- a governed disposition ledger requiring authority, rationale, timestamp, and evidence for non-open findings;
- separate **materiality**, **review urgency**, and **assurance impact** signals;
- deterministic capability pulse, convergence, specification/implementation alignment, and attention signals;
- machine-addressable assertions with stable IDs, review class, metrics, and evidence URLs;
- a decision-first DTG Domain Brief and dashboard: review now → watch → disposed → portfolio movement → raw evidence;
- observation provenance including evidence-through time, source revision, workflow run, and publication state;
- machine-readable event, finding, and awareness snapshots with bounded retention;
- daily and weekly report products;
- stable GitHub Pages routes with build-time validation;
- scheduled GitHub Actions collection and exact-revision Pages deployment;
- release automation that validates synchronized version declarations, tests, documentation build, and routes before tagging and publishing.

## Start here

For an existing deployment:

1. Open the generated **DTG Domain Brief** to see decision-required and watch signals.
2. Use the **Dashboard** for the portfolio-level review queue and capability movement.
3. Use **Portfolio Status** for the canonical event register and source links.
4. Inspect `data/awareness/` for the machine-readable assertion/provenance snapshot.
5. Record any authorized finding disposition in `config/finding-dispositions.yaml` through the normal issue/PR review path.

For a new deployment, enable **Settings → Pages → Source: GitHub Actions**, run **Collect DTG portfolio activity** manually once, and confirm that the resulting evidence commit is the exact revision deployed by the downstream Pages workflow.

## Local use

```bash
python -m pip install -r requirements.txt
python -m dtg_monitor validate
GITHUB_TOKEN=... python scripts/discover_repositories.py
GITHUB_TOKEN=... python -m dtg_monitor collect --lookback-days 7
python -m dtg_monitor report --period daily
python -m dtg_monitor report --period weekly
python -m unittest discover -s tests
```

## Executable governance model

The monitor separates seven concerns:

1. **Collection** records source activity without interpretation.
2. **Normalisation** maps GitHub objects into a stable local event schema.
3. **Consolidation** turns duplicate API representations into one logical change unit while preserving every evidence URL.
4. **Classification** applies visible deterministic materiality rules.
5. **Portfolio semantics** declare capabilities and allowed analytical relationships.
6. **Assertions and findings** create machine-addressable review obligations and coordination signals.
7. **Disposition and reporting** preserve authorized decisions separately from generated observations and render a decision-first operator view.

Automated interpretation remains subordinate to traceable evidence. The awareness layer is deterministic and does not require an LLM.

## Tracked scope

`config/repositories.yaml` is the curated authority for explicitly modelled repositories. `config/repository-discovery.yaml` adds deterministic automatic discovery from two trusted organizational namespaces: **`trustoverip/dtgwg*`** and **all public, non-archived `OpenVTC/*` repositories**. Each collection run writes `data/repository-discovery.json` and `data/effective-repositories.yaml`; collection and reporting consume the effective registry, and `docs/repositories.md` is regenerated from the same scope evidence.

Repositories under `sankarshanmukhopadhyay` or any other untrusted owner are not automatically admitted by naming similarity. They remain governed by explicit curated entries. This prevents personal forks, assurance tooling, profiles, and experiments from being conflated with the trusted dynamic scope. Existing curated OpenVTC entries override discovered defaults. See [Repository discovery](docs/repository-discovery.md).

## Governance boundary

The monitor may create findings and assertions **in this repository**, but it does not automatically open issues, submit comments, modify upstream content, or execute external assurance tooling. Upstream engagement and any assurance execution remain explicit human governance decisions.

`config/finding-dispositions.yaml` is governed source. Generated workflows read it but do not modify it. A finding therefore cannot mark itself resolved.

## Cross-specification coordination

`config/cross-spec-pressure-tests.yaml` records declared DTG composition seams as portfolio metadata. In v0.5.0 these declarations are **coordination inputs only**: the Portfolio Monitor does not invoke RAHP or another external assurance runner. This preserves the separation between observing/routing a review need and executing an assurance method.

## Licence

Apache-2.0. See [LICENSE](LICENSE).
