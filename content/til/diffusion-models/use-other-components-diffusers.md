---
title: 'Use Other Components with Diffusers'
description: ''
date: 2025-10-29T08:00:00+09:00
lastmod: 
math: true
draft: false
---

In Diffusers, you can mix and match different pre-trained components (like the U-Net, VAE, and text encoder) from various models. This allow you to experiment with different combinations to see how they affect the generated images.

```python
import torch
from diffusers import StableDiffusionPipeline, AutoencoderKL

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Switch to better VAE for SD1.x
vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse")
pipe.vae = vae

pipe = pipe.to(device)

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("astronaut_rides_horse.png")
```
