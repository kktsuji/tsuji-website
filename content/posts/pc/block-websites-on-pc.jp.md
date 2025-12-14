---
title: "PCでウェブサイトをブロックする"
description: "PCでウェブサイトをブロックする方法についてのToday I Learned投稿"
date: 2024-05-30T20:29:55+09:00
lastmod:
draft: false
---

## Windows

1. `C:\Windows\System32\drivers\etc\hosts`をバックアップする
2. `hosts`ファイルを開き、localhostのIPアドレス`127.0.0.1`とブロックしたいウェブサイトのドメインを追加する

```bash
# Block Lists
127.0.0.1 twitter.com
127.0.0.1 x.com
```

3. 保存する

`hosts`に追加したすべてのウェブサイトは、すべてのウェブブラウザでブロックされます。

時間を節約しましょう！

（注：`ping`コマンドなどのすべての方法も、このPCでブロックされます）
