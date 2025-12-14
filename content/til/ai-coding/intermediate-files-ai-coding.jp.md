---
title: "中間ファイルを使ってAIコーディングのパフォーマンスを向上させる"
description: ""
date: 2025-12-13T8:00:00+09:00
lastmod:
math: true
draft: false
---

## 中間ファイルを使ってAIコーディングのパフォーマンスを向上させる

難しい指示を与えると、GitHub CopilotのようなAIエージェントはタスクを効果的に完了できないことがあります。重要なコンテキストを忘れたり、ミスをしたりすることがあります。これを改善するために、`中間ファイル`を使用して複雑なタスクを小さく管理しやすい部分に分割できます。

例えば、このプロンプトは**複雑すぎます**:

```text
このプロジェクトの仕様を変更したいです。

変更前: XXX
変更後: YYY

これらの変更を反映するために、関連するすべてのソースコードファイルを更新してください。
```

代わりに、タスクをいくつかのステップに分割し、各ステップで中間ファイルを作成できます。

重要なポイント:

1. タスクを分割する
2. 各ステップで中間ファイルを作成する
3. 前のステップで作成した中間ファイルを使用して、ステップバイステップで実行する

メリット:

- 小さいタスクはAIが処理しやすい
- 中間ファイルはコンテキストと指示を保持する
- TODOリストは何をすべきかを明確にする
- 次に進む前に各ステップをレビューして検証できる

## 1. ステップに分割する

まず、複雑なタスクを小さなステップに分割します。

例:

1. コードのどの部分を変更する必要があるか調査する
2. 実行可能な変更のTODOリストを作成する
3. TODOリストに基づいて変更を実装する
4. 変更を確認してテストする

## 2. 各ステップで中間ファイルを作成する

各ステップで、そのステップに必要な情報や指示を含む中間ファイルを作成します。

例:

### ステップ1: 変更を調査する

```text
I want to change the specifications in this project.

Before: XXX
After: YYY

Please analyze the `src/aaa/*.py` files and summarize which parts of the code need to be changed to reflect these new specifications.
And save the summary in `docs/change_summary.md`.
```

### ステップ2: TODOリストを作成する

```text
Based on the analysis in `docs/change_summary.md`, please create an executable TODO list of changes that need to be made to the source code files.
Save the TODO list in `docs/change_todo.md`.
```

注: 新しいTODOファイルを作成する代わりに、既存のサマリーファイルに新しいセクションとしてTODOリストを追加するのも良い方法です。

### ステップ3: 変更を実装する

```text
Please implement the changes following the todo list in `docs/change_todo.md`.
After completing the changes, please mark each item in the todo list as done.
```

### ステップ4: 変更を確認してテストする

```text
`docs/change_todo.md` is the todo list with completed changes marked.
Please confirm that all changes have been made correctly.
Also, run tests to ensure everything works as expected.
```

注: 手動で行うのではなく、レビューとテストにAIエージェントを使用する方が良いです。

### ステップ5：手動レビュー

最後に、変更とテスト結果を手動でレビューして、すべてが正しいことを確認します。
