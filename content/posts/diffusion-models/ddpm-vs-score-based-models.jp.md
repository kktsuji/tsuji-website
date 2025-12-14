---
title: "DDPM vs. スコアベースモデル"
description: ""
date: 2025-12-11T8:00:00+09:00
lastmod:
math: true
draft: false
---

## 主な違い

**DDPM (Denoising Diffusion Probabilistic Models)**:

- **フレームワーク**：離散時間マルコフ連鎖
- **学習**：各タイムステップで追加された**ノイズ**$\epsilon$を予測
- **目的関数**：変分下限（ELBO）
- **プロセス**：固定された順方向プロセスがガウシアンノイズを追加し、逆方向プロセスを学習
- **式**：$\|\epsilon - \epsilon_\theta(x_t, t)\|^2$を最小化

**スコアベースモデル**:

- **フレームワーク**：連続時間Diffusion（SDE）
- **学習**：**スコア関数**$\nabla_x \log p(x)$（対数密度の勾配）を予測
- **目的関数**：スコアマッチング（デノイジングスコアマッチング）
- **プロセス**：複数のスケールでノイズを追加し、各ノイズレベルでスコアを学習
- **式**：$\|\nabla_x \log p(x_t) - s_\theta(x_t, t)\|^2$を最小化

## 関連性

これらは**本質的に同等**です！Song et al. (2021)は以下を示しました：

- DDPMのノイズ予測$\epsilon_\theta$はスコアと関連しています：$s_\theta(x_t, t) = -\frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}}$
- Score-Based Modelは連続時間（離散ステップの代わりにSDE）を使用することでDDPMを一般化します
- 両者は異なるパラメータ化を通じて同じ基本構造を学習します

Score-Basedの視点は、より柔軟性を提供します（連続時間、異なるノイズスケジュール、確率フローODEなどの代替サンプラー）。
