---
title: "自動生成されたClaude Code Reviewワークフローのバグ - レビューコメントが投稿されない"
description: ""
date: 2026-03-08T11:00:00+09:00
lastmod:
math: true
draft: false
---

## 問題

- GitHubのPRレビュー用に自動生成された`.github/workflows/claude-code-review.yml`にバグがある
  - 注：`Claude Code CLI`の`/install-github-app`コマンドで生成されたもの
- このワークフローは`pull_request`イベントをトリガーとして、`code-review`プラグインを実行してPRを分析し、GitHubにレビューコメントを投稿するはずである
- しかし、ワークフローが正常に完了（緑のチェックマーク）しても、PRにコメントが投稿されない

## 解決策

自動生成されたワークフローの代わりに、[anthropic/claude-code-action](https://github.com/anthropics/claude-code-action?tab=readme-ov-file)の[公式サンプル](https://github.com/anthropics/claude-code-action/blob/main/docs/solutions.md)を使用します。

## 根本原因

Claude Code CLIが自動生成する`.github/workflows/claude-code-review.yml`は単なるテンプレートであり、そのままでは完全に機能しません。特にPRにレビューコメントを投稿するためには、手動での調整が必要です。

## ワークフローの例

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize, ready_for_review, reopened]

jobs:
  review:
    # フォークされたPRをスキップ: フォークのワークフローではリポジトリのシークレットが利用できない
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: anthropics/claude-code-action@26ec041249acb0a944c0a47b6c0c13f05dbc5b44 # v1.0.70
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          track_progress: true # トラッキングコメントを有効化
          prompt: |
            REPO: ${{ github.repository }}
            PR NUMBER: ${{ github.event.pull_request.number }}

            このプルリクエストを以下の観点でレビューしてください：
            - コード品質とベストプラクティス
            - 潜在的なバグや問題点
            - セキュリティへの影響
            - パフォーマンスの考慮点

            特定の問題についてはインラインコメントを使って詳細なフィードバックを提供してください。

          claude_args: |
            --allowedTools "mcp__github_inline_comment__create_inline_comment,Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*)"
```

## 結果

ワークフロー実行中のトラッキングコメント：

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-0.jpg)

ワークフロー完了後にGitHub PRに投稿されたレビューコメント：

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-1.jpg)

## claude.ymlは手動での調整が不要

実際には、Claude Code CLIの`/install-github-app`コマンドは2つのファイルを生成します

- `.github/workflows/claude-code-review.yml`：PRレビュー用（バグあり）
- `.github/workflows/claude.yml`：コメント内で`@claude`がメンションされた場合の一般的な自動化（調整なしで正常に動作する）

1つ目にはバグがあり手動での調整が必要ですが、2つ目は以下の画像のように調整なしで正常に動作します：

![img](https://img.tsuji.tech/auto-generated-claude-code-review-workflow-bug-2.jpg)
