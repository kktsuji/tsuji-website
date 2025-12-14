---
title: "機械学習におけるtorch.nn.Conv2d vs torch.nn.ConvTranspose2d"
description: ""
date: 2025-11-28T08:00:00+09:00
lastmod:
math: true
draft: false
---

`torch.nn.Conv2d`と`torch.nn.ConvTranspose2d`は逆の操作です：

## Conv2d（標準畳み込み）

- 空間次元を削減（ダウンサンプリング）
- 特徴抽出に使用
- 出力サイズは入力より小さい（パディングで補償しない限り）
- 式：`output_size = floor((input_size + 2*padding - kernel_size) / stride) + 1`

## ConvTranspose2d（転置畳み込み/逆畳み込み）

- 空間次元を増加（アップサンプリング）
- 再構成/生成に使用（例：autoencoderのdecoder、GANのgenerator）
- 出力サイズは入力より大きい
- 式：`output_size = (input_size - 1) * stride - 2*padding + kernel_size + output_padding`

## 主な違い

1. **目的**：Conv2dは特徴を抽出して解像度を削減、ConvTranspose2dは再構成/生成して解像度を増加

2. **データフロー**：Conv2dは多対一（複数の入力位置→1つの出力位置）、ConvTranspose2dは一対多（1つの入力位置→複数の出力位置）

3. **一般的な使用例**：
   - Conv2d：CNN、encoder、特徴抽出
   - ConvTranspose2d：GAN、VAE、セマンティックセグメンテーション（アップサンプリングパス）、超解像、Diffusionモデルのdecoder

4. **チェッカーボードアーティファクト**：ConvTranspose2dは`kernel_size`が`stride`で割り切れない場合、チェッカーボードアーティファクトを生成する可能性があります
