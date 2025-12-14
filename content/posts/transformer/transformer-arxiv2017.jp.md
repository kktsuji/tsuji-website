---
title: "Attention Is All You Need"
description: ""
date: 2024-09-08T14:00:00+09:00
lastmod:
draft: false
---

Title: Attention Is All You Need

Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin

Published: Jun 12 2017

Link: [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

Summary（Microsoft Copilotにより生成）：

**導入：**

- この論文は、再帰や畳み込みを必要とせず、注意メカニズムのみに基づく新しいニューラルネットワークアーキテクチャである**Transformer**を紹介しています。

**課題：**

- 従来のシーケンストランスダクションモデルは再帰型または畳み込みニューラルネットワークに依存しており、並列化が困難で学習に時間がかかります。

**手法：**

- Transformerはエンコーダーとデコーダーの両方に**マルチヘッド自己注意**と**ポイントワイズ全結合層**を使用します。

**新規性：**

- このモデルは機械翻訳タスクで優れたパフォーマンスを達成し、大幅に並列化可能であり、学習時間を短縮します。

**結果：**

- WMT 2014英語-ドイツ語タスクで**28.4 BLEU**、英語-フランス語タスクで**41.8 BLEU**を達成しました。

**パフォーマンス：**

- アンサンブルを含む以前の最先端モデルを、学習コストのほんの一部で上回ります。

**制限事項：**

- この論文では具体的な制限事項については議論されておらず、Transformerモデルの利点に焦点を当てています。

**考察：**

- Transformerは英語構文解析などの他のタスクにもよく汎化し、様々な領域での将来の応用に期待が持てます。
