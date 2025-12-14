---
title: "Diffusersのset_adapters()を使用してLoRAの重みを設定する"
description: ""
date: 2025-02-22T17:00:00+09:00
lastmod:
draft: false
---

## LoRAの重みを設定する

`set_adapters()`を使用してLoRAの重みを設定し、モデルに対するLoRAの影響を調整します。

```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "./my_model.safetensors"
seed = 0123

# モデルを読み込む
pipe = StableDiffusionPipeline.from_single_file(
    model_id,
    torch_dtype=torch.float16)
pipe.to("cuda")


lora_id = "./my_lora.safetensors"
adapter_name = "my_lora"
adapter_weight = 0.5

# LoRAを読み込む
pipe.load_lora_weights(lora_path, adapter_name=adapter_name)

# LoRAの重みを[0., 1.]の範囲で設定
pipe.set_adapters(adapter_name, adapter_weight)

prompt = "a prompt for the model"

image = pipe(
    prompt,
    generator = torch.Generator(device="cuda").manual_seed(seed)
).images[0]
```

## 参考文献

- [Load adapters - Diffusers, Hugging Face](https://huggingface.co/docs/diffusers/using-diffusers/loading_adapters)
