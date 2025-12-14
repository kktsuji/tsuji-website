---
title: "VSCode設定の初期化"
description: "VSCodeの設定を初期化する方法"
date: 2024-06-13T08:37:58+09:00
lastmod:
draft: false
---

## Windows

1. VSCodeウィンドウを閉じる
2. ファイルエクスプローラーまたはpowershellを開く
3. `%APPDATA%\Code\User\settings.json`をバックアップして削除する

## WSL（Windows Subsystem for Linux）

1. VSCodeウィンドウを閉じる
2. ターミナルでwslを開く
3. `~/.vscode-server/data/Machine/settings.json`をバックアップして削除する
