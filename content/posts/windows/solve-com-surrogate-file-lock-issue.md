---
title: "Solve 'The action can't be completed because the file is open in COM Surrogate': COM Surrogate File Lock Issue in Windows"
description: ""
date: 2025-12-27T16:00:00+09:00
lastmod:
draft: false
---

When deleting files in Windows, the issue of COM Surrogate (dllhost.exe) locking files can arise, preventing their deletion. The error message is 'The action can't be completed because the file is open in COM Surrogate'.

## Restart Explorer

1. Open Task Manager (`Ctrl` + `Shift` + `Esc`).
2. Find and select `Windows Explorer` in the Processes tab.
3. Click `Restart` at the bottom right.

## End COM Surrogate Processes

1. Open Task Manager (`Ctrl` + `Shift` + `Esc`).
2. Look for `COM Surrogate` or `dllhost.exe` processes in the Processes tab.
3. Select each `COM Surrogate` process and click `End Task`.
