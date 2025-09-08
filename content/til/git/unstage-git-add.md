---
title: 'Unstage Git Add Command'
description: ''
date: 2024-10-10T18:00:00+09:00
lastmod: 
draft: false
---

If you want to undo `git add` command, use `git reset`.

* `git reset <file>`: Unstage a specific file.
* `git reset`: Unstage all files.

A example for a specific file.

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

A example for all files.

```bash
git add .
git reset
```

Additionally, you can use `HEAD` or a `commit ID` with `git reset` command.

```bash
# For a specific file
git reset file.txt # Same as "git reset HEAD file.txt"
git reset HEAD file.txt # Same as "git reset file.txt"
git reset abc123 file.txt # Reset to the file.txt of the commit ID "abc123"

# For all files
git reset
git reset HEAD
git reset abc123
```

According to the message of `git status`, `git rm --cached <file>` also works. However, this command can only be applied to a specific file.
