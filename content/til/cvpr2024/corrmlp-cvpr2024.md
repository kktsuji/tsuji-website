---
title: 'Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration'
description: ''
date: 2024-06-25T20:26:48+09:00
lastmod: 
draft: false
---

## Overview

Paper: Meng et al., Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Meng_Correlation-aware_Coarse-to-fine_MLPs_for_Deformable_Medical_Image_Registration_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2406.00123)).

![img](https://img.tsuji.tech/corrmlp-cvpr2024-0.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-1.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* Multi-layer perceptron (MLP) without self-attention is one of efficient methods in terms of computational costs and memory usages but it doesn’t account for inductive bias.
* To solve this problem, authors proposed a registration method called correlation-aware MLP-based (CorrMLP) network.
* Two key points are a CNN-based hierarchical feature extraction encoder and a correlation-aware coarse-to-fine registration decoder.
*  Correlation-aware multi-window MLP (CMW-MLP) blocks in the later decoder treat multiple size features extracted by the former encoder, which makes CorrMLP possible to utilize fine-grained long-range features on full resolution images.
* CorrMLP can solve local non-linear and wide range deformations for image registration. 

## Performance Evaluation Methods

* They compared CorrMLP to other methods incluing SyN, NifyReg, VoxelMorph, Swin-CoxelMorph, TransMorph, TransMatch, LapIRN, ULAE-net, Dual-PRNet++, SDHNet, NICE-Net and NICE-Trans.
*  Dataset: ADNI, ABIDE, ADHD, IXI, Mindboggle and Buckner for 3D inter-patient brain image registration, ACDC for 4D intra-patient cardiac image registration.

![img](https://img.tsuji.tech/corrmlp-cvpr2024-2.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-3.jpg)

## Discussions

* CorrMLP performed better than other methods (transformers, CNNs and MLPs) on the DSC and NJD indices.
* The both image-level and step-level correlations are necessary for the CorrMLP's best performans.

## What I learned

* Inductive bias is implemented by a combination of CNN (in the former encoder) and global average pooling (in the later decoder), I guess.
* MLPs doesn't take into account indactive bias.
* Transformer has the capability to capture wide-range features in an image, but it may difficult to treat fine-grained long-range dependences at the input image size since downsample features are commonly used to reduce computation and memory consumption.
