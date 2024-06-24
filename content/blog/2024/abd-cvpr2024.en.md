---
title: 'ABD: Adaptive Bidirectional Displacement, CVPR2024'
description: 'Summary of the paper ABD in CVPR2024.'
date: 2024-06-24T08:21:00+09:00
lastmod: 
math: false
draft: false
---

## Overview

Paper: Chi et al., Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Chi_Adaptive_Bidirectional_Displacement_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2405.00378)).

![img](https://img.tsuji.tech/abd-cvpr2024-0.jpg)

(Figures and tables in this post are from the original paper)

## Novelties of the Paper

* They proposed an "Adaptive Bidirectional Displacement" (ABD) method to solve the propbems of consistency learning on semi-supervised medical image segmentation.
* If the consistency learning utilizes multiple perturbations, it's learning process will easily get uncontrollable.
* The ABD was introduced to make it enable to employ mutiple perturbations.
* ABD has two perturbatons. Image argumentation proceses are used as the image purturbation, resulting weak and strong augmentations. In addition, two networks are also utilized as the network perturbation.
* ABD framework consists of two types of displacement methods, ABD-R and ABD-I.
* ABD-R is an adaptive bidirectional displacement with reliable confidence. The lowest confidence patches in the augmented image are displaces with the most reliable regions in the other augmented image.
* ABD-I is an ABD with inverse confidence. The highest confidence regions in the augmented image are replaced by the lowest reliability patches in the other augmented image.
* Displaced images are treated as new samples.
* ABC approach an be added to exsisting methods.

Translated with DeepL (https://www.deepl.com/app/?utm_source=ios&utm_medium=app&utm_campaign=share-translation)

## Performance Evaluation Methods

* Two dataset are used: ACDC and PROMISE12.
* They evaluated how ACD can improve the existing models, Cross Teaching and BCP, and compare them to other models including U-Net, DTC, URPC, MC-Net, SS-Net, SCP-Net, Cross Teaching and BCP.

![img](https://img.tsuji.tech/abd-cvpr2024-1.jpg)

## Discussions

* ABD can improve performance of existing methods and achieved the best results.
* They examined that it's important to obtain the best performance of ABD to use all three compornents: image purturbation, ABD-R and ABD-I.
