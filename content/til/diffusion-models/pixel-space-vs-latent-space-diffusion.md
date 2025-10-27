---
title: 'Diffusion Models: Pixel Space vs. Latent Space'
description: ''
date: 2025-10-27T20:00:00+09:00
lastmod: 
math: true
draft: false
---

## Pixel Space vs. Latent Space

**Pixel space diffusion models** operate directly on the raw pixel values of images. They learn to generate images by progressively denoising pixel-level representations.

On the other hand, **latent space diffusion models** work on compressed representations of images, known as latent vectors. These models first encode images into a lower-dimensional latent space using an encoder (like a variational autoencoder; VAE), perform the diffusion process in this latent space, and then decode the generated latent vectors back into pixel space using a decoder.

## Merits of Latent Space Diffusion Models

The latent space diffusion models have several advantages over pixel space ones:

### 1. Computational Efficiency

Latent space diffusion models are generally more computationally efficient than pixel space models.

If training image size is 512 x 512 x 3 channels:

- Pixel space model: 512 x 512 x 3 = 786,432 pixels
- Latent space model: 64 x 64 x 4 = 16,384 latent dimensions (assuming a 8x downsampling and 4 channels in latent space)

In this example, the latent space model processes 1 / 48th of the data compared to the pixel space model. This reduction in data size leads to significant savings in memory usage and computational resources, allowing for faster training and inference times, and using cheaper GPUs.

### 2. Split Roles into Encoder, Diffusion Model, and Decoder

Latent space diffusion models separate the tasks of representation learning and generative modeling.

- The encoder: Extracts abstract and essential features from images, capturing high-level semantics.
- The diffusion model: Focuses on learning the generative process with only the essential features in the latent space.
- The decoder: Reconstructs the detailed pixel-level images from the abstract latent representations.

For example, in generating a cat image, the encoder captures the concept of "catness" (shape, posture, texture) while the diffusion model generates variations of this concept in latent space. The decoder then translates these variations back into detailed pixel images.

On the other hand, pixel space models must learn both low-level details and high-level semantics simultaneously, which can be more challenging and less efficient. Pixel space models are responsible for generating every pixel accurately (for example, a detailed single hair of the cat).
