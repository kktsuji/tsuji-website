---
title: "Gitタグ"
description: ""
date: 2025-12-16T8:00:00+09:00
lastmod:
draft: false
---

## タグの作成

```bash
# 軽量タグ
git tag <tagname>

# メッセージ付き
git tag -a <tagname> -m "タグメッセージ"

# 特定のコミットに対して
git tag <tagname> <commit>
```

## リモートへのタグのプッシュ

```bash
# 単一のタグをプッシュ
git push <remote> <tagname>

# すべてのタグをプッシュ
git push <remote> --tags
```

## タグの表示

```bash
# すべてのタグを一覧表示
git tag

# タグの詳細を表示
git show <tagname>
```
