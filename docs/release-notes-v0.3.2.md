---
title: v0.3.2 release notes
nav_order: 8
permalink: /releases/v0.3.2/
---
# v0.3.2: Theme and legacy-route compatibility

This hotfix ensures that GitHub Pages is built with the Just the Docs gem theme and that both the current clean routes and the two previously published `.md` URLs remain available.

The legacy URLs now redirect to their canonical pages:

- `/repositories.md` → `/repositories/`
- `/portfolio-status.md` → `/portfolio-status/`

The Pages workflow validates theme assets, clean routes, compatibility routes, and redirect targets before deployment.
