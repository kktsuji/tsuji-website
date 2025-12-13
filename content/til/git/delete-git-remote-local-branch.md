---
title: "Delete Git Remote and Local Branch"
description: ""
date: 2024-11-08T21:00:00+09:00
lastmod:
draft: false
---

```bash
git --version
# git version 2.34.1
```

Delete remote branch:

```bash
git push -d <remote> <branch>
git push --delete <remote> <branch>
git push <remote> :<branch>

# For example:
git push -d origin feature/foo
git push origin :future/foo

git --help push
# OPTIONS
#       -d, --delete
#           All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.
```

Delete local branch

```bash
git branch -d <branch>
git branch --delete <branch>

git branch -D <branch>
git branch --delete --force <branch>

git --help branch
# OPTIONS
#        -d, --delete
#            Delete a branch. The branch must be fully merged in its upstream branch, or in HEAD if no upstream was set with --track or --set-upstream-to.
#        -D
#            Shortcut for --delete --force.
#        -f, --force
#            Reset <branchname> to <startpoint>, even if <branchname> exists already. Without -f, git branch refuses to change an existing branch. In combination with -d (or --delete), allow deleting the
#            branch irrespective of its merged status, or whether it even points to a valid commit. In combination with -m (or --move), allow renaming the branch even if the new branch name already exists,
#            the same applies for -c (or --copy).
```
