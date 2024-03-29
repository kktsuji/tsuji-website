---
title: 'GAN-DL for dataset rxrx19a and rxrx1'
slug: 'gan-dl-rxrx19a-rxrx1'
description: ''
date: 2024-03-26T22:38:26+09:00
lastmod: 
math: false
tocOpen: true
draft: false
---

This post introduces a paper that proposed a deep learning technology GAN-DL[^1] witten by Mascolini *et. al.*

## Overview of this paper

* Authors proposed a self-supervised learning framework called "Generative Adversarial Network Discriminator Learner (GAN-DL)[^1]" based on NVIDIA's StyleGAN2 architecture[^2].
* GAN-DL was trained by using a public dataset RxRx19a[^3] consist of fluorescence microscopy images of human cells infected COVID-19.
* Features of trained GAN-DL's discriminator were applied to some downstream tasks like classification.
* Methods of some previous research were used to evaluate GAN-DL's performance.

## Which points are better than others?

* No image annotations required.
  * Some related works[^4] [^5] need labels of a target dataset to generate their embedding data.
  * On the other hand, GAN-DL works without labels and annotations.

## Which points are important?

* xxx

## Summary of proposed methods

* StyleGAN2
  * First convolutional layer was modified.

## How was this performance validated?

* xxx

## What was being discussed?

* xxx

## Is source code aveilable?

* Not available.
* But authors has pablished embedding data that is a result of GAN-DL.

## Is dataset available?

* Yes.

## What I learned

* NVIDIA's StyleGan2 is a Wasserstein Generative Adcersarial Networks family.

## Which paper should I read next?

* xxx



[^1]: Alessio Mascolini, Dario Cardamone, Francesco Ponzio, Santa Di Cataldo and Elisa Ficarra. Exploiting generative self-supervised learning for the assessment of biological images with lack of annotations. *BMC Bioinformatics*, 23, 295, 2022. [https://doi.org/10.1186/s12859-022-04845-1](https://doi.org/10.1186/s12859-022-04845-1)

[^2]: Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen and Timo Aila. Analyzing and improving the image quality of stylegan. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 8110–19, 2020.

[^3]: Recursion. RxRx19a dataset. [https://www.rxrx.ai/rxrx19a](https://www.rxrx.ai/rxrx19a) (2020).

[^4]: Dylan Zhuangand Ali K. Ibrahim. Deep learning for drug discovery: a study of identifying high efficacy drug compounds using a cascade transfer learning approach. *Applied Sciences*. 2021;11(17):7772, 2021.

[^5]: M. Sadegh Saberian, Kathleen P. Moriarty, Andrea D. Olmstead, Christian Hallgrimson, François Jean, Ivan R. Nabi, Maxwell W. Libbrecht and Ghassan Hamarneh. DEEMD: Drug Efficacy Estimation Against SARS-CoV-2 Based on Cell Morphology With Deep Multiple Instance Learning. *Medical Image Computing and Computer Assisted Intervention – MICCAI 2023*, vol.14227, pp.676, 2023.
