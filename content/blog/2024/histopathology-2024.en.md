---
title: 'Memo of Histopathology Papers, Computer Vision and AI, 2024'
description: 'Memo of Histopathology Papers, Computer Vision and AI, 2024.'
date: 2024-08-01T09:28:45+09:00
lastmod: 2024-08-08T06:50:00+09:00
math: false
draft: false
---

Note: Figures and tables in this post are from the respective original papers.

## PFPs: Prompt-guided Flexible Pathological Segmentation

Cui et al., "PFPs: Prompt-guided Flexible Pathological Segmentation for Diverse Potential Outcomes Using Large Vision and Language Models" ([arXiv](https://arxiv.org/abs/2407.09979)).

![img](https://img.tsuji.tech/pfps-arxiv2024-0.jpg)

![img](https://img.tsuji.tech/pfps-arxiv2024-1.jpg)

* Published: Jul. 13, 2024
* Authors proposed a method called PFPs that increases a potential and flexibility of the efficient segment anything model (EfficientSAM, Xiong et al., 2024) for pathology image segmentation tasks.
* They was inspired by Omni-seg (Deng et al., 2023) and HATs (Deng et al., 2024).
* Low-rank adaptation (LoRA, Hu et al., 2021) was used for fine-tuning of pre-trained large language model (LLM) called TinyLLaMA (Zhang et al., 2024).
* Dataset: a kidney dataset NEPTUNE (Barisoni et al., 2013).
* They define 9 types of tasks such as "Segmentation of the nuclei outside the capsule region".
* What I learned: Segment anything model (SAM, Kirillov, 2023), dynamic head concept in Omni-seg and HATs.

## Prompting Medical Large Vision-Language Models

Guo ea al., “Prompting Medical Large Vision-Language Models to Diagnose Pathologies by Visual Question Answering” ([arXiv](https://arxiv.org/abs/2407.21368)).

![img](https://img.tsuji.tech/prompting-medical-lvlm-arxiv2024-0.jpg)

* Published: Jul. 31, 2024
* Authors introduced two prompting methods to reduce hallucinations on medical large vision-language model (LVLMs) and improve visual question answering (VQA) tasks:
    1. Provide detailed pathological descriptions to the question queries.
    2. Introduce “weak learner” to provide its prediction results to the question queries as a reference opinion.
* Proposed method improves the diagnostic F1 score by up to 0.27 on the MIMIC-CXR-JPG and Chexpert dataset.

## Pathology Foundation Models

Ochi et al., "Pathology Foundation Models" ([arXiv](https://arxiv.org/abs/2407.21317)).

![img](https://img.tsuji.tech/pathology-foundation-models-arxiv2024-0.jpg)

* Published: Jul. 31, 2024
* Authors summarized pathology foundation models.

## Multistain Pretraining for Slide Representation Learning in Pathology

* Authors: Guillaume Jaume et al.
* Published: Aug. 5, 2024
* Link: [arXiv](http://arxiv.org/abs/2408.02859)
* Authors proposed a multimodal pretraining strategy called "MADELEINE", a slide representation learning method, leveraging multiple stained slides images for richer training.
* Trained MADELEINE encoder can be used for some downstream tasks such as few-shot classification, prognostication and fine-tuning.
* Training process utilizes a dual global-local cross-stain alignment objective with breast cancer samples and kidney transplant samples.

![img](https://img.tsuji.tech/madeleine-arxiv2024-0.jpg)

![img](https://img.tsuji.tech/madeleine-arxiv2024-1.jpg)
