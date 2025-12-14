---
title: "継続的自己教師あり学習：普遍的なマルチモーダル医療データ表現学習を目指して"
description: ""
date: 2024-06-20T08:51:23+09:00
lastmod:
draft: false
---

## 概要

論文：Ye et al., Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2311.17597)）

![img](https://img.tsuji.tech/medcoss-cvpr2024-0.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- モダリティの衝突と破滅的忘却を防ぐためにMedical Continual Self-Supervised（MedCoSS）パラダイムを提案した。
- MedCoSSは継続学習において各モダリティデータを個別の訓練段階に割り当てる。
- 以前のモダリティデータを保持するためにリハーサルバッファーが導入された。
- モダリティ：レポート、X線、CT、MRI、病理画像。

## 性能評価手法

- MedCoSSを単一モダリティ事前学習およびマルチモーダル事前学習（Joint SSL、EWC、ER、PackNet、CaSSLeを含む）と比較した（表を参照）。

![img](https://img.tsuji.tech/medcoss-cvpr2024-1.jpg)

## 議論

- MedCoSSは一部のモーダルで最高性能を示すが、他のモーダルではそうではない
- リハーサルバッファのサイズは性能とマルチモーダルデータの衝突および計算コストとのトレードオフである
