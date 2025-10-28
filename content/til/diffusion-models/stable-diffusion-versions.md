---
title: 'Versions of Stable Diffusion'
description: ''
date: 2025-10-28T18:00:00+09:00
lastmod: 
math: true
draft: false
---

## Stable Diffusion v1.x (v1.1 to v1.4)

Stable Diffusion v1.x is the initial release of the Stable Diffusion model developed by CompVis (Ludwig Maximilian University of Munich), collaborating with Stability AI and Runway.

- Core: Latent Diffusion with a U-Net; CLIP ViT-L/14 text encoder.
- Native resolution: 512x512 pixels.
- Data: LAION subsets with aesthetics filtering.
- Hugging Face: [CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- GitHub: [CompVis/stable-diffusion](https://github.com/compvis/stable-diffusion)
- Paper: [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)

```python
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe.to("cuda")

image = pipe("A fantasy landscape, trending on artstation").images[0]
image.save("fantasy_landscape.png")
```

## Stable Diffusion 2.x (2.0, 2.1)

Stable Diffusion v2.x is an improved version of the original Stable Diffusion model, released by Stability AI.

- What changed vs 1.x:
  - New text encoder: OpenCLIP Vit-H/14 (different tokenization/semantics than v1.x).
  - Added 768x768 native model (alongside 512 variant).
  - Expanded official variants: depth-to-image, inpainting, x4 upscaler.
  - Stronger data filtering; prompt vocabulary shifted.
- Hugging Face: [stabilityai/stable-diffusion-2-1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)
- GitHub: [Stability-AI/stablediffusion](https://github.com/Stability-AI/stablediffusion)

```python
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base")
pipe.to("cuda")
```

## SDXL 1.0 (Base + Refiner)

Also released by Stability AI.

- Architecture:
  - Two stage diffusion processes (Base + Refiner).
  - "Ensemble of experts" pipeline: Base for coarse denoising + optional Refiner for final denoising step.
  - OpenCLIP ViT-G/14 + CLIP ViT-L/14 (two encoders)
- Native resolution: 1024x1024 pixels.
- Quality: Big jump in composition, color fidelity, photorealism, and prompt alignment vs 1.4/2.1.
- Trade-offs: Heavier and slower than prior versions.
- Hugging Face:
  - [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
  - [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)

## SDXL-Turbo

(by Stability AI)

- Difference from SDXL 1.0:
  - Single U-Net model (no separate Refiner).
  - Optimized for speed and cost-efficiency.
  - Slightly lower quality than SDXL 1.0 but still superior to v1.4/2.1.
  - A distilled version of SDXL 1.0 by using Adversarial Diffusion Distillation.
- Optimized around 512x512.
- Hugging Face: [stabilityai/stable-diffusion-xl-turbo-1.0](https://huggingface.co/stabilityai/sdxl-turbo)
- [Project Page](https://stability.ai/research/adversarial-diffusion-distillation)

## Stable Diffusion 3.x (3.0, 3.5)

(by Stability AI)

- Architecture: Diffusion Transformer (DiT) + flow matching.
- Strengths reported: Better multi-subject composition, improved spelling/text, and overall prompt adherence.
- Hugging Face:
  - [stabilityai/stable-diffusion-3-medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
  - [stabilityai/stable-diffusion-3.5-medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
- [Project Page](https://stability.ai/news/stable-diffusion-3-research-paper)
