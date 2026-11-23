# Public repository baseline

This record captures controls reviewed under issue #21. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/adoption/authority | PASS | `README.md`, docs/config/status surfaces | Source repositories and assurance engines remain authoritative. |
| Licensing | PASS | `LICENSE` | None identified. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue/PR templates | None identified. |
| Dependency updates | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch protection | PASS | GitHub REST read-back on 2026-11-23: active `protect-main` ruleset [#25613855](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/rules/25613855), targeting `~DEFAULT_BRANCH`; deletion/non-fast-forward protection, linear history, PR and resolved conversation requirements; required native checks `DCO / DCO`, `validate`, `pages-build` (GitHub Actions integration `15368`); zero bypass actors. | Hosted rules may subsequently change; recheck API to validate ongoing enforcement. |
| Tests/evidence/publication | PASS / bounded | workflows, generated data/docs, validation and reconciliation machinery | Workflow green is not assurance green. |
| Version/release provenance | PASS | `VERSION`, `CHANGELOG.md`, release/docs surfaces | Publication remains maintainer judgment. |
| Authority boundary | PASS | README/methodology | Monitor state is derived evidence, not project or assessor authority. |

## Completion boundary

Repository-owned baseline controls, including the hosted default-branch protection ruleset, are now recorded as PASS based on the **2026-11-23 API read-back**, not merely repository policy text. This is a point-in-time governance configuration verification, not a guarantee against future administrator changes or an external certification. Follow [issue #27](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor/issues/27) for the administrative enforcement evidence and closure decision.
