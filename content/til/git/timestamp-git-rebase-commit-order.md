---
title: 'Timestamp When Git Rebase Modifies the Commit Order'
description: ''
date: 2024-10-12T15:00:00+09:00
lastmod: 
draft: false
---

**Summary:** If `git rebase` command switches some commits, the commit order is modified. This means the commits are not ordered by time in git history.

In this example, timestamp of three commits are below.

* Third commit: 15:03:10
* Second commit 15:02:49
* Initial commit 15:02:34

```bash
git log

# commit 10bcb79e99dde756b16e74a3d27a26ea779a925c (HEAD -> main)
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:03:10 2024 +0900

#     Third commit

# commit 9c5a4d0ff35c9d960da8a0aba916613e05e6385f
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:02:49 2024 +0900

#     Second commit

# commit 0f76eb1e98f8c5071f3884587b3106f91b0a5c7a
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:02:34 2024 +0900

#     Initial commit
```

Let's switch the second and third commits by using `git rebase` command.

```bash
 git rebase -i HEAD~2

# Modify from
pick 9c5a4d0 Second commit
pick 10bcb79 Third commit

# to
pick 10bcb79 Third commit
pick 9c5a4d0 Second commit

# then save and close the editor
```

We can see the second and third commits are switched, which means the timestamp of commits are not ordered by time in git history.

* Second commit 15:02:49
* Third commit: 15:03:10
* Initial commit 15:02:34

```bash
git log

# commit 4f2c5197b69a7cc2c677e53f2d9817efa74d4103 (HEAD -> main)
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:02:49 2024 +0900

#     Second commit

# commit 7429f56400a5134874aeb8fa05bfb58b4fe36b2c
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:03:10 2024 +0900

#     Third commit

# commit 0f76eb1e98f8c5071f3884587b3106f91b0a5c7a
# Author: xxx <xxx@xxx.com>
# Date:   Sat Oct 12 15:02:34 2024 +0900

#     Initial commit
```
