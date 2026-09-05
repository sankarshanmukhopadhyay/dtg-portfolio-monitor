# Security policy

## Supported versions

Security fixes are applied to current `main` and the latest supported release identified by repository version/release metadata. Older versions should be treated as unsupported unless a maintainer explicitly states otherwise.

## Reporting a vulnerability

Do not disclose undisclosed vulnerabilities in public issues. Use GitHub private vulnerability reporting when available, or contact the repository maintainer through a private channel identified on the maintainer profile.

Do not include GitHub tokens, private repository data, personal access tokens, workflow secrets, or sensitive deployment evidence in issues, reports, fixtures, or test output. The monitor is designed to operate with the least-privileged built-in `GITHUB_TOKEN` against public repositories.

Generated content is untrusted input. Reports must escape or normalise source text before publication and must never execute content retrieved from monitored repositories.

A defect in collection, routing, retained state, evidence reconciliation, or publication can invalidate derived portfolio evidence. Remediation must identify affected evidence and must not convert missing/indeterminate evidence into PASS or project authority.
