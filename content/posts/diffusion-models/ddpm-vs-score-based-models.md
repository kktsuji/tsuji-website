---
title: "DDPM vs. Score-Based Models"
description: ""
date: 2025-12-11T8:00:00+09:00
lastmod:
math: true
draft: false
---

## Key Differences

**DDPM (Denoising Diffusion Probabilistic Models)**:

- **Framework**: Discrete-time Markov chain
- **Training**: Predicts the **noise** $\epsilon$ added at each timestep
- **Objective**: Variational lower bound (ELBO)
- **Process**: Fixed forward process adds Gaussian noise, learns reverse process
- **Formula**: Minimizes $\|\epsilon - \epsilon_\theta(x_t, t)\|^2$

**Score-Based Models**:

- **Framework**: Continuous-time diffusion (SDEs)
- **Training**: Predicts the **score function** $\nabla_x \log p(x)$ (gradient of log density)
- **Objective**: Score matching (denoising score matching)
- **Process**: Adds noise at multiple scales, learns score at each noise level
- **Formula**: Minimizes $\|\nabla_x \log p(x_t) - s_\theta(x_t, t)\|^2$

## Connection

They're **essentially equivalent**! Song et al. (2021) showed:

- DDPM's noise prediction $\epsilon_\theta$ is related to the score: $s_\theta(x_t, t) = -\frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}}$
- Score-based models generalize DDPM by using continuous time (SDEs instead of discrete steps)
- Both learn the same underlying structure through different parameterizations

The score-based view provides more flexibility (continuous time, different noise schedules, alternative samplers like probability flow ODEs).
