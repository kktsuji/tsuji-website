---
title: 'MedCoSS: Rehearsal-Based Multi-Modal Representation Learning, CVPR2024'
description: 'Summary of the paper MedCoSS in CVPR2024.'
date: 2024-06-20T08:51:23+09:00
lastmod: 
draft: false
---

## Overview

Paper: Ye et al., Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2311.17597)).

![img](https://img.tsuji.tech/medcoss-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* They proposed Medical Continual Self-Supervised (MedCoSS) paradigm to prevent modal conflicts and catastrophic forgetting.
* MedCoSS assingns each modality data to separate training stage in continual learning.
* Rehearsal buffers are introduced to keep previous modal data.
* Modalities: Report, X-ray, CT, MRI and Pathological images.

## Performance Evaluation Methods

* They compared MedCoSS to single-modal pre-training and, multi-modal pre-traingin incluing Joint SSL, EWC, ER, PackNet, CaSSLe (see table).

![img](https://img.tsuji.tech/medcoss-cvpr2024-1.jpg)

## Discussions

* MedCoSS performs best in some modalities, but not others.
* The size of the rehearsal buffers is a trade-off between performance and multi-modal data collision and computational costs.
