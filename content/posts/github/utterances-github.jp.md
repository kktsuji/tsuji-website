---
title: "GitHub Issuesを利用した静的ウェブサイト向けコメントシステム「utterances」"
description: ""
date: 2024-11-03T20:00:00+09:00
lastmod:
draft: false
---

**注：このブログはGiscusを採用しました。[この投稿](https://tsuji.tech/giscus-github/)を参照してください。**

[utterances](https://github.com/utterance/utterances)は、静的ウェブサイトにコメントフォームを埋め込むためのGitHub上に構築されたクールなツールです。

メリット：

- 無料、軽量、見た目がクール
- コメントは自分のリポジトリのGitHub issuesに保存される
- コメントするにはGitHubログインが必要（スパム防止）

デメリット：

- GitHubアカウントを持たない訪問者はコメントできない（技術ブログには問題なし）。

インストールはとても簡単です：

1. リポジトリに[utterances App](https://github.com/apps/utterances)をインストールします。（utterances-botがこのリポジトリのIssuesにコメントを書き込みます。ブログリポジトリを使用するか、コメント専用の新しいリポジトリを作成してください）
2. utterancesインストールページがコメントフォーム用のjavascriptを作成します。
3. ブログコードにスクリプトを追加します。

スクリプトは以下のようになります：

```javascript
<script
  src="https://utteranc.es/client.js"
  repo="account/repository"
  issue-term="pathname"
  label="comment"
  theme="github-dark"
  crossorigin="anonymous"
  async
></script>
```
