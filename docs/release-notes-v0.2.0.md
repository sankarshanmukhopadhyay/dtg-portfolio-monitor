---
title: v0.2.0 release notes
nav_order: 10
permalink: /releases/v0.2.0/
---
# v0.2.0: Resilient collection and portfolio findings

The initial workflow exposed a valid but previously unhandled GitHub condition: the transitional `trustoverip/dtgwg-ux-tf` repository is empty, and GitHub responds to its commits endpoint with HTTP 409.

Version 0.2.0 treats this as evidence about repository state rather than as a system failure. Collection now continues when an individual activity stream is empty or unavailable, while non-ignorable failures are preserved as explicit warnings and review findings.

The release also introduces repository-health reporting, staleness checks, material cross-reference findings, machine-readable finding records, and Node 24-compatible GitHub Actions.
