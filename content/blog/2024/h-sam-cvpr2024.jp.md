---
title: 'H-Sam: 階層的 Segment Anything モデル, Cvpr2024'
description: 'H-SAM を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-22T07:20:47+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Cheng et al., Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_Unleashing_the_Potential_of_SAM_for_Medical_Adaptation_via_Hierarchical_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2403.18271)).

![img](https://img.tsuji.tech/h-sam-cvpr2024-0.jpg)

(本ポストの図と表は論文からの引用である)

## 論文の新規性

* 彼らはプロンプトフリーの手法 "H-SAM" (2段階の階層的デコード手順を持つ Segment Anything Model (SAM) の一種) を提案した。
* 彼らはオリジナルの SAM のデコーダーの後ろに Hierarchical Mask Decoder (階層的マスクデコーダー) と呼ばれる2段目のデコーダーを追加した（オリジナルの SAM は単一のデコーダーを持つ）。
* Class-balanced mask-guided self-attention (CMAttn) と learnable mask cross-attention がキーポイントである。

## 性能評価手法

* H-SAM と他の手法を比較した (STransUnet, SwinUnet, TransDeepLab, DAE-Former, MERIT, AutoSAM, SAM Adapter, SAMed, UA-MT, SASSNet, DTC, URPC, MC-Net, SS-Net, BCP and nnUnet).
* 3つのデータセットを使用した (Synapse Multi-Organ CT, left atrial dataset and PROMISE12).
* Dice coefficient と acerage Hausdorff distance を評価指標に使用した。

![img](https://img.tsuji.tech/h-sam-cvpr2024-1.jpg)

## 議論

* 彼らの提案した方法の良い点だけが述べられている。
