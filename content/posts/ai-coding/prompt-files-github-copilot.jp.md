---
title: "GitHub Copilotのカスタムスラッシュコマンド定義（プロンプトファイル）"
description: ""
date: 2025-12-26T08:00:00+09:00
lastmod:
math: true
draft: false
---

## GitHub Copilotのプロンプトファイル

GitHub Copilotでは、カスタムプロンプトを作成してエクスペリエンスを向上させるための[プロンプトファイル](https://code.visualstudio.com/docs/copilot/customization/prompt-files)を作成できます。

## GitHub Copilotのプロンプトファイルの作成方法

手動:

1. リポジトリの`.github/prompts/`ディレクトリに新しいファイル`namespace.prompt-name.prompt.md`を作成します。
2. frontmatterと指示を使用してファイル内にプロンプトの動作を定義します。

GUI:

1. Visual Studio CodeでGitHub Copilotチャットサイドバーを開きます。
2. チャットサイドバーの上部にある設定歯車アイコンの"Create New Prompt"をクリックします。
3. 提供されたインターフェースを使用して、プロンプトの名前、説明、および動作を定義します。

## プロンプトファイルのVSCode設定

`.vscode/settings.json`を設定して、プロンプトファイルのSUGGESTED ACTIONSを次のように設定できます:

```json
{
  "chat.promptFilesRecommendations": {
    "namespace.prompt-name": true
  }
}
```

`chat.promptFilesRecommendations`の下にリストされたプロンプトファイルは、GitHub Copilotチャットサイドバーに推奨アクションとして表示されます。

## プロンプトファイル定義の例

```markdown
---
description: 英語のテキストをフランス語に翻訳します。
name: namespace.prompt-name
argument-hint: フランス語に翻訳される英語のテキスト。
agent: agent # ここにカスタムエージェントを指定することもできます
model: gpt-5
tools: ["file_search"]
---

# プロンプトの指示

あなたはプロフェッショナルな翻訳者です。以下の英語のテキストを、元の意味とトーンを維持しながらフランス語に翻訳してください。
...
```

GitHub Copilotのためのプロンプトファイルの作成と設定の詳細については、[公式ドキュメント](https://code.visualstudio.com/docs/copilot/customization/prompt-files)を参照してください。

## プロンプトファイルの使用方法

1. Visual Studio CodeでGitHub Copilotチャットサイドバーを開きます。
2. チャット入力ボックスにスラッシュ付きのプロンプト名(例:`/namespace.prompt-name`)を入力します。
3. 必要に応じて必要な引数を提供し、プロンプトと対話します。

## プロンプトファイルvs.カスタムエージェント

| Feature     | [プロンプトファイル](https://code.visualstudio.com/docs/copilot/customization/prompt-files) | [カスタムエージェント](https://code.visualstudio.com/docs/copilot/customization/custom-agents) |
| ----------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Purpose     | エージェントを呼び出すシンプルなトリガー                                                    | 複雑なタスクのための完全な実装ロジック                                                         |
| File Type   | `.prompt.md`ファイル                                                                        | `.agent.md`ファイル                                                                            |
| Complexity  | 最小限のfrontmatter、エージェントを指すだけ                                                 | ツール、ハンドオフ、指示を含む詳細なfrontmatter                                                |
| Use Cases   | クイックコマンド、シンプルなタスク                                                          | 包括的なワークフロー、マルチステッププロセス                                                   |
| Persistence | 呼び出しごとに1つの応答のみ                                                                 | セッション内の複数のインタラクションにわたってコンテキストを維持できる                         |

ファイル構造:

```text
.github/
├── agents/
│   └── namespace.agent-name.agent.md     # カスタムエージェント
└── prompts/
    └── namespace.prompt-name.prompt.md    # プロンプトファイル
```
