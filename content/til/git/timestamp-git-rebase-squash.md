---
title: 'Timestamp of Git Rebase Squash'
description: ''
date: 2024-10-11T7:00:00+09:00
lastmod: 
draft: false
---

**Summary:** The `squash` in the `git rebase` command merges several commits into one commit. The timestamp of the integrated new commit is same as the picked commit that was squashed. 

First, check the git history. In this example, we see there are three commits.

```bash
git log -n 3

# commit 740a6c0eefa416a23238263735ce2eba40b516bc (HEAD -> main)
# Author: xxx <xxx@xxx.com>
# Date:   Fri Oct 11 07:57:34 2024 +0900

#     Third commit

# commit 3a4da3017d82b33d88306acbbe657a0e6b930510
# Author: xxx <xxx@xxx.com>
# Date:   Fri Oct 11 07:56:38 2024 +0900

#     Second commit

# commit 3fd876ecb7ca5efa2060cf4aaa2236ffcecda963
# Author: xxx <xxx@xxx.com>
# Date:   Fri Oct 11 07:56:14 2024 +0900

#     Initial commit
```

Let's squash the second and third commits.

```bash
git rebase -i HEAD~2
```

Git automatically opens the text editor to modify commit history. In the example below, this means the commit `740a6c0` is squashed into `3a4da30`. `s` or `squash` indicate the squash operation.

```bash
# Modify from
pick 3a4da30 Second commit
pick 740a6c0 Third commit

# to
pick 3a4da30 Second commit
s 740a6c0 Third commit

# then save and close the editor
```

Git re-opens the text editor again. We will edit comments of squashed commit.

```bash
# Modify comments from

# This is a combination of 2 commits.
# This is the 1st commit message:

Second commit

# This is the commit message #2:

Third commit

# --------------
# to

Squash two commits

# then save and close the editor
```

Re-check the git history.

```bash
git log

# commit 6ec67b0b200bfbc754c97ec78e44b1cba66bf294 (HEAD -> main)
# Author: xxx <xxx@xxx.com>
# Date:   Fri Oct 11 07:56:38 2024 +0900

#     Squash two commits

# commit 3fd876ecb7ca5efa2060cf4aaa2236ffcecda963
# Author: xxx <xxx@xxx.com>
# Date:   Fri Oct 11 07:56:14 2024 +0900

#     Initial commit
```

See the timestamp of the new squashed commit `6ec67b0b200bfbc754c97ec78e44b1cba66bf294`. This is same as the picked one `3a4da3017d82b33d88306acbbe657a0e6b930510` in the original git history.
