---
title: 'Git Cherry-Pick No Commit Option'
description: ''
date: 2024-11-27T18:00:00+09:00
lastmod: 
draft: false
---

Use the option `-n` or `--no-commit`.

```bash
git cherry-pick -n <commit-ish>
git cherry-pick --no-commit <commit-ish>

# Examples
git cherry-pick -n feature/foo # branch
git cherry-pick -n abc012 # commit id
```

Usage:

```bash
git cherry-pick
# usage: git cherry-pick [<options>] <commit-ish>...
#    or: git cherry-pick <subcommand>

#     ...
#     -n, --no-commit       don't automatically commit
```
