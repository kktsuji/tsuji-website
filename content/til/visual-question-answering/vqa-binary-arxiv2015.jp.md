---
title: "Yin and Yang: Balancing and Answering Binary Visual Questions"
description: ""
date: 2024-09-07T15:15:00+09:00
lastmod:
draft: false
---

Title: Yin and Yang: Balancing and Answering Binary Visual Questions

Authors: Peng Zhang, Yash Goyal, Douglas Summers-Stay, Dhruv Batra, Devi Parikh

Published: Nov 16 2015

Link: [https://arxiv.org/abs/1511.05099](https://arxiv.org/abs/1511.05099)

Summary（Microsoft Copilot生成）：

**Introduction:**

- 本論文は抽象シーンにおける二値Visual Question Answering（VQA）に取り組み、質問で問われる概念の視覚的検証に焦点を当てている。

**Challenges:**

- 言語事前分布は真の視覚的理解なしに表面的なパフォーマンスにつながる可能性がある。
- データセットバイアスはマルチモーダルAIの進歩を妨げる可能性がある。

**Methods:**

- 質問を視覚的概念を要約するタプルに変換する。
- 抽象シーンを使用してデータセットをバランスさせ、各質問に対して「yes」と「no」の回答が等しくなるようにする。

**Novelties:**

- 補完的なシーンによるバランスの取れたデータセット作成。
- 簡潔な視覚的概念表現のためのタプル抽出。

**Results:**

- 言語のみのモデルはバランスの取れたデータセットで貧弱なパフォーマンスを示す。
- 提案されたアプローチは不均衡なデータセットで最先端のパフォーマンスに匹敵し、バランスの取れたデータセットで優れたパフォーマンスを示す。

**Performances:**

- 視覚的推論と理解の大幅な改善。
- 関連する画像領域に注意を向けることでより良いパフォーマンス。

**Limitations:**

- 限られたクリップアートライブラリのため、一部のシーンは変更できない。
- 否定的な質問の処理は依然として困難である。

**Discussion:**

- データセットのバランスを取ることで視覚的理解を改善できる。
- 将来の研究は詳細な視覚的意味論と実際の画像に焦点を当てるべきである。
