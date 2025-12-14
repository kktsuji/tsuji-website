---
title: "A2MIM: Architecture-Agnostic Masked Image Modeling, ICML2023"
description: "ICML2023におけるA2MIM論文の要約"
date: 2024-07-01T21:00:00+09:00
lastmod:
draft: false
---

## 概要

Paper: Li et al., Architecture-Agnostic Masked Image Modeling - From ViT back to CNN（[icml2023 open access](https://icml.cc/virtual/2023/poster/24861)または[arxiv](https://arxiv.org/abs/2205.13943)）

![img](https://img.tsuji.tech/a2mim-icml2023-0.jpg)

（この投稿の図と表は原論文からのものです）

## 論文の新規性

- パッチ間の中次相互作用の利点を強化するために「Architecture-Agnostic Masked Image Modeling」（A2MIM）と呼ばれる新しいアプローチを提案しました。
- 既存のMIMフレームワークにおける学習可能なマスクトークンの代わりに、マスクされたパッチの平均RGB値を利用しました。
- Focal Frequency lossに触発されたフーリエ領域損失をA2MIMに導入し、中次相互作用を扱いました。
- A2MIMはCNNsとTransformersの両方の改善に適用できます。

## パフォーマンス評価方法

- 分類のためのファインチューニング、物体検出とセグメンテーションのための転移学習という3つの観点でA2MIMの能力を評価しました。
- A2MIMが事前学習されたネットワークの表現パフォーマンスを向上させることができることを示しました。

![img](https://img.tsuji.tech/a2mim-icml2023-1.jpg)

## 考察

- A2MIMを適用する際のCNNsの利点はTransformersよりも少なかったです。著者らは、中次相互作用学習がCNNsの帰納的バイアスによって制限されていると推測しました。
- TransformersはA2MIMを用いたより長い事前学習でより高い効果を示しました。

## 学んだこと

- ViTとCNNはそれぞれローパスフィルタリングとハイパスフィルタリングの特性を持ち、特定の周波数帯域を持っているため、中次相互作用をうまくモデル化することが困難です。
