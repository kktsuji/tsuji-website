---
title: "Diffusersのfrom_single_file()で単一のDiffusionモデルファイルをロードする"
description: ""
date: 2025-02-19T22:00:00+09:00
lastmod:
draft: false
---

## Diffusersのfrom_single_file()

`from_pretrained()`の代わりに`from_single_file()`を使用して、単一ファイルからDiffusionモデルを読み込みます。

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

## 参考文献

- [Single Files - diffusers API, Hugging Face](https://huggingface.co/docs/diffusers/api/loaders/single_file)
