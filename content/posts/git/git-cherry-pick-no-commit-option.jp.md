---
title: "Git Cherry-PickのNo Commitオプション"
description: ""
date: 2024-11-27T18:00:00+09:00
lastmod:
draft: false
---

オプション`-n`または`--no-commit`を使う。

```bash
git cherry-pick -n <commit-ish>
git cherry-pick --no-commit <commit-ish>

# 例
git cherry-pick -n feature/foo # branch
git cherry-pick -n abc012 # commit id
```

使い方:

```bash
git cherry-pick
# usage: git cherry-pick [<options>] <commit-ish>...
#    or: git cherry-pick <subcommand>

#     ...
#     -n, --no-commit       don't automatically commit
```
