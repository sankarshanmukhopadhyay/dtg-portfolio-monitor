---
title: v0.3.0 release notes
nav_order: 9
permalink: /releases/v0.3.0/
---
# v0.3.0: Reliable publication and change intelligence

Version 0.3.0 repairs the GitHub Pages publication contract and improves the usefulness of portfolio reports.

The Pages workflow now loads the root Jekyll configuration explicitly, uses the configured project base path, validates the built site, and publishes stable clean URLs. Source Markdown names are no longer presented as public URLs.

The reporting layer now consolidates duplicate commit and pull-request representations into change units, identifies recurring themes, publishes a compact portfolio dashboard, and generates report navigation artifacts.
