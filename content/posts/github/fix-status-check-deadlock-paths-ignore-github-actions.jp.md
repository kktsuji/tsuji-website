---
title: 'GitHub Actionsのpaths-ignoreスキップワークフローで必須ステータスチェックのデッドロックを解消する'
description: ""
date: 2026-03-07T16:00:00+09:00
lastmod:
draft: false
---

## デッドロックの状況

### ブランチ保護設定

- ステータスチェック: `unit-tests`（必須）

### GitHub Actionsワークフロー

ワークフロー`.github/workflows/tests.yml`は、`src/`または`tests/`が変更された場合にのみ実行される。

```yaml
name: Tests

on:
  pull_request:
    branches: [main]
    # ソースコードとテストが変更された場合にのみ実行
    paths:
      - "src/**"
      - "tests/**"

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      # テストを実行する
...
```

### Pull Request

- `src/`と`tests/`が**変更されていない**場合。

### 結果

- ステータスチェック`unit-tests`が**トリガーされない**。
- 必須ステータスチェック`unit-tests`が成功していないため、pull requestをマージできない。
- pull requestがデッドロック状態になる。

## 解決策

### スキップワークフローを作成する

`paths-ignore`オプションを使い、スキップワークフロー`.github/workflows/tests-skip.yml`を作成する。

```yaml
name: Tests (skip)

on:
  pull_request:
    branches: [main]
    # ソースコードとテスト”以外”が変更された場合に実行する
    paths-ignore:
      - "src/**"
      - "tests/**"

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      # メッセージ出力のみ（テストは実行しない）
      - run: echo "No source changes — skipping tests"
```

### スキップワークフローを使った結果

- `src/`と`tests/`が**変更されていない**場合、スキップワークフローがトリガーされ、ステータスチェック`unit-tests`が成功する。
- pull requestがマージ可能となる。
- デッドロックが発生しない。
