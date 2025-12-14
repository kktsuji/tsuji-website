---
title: "Gitのrebase squashのtimestamp"
description: ""
date: 2024-10-11T7:00:00+09:00
lastmod:
draft: false
---

**要約:** `git rebase`コマンドの`squash`は、複数のcommitを1つのcommitにまとめる。統合された新しいcommitのtimestampは、squashされた方のcommitと同じになる。

まず、Gitの履歴を確認する。この例では、3つのcommitがある。

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

2番目と3番目のcommitをsquashする。

```bash
git rebase -i HEAD~2
```

Gitは自動的にテキストエディタを開いてcommit履歴を編集できるようにする。以下の例では、commit `740a6c0`が`3a4da30`にsquashされることを意味する。`s`または`squash`はsquash操作を示す。

```bash
# 以下のように変更
pick 3a4da30 Second commit
pick 740a6c0 Third commit

# 変更後
pick 3a4da30 Second commit
s 740a6c0 Third commit

# 保存してエディタを閉じる
```

Gitは再度テキストエディタを開く。squashされたcommitのコメントを編集する。

```bash
# コメントを以下のように変更

# This is a combination of 2 commits.
# This is the 1st commit message:

Second commit

# This is the commit message #2:

Third commit

# --------------
# 変更後

Squash two commits

# 保存してエディタを閉じる
```

Gitの履歴を再確認する。

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

新しくsquashされたcommit `6ec67b0b200bfbc754c97ec78e44b1cba66bf294`のtimestampを確認する。これは元のGit履歴でpickされた方の`3a4da3017d82b33d88306acbbe657a0e6b930510`と同じになっている。
