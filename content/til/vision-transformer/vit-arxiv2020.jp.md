---
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
description: ""
date: 2024-09-05T09:30:00+09:00
lastmod:
draft: false
---

Title: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

Authors: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby

Published: Oct 22 2020

Link: [https://arxiv.org/abs/2010.11929](https://arxiv.org/abs/2010.11929)

学んだこと：

- Transformerアーキテクチャは、CNNsが持つ帰納的バイアスの一部を欠いています。
- 大規模なTransformerベースのモデルは、多くの場合2段階の戦略を持ちます：1) 事前学習、2) ファインチューニング
  - BERT：ノイズ除去自己教師あり事前学習タスク
  - GPT：事前学習タスクとしての言語モデリング
- 帰納的バイアスの違い
  - CNNs：局所情報、2D近傍構造情報、平行移動同変性がモデル全体の各層に学習されます。
  - ViT:
    - MLP層：局所性と平行移動同変性
    - 自己注意層：グローバル
    - パッチの作成と位置埋め込みのファインチューニング：2D近傍構造

Summary（Microsoft Copilotにより生成）：

**導入：**

- この論文は、画像をパッチのシーケンスとして処理する**Vision Transformer（ViT）**を提案し、画像認識への**Transformers**の適用を探究しています。

**課題：**

- **Transformers**は、平行移動同変性や局所性などの**CNNs**に固有の**帰納的バイアス**を欠いているため、小規模なデータセットでは効果が低くなります。

**手法：**

- 画像はパッチに分割され、線形埋め込みされて**Transformer**に入力されます。モデルは大規模データセットで事前学習され、小規模なベンチマークでファインチューニングされます。

**新規性：**

- このアプローチは**CNNs**の必要性を排除し、画像分類に純粋な**Transformer**アーキテクチャを使用します。

**結果：**

- **ViT**は、大規模データセットで事前学習された場合、**ImageNet**や**CIFAR-100**などのベンチマークで優れた結果を達成します。

**パフォーマンス：**

- **ViT**は、大規模データセットで事前学習された場合、より少ない計算リソースで最先端の**CNNs**を上回ります。

**制限事項：**

- **ViT**は**帰納的バイアス**の欠如により、小規模なデータセットではパフォーマンスが低下します。

**考察：**

- この論文は、**大規模事前学習**が**Transformers**における帰納的バイアスの欠如を補い、**CNNs**と競争力を持たせることができることを示唆しています。今後の研究には、他のビジョンタスクへの**ViT**の適用や自己教師あり事前学習方法の探索が含まれます。
