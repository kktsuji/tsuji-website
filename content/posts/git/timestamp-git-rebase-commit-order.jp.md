---
title: "Gitのrebaseでcommitの順序を変更した時のtimestamp"
description: ""
date: 2024-10-12T15:00:00+09:00
lastmod:
draft: false
---

**要約:** `git rebase`コマンドでcommitを入れ替えると、commitの順序が変更される。これはGitの履歴においてcommitが時系列順に並んでいないことを意味する。

この例では、3つのcommitのtimestampは以下の通り。

- 3番目のcommit: 15:03:10
- 2番目のcommit 15:02:49
- 最初のcommit 15:02:34

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

`git rebase`コマンドを使って2番目と3番目のcommitを入れ替えてみる。

```bash
 git rebase -i HEAD~2

# 以下のように変更
pick 9c5a4d0 Second commit
pick 10bcb79 Third commit

# 変更後
pick 10bcb79 Third commit
pick 9c5a4d0 Second commit

# 保存してエディタを閉じる
```

2番目と3番目のcommitが入れ替わっており、これはGitの履歴でcommitのtimestampが時系列順に並んでいないことを意味する。

- 2番目のcommit 15:02:49
- 3番目のcommit: 15:03:10
- 最初のcommit 15:02:34

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
