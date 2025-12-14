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

ここで、$ \sigma: \mathbb{R}^K \to (0, 1)^K $、$ K > 1 $、ベクトル$ \mathbf{x} = (x_1, ..., x_K) \in \mathbb{R}^K $

Softmax functionはneural networkの最終層でactivation functionとして使用される。

"softargmax"と"normalized exponential function"という用語は"softmax function"の同義語である。

Softmax functionは[sigmoid function](https://tsuji.tech/sigmoid-function/)のone-hot arg maxの滑らかな近似である。

## 参考文献

- [Softmax Function - Wiki](https://en.wikipedia.org/wiki/Softmax_function)
