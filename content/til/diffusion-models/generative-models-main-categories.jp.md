---
title: "生成モデルの主要カテゴリ"
description: ""
date: 2025-12-11T8:00:00+09:00
lastmod:
math: true
draft: false
---

## 主要な分類

**1. 尤度ベースモデル**（explicit densityモデル）

- **Autoregressiveモデル**：PixelCNN、PixelRNN、GPT、BERT
- **Variational Autoencoders（VAE）**：標準VAE、β-VAE、VQ-VAE
- **Flowベースモデル**：RealNVP、Glow、NICE
- **エネルギーベースモデル（EBM）**：Restricted Boltzmann Machines
- **Diffusionモデル**：DDPM、Score-basedモデル

**2. 暗黙的生成モデル**（explicit densityなし）

- **Generative Adversarial Networks（GAN）**：DCGAN、StyleGAN、Progressive GAN、Conditional GAN

## 主な違い

- **尤度ベース**：明示的な確率分布$p(x|\theta)$を定義し、尤度を計算可能
- **暗黙的**：明示的な密度関数を定義せずに直接サンプルを生成

一部のモデルはこれらのカテゴリを曖昧にします：

- **Diffusionモデル**は尤度ベースですが、反復的なdenoisingプロセスを通じてサンプルを生成します
- **Score-basedモデル**は密度自体ではなく、対数密度の勾配を学習します

各アプローチには以下の点でトレードオフがあります：

- トレーニングの安定性
- サンプル品質
- 尤度計算
- 生成速度
- モードカバレッジ
