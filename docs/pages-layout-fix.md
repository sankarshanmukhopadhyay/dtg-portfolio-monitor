---
title: Pages layout fix
nav_exclude: true
layout: default
permalink: /maintenance/pages-layout-fix/
---

# Pages layout correction

The documentation build now applies the Just the Docs `default` layout to all normal pages through Jekyll defaults. Legacy `.md` compatibility redirects explicitly retain `layout: null`.

The site validator checks CSS class tokens rather than exact class attributes, allowing legitimate additional theme classes while still requiring the Just the Docs sidebar, header, and main layout.
