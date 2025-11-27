---
title: 'torch.nn.Conv2d vs torch.nn.ConvTranspose2d in Machine Learning'
description: ''
date: 2025-11-28T08:00:00+09:00
lastmod: 
math: true
draft: false
---

`torch.nn.Conv2d` and `torch.nn.ConvTranspose2d` are opposite operations:

## Conv2d (Standard Convolution)

- Reduces spatial dimensions (downsampling)
- Used for feature extraction
- Output size is smaller than input (unless padding compensates)
- Formula: `output_size = floor((input_size + 2*padding - kernel_size) / stride) + 1`

## ConvTranspose2d (Transposed Convolution / Deconvolution)

- Increases spatial dimensions (upsampling)
- Used for reconstruction/generation (e.g., decoder in autoencoders, generators in GANs)
- Output size is larger than input
- Formula: `output_size = (input_size - 1) * stride - 2*padding + kernel_size + output_padding`

## Key differences

1. **Purpose**: Conv2d extracts features and reduces resolution; ConvTranspose2d reconstructs/generates and increases resolution

2. **Data flow**: Conv2d: many-to-one (multiple input positions → one output position); ConvTranspose2d: one-to-many (one input position → multiple output positions)

3. **Common use cases**:
   - Conv2d: CNNs, encoders, feature extraction
   - ConvTranspose2d: GANs, VAEs, semantic segmentation (upsampling path), super-resolution, Diffusion model decoders

4. **Checkerboard artifacts**: ConvTranspose2d can produce checkerboard artifacts when `kernel_size` is not divisible by `stride`
