---
title: "Create PowerShell Functions in Windows"
description: ""
date: 2026-07-17T8:00:00+09:00
lastmod:
draft: false
---

## Create PowerShell Functions in Windows

Confirm the profile file exists.

```powershell
Test-Path $PROFILE
```

If the result is `False`, create the profile file (no need if it already exists).

```powershell
New-Item -Type File -Path $PROFILE -Force
```

Open the profile file in Notepad.

```powershell
notepad $PROFILE
```

Write the function in the profile file.

```powershell
function cdpj {
    Set-Location "D:\my-project"
}
```

Refresh the profile file to apply the changes.

```powershell
. $PROFILE
```
