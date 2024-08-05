---
title: '病理組織学の論文メモ, 2024年'
description: '病理組織学の論文のメモ。'
date: 2024-08-01T09:28:45+09:00
lastmod: 
math: false
draft: false
---

注意：本ポストの図と表はそれぞれの論文からの引用である。

## PFPs: Prompt-guided Flexible Pathological Segmentation

Cui et al., "PFPs: Prompt-guided Flexible Pathological Segmentation for Diverse Potential Outcomes Using Large Vision and Language Models" ([arXiv](https://arxiv.org/abs/2407.09979)).

![img](https://img.tsuji.tech/pfps-arxiv2024-0.jpg)

![img](https://img.tsuji.tech/pfps-arxiv2024-1.jpg)

* 投稿日: 2024/07/13
* 著者らは、病理画像セグメンテーションタスク向けの efficient segment anything model (EfficientSAM, Xiong et al) のポテンシャルと柔軟性を向上させるため、PFPs と呼ばれる手法を提案した。
* PFPs は、Omni-seg (Deng et al., 2023) と HATs (Deng et al., 2024) から着想を得ている。
* 低ランク適応（LoRA, Hu et al., 2021）は、TinyLLaMA（Zhang et al., 2024）と呼ばれる事前訓練済みの大規模言語モデル (LLM) のファインチューニングに用いられる。
* データセット：腎臓データセット NEPTUNE (Barisoni et al., 2013)。
* 彼らは「カプセル領域外の細胞核のセグメンテーション」など、9種類のタスクを定義した。
* 学んだこと：Segment anything model (SAM, Kirillov, 2023)、Omni-seg や HATs の dynamic head コンセプト。
