---
title: "GitHub Copilotのカスタムエージェント"
description: ""
date: 2025-12-25T10:00:00+09:00
lastmod:
math: true
draft: false
---

## GitHub Copilotのカスタムエージェント

GitHub Copilotでは、要件に基づいて特定のタスクを実行できる[カスタムエージェント](https://code.visualstudio.com/docs/copilot/customization/custom-agents)を作成できます。

## GitHub Copilotのカスタムエージェントの作成方法

手動:

1. リポジトリの`.github/agents/`ディレクトリに`namespace.angent-name.agent.md`という新しいファイルを作成します。
2. ファイル内でfrontmatterと指示を使用してagentの動作を定義します。

GUI:

1. Visual Studio CodeでGitHub Copilotのチャットサイドバーを開きます。
2. agent選択ドロップダウン(チャット入力ボックスの左下)の"Create New Agent"ボタンをクリックします。
3. 提供されたインターフェースを使用して、agentの名前、説明、および動作を定義します。

## Custom Agent定義の例

```markdown
---
description: このagentはコードレビューを支援し、提案と改善を提供します。
tools: ["file_search", "fetch_webpage"] # agentが使用できる組み込みツールのリスト
handoffs:
model: Claude Sonnet 4.5
- label: 改善を提案
  agent: agent
  prompt: "次のコードの改善を提案してください:"
---

# agentへの指示

あなたはプロフェッショナルなコードレビュアーです。提供されたコードを分析し、改善、最適化、およびベストプラクティスを提案してください。

...
```

GitHub Copilotのカスタムエージェントの作成と設定の詳細については、[公式ドキュメント](https://code.visualstudio.com/docs/copilot/customization/custom-agents)を参照してください。

## カスタムエージェントの使用方法

1. Visual Studio CodeでGitHub Copilotのチャットサイドバーを開きます。
2. agent選択ドロップダウン(チャット入力ボックスの左下)からcustom agentを選択します。
3. チャット入力ボックスにプロンプトやコマンドを入力して、agentと対話します。

## プロンプトファイルvs.カスタムエージェント

| 機能           | [プロンプトファイル](https://code.visualstudio.com/docs/copilot/customization/prompt-files) | [カスタムエージェント](https://code.visualstudio.com/docs/copilot/customization/custom-agents) |
| -------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 目的           | agentを呼び出すシンプルなトリガー                                                           | 複雑なタスクのための完全な実装ロジック                                                         |
| ファイルタイプ | `.prompt.md`ファイル                                                                        | `.agent.md`ファイル                                                                            |
| 複雑さ         | 最小限のfrontmatter、agentを指すだけ                                                        | tools、handoffs、指示を含む詳細なfrontmatter                                                   |
| ユースケース   | クイックコマンド、シンプルなタスク                                                          | 包括的なワークフロー、マルチステッププロセス                                                   |
| 永続性         | 呼び出しごとに1つの応答のみ                                                                 | セッション内の複数のやり取りでコンテキストを維持可能                                           |

ファイル構造:

```text
.github/
├── agents/
│   └── namespace.agent-name.agent.md     # カスタムエージェント
└── prompts/
    └── namespace.prompt-name.prompt.md   # プロンプトファイル
.vscode/
└── settings.json                         # プロンプトファイルのVSCode設定 (任意)
```
