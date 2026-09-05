# Public repository baseline

This record captures controls reviewed under issue #21. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/adoption/authority | PASS | `README.md`, docs/config/status surfaces | Source repositories and assurance engines remain authoritative. |
| Licensing | PASS | `LICENSE` | None identified. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue/PR templates | None identified. |
| Dependency updates | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch protection | EVIDENCE REQUIRED | rulesets API returned no active ruleset on 2026-09-05 | Tracked separately as a repository-setting control. |
| Tests/evidence/publication | PASS / bounded | workflows, generated data/docs, validation and reconciliation machinery | Workflow green is not assurance green. |
| Version/release provenance | PASS | `VERSION`, `CHANGELOG.md`, release/docs surfaces | Publication remains maintainer judgment. |
| Authority boundary | PASS | README/methodology | Monitor state is derived evidence, not project or assessor authority. |

## Completion boundary

Repository-owned baseline gaps are closed by the remediation PR. Default-branch protection remains a GitHub-hosted residual tracked separately rather than represented as PASS.
