# Contributing

Contributions should improve the monitor's evidence quality, reproducibility, or usefulness without presenting this repository as an authoritative DTG source.

## Principles

- Preserve source URLs and collection timestamps.
- Keep significance rules visible and deterministic.
- Separate observed facts from inferred implications.
- Do not automatically modify monitored upstream repositories.
- Add or update tests when changing collection, classification, or reporting behaviour.
- Avoid committing secrets, API tokens, or private repository content.

## Adding a repository

1. Add a unique entry to `config/repositories.yaml`.
2. Assign an organisation, workstream, role, lifecycle status, and reporting weight.
3. Add material paths and relevant labels when known.
4. Run `python -m dtg_monitor validate`.
5. Explain the monitoring rationale in the pull request.
