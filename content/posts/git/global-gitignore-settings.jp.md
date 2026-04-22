---
title: "グローバルなgitignore設定"
description: ""
date: 2026-04-22T09:00:00+09:00
lastmod:
draft: False
---

システム上のすべてのリポジトリ全体でファイルを無視するためのグローバルなgitignore設定をセットアップします。

Bash:

```bash
# グローバルなgitignoreファイルをセットアップする
git config --global core.excludesfile ~/.gitignore_global

# グローバルなgitignoreファイルを作成する
touch ~/.gitignore_global

# グローバルなgitignoreファイルにパターンを追加する
echo ".local-tmp/" >> ~/.gitignore_global

# グローバルなgitignore設定を確認する
git config --global core.excludesfile
cat ~/.gitignore_global
```

PowerShell:

```PowerShell
# グローバルなgitignoreファイルをセットアップする
git config --global core.excludesfile $env:USERPROFILE\.gitignore_global

# グローバルなgitignoreファイルを作成する
New-Item -ItemType File -Path $env:USERPROFILE\.gitignore_global -Force

# グローバルなgitignoreファイルにパターンを追加する
Add-Content -Path $env:USERPROFILE\.gitignore_global -Value ".local-tmp/"

# グローバルなgitignore設定を確認する
git config --global core.excludesfile
Get-Content -Path $env:USERPROFILE\.gitignore_global
```
