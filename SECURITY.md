# Security policy

Report vulnerabilities privately to the repository maintainer.

Do not include GitHub tokens, private repository data, personal access tokens, or workflow secrets in issues, reports, fixtures, or test output. The monitor is designed to operate with the least-privileged built-in `GITHUB_TOKEN` against public repositories.

Generated content should be treated as untrusted input. Reports escape or normalise source text before publication and should never execute content retrieved from monitored repositories.
