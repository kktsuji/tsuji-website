---
title: "期待値"
description: '\'
date: 2025-10-24T22:00:00+09:00
lastmod:
math: true
draft: false
---

## 離散確率変数

確率変数$X$が有限または可算無限個の値$x_1, x_2, \ldots$を取ることができ、それぞれが確率$P(X=x_i) = p_i$に対応する場合、期待値は次のように定義されます：

$$E[X] = \sum_{i} x_i p_i$$

## 連続確率変数

確率変数$X$が確率密度関数$f(x)$を持つ連続変数である場合、期待値は次のように定義されます：

$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
