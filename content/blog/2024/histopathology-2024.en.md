---
title: 'Memo of Histopathology Papers, 2024'
description: 'Memo of Histopathology Papers.'
date: 2024-08-01T09:28:45+09:00
lastmod: 
math: false
draft: false
---

Note: Figures and tables in this post are from the respective original papers.

## PFPs: Prompt-guided Flexible Pathological Segmentation

Cui et al., "PFPs: Prompt-guided Flexible Pathological Segmentation for Diverse Potential Outcomes Using Large Vision and Language Models" ([arXiv](https://arxiv.org/abs/2407.09979)).

![img](https://img.tsuji.tech/pfps-arxiv2024-0.jpg)

![img](https://img.tsuji.tech/pfps-arxiv2024-1.jpg)

* Authors proposed a method called PFPs that increases a potential and flexibility of the efficient segment anything model (EfficientSAM, Xiong et al., 2024) for pathology image segmentation tasks.
* They was inspired by Omni-seg (Deng et al., 2023) and HATs (Deng et al., 2024).
* Low-rank adaptation (LoRA, Hu et al., 2021) was used for fine-tuning of pre-trained large language model (LLM) called TinyLLaMA (Zhang et al., 2024).
* Dataset: a kidney dataset NEPTUNE (Barisoni et al., 2013).
* They define 9 types of tasks such as "Segmentation of the nuclei outside the capsule region".
* What I learned: Segment anything model (SAM, Kirillov, 2023), dynamic head concept in Omni-seg and HATs.
