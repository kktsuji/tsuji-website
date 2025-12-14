---
title: "Improving Language Understanding by Generative Pre-Training"
description: ""
date: 2024-09-04T07:00:00+09:00
lastmod:
draft: false
---

Title: Improving Language Understanding by Generative Pre-Training

Authors: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever

Published: Jun 11, 2018

Link: [https://openai.com/index/language-unsupervised/](https://openai.com/index/language-unsupervised/)

Summary（Microsoft Copilotにより生成）：

**導入：**

- この論文は、教師なし事前学習と教師あり微調整の組み合わせを使用した自然言語理解タスクのための半教師あり学習アプローチを探究しています。

**課題：**

- 特定のタスクのラベル付きデータの不足
- ラベルなしデータから言語情報を活用することの困難さ
- 最適化目標と効果的な転移方法の不確実性

**手法：**

- 2段階学習：大規模なテキストコーパスでの教師なし事前学習と、それに続く特定のタスクでの教師あり微調整
- 長期依存関係をより適切に処理するためのTransformerモデルの使用

**新規性：**

- 微調整中のタスク対応入力変換
- 効果的な転移のためのモデルアーキテクチャへの最小限の変更

**結果：**

- 12の自然言語理解タスクのうち9つで大幅な改善
- 常識推論、質問応答、テキスト含意における顕著なパフォーマンス向上

**パフォーマンス：**

- 様々なベンチマークで最先端の結果を達成（Stories Cloze Testで8.9%、RACEで5.7%の改善を含む）

**制限事項：**

- RTEのような小規模データセットでのパフォーマンスは、大規模データセットと比較して低かった。

**考察：**

- このアプローチは、自然言語理解タスクの改善における生成的事前学習と識別的微調整の効果を実証しています。
