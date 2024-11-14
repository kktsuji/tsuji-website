---
title: 'Git Merge Fast-Forward Options'
description: ''
date: 2024-11-14T9:00:00+09:00
lastmod: 
draft: false
---

Three types of git merge options related to the way of merging:

- ``--ff``: Default. Merge without a commit if fast-forward is possible. Create a merge commit if not possible.
- ``--no-ff``: Always create a merge commit.
- ``--ff-only``: Merge without a commit if fast-forward is possible. Abort a process if not possible.

References:

- [git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
