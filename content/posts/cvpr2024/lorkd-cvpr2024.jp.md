---
title: "医療基盤モデルのための低ランク知識分解"
description: ""
date: 2024-06-23T12:10:31+09:00
lastmod:
draft: false
---

## 概要

論文：Zhou et al., Low-Rank Knowledge Decomposition for Medical Foundation Models（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Low-Rank_Knowledge_Decomposition_for_Medical_Foundation_Models_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2309.15266)）。

![img](https://img.tsuji.tech/lorkd-cvpr2024-0.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- 計算コストを削減し専門性を向上させるために、医療基盤モデルを複数の「軽量エキスパート」に分解する「知識分解」（KD）と呼ばれる新しいパラダイムを提案した。
- 知識分解を達成するために、低ランク適応（LoRA）技術に触発された低ランク知識分解（LoRKD）フレームワークも提案した。
- 効率的知識分離畳み込み（EKS Conv.）はLoRKDの重要な手法の1つであり、入力がどのタスクに属するかを表すone-hotベクトルを畳み込みに追加することで計算複雑度を削減する。
- タスク知識転移損失は、基盤モデルの知識を各軽量エキスパートモデルに転移させるLoRKDのもう1つの重要な構成要素である。
- 知識エキスパートのデプロイメントはパラメータの加算と減算によって実行できる。

## 性能評価手法

- 3つのデータセットを使用した：Redimagenet、MedMist、Med-MT。
- 事前学習モデルと軽量エキスパートモデルにそれぞれResNet50とShuffleNetV2を適用した。
- LoRKDをbaseline、single-task learning（STL）、multi-task learning（MTL）、STL-KD、MTL-KD、MoC-MTL、Aligned-MTL、KFを含むいくつかの手法と比較した。

![img](https://img.tsuji.tech/lorkd-cvpr2024-1.jpg)

## 考察

- LoRKDの軽量エキスパートモデルは、パラメータ数が少ないにもかかわらず、ほとんどの下流タスクで他の手法よりも優れているか同等の性能を示した。
