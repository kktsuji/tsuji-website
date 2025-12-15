---
title: "Spec Kitの標準ドキュメントで各Featureの仕様のコンフリクトを軽減"
description: ""
date: 2025-12-15T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Spec Kitのための標準ドキュメント

[Spec Kit](https://github.com/github/spec-kit)は、AIを活用した仕様駆動開発のための便利なツールです。

しかし、複数のメンバーがSpec Kitを使用して並行開発を行うと、機能間の詳細な仕様が競合する可能性があります。これに対処するには、プロジェクトの標準ドキュメントを準備することが有効な解決策の1つです。

1. 標準ドキュメントを準備する
2. 標準ドキュメントを明確に示すプロンプトでSpec Kitを使用する

## 標準ドキュメントの準備

プロジェクトメンバーが従うべきルールとガイドラインを定義することが重要です。標準ドキュメントの例には以下が含まれます:

```text
docs/
├── README.md   # 標準ドキュメントのエントリーポイント
├── architecture.md
├── coding-standards.md
├── api-specifications.md
├── data-models.md
├── database-schema.md
├── testing-guidelines.md
└── etc.
```

注意:

- 最初から完璧なドキュメントを準備する必要はありません。プロジェクトの進行に伴って反復的に改善できます。
- `README.md`を提供することを推奨します。これは、プロジェクトの概要を提供し、他の標準ドキュメントへのリンクを記載するためです。

## 標準ドキュメントを使用したSpec Kitの利用

Spec Kitを使用する際は、プロンプトに標準ドキュメントへの参照を含めるようにしてください。例えば:

```text
/speckit.specify
ユーザーは、ユーザー名、メール、パスワードを提供することでアカウントを作成できます。

**必須**: `docs/README.md`で提供されている標準ドキュメントに従ってください。
```
