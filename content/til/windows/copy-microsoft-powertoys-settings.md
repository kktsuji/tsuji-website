---
title: "Copy Microsoft PowerToys Settings"
description: ""
date: 2025-10-18T16:00:00+09:00
lastmod:
draft: false
---

## Copy Microsoft PowerToys Settings

Open `%LocalAppData%\Microsoft\PowerToys\` in File Explorer. It contains settings files for each PowerToys module.

- Copy desired `settings.json`.
- Paste it to the same path on another PC.
- Restart PowerToys if it is running.

Examples:

You can check the contents of each json file to understand.

- PowerToys' general settings: `%LocalAppData%\Microsoft\PowerToys\settings.json`
- Keyboard Manager's remap settings: `%LocalAppData%\Microsoft\PowerToys\Keyboard Manager\default.json`
- etc.
