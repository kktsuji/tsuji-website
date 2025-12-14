---
title: "GitHub Discussionsを利用した静的ウェブサイト向けコメントシステム「Giscus」"
description: ""
date: 2024-11-04T09:00:00+09:00
lastmod:
draft: false
---

## 概要

[Giscus](https://github.com/giscus/giscus)は、静的ウェブサイトにコメントフォームを埋め込むためのGitHub Discussions上に構築されたコメントシステムです。

メリット：

- 無料、軽量、見た目がクール
- コメントは自分のリポジトリのGitHub Discussionsに保存される
- コメントするにはGitHubログインが必要（スパム防止）

デメリット：

- GitHubアカウントを持たない訪問者はコメントできない（しかし技術ブログには問題なし）

## Giscus vs utterances

Giscusは[utterances](https://github.com/utterance/utterances)から強くインスパイアされています。主要なコンセプトと使用方法はほぼ同じですが、いくつかの違いがあります。

- Gisccus
  - コメントを保存するためにGitHub Discussionsを使用
  - utterancesよりも豊富な機能（例：リアクション、投票）
- utterances
  - コメントを保存するためにGithub Issuesを使用

私はこのブログにGiscusを採用しました。なぜなら、GitHub IssuesよりもGitHub Discussionsの方がコメントを保存するのに適していると感じたからです。

## インストール

インストール手順：

1. リポジトリでDiscussions機能を有効にする（[GitHub document](https://docs.github.com/en/discussions)を参照）（giscus-botがこのリポジトリのDiscussionsにコメントを書き込みます。ブログリポジトリを使用するか、コメント専用の新しいリポジトリを作成してください）
2. リポジトリに[Giscus App](https://github.com/apps/giscus)をインストールします。
3. [giscus.app](https://giscus.app/)でjavascriptを作成します。いくつかのオプションをカスタマイズできます。
4. スクリプトをコピーしてブログコードに追加します。

スクリプトの例は以下のようになります：

```javascript
<script
  src="https://giscus.app/client.js"
  data-repo="user/repository"
  data-repo-id="xxxxxxx"
  data-category="Comments"
  data-category-id="xxxxxx"
  data-mapping="pathname"
  data-strict="0"
  data-reactions-enabled="1"
  data-emit-metadata="0"
  data-input-position="top"
  data-theme="dark"
  data-lang="en"
  crossorigin="anonymous"
  async
></script>
```

## 動的なテーマ変更

ページテーマの変更に合わせてGiscusのテーマを動的に変更するには、いくつかのコーディングが必要です。

私は、Hugoで動作する私のブログにこの機能を実装するために、Issueの[このコメント](https://github.com/giscus/giscus/issues/1200#issuecomment-1954929802)を参照しました。

以下のコードをhtmlに追加しました。

```javascript
<script>
    var theme = localStorage.getItem('data-theme') == null ? 'dark' : 'light';
</script>

<div class="comments">
    <script src="https://giscus.app/client.js"
        data-repo="user/repository"
        data-repo-id="xxxxxxx"
        data-category="Comments"
        data-category-id="xxxxxx"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="dark"
        data-lang="en"
        crossorigin="anonymous"
        async>
    </script>
</div>

<script>
    document.querySelector('script[src="https://giscus.app/client.js"]').setAttribute('data-theme', theme);
</script>
```

その後、javascriptのテーマ変更機能にこのスクリプトも追加しました。

```javascript
    const initTheme = (state) => {
        if (state === THEMES.DARK) {
            document.documentElement.classList.add(THEMES.DARK);
            document.documentElement.classList.remove(THEMES.LIGHT);
+            setGiscusTheme(THEMES.DARK);
        } else if (state === THEMES.LIGHT) {
            document.documentElement.classList.remove(THEMES.DARK);
            document.documentElement.classList.add(THEMES.LIGHT);
+            setGiscusTheme(THEMES.LIGHT);
        }
    };

+    function setGiscusTheme(theme) {
+        var iframe = document.querySelector('.giscus-frame');
+
+        if (iframe) {
+        var url = new URL(iframe.src);
+        url.searchParams.set('theme', theme);
+        iframe.src = url.toString();
+        }
+    }
```

詳細については[私のブログテーマリポジトリ](https://github.com/kktsuji/tsuji-website-theme)を参照してください。

## GitHub Discussions

Giscusシステムはこのブログのコメントを[私のブログリポジトリのDiscussions](https://github.com/kktsuji/tsuji-website/discussions)に保存します。
