---
title: 'ABD: 適応的双方向 Displacement, CVPR2024'
description: 'ABD を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-24T08:21:00+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Chi et al., Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Chi_Adaptive_Bidirectional_Displacement_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2405.00378)).

![img](https://img.tsuji.tech/abd-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## 論文の新規性

* Consistency learning (一貫性学習) が複数の perturbation (摂動) を利用する場合、学習過程が制御不能になりやすいという問題がある。
* 彼らは、半教師あり医用画像セグメンテーションにおける consistency learning の問題点を解決するために、"Adaptive Bidirectional Displacement" (ABD) 手法を提案した。
* ABD を導入することで、複数の perturbation を用いることが可能となった。
* ABD は2つの摂動を持っており、画像の摂動として画像の argumentation が用いられ、その結果、弱い摂動と強い摂動の画像が生成される。 また、ネットワーク摂動として2つのネットワークが利用される。
* ABD フレームワークは ABD-R と ABD-I の2種類の displacement 手法から構成される。
* ABD-R は信頼度の高い (reliable confidence) 情報を用いる。具体的には、片方の augmentation 結果の画像の中で信頼度が最も低いパッチを、もう片方の augmentation 結果画像のうち信頼度が最も高いパッチと置換する方法である。
* ABD-I は逆信頼度 (inverse confidence) の情報を用いる。augmentation 画像内の最も信頼度の高い領域を、もう一方の augmentation 画像内の最も信頼度の低いパッチで置き換える手法である。
* 置き換えられた画像は新しいサンプルとして扱われる。
* ABC は既存のモデルに追加することが可能である。

Translated with DeepL (https://www.deepl.com/app/?utm_source=ios&utm_medium=app&utm_campaign=share-translation)

## 性能評価手法

* 2つのデータセットを使用：ACDC と PROMISE12。
* 彼らは ACD が既存のモデルである Cross Teaching と BCP をどのように改善できるかを評価し、U-Net、DTC、URPC、MC-Net、SS-Net、SCP-Net、Cross Teaching、BCP などの他のモデルと比較した。

![img](https://img.tsuji.tech/abd-cvpr2024-1.jpg)

![img](https://img.tsuji.tech/abd-cvpr2024-2.jpg)

## 議論

* ABD は既存の手法の性能を向上させ、かつベストパフォーマスの結果を得ることができた。
* ABD の最高の性能を得るためには、画像摂動、ABD-R、ABD-I の3つの要素をすべて使用することが重要である。
