---
title: 'A2MIM: Architecture-Agnostic Masked Image Modeling, ICML2023'
description: 'Summary of the paper A2MIM in ICML2023.'
date: 2024-07-01T21:00:00+09:00
lastmod: 
draft: false
---

## Overview

Paper: Li et al., Architecture-Agnostic Masked Image Modeling - From ViT back to CNN ([icml2023 open access](https://icml.cc/virtual/2023/poster/24861) or [arxiv](https://arxiv.org/abs/2205.13943)).

![img](https://img.tsuji.tech/a2mim-icml2023-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* They proposed a new approach called “Architecture-Agnostic Masked Image Modeling” (A2MIM) to enhance benefits of middle-order interactions between patches.
* They utilized the mean RGB value of masked patch instead of the learnable mask token in existing MIM frameworks.
* Fourier domain loss, inspired by Focal Frequency loss, was introduced to A2MIM to treat middle-order interaction.
* A2MIM can be applied to improve CNNs and Transformers.

## Performance Evaluation Methods

* They evaluated the abilities of A2MIM with three perspectives: fine-tuning for classification, transfer learning for object detection and segmentation.
* They showed A2MIM can improve representation performances of pre-trained network.

![img](https://img.tsuji.tech/a2mim-icml2023-1.jpg)

## Discussions

* There were less benefits of CNNs than transformers to apply A2MIM. Authors guessed middle-order intersections learning was limited by inductive bias of CNNs.
* Transformers showed more effectiveness on longer pre-training with A2MIM.

## What I learned

* ViT and CNN have low-pass and high-pass filtering characteristics, respectively, and have specific frequency bands, making it difficult to model middle-order interactions well.