---
title: 'Segment Anything in Medical Images'
description: ''
date: 2024-09-15T18:30:00+09:00
lastmod: 
draft: false
---

Title: Segment Anything in Medical Images

Authors: Jun Ma, Yuting He, Feifei Li, Lin Han, Chenyu You, Bo Wang

Published: Apr 24 2023

Link: [https://arxiv.org/abs/2304.12306](https://arxiv.org/abs/2304.12306)

Summary (Generated by Microsoft Copilot):

**Introduction**:
- **MedSAM** is a foundation model for **universal medical image segmentation**, developed to address the lack of generalizability in existing methods.

**Challenges**:
- Existing models are often **task-specific** and struggle with **generalization** across different medical imaging modalities and tasks.

**Methods**:
- MedSAM is trained on a **large-scale dataset** with over **1.5 million image-mask pairs** from **10 imaging modalities** and **30 cancer types**.

**Novelties**:
- MedSAM uses a **promptable segmentation approach** with bounding boxes, enhancing flexibility and adaptability.

**Results**:
- MedSAM outperforms state-of-the-art models in both **internal** and **external validation tasks**.

**Performances**:
- Demonstrates **better accuracy and robustness** compared to specialist models, achieving high **Dice Similarity Coefficient (DSC)** scores.

**Limitations**:
- **Modality imbalance** in the training set and difficulty in segmenting **vessel-like branching structures**.

**Discussion**:
- MedSAM shows potential for **improving diagnostic tools** and **personalizing treatment plans**, despite some limitations.