---
title: 'MedCoSS: リハーサルバッファに基づくマルチモーダル表現学習, CVPR2024'
description: 'MedCoSS を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-20T08:51:23+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Ye et al., Continual Self-supervised Learning: Towards Universal Multi-modal Medical
Data Representation Learning
 ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2311.17597)).

![img](https://img.tsuji.tech/medcoss-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## 論文の新規性

* 彼らは modal conflicts と catastrophic forgetting を防ぐために、Medical Continual Self-Supervised (MedCoSS) を提案した。
* MedCoSS は、各モダリティのデータを別々の学習ステージに割り当て、継続的に学習する。
* リハーサルバッファ (Rehearsal buffers) を導入し、過去のモーダルデータを保持する。
* モダリティ：Report, X-ray, CT, MRI and Pathological images.

## 性能評価手法

* MedCoSS による結果と single-modal pre-training による結果、および multi-modal pre-traingin (手法は Joint SSL, EWC, ER, PackNet, CaSSLe) による結果を比較した (see table).

![img](https://img.tsuji.tech/medcoss-cvpr2024-1.jpg)

## 議論

* MedCoSS はいくつかのモダリティでは最高の性能を得るが、他のモダリティではそうではない。
* リハーサルバッファのサイズは、性能と、マルチモーダルデータ衝突 (data collision) と計算コストとのトレードオフである。
