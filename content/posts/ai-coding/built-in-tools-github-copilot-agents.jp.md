---
title: "GitHub Copilotエージェントのビルトインツール"
description: ""
date: 2025-12-23T8:00:00+09:00
lastmod:
math: true
draft: false
---

## GitHub Copilotエージェントのビルトインツール

GitHub Copilot エージェントは、その機能を強化できる[ビルトインツール](https://code.visualstudio.com/docs/copilot/chat/chat-tools)の使用をサポートしています。

## Configure Tools (GUI)

Visual Studio CodeのGitHub Copilot設定で、AIエージェントに対してどのビルトインツールを有効にするかを設定できます。

1. VS Codeでチャットサイドバーを開く
2. 設定したいエージェントを選択する(チャット入力ボックスの左下のドロップダウン)
3. エージェント名の横にあるツールアイコンをクリックする(チャット入力ボックスの下部)
4. "Configure Tools"ダイアログで、選択したエージェントに対して特定のツールを有効または無効にできます。

## Custom Agents Settings

[カスタムエージェント](https://code.visualstudio.com/docs/copilot/customization/custom-agents)を定義する際、エージェント定義ファイル(`.agent.md`)に`tools`セクションを含めることで、エージェントが使用できるビルトインツールを指定できます。

```markdown
---
description: aaa
tools: ["create_directory", "create_file"] # エージェントが使用できるビルトインツールのリスト
handoffs:
  - label: xxx
    agent: yyy
    prompt: zzz
    send: false
---
```

## List Command

チャットで`/list`コマンドを使用して、エージェントで利用可能なツールのリストを確認できます。

プロンプト:

```text
/list
```

レスポンス:

```markdown
Available tools:

- create_directory
- create_file
- create_new_jupyter_notebook
- create_new_workspace
- edit_notebook_file
- fetch_webpage
- file_search
- grep_search
- get_changed_files
- get_errors
- copilot_getNotebookSummary
  ...
```

これらのツールをチャットで直接実行することはできません。代わりに、AIエージェントがチャットでの自然言語リクエストのコンテキストに基づいて、内部的にいつ使用するかを自動的に決定します。

例えば:

- 「設定ファイルを読んで」と指示→AIは`read_file`ツールを使用
- 「login関数の使用箇所を全て見つけて」と指示→AIは`list_code_usages`または`grep_search`を使用
- 「テストを実行して」と指示→AIは`run_in_terminal`を使用

各ツールの説明を知りたい場合は、[公式ドキュメント](https://code.visualstudio.com/docs/copilot/chat/chat-tools)を参照するか、エージェントに尋ねることができます:

プロンプト:

```markdown
使用可能なbuilt-in toolsをリストして説明してください。
```

レスポンス:

```markdown
## File Operations

- create_file - コンテンツを含む新しいファイルを作成
- read_file - 行範囲を指定してファイルの内容を読み取り
- replace_string_in_file - 完全一致する文字列を置換してファイルを編集
- multi_replace_string_in_file - 1回の操作で複数のファイル編集を実行
- list_dir - ディレクトリの内容をリスト
- create_directory - ディレクトリ構造を作成
  ...
```

## Chat Debug View

VS Codeの`Chat Debug View`でそれらの詳細を確認することもできます（[以前の投稿](https://tsuji.tech/jp/chat-debug-view-github-copilot/)を参照）。

- エージェントによって使用されたビルトインツール
- ビルトインツールに渡された入力パラメータ
- ビルトインツールから返された出力結果
- など
