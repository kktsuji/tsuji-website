---
title: 'VSCode Settings の初期化方法'
description: 'VSCode Settings の初期化方法'
date: 2024-06-13T08:37:58+09:00
lastmod: 
math: false
draft: false
---

## Windows

1. VSCode windows を閉じる
2. file explorer or terminal を起動
2. ``%APPDATA%\Code\User\settings.json`` をバックアップした上で削除

## WSL (Windows Subsystem for Linux)

1. VSCode windows を閉じる
2. terminal で wsl を起動
3. ``~/.vscode-server/data/Machine/settings.json`` をバックアップした上で削除
