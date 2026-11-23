# DTG Portfolio Monitor observation publication credential

The collector generates **derived observations**, which become canonical
portfolio evidence only after protected-main PR acceptance. RAHP and the
Assessment Registry must not accept an unmerged branch or stale collection
artifact as the latest authoritative source.

## Dedicated GitHub App prerequisite

Install a GitHub App **only** on
`sankarshanmukhopadhyay/dtg-portfolio-monitor`, with repository permissions
**Contents: Read/write** and **Pull requests: Read/write**. This is separate
from the Toolkit's state-persistence App. Configure in Monitor repository
Settings → Secrets and variables → Actions:

- Repository **variable** `DTG_MONITOR_APP_ID`: numeric App ID.
- Repository **secret** `DTG_MONITOR_APP_PRIVATE_KEY`: complete PEM private key.

The workflow deliberately fails **before collection** if either setting is
absent. It does not fall back to the default GitHub Actions token, because
that can be prohibited from creating PRs and does not trigger the native
`pull_request` workflows needed for DCO/validation. Do not print the key.

## Publication and qualification

The collector uses the pinned `create-github-app-token` action with an
installation token constrained to this repository and the two exact write
permissions. The App's bot identity signs the generated-evidence commit using
its GitHub noreply address. `peter-evans/create-pull-request` creates a
reviewable PR. Required native DCO, validation and other protected-main rules
must pass. The App's merge attempt cannot bypass review or other rules.

A rejected merge leaves the PR for normal maintainer disposition. Its
observation is **not current accepted evidence** until merged. A missing
token, unexpected installation, permission error or branch-protection
rejection must not be disguised as source collection success. The source
collection window determines bounded catch-up, not unconditional freshness.
Review actual generated observation dates after publication.

## Live acceptance

1. Verify a scheduled or deliberately dispatched run obtains a scoped App
   token, collects actual source changes and produces a DCO-signed App-authored
   PR with a native PR event.
2. Verify required checks are attached to its merge candidate and normal
   protected-main acceptance succeeds.
3. Verify the accepted evidence path is readable by Toolkit
   `fetch_dtg_portfolio_snapshot.py --lookback-days 2` and Registry's live
   shadow. Do not enlarge the lookback window just to make a stale source pass.
4. Retain the run, PR, source commit, and acceptance evidence in the relevant
   operator tracker. This does not independently authorize Toolkit-to-Registry
   external assessment case writing.

Failure to satisfy these steps leaves monitor source publication unqualified.
