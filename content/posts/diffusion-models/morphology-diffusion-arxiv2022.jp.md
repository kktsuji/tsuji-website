---
title: "A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images"
description: ""
date: 2024-09-18T19:15:00+09:00
lastmod:
draft: false
---

Title: A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images

Authors: Puria Azadi Moghadam, Sanne Van Dalen, Karina C. Martin, Jochen Lennerz, Stephen Yip, Hossein Farahani, Ali Bashashati

Published: Sep 27 2022

Link: [https://arxiv.org/abs/2209.13167](https://arxiv.org/abs/2209.13167)

Summary（Microsoft Copilotによる生成）：

**Introduction：**

- この論文は、**Diffusion Probabilistic Model**を使用して脳腫瘍に焦点を当てた合成病理組織画像を生成することを探求しています。

**Challenges：**

- **病理組織診断**は時間がかかり主観的であり、稀な変異体への露出が限られています。
- 病理学における**Generative Model**はまだ初期段階です。

**Methods：**

- 画像品質を向上させるために**色正規化**と**知覚優先重み付け**を利用します。
- Diffusion Modelを**Generative Adversarial Networks (GANs)**と比較します。

**Novelties：**

- 病理組織画像合成に**Diffusion Probabilistic Model**を使用することを初めて提案しました。
- 画像の詳細を改善するために**形態学的優先順位付け**を導入しました。

**Results：**

- Diffusion ModelはGANを上回る高品質な画像を生成します。
- 合成画像は実際の画像とほぼ区別がつきません。

**Performances：**

- **Inception Score (IS)**、**Fréchet Inception Distance (FID)**、**sFID**メトリクスでより良いスコアを達成しました。
- 画像品質と多様性において、より高い**精度と再現率**を示しました。

**Limitations：**

- 複数のDiffusionステップのため、GANと比較して**サンプリング時間が長い**です。

**Discussion：**

- この手法は**教育、プライバシー、データ拡張**アプリケーションに使用できる可能性があります。
- 今後の研究には、サンプリング時間を短縮するためのモデルの最適化が含まれます。
