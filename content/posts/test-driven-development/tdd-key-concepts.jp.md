---
title: "Test-Driven Development主要概念"
description: ""
date: 2024-08-27T20:00:00+09:00
lastmod:
draft: false
---

Test-Driven Development（TDD）のシンプルかつ強力な主要概念は以下の通りです：

- 自動テストが失敗した場合のみ新しいコードを書く
- 重複を削除する

これらの概念は以下の手順につながります：

1. Red：常に失敗する小さなテストコードを書く
2. Green：テストを成功させるための新しいコードを書く（このプロセスではどんな汚いコードでも許容される）
3. Refactor：すべての重複を削除し、コード品質を向上させる

Red、green、refactorもTest-Driven Developmentの中核原則です。

> "Clean code that works, in Ron Jeffries' pithy phrase, is the goal of Test-Driven Development (TDD). Clean code that works is a worthwhile goal for a whole bunch of reasons."<br>
> Kent Beck, <cite>Test-Driven Development by Example</cite>.
