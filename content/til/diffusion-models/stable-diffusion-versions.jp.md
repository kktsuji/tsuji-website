---
title: "Stable Diffusionのバージョン"
description: ""
date: 2025-10-28T18:00:00+09:00
lastmod:
math: true
draft: false
---

## Stable Diffusion v1.x（v1.1からv1.4）

Stable Diffusion v1.xは、CompVis（ルートヴィヒ・マクシミリアン大学ミュンヘン）がStability AIおよびRunwayと協力して開発したStable Diffusionモデルの最初のリリースです。

- コア：U-Netを使用したLatent Diffusion、CLIP ViT-L/14テキストエンコーダー。
- ネイティブ解像度：512x512ピクセル。
- データ：美的フィルタリングを伴うLAIONサブセット。
- Hugging Face：[CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- GitHub：[CompVis/stable-diffusion](https://github.com/compvis/stable-diffusion)
- 論文：[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)

```python
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe.to("cuda")

image = pipe("A fantasy landscape, trending on artstation").images[0]
image.save("fantasy_landscape.png")
```

## Stable Diffusion 2.x（2.0、2.1）

Stable Diffusion v2.xは、Stability AIによってリリースされた元のStable Diffusionモデルの改良版です。

- v1.xとの変更点：
  - 新しいテキストエンコーダー：OpenCLIP Vit-H/14（v1.xとは異なるトークン化/セマンティクス）。
  - 768x768ネイティブモデルを追加（512バリアントと並行）。
  - 公式バリアントを拡張：depth-to-image、inpainting、x4 upscaler。
  - より強力なデータフィルタリング、プロンプト語彙がシフト。
- Hugging Face：[stabilityai/stable-diffusion-2-1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)
- GitHub：[Stability-AI/stablediffusion](https://github.com/Stability-AI/stablediffusion)

## SDXL 1.0（BaseとRefiner）

Stability AIによってもリリースされました。

- アーキテクチャ：
  - 2段階のdiffusionプロセス（BaseとRefiner）。
  - "Ensemble of experts"パイプライン：粗いdenoising用のBaseとオプションの最終denoising step用のRefiner。
  - OpenCLIP ViT-G/14とCLIP ViT-L/14（2つのエンコーダー）
- ネイティブ解像度：1024x1024ピクセル。
- 品質：v1.4/2.1と比較して、構成、色の忠実度、フォトリアリズム、プロンプト整合性が大幅に向上。
- トレードオフ：以前のバージョンよりも重く、遅い。
- Hugging Face：
  - [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
  - [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)

## SDXL-Turbo

（Stability AI）

- SDXL 1.0との違い：
  - 単一のU-Netモデル（個別のRefinerなし）。
  - 速度とコスト効率のために最適化。
  - SDXL 1.0よりもわずかに品質が低いが、v1.4/2.1よりも優れている。
  - Adversarial Diffusion Distillationを使用したSDXL 1.0の蒸留版。
- 512x512付近で最適化。
- Hugging Face：[stabilityai/stable-diffusion-xl-turbo-1.0](https://huggingface.co/stabilityai/sdxl-turbo)
- [プロジェクトページ](https://stability.ai/research/adversarial-diffusion-distillation)

## Stable Diffusion 3.x（3.0、3.5）

（Stability AI）

- アーキテクチャ：Diffusion Transformer（DiT）とflow matching。
- 報告された強み：複数被写体の構成の改善、スペル/テキストの改善、全体的なプロンプト順守の改善。
- Hugging Face：
  - [stabilityai/stable-diffusion-3-medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
  - [stabilityai/stable-diffusion-3.5-medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
- [プロジェクトページ](https://stability.ai/news/stable-diffusion-3-research-paper)
