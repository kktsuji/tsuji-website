---
title: "Softmax Function"
description: ""
date: 2024-12-12T9:00:00+09:00
lastmod:
draft: false
math: true
---

## Softmax Function

$ \sigma(\mathbf{x}) = \dfrac{e^{x*i}}{\sum*{j=1}^{K} e^{\mathbf{x}\_i}} $

where $ \sigma: \mathbb{R}^K \to (0, 1)^K $, $ K > 1 $, a vector $ \mathbf{x} = (x_1, ..., x_K) \in \mathbb{R}^K $.

The softmax function is used as the activation function in the last layer of a neural network.

The terms "softargmax" and "normalized exponential function" are synonyms for the "softmax function".

The softmax function is a smooth approximation of one-hot arg max of the [sigmoid function](https://tsuji.tech/sigmoid-function/).

## References

- [Softmax Function - Wiki](https://en.wikipedia.org/wiki/Softmax_function)
