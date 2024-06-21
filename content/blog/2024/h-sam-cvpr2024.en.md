---
title: 'H-SAM: Hierarchical Segment Anything Model, Cvpr2024'
description: 'Sammary of the paper H-SAM in CVPR2024.'
date: 2024-06-22T07:20:47+09:00
lastmod: 
math: false
draft: false
---

## Overview

Paper: Cheng et al., Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_Unleashing_the_Potential_of_SAM_for_Medical_Adaptation_via_Hierarchical_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2403.18271)).

![img](https://img.tsuji.tech/h-sam-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* They proposed a prompt-free H-SAM approach, a type of segment anything model (SAM) with a two-stage hierarchical decoding procedure.
* They added a second decorder called the 'Hierarchical Mask Decoder' behind the original SAM's decoder (the original SAM has a single decoder).
* A class-balanced mask-guided self-attention (CMAttn) and a learnable mask cross-attention are their key implementations.

## Performance Evaluation Methods

* They compared their H-SAM to other models including STransUnet, SwinUnet, TransDeepLab, DAE-Former, MERIT, AutoSAM, SAM Adapter, SAMed, UA-MT, SASSNet, DTC, URPC, MC-Net, SS-Net, BCP and nnUnet.
* Three dataset the Synapse Multi-Organ CT, the left atrial dataset and the PROMISE12 were used for this experiments.
* The Dice coefficient and the acerage Hausdorff distance were utilized as the metrics.

![img](https://img.tsuji.tech/h-sam-cvpr2024-1.jpg)

## Discussions

* Only the good points of their proposed method were mentioned.
