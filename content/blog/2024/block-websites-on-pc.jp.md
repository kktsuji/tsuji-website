---
title: 'PC から Web サイトへのアクセスをブロック'
description: 'PC から Web サイトへのアクセスをブロクする方法に Today I Learned ポスト。'
date: 2024-05-30T20:29:55+09:00
lastmod: 
math: false
draft: false
---

## Windows

1. ``C:\Windows\System32\drivers\etc\hosts`` をバックアップ
2. ``hosts`` を開き、localhost IPアドレス ``127.0.0.1`` と、ブロックしたいWebサイトのドメインを追加

```bash
# Block Lists
127.0.0.1 twitter.com
127.0.0.1 x.com
```

3. 上書き保存

これで、``hosts`` に記載した Web サイトは、どの Web ブラウザからからのアクセスもブロックされるようになる。

Save your time!

(注意：``ping`` コマンドなどを含む、いかなる方法もブロックされることに留意が必要)