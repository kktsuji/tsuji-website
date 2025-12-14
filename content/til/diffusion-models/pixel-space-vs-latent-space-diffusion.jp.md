---
title: "Diffusion Models: Pixel Space vs. Latent Space"
description: ""
date: 2025-10-27T20:00:00+09:00
lastmod:
math: true
draft: false
---

## Pixel Space vs. Latent Space

**Pixel Space Diffusion Model**は画像の生のピクセル値に直接作用します。これらは、ピクセルレベルの表現を段階的にノイズ除去することによって画像を生成することを学習します。

一方、**Latent Space Diffusion Model**は、Latentベクトルとして知られる画像の圧縮表現で動作します。これらのモデルは、最初にEncoder（Variational Autoencoder、VAEなど）を使用して画像を低次元のLatent Spaceにエンコードし、このLatent SpaceでDiffusionプロセスを実行し、次にDecoderを使用して生成されたLatentベクトルをPixel Spaceにデコードします。

## Latent Space Diffusion Modelのメリット

Latent space diffusion modelはpixel spaceモデルに比べていくつかの利点があります：

### 1. 計算効率

Latent space diffusion modelは一般的にpixel spaceモデルよりも計算効率が高くなります。

訓練画像サイズが512 x 512 x 3チャンネルの場合：

- Pixel spaceモデル：512 x 512 x 3 = 786,432ピクセル
- Latent spaceモデル：64 x 64 x 4 = 16,384 latent次元（8倍のダウンサンプリングとlatent spaceの4チャンネルを仮定）

この例では、latent spaceモデルはpixel spaceモデルと比較して1/48のデータを処理します。このデータサイズの削減により、メモリ使用量と計算リソースが大幅に節約され、訓練と推論時間が高速化され、より安価なGPUを使用できます。

### 2. Encoder、Diffusion Model、Decoderへの役割分担

Latent space diffusion modelは表現学習と生成モデリングのタスクを分離します。

- Encoder：画像から抽象的で本質的な特徴を抽出し、高レベルのセマンティクスをキャプチャします。
- Diffusion model：Latent spaceの本質的な特徴のみを使用して生成プロセスの学習に集中します。
- Decoder：抽象的なlatent表現から詳細なピクセルレベルの画像を再構築します。

例えば、猫の画像を生成する場合、encoderは「猫らしさ」の概念（形状、姿勢、テクスチャ）をキャプチャし、diffusion modelはlatent spaceでこの概念のバリエーションを生成します。その後、decoderはこれらのバリエーションを詳細なピクセル画像に変換します。

一方、pixel spaceモデルは低レベルの詳細と高レベルのセマンティクスを同時に学習する必要があり、これはより困難で効率が低くなる可能性があります。Pixel spaceモデルは各ピクセルを正確に生成する責任があります（例えば、猫の詳細な1本の毛）。

効率が高いだけでなく、デバッグも容易です。生成された画像に問題がある場合、どのコンポーネント（encoder、diffusion model、またはdecoder）が問題を引き起こしているかを調査できます。
