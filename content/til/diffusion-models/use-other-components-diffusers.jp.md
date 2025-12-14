---
title: "Diffusersで他のコンポーネントを使用する"
description: ""
date: 2025-10-29T08:00:00+09:00
lastmod:
math: true
draft: false
---

Diffusersでは、さまざまなモデルの異なる事前学習済みコンポーネント（U-Net、VAE、テキストエンコーダーなど）を組み合わせることができます。これにより、異なる組み合わせを実験して、生成される画像にどのような影響を与えるかを確認できます。

```python
import torch
from diffusers import StableDiffusionPipeline, AutoencoderKL

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# SD1.x用のより良いVAEに切り替え
vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse")
pipe.vae = vae

pipe = pipe.to(device)

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("astronaut_rides_horse.png")
```
