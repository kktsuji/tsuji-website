---
title: 'Use Diffusers from_single_file() to Load Single Diffusion Model Files'
description: ''
date: 2025-02-19T22:00:00+09:00
lastmod: 
draft: false
---

## Diffusers from_single_file()

Use `from_single_file()` to load a diffusion model from a single file instead of `from_pretrained()`.

```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "./my-model.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    model_id,
    torch_dtype=torch.float16)
pipe.to("cuda")

prompt = "a prompt for the model"
image = pipe(prompt).images[0]
```

## Reference

- [Single Files - diffusers API, Hugging Face](https://huggingface.co/docs/diffusers/api/loaders/single_file)
