---
title: "半教師あり医用画像セグメンテーションのための適応的双方向変位"
description: ""
date: 2024-06-24T08:21:00+09:00
lastmod:
draft: false
---

## 概要

論文：Chi et al., Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Chi_Adaptive_Bidirectional_Displacement_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2405.00378)）。

![img](https://img.tsuji.tech/abd-cvpr2024-0.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- 半教師あり医用画像セグメンテーションにおける一貫性学習の問題を解決するために「Adaptive Bidirectional Displacement」（ABD）手法を提案した。
- 一貫性学習が複数の摂動を利用する場合、学習プロセスは容易に制御不能になる。
- ABDは複数の摂動を採用可能にするために導入された。
- ABDは2つの摂動を持つ。画像摂動として画像拡張処理が使用され、弱い拡張と強い拡張が生成される。さらに、ネットワーク摂動として2つのネットワークも利用される。
- ABDフレームワークは2種類の変位手法、ABD-RとABD-Iで構成される。
- ABD-Rは信頼性の高い信頼度を持つ適応的双方向変位である。拡張画像内の最も低い信頼度パッチが、他の拡張画像内の最も信頼性の高い領域と置き換えられる。
- ABD-Iは逆信頼度を持つABDである。拡張画像内の最も高い信頼度領域が、他の拡張画像内の最も低い信頼性パッチと置き換えられる。
- 変位された画像は新しいサンプルとして扱われる。
- ABCアプローチは既存の手法に追加可能である。

Translated with DeepL (https://www.deepl.com/app/?utm_source=ios&utm_medium=app&utm_campaign=share-translation)

## 性能評価手法

- 2つのデータセットが使用された：ACDCとPROMISE12。
- ABDが既存モデル（Cross TeachingとBCP）をどのように改善できるかを評価し、U-Net、DTC、URPC、MC-Net、SS-Net、SCP-Net、Cross Teaching、BCPを含む他のモデルと比較した。

![img](https://img.tsuji.tech/abd-cvpr2024-1.jpg)

![img](https://img.tsuji.tech/abd-cvpr2024-2.jpg)

## 議論

- ABDは既存手法の性能を改善し、最高の結果を達成
- ABDの最高性能を得るには、画像摂動、ABD-R、ABD-Iの3つの構成要素すべてを使用することが重要であることを検証
