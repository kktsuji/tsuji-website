---
title: "Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering"
description: ""
date: 2024-09-06T22:30:00+09:00
lastmod:
draft: false
---

Title: Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering

Authors: Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, Devi Parikh

Published: Dec 2 2016

Link: [https://arxiv.org/abs/1612.00837](https://arxiv.org/abs/1612.00837)

Summary（Microsoft Copilot生成）：

**Introduction:**

- 本論文はVisual Question Answering（VQA）における言語バイアスの問題に取り組み、画像理解の役割を高めることを目指している。

**Challenges:**

- 既存のVQAモデルは言語事前分布を利用することが多く、真の視覚的理解なしにパフォーマンスが水増しされている。

**Methods:**

- 著者らは補完的な画像を収集することでバランスの取れたVQAデータセットを作成し、各質問が異なる回答を持つ2つの画像を持つことを保証している。

**Novelties:**

- 言語バイアスを低減するバランスの取れたデータセットの導入と、反例ベースの説明を提供する新しい解釈可能なモデル。

**Results:**

- 最先端のVQAモデルはバランスの取れたデータセットで著しく悪いパフォーマンスを示し、言語事前分布への依存を確認している。

**Performances:**

- バランスの取れたデータセットで訓練されたモデルは改善されたパフォーマンスを示し、より大規模でバランスの取れたデータセットの必要性を示している。

**Limitations:**

- データセットは完全にはバランスが取れておらず、一部の質問には適切な補完画像がない可能性がある。

**Discussion:**

- バランスの取れたデータセットと反例説明はVQAモデルへの信頼構築に役立ち、より良い視覚的理解に向けて分野を押し進めることができる。
