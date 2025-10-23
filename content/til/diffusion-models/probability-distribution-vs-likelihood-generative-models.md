---
title: 'Probability Distribution vs. Likelihood in Generative Models'
description: ''
date: 2025-10-23T18:00:00+09:00
lastmod: 
draft: false
math: true
---

## Prerequisites

- Training dataset: $D = \\{ x_1, \ldots, x_N \\}$ ($x_i \in \mathbb{R}^{d}$)
- Each data point $x_i$ is sampled independently from an unknown true probability distribution $p(x)$.
- Generative model with parameters $\theta$ defines a probability distribution $p(x|\theta)$.
- Generative model can generate new data points $x$ by sampling from $p(x|\theta)$.
- The goal of training the generative model is to find the optimal parameters $\theta^*$ that make the model's distribution $p(x|\theta)$ approximate the true distribution $p(x)$ as closely as possible.

## Probability Distribution over $x$

- Object: $p(x|\theta)$ viewed as a function of $x$ with model parameters $\theta$ fixed.
- Purpose: Describes how probability (mass/density) the model assigns to each data point $x$ under parameters $\theta$.
- Normalization: $\sum_x p(x|\theta) = 1$ (discrete $x$) or $\int p(x|\theta) dx = 1$ (continuous $x$).
- $p(x|\theta)$, $p_\theta(x)$ are often used.
- Used in sampling new data points from the model.

## Likelihood over $\theta$

- Object: $L(\theta; x)$ viewed as a function of $\theta$ with observed data $x$ fixed.
- Purpose: Measures how well the model with parameters $\theta$ explains the observed data $x$.
- Normalization: Not normalized over $\theta$; does not sum/integrate to 1.
- $L(\theta; x)$, $L_x(\theta)$ are often used.
- Used in parameter estimation (e.g., MLE).
- Not a probability distribution over $\theta$.

## Abuse of Notation of $p(x|\theta)$ and $p_\theta(x)$

In practice, the same notations $p(x|\theta)$ and $p_\theta(x)$ is often used for both the probability distribution over $x$ and the likelihood over $\theta$. You need to distinguish them based on the context:

- As a function of $x$ ($\theta$ fixed): probability distribution $p(x|\theta)$ over $x$.
- As a function of $\theta$ ($x$ fixed): likelihood $p(x|\theta)$ over $\theta$.
