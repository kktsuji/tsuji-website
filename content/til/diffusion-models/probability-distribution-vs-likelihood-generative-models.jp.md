---
title: "Generative Modelにおける確率分布vs尤度"
description: ""
date: 2025-10-23T18:00:00+09:00
lastmod:
draft: false
math: true
---

## 前提条件

- 学習データセット：$D = \\{ x_1, \ldots, x_N \\}$（$x_i \in \mathbb{R}^{d}$）
- 各データポイント$x_i$は、未知の真の確率分布$p(x)$から独立にサンプリングされます。
- パラメータ$\theta$を持つGenerative Modelは確率分布$p(x|\theta)$を定義します。
- Generative Modelは$p(x|\theta)$からサンプリングすることで新しいデータポイント$x$を生成できます。
- Generative Modelの学習の目標は、モデルの分布$p(x|\theta)$が真の分布$p(x)$にできるだけ近似するような最適なパラメータ$\theta^*$を見つけることです。

## $x$上の確率分布

- 対象：モデルパラメータ$\theta$を固定した$x$の関数としての$p(x|\theta)$。
- 目的：パラメータ$\theta$のもとで、モデルが各データポイント$x$にどれだけの確率（mass/density）を割り当てるかを記述します。
- 正規化：$\sum_x p(x|\theta) = 1$（離散$x$）または$\int p(x|\theta) dx = 1$（連続$x$）。
- $p(x|\theta)$、$p_\theta(x)$がよく使用されます。
- モデルから新しいデータポイントをサンプリングする際に使用されます。

## $\theta$上の尤度

- 対象：観測データ$x$を固定した$\theta$の関数としての$L(\theta; x)$。
- 目的：パラメータ$\theta$を持つモデルが観測データ$x$をどれだけうまく説明するかを測定します。
- 正規化：$\theta$上で正規化されていません；合計/積分は1になりません。
- $L(\theta; x)$、$L_x(\theta)$がよく使用されます。
- パラメータ推定（例えばMLE）に使用されます。
- $\theta$上の確率分布ではありません。

## $p(x|\theta)$と$p_\theta(x)$の表記の濫用

実際には、同じ表記$p(x|\theta)$と$p_\theta(x)$が$x$上の確率分布と$\theta$上の尤度の両方に使用されることがよくあります。文脈に基づいてそれらを区別する必要があります：

- $x$の関数として（$\theta$固定）：$x$上の確率分布$p(x|\theta)$。
- $\theta$の関数として（$x$固定）：$\theta$上の尤度$p(x|\theta)$。
