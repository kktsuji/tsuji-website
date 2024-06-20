---
title: 'MedCoSS: Multi-Modal Representation Learning, CVPR2024'
description: ''
date: 2024-06-20T08:51:23+09:00
lastmod: 
math: false
draft: false
---

## Overview

Paper: Ye *et al.*, Continual Self-supervised Learning: Towards Universal Multi-modal Medical
Data Representation Learning
 ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2311.17597)).

![img](https://img.tsuji.tech/medcoss-multi-modal-representation-learning-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelty in the Paper

* 彼らは modal conflicts と catastrophic forgetting を防ぐために、Medical Continual Self-Supervised (MedCoSS) を提案した。
* MedCoSS は、各モダリティのデータを別々の学習ステージに割り当て、継続的に学習する。
* リハーサルバッファ (Rehearsal buffers) を導入し、過去のモーダルデータを保持する。
* モダリティ：Report, X-ray, CT, MRI and Pathological images.

## Performance Evaluation Methods

* MedCoSS による結果と single-modal pre-training による結果、および multi-modal pre-traingin (手法は Joint SSL, EWC, ER, PackNet, CaSSLe) による結果を比較した (see table).

![img](https://img.tsuji.tech/medcoss-multi-modal-representation-learning-cvpr2024-1.jpg)

## Discussions

* MedCoSS はいくつかのモダリティでは最高の性能を得るが、他のモダリティではそうではない。
* リハーサルバッファのサイズは、性能と、マルチモーダルデータの衝突と計算コストとのトレードオフである。
