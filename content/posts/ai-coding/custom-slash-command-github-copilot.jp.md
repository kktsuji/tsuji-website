---
title: "GitHub CopilotのカスタムSlashコマンド"
description: ""
date: 2025-12-14T10:00:00+09:00
lastmod:
math: true
draft: false
---

## GitHub CopilotのカスタムSlashコマンド

GitHub Copilot用のカスタムslashコマンドを作成できます。

[spec-kit](https://github.com/github/spec-kit)がどのようにカスタムslashコマンドを実装しているか、workspaceの構造と設定ファイルを調べて分析しました。

## GitHub CopilotのカスタムSlashコマンドの作成方法

spec-kitの実装に基づいて、カスタムslashコマンドの仕組みを説明します:

### **コアアーキテクチャ**

カスタムslashコマンドは**2種類のファイル**で構成されます:

1. **Promptファイル**(`.github/prompts/*.prompt.md`) - シンプルなトリガー
2. **Agentファイル**(`.github/agents/*.agent.md`) - 完全な実装ロジック

### **ファイル構造**

```text
.github/
├── prompts/
│   └── speckit.specify.prompt.md    # agentへのシンプルなポインター
└── agents/
    └── speckit.specify.agent.md     # 完全なコマンドロジック
```

### **1. Promptファイル(.prompt.md)**

これらはagentを参照する最小限のトリガーファイルです:

```markdown
---
agent: speckit.specify
---
```

これだけです!promptファイルは単にCopilotにどのagentを呼び出すかを伝えるだけです。

### **2. Agentファイル(.agent.md)**

これらはfrontmatterと指示を含む実際のコマンド実装を含みます:

````markdown
---
description: このコマンドが何をするかの簡単な説明
handoffs:
  - label: Next Command Label
    agent: speckit.nextcommand
    prompt: Suggested user prompt
    send: true # オプション: auto-send
---

## User Input

```text
$ARGUMENTS
```
````

## Outline

[コマンドの詳細な指示...]

## [必要に応じて追加のセクション]

````

**主要な要素:**
- **description**: コマンドが何をするか
- **handoffs**: 次に提案する関連コマンド
- **$ARGUMENTS**: slashコマンドの後のテキストをキャプチャ
- **Instructions**: Copilotが従うべき詳細なワークフロー

### **3. VS Code設定の登録**

[.vscode/settings.json](.vscode/settings.json)でコマンドを有効にします:

```json
{
    "chat.promptFilesRecommendations": {
        "speckit.specify": true,
        "speckit.plan": true,
        "yourname.mycommand": true
    }
}
````

### **命名規則**

- **ファイル名**: `namespace.commandname.{agent|prompt}.md`
- **例**: speckit.specify.agent.mdは`/speckit.specify`コマンドを作成
- namespace(例:`speckit`)は関連するコマンドをグループ化

### **独自のコマンドの作成 - 例**

**1. 作成** .github/prompts/mykit.review.prompt.md:

```markdown
---
agent: mykit.review
---
```

**2. 作成** .github/agents/mykit.review.agent.md:

````markdown
---
description: コード品質とベストプラクティスをレビュー
handoffs:
  - label: Fix Issues
    agent: mykit.fix
    prompt: Fix the identified issues
---

## User Input

```text
$ARGUMENTS
```
````

## Outline

1. 現在のファイルまたは選択されたコードを分析
2. チェック項目:
   - コード品質の問題
   - ベストプラクティス違反
   - セキュリティ上の懸念
3. 詳細なレポートを生成
4. 改善を提案

````

**3. 追加** [.vscode/settings.json](.vscode/settings.json):
```json
{
    "chat.promptFilesRecommendations": {
        "mykit.review": true
    }
}
````

### **高度な機能**

- **Scripts**: コマンドは`.specify/scripts/`内のbash/PowerShellスクリプトを呼び出せる
- **Templates**: `.specify/templates/`に再利用可能なコンテンツを保存
- **Auto-approval**: 設定で信頼されたスクリプトの自動実行を構成
- **Handoffs**: 提案されたフォローアップでコマンドを連鎖

このシステムは非常に柔軟です - 基本的な指示を持つシンプルなコマンドから、複数フェーズ、スクリプト実行、ファイル生成を伴う複雑なワークフローまで作成できます!

## .vscode.settings.json

必須ではありませんが、より良いユーザー体験のために**強く推奨**されます。

### コマンドの動作方法:

**settings.jsonなし:**

- 手動で入力すればコマンドは動作します(例:`/speckit.specify`)
- Copilotは`.github/prompts/*.prompt.md`ファイルからそれらを見つける
- `/`を入力してもオートコンプリートの提案はなし

**`chat.promptFilesRecommendations`あり:**

- ✅コマンドがオートコンプリートのドロップダウンに表示される
- ✅ユーザーが利用可能なコマンドを簡単に発見できる
- ✅コマンドの説明を表示
- ✅より良いIDE統合

### ベストプラクティス:

```json
{
  "chat.promptFilesRecommendations": {
    "mykit.review": true,
    "mykit.fix": true,
    "mykit.test": true
  }
}
```

**settings.jsonを使用する場合:**

- ユーザーに簡単に発見してほしいコマンド
- チーム/プロジェクト固有のワークフロー
- 頻繁に使用されるコマンド

**スキップする場合:**

- 実験的/内部コマンド
- "隠しておきたい"コマンド
- 単一ユーザーの一時的なコマンド

### 代替の場所:

これを以下で定義することもできます:

- **User settings**(settings.json) - 個人用コマンド
- **Workspace settings**(settings.json) - チーム/プロジェクト用コマンド ← **共有プロジェクトに推奨**
