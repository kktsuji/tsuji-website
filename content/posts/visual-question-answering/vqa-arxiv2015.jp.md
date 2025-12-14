---
title: "VQA: Visual Question Answering"
description: ""
date: 2024-09-09T09:15:00+09:00
lastmod:
draft: false
---

Title: VQA: Visual Question Answering

Authors: Aishwarya Agrawal, Jiasen Lu, Stanislaw Antol, Margaret Mitchell, C. Lawrence Zitnick, Dhruv Batra, Devi Parikh

Published: May 3 2015

Link: [https://arxiv.org/abs/1505.00468](https://arxiv.org/abs/1505.00468)

Summary（Microsoft Copilot生成）：

**Introduction:**

- 本論文は画像に関する自然言語の質問に答える**Visual Question Answering（VQA）**のタスクを紹介している。

**Challenges:**

- VQAは単純な画像キャプション生成を超えた**詳細な画像理解**と**複雑な推論**を必要とする。

**Methods:**

- 著者らは約0.25M枚の画像、約0.76M個の質問、約10M個の回答を含む**大規模データセット**を提供している。
- 彼らはVQAのための様々な**ベースラインと手法**を比較している。

**Novelties:**

- このタスクは**オープンエンドで自由形式の質問**と回答を含み、必要な知識と推論の多様性を増加させている。

**Results:**

- データセットにはMS COCOからの**204,721枚の画像**と**50,000枚の抽象シーン**が含まれている。
- 各画像またはシーンに対して**3つの質問**が収集され、**10人の被験者**によって回答された。

**Performances:**

- 本論文はVQAにおける**人間のパフォーマンス**と**自動評価**メトリクスについて議論している。

**Limitations:**

- いくつかの質問は画像なしで**常識的知識**を使用して回答できる。

**Discussion:**

- VQAは**AI完全**問題の解決への一歩と見なされ、**コンピュータビジョン**と**自然言語処理**の境界を押し広げている。
