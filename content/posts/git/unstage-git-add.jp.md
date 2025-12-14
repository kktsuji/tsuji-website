---
title: "Git addコマンドのUnstage"
description: ""
date: 2024-10-10T18:00:00+09:00
lastmod:
draft: false
---

`git add`コマンドを取り消したい場合は、`git reset`を使う。

- `git reset <file>`: 特定のファイルをunstageする。
- `git reset`: すべてのファイルをunstageする。

特定のファイルの例。

```bash
echo "test" >> file.txt
git add file.txt

git status
# Changes to be committed:
#  (use "git rm --cached <file>..." to unstage)
#        new file:   file.txt

git reset file.txt

git status
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         file.txt
```

すべてのファイルの例。

```bash
git add .
git reset
```

さらに、`git reset`コマンドには`HEAD`または`commit ID`を使うこともできる。

```bash
# 特定のファイル
git reset file.txt # "git reset HEAD file.txt"と同じ
git reset HEAD file.txt # "git reset file.txt"と同じ
git reset abc123 file.txt # commit ID "abc123"のfile.txtにリセット

# すべてのファイル
git reset
git reset HEAD
git reset abc123
```

`git status`のメッセージによると、`git rm --cached <file>`も機能する。しかし、このコマンドは特定のファイルにのみ適用できる。
