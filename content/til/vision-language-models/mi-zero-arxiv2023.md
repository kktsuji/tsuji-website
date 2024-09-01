---
title: 'Visual Language Pretrained Multiple Instance Zero-Shot Transfer for Histopathology Images'
description: ''
date: 2024-08-29T21:26:00+09:00
lastmod: 2024-09-01T16:30:00+09:00
math: false
draft: false
---

Title: Visual Language Pretrained Multiple Instance Zero-Shot Transfer for Histopathology Images

Authors: Ming Y. Lu, Bowen Chen, Andrew Zhang, Drew F.K. Williamson, Richard J. Chen, Tong Ding, Long Phi Le, Yung-Sung Chuang, Faisal Mahmood

Published: Jun 13, 2023

Link: [https://arxiv.org/abs/2306.07831](https://arxiv.org/abs/2306.07831)

Summary (Generated by Microsoft Copilot):

**Introduction:**
- The paper presents **MI-Zero**, a framework for zero-shot transfer in histopathology images using contrastive visual language pretraining.

**Challenges:**
- **Data limitations**: Lack of large-scale, publicly available paired image-text datasets.
- **Computational challenges**: Handling gigapixel whole slide images (WSIs) that can span up to 100,000 × 100,000 pixels.

**Methods:**
- **Multiple Instance Learning (MIL)**: Reformulates zero-shot transfer to handle large images.
- **Pretraining**: Uses over 550k pathology reports and 33k histopathology image-caption pairs.

**Novelties:**
- **Zero-shot transfer**: First application in pathology for WSIs.
- **MI-Zero framework**: Utilizes pretrained visual language encoders for diagnostic tasks without additional labels.

**Results:**
- Achieves an average median zero-shot accuracy of **70.2%** across three cancer subtyping tasks.

**Performances:**
- **TopK pooling**: Performs better than mean pooling.
- **Spatial smoothing**: Does not significantly change performance.

**Limitations:**
- **Data constraints**: Limited by the size and quality of the curated dataset.

**Discussion:**
- Potential for **semi-supervised learning** workflows and applications in other fields like satellite imaging. Future work includes collecting more datasets and improving sample efficiency.