---
title: "Main Categories of Generative Models"
description: ""
date: 2025-12-11T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Major Categorizations

**1. Likelihood-based models** (explicit density models)

- **Autoregressive models**: PixelCNN, PixelRNN, GPT, BERT
- **Variational Autoencoders (VAEs)**: Standard VAE, β-VAE, VQ-VAE
- **Flow-based models**: RealNVP, Glow, NICE
- **Energy-based models (EBMs)**: Restricted Boltzmann Machines
- **Diffusion models**: DDPM, Score-based models

**2. Implicit generative models** (no explicit density)

- **Generative Adversarial Networks (GANs)**: DCGAN, StyleGAN, Progressive GAN, Conditional GAN

## Key Differences

- **Likelihood-based**: Define explicit probability distribution $p(x|\theta)$, can compute likelihood
- **Implicit**: Generate samples directly without defining explicit density function

Some models blur these categories:

- **Diffusion models** are likelihood-based but generate samples through an iterative denoising process
- **Score-based models** learn the gradient of the log density rather than the density itself

Each approach has trade-offs in terms of:

- Training stability
- Sample quality
- Likelihood computation
- Generation speed
- Mode coverage
