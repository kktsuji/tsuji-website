---
title: 'A2MIM: 画像の構造に依存しないマスク画像モデリング, ICML2023'
description: 'A2MIM を提案する ICML2023 の論文のサマリ。'
date: 2024-07-01T21:00:00+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Li et al., Architecture-Agnostic Masked Image Modeling - From ViT back to CNN ([icml2023 open access](https://icml.cc/virtual/2023/poster/24861) or [arxiv](https://arxiv.org/abs/2205.13943)).

![img](https://img.tsuji.tech/a2mim-icml2023-0.jpg)

(本ポストの図と表は論文からの引用である)

## 論文の新規性

* 著者らは、画像内の中域のパッチ間の相互作用の利点を増大させるため、"画像の構造に依存しないマスク画像モデリング（意訳）" (A2MIM, Architecture-Agnostic Masked Image Modeling) と呼ばれる新しいアプローチを提案した。
* 彼らは、既存の MIM フレームワークにおける学習可能なマスクトークンの代わりに、マスクされたパッチの RGB値の平均値を用いた。
* A2MIM では、中域の相互作用を学習するために、Focal Frequency Loss にヒントを得たフーリエドメイン損失 (Fourier domain Loss) を導入した。
* A2MIM は CNN や Transformer の改良に応用できる。

## 性能評価手法

* 分類のためのファインチューニング、物体検出とセグメンテーションのための転移学習の、3つの観点から A2MIM の能力を評価した。
* 彼らは、A2MIM が事前に学習されたネットワークの表現性能を向上させることができることを示した。

![img](https://img.tsuji.tech/a2mim-icml2023-1.jpg)

## 議論

* A2MIM を適用する上で、CNN が得られる利点はトランスフォーマーほどではなかった。著者らは、CNN の帰納的バイアスに (inductive bias) より、中域の相互作用の制限されていると推測した。
* トランスフォーマーは、A2MIM を用いた事前学習において、エポックが長いほどより良い改善効果を示した。

## 学んだこと

* ViT と CNN はそれぞれローパスとハイパスのフィルタリング特性を持ち、特定の周波数帯域を持つため、中域の相互作用をうまくモデル化することが難しい。