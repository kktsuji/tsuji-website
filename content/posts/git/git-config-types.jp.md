---
title: "Git Configの種類"
description: ""
date: 2024-11-09T12:00:00+09:00
lastmod:
draft: false
---

3種類のgit config:

| オプション | ファイルの場所                   | 説明                         |
| ---------- | -------------------------------- | ---------------------------- |
| `--system` | `/etc/gitconfig`                 | システム全体（全ユーザー）用 |
| `--global` | `~/.gitconfig`                   | ユーザーの全リポジトリ用     |
| `--local`  | `project_folder/.git/.gitconfig` | リポジトリ用                 |

Gitは`--system`、`--global`、`--local`の順にconfigを読み込む。後から読み込まれた設定が優先される。

設定リストを表示:

```bash
# すべての設定
git config -l

# Globalの設定
git config --global -l
```

使い方:

```bash
git config
```

参考文献:

- [Customizing Git - Git Configuration - git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
