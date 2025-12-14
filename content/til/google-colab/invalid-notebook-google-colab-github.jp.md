---
title: "GitHubに保存したGoogle Colabのノートブックが無効になる"
description: ""
date: 2025-07-09T09:00:00+09:00
lastmod:
draft: false
---

## GitHubに保存したGoogle Colabのノートブックが無効になる

Google ColabでGitHubに保存する際に、無効なノートブックが作成されることがある。

- Google ColabのTab > File > Save a copy in GitHub
- GitHubでノートブックを表示

```text
Invalid Notebook
There was an error rendering your Notebook: the 'state' key is missing from 'metadata.widgets'. Add 'state' to each, or remove 'metadata.widgets'.
```

## 原因

この問題は、ノートブックが`ipywidgets`を使用してスライダー、ボタン、プログレスバーなどのウィジェットを表示している場合に発生する。

## 解決策

GitHubに保存する前に、ノートブック内のすべての出力を削除する。

- Google ColabのTab > Edit > Clear all outputs
- ノートブックを再度保存（ctrl + s）
- Google ColabのTab > File > Save a copy in GitHub
