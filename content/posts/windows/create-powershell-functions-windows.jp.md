---
title: "WindowsでPowerShell関数を作成する"
description: ""
date: 2026-07-17T8:00:00+09:00
lastmod:
draft: false
---

## WindowsでPowerShell関数を作成する

プロファイルファイルが存在するか確認します。

```powershell
Test-Path $PROFILE
```

結果が `False` なら、プロファイルファイルを作成します（すでに存在する場合は不要です）。

```powershell
New-Item -Type File -Path $PROFILE -Force
```

Notepadでプロファイルファイルを開きます。

```powershell
notepad $PROFILE
```

プロファイルファイルに関数を書き込みます。

```powershell
function cdpj {
    Set-Location "D:\my-project"
}
```

変更を反映するために、プロファイルファイルを再読み込みします。

```powershell
. $PROFILE
```
