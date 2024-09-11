---
title: 'LoRKD: Knowledge Decomposition for Medical Fundation Models, CVPR2024'
description: 'Sammary of the paper LoRKD in CVPR2024.'
date: 2024-06-23T12:10:31+09:00
lastmod: 
math: false
draft: false
---

## Overview

Paper: Cheng et al., Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Low-Rank_Knowledge_Decomposition_for_Medical_Foundation_Models_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2403.18271)).

![img](https://img.tsuji.tech/lorkd-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* They proposed a new paradigm called "knowledge decomposition" (KD), which breaks down a medical foundation model into multiple "lightweight experts" to reduce computational costs and improve its expertise.
* To achieve kowledge decomposition, they also proposed a low-rank knowledge decomposition (LoRKD) framework inspired by low-rank adaptiation (LoRA) techniques.
* Efficient knowledge separation convolution (EKS Conv.) is one of the important methods in LoRKD, which reduces computational complexity by adding the one-hot vector, represeting which task the input belongs, to the convolution.
* A task knowledge transfer loss is an another key component of LoRKD to transfer knowledge of the foundation model to each lightweight expert model.
* Deployment of knowledge expert knowledge can be performed by adding and subtracting parameters.

## Performance Evaluation Methods

* They used three dataset: Redimagenet, MedMist and Med-MT.
* They applied ResNet50 and ShuffleNetV2 for pre-trained models and lightweight expert models respectively.
* LoRKD was compared to some methods including baseline, single-task learning (STL), multi-task learning (MTL), STL-KD, MTL-KD, MoC-MTL, Aligned-MTL and KF.

![img](https://img.tsuji.tech/lorkd-cvpr2024-1.jpg)

## Discussions

* The lightweight expert models of LoRKD performed better than or equal to the others on most downstream tasks, even with fewer number of parameters.
