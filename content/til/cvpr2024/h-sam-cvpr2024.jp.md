---
title: "階層的デコーディングによる医療適応のためのSAMの潜在能力の解放"
description: ""
date: 2024-06-22T07:20:47+09:00
lastmod:
draft: false
---

## 概要

論文：Cheng et al., Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_Unleashing_the_Potential_of_SAM_for_Medical_Adaptation_via_Hierarchical_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2403.18271)）。

![img](https://img.tsuji.tech/h-sam-cvpr2024-0.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- プロンプト不要のH-SAMアプローチを提案した。これは2段階の階層的デコーディング手順を持つsegment anything model（SAM）の一種である。
- 元のSAMのデコーダー（元のSAMは単一のデコーダーを持つ）の後ろに「Hierarchical Mask Decoder」と呼ばれる第2のデコーダーを追加した。
- クラスバランスマスクガイド自己注意機構（CMAttn）と学習可能なマスククロスアテンションが重要な実装である。

## 性能評価手法

- H-SAMをSTransUnet、SwinUnet、TransDeepLab、DAE-Former、MERIT、AutoSAM、SAM Adapter、SAMed、UA-MT、SASSNet、DTC、URPC、MC-Net、SS-Net、BCP、nnUnetを含む他のモデルと比較した。
- この実験には3つのデータセット（Synapse Multi-Organ CT、左心房データセット、PROMISE12）が使用された。
- 評価指標としてDice係数と平均Hausdorff距離が利用された。

![img](https://img.tsuji.tech/h-sam-cvpr2024-1.jpg)

## 考察

- H-SAMは他の手法よりも優れた性能を示した。
- H-SAMが最良性能を達成するには、3つの重要なコンポーネント（学習可能なマスクアテンション、階層的ピクセルデコーダー、CM自己注意機構）すべてが必要である。
