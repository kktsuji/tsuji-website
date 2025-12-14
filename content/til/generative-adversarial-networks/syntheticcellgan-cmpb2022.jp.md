---
title: "Automatic generation of artificial images of leukocytes and leukemic cells using generative adversarial networks (syntheticcellgan)"
description: ""
date: 2024-09-30T9:10:00+09:00
lastmod:
draft: false
---

タイトル: Automatic generation of artificial images of leukocytes and leukemic cells using generative adversarial networks（syntheticcellgan）

著者: Kevin Barreraa、Anna Merino、Angel Molina、José Rodellar

発行: 2022年12月

リンク: [https://doi.org/10.1016/j.cmpb.2022.107314](https://doi.org/10.1016/j.cmpb.2022.107314)

要約（Microsoft Copilotによる生成）:

**Introduction:**

- この研究はgenerative adversarial networks（GANs）を使用して白血球および白血病細胞の人工画像を生成するシステムであるSyntheticCellGAN（SCG）の開発に焦点を当てています。

**Challenges:**

- 特に微妙な形態学的差異を持つ低有病率疾患において、モデルの訓練のための大規模でよくアノテーションされた画像セットの収集が困難です。

**Methods:**

- SCGは2つの連続したGANsを使用します: 低解像度画像用のWasserstein GANと特定の細胞タイプの高解像度画像用のimage-to-image translation GANです。

**Novelties:**

- このシステムは正常な白血球と、血液塗抹標本で見つけるのが困難な非定型前骨髄球や有毛細胞などの稀な細胞タイプの両方の高解像度画像を生成します。

**Results:**

- 生成された画像は定量的メトリクス、専門家による形態学的検証、および分類精度テストを通じて評価され、高い精度とリアリズムを示しました。

**Performances:**

- SCG画像で訓練された分類器は実際の細胞を識別する際に最大100%の精度を達成し、訓練目的のための合成画像の有効性を実証しました。

**Limitations:**

- 訓練のための実際の画像の収集には数年かかり、システムは現在限られた数の細胞タイプに焦点を当てています。

**Discussion:**

- SCGシステムは画像データセットの増強および臨床実践における自動認識モデルの改善において有望性を示していますが、より多くの細胞タイプを含め、異なる研究室間で標準化するためのさらなる作業が必要です。
