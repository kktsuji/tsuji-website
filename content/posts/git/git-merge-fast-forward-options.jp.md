---
title: "Git MergeのFast-Forwardオプション"
description: ""
date: 2024-11-14T9:00:00+09:00
lastmod:
draft: false
---

mergeの方法に関連する3種類のgit mergeオプション:

- `--ff`: デフォルト。fast-forwardが可能ならcommitせずにmergeする。不可能ならmerge commitを作成する。
- `--no-ff`: 常にmerge commitを作成する。
- `--ff-only`: fast-forwardが可能ならcommitせずにmergeする。不可能なら処理を中止する。

参考文献:

- [git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
