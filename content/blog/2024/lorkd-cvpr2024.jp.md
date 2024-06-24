---
title: 'LoRKD: 医療基盤モデルの知識分解, CVPR2024'
description: 'LoRKD を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-23T12:10:31+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Cheng et al., Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Low-Rank_Knowledge_Decomposition_for_Medical_Foundation_Models_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2403.18271)).

![img](https://img.tsuji.tech/h-sam-cvpr2024-0.jpg)

(本ポストの図と表は論文からの引用である)

## 論文の新規性

* 医療基盤モデルを複数の "軽量エキスパート" (lightweight experts) に分解し、計算コストの削減と専門性の向上を図る "知識分解" (KD: kowledge decomposition) と呼ばれる新しい手法を提案した。
* 知識分解を実現するために、低ランク適応 (LoRA: low-rank adaptation) 技術に着想を得た、低ランク知識分解 (LoRKD: low-rank knowledge decomposition) フレームワークを提案した。
* 効率的知識分離畳み込み (EKS Conv.: efficient knowledge separation convolution) は、LoRKD における重要な手法の一つであり、入力がどのタスクに属するかを表すワンホットベクタを畳み込みに加えることで計算量を削減する。
* タスク知識伝達損失 (task knowledge transfer loss) は、LoRKD のもう一つの重要な要素であり、基盤モデルの知識を各軽量エキスパートモデルに伝達する。
* 軽量エキスパートの知識は、パラメータの加算や減算により展開できる。

## 性能評価手法

* 彼らは3つのデータセットを使用した： Redimagenet、MedMist、Med-MT。
* ResNet50 は事前学習済みモデル、ShuffleNetV2 は軽量エキスパートモデルに使用される。
* LoRKD は、ベースライン、シングルタスク学習 (STL)、マルチタスク学習 (MTL)、STL-KD、MTL-KD、MoC-MTL、Aligned-MTL、KF などの手法と比較された。

![img](https://img.tsuji.tech/h-sam-cvpr2024-1.jpg)

## 議論

* LoRKD の軽量エキスパートモデルは、より少ないパラメータ数でも、ほとんどのダウンストリームタスクで他のモデルより優れているか、同等であった。 
