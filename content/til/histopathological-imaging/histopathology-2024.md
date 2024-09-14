---
title: 'Memo of Histopathology Papers, Computer Vision and AI, 2024'
description: 'Memo of Histopathology Papers, Computer Vision and AI, 2024.'
date: 2024-08-01T09:28:45+09:00
lastmod: 2024-08-08T10:00:00+09:00
draft: false
---

Note: Figures and tables in this post are from the respective original papers.

## Multistain Pretraining for Slide Representation Learning in Pathology

* Authors: Guillaume Jaume et al.
* Published: Aug. 5, 2024
* Link: [arXiv](http://arxiv.org/abs/2408.02859)
* Authors proposed a multimodal pretraining strategy called "MADELEINE", a slide representation learning method, leveraging multiple stained slides images for richer training.
* Trained MADELEINE encoder can be used for some downstream tasks such as few-shot classification, prognostication and fine-tuning.
* Training process utilizes a dual global-local cross-stain alignment objective with breast cancer samples and kidney transplant samples.

![img](https://img.tsuji.tech/madeleine-arxiv2024-0.jpg)

![img](https://img.tsuji.tech/madeleine-arxiv2024-1.jpg)
