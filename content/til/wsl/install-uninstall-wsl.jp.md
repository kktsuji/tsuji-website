---
title: "WSLのインストールとアンインストール"
description: ""
date: 2025-02-01T16:00:00+09:00
lastmod:
draft: false
---

## 前提条件

1. コントロールパネル > プログラム > Windowsの機能の有効化または無効化を開く
2. 以下を有効にする：
   - Windows Subsystem for Linux
   - 仮想マシンプラットフォーム
   - （Hyper-Vは不要）

## WSLのインストール

1. PowerShellを管理者として開く
2. 以下のコマンドを実行してWSL2をインストール：

```powershell
# WSL2をインストール
wsl --install

# WSLをアップデート
wsl --update

# デフォルトバージョンをWSL2に設定
wsl --set-default-version 2

# 利用可能なディストリビューションをリスト
wsl -l -o

# Ubuntu 22.04をインストール
wsl --install -d Ubuntu-22.04
```

よく使う他のコマンド：

```powershell
# ヘルプ
wsl --help

# デフォルトディストリビューションを設定
wsl --set-default Ubuntu-22.04

# インストール済みディストリビューションを表示
wsl -l -v

# WSLをシャットダウン
wsl --shutdown
```

## WSLディストリビューションのアンインストール

1. WSLをシャットダウン `wsl --shutdown`
2. ディストリビューションが停止したことを確認 `wsl -l -v`
3. 設定 > アプリ > インストール済みアプリ > Ubuntu-22.04 > アンインストール

## 参考文献

- [Manual installation steps for older versions of WSL - Windows Learn](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
- [How to install Linux on Windows with WSL - Windows Learn](https://learn.microsoft.com/en-us/windows/wsl/install)
