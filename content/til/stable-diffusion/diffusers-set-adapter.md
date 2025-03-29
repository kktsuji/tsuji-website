---
title: 'Use Diffusers set_adapters() to Set LoRA Weight'
description: ''
date: 2025-02-22T17:00:00+09:00
lastmod: 
draft: false
---

## Set LoRA Weight

Use `set_adapters()` to set the LoRA weight for adjusting the effect LoRA has on a model.

```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "./my_model.safetensors"
seed = 0123

# Load the model
pipe = StableDiffusionPipeline.from_single_file(
    model_id,
    torch_dtype=torch.float16)
pipe.to("cuda")


lora_id = "./my_lora.safetensors"
adapter_name = "my_lora"
adapter_weight = 0.5

# Load the LoRA
pipe.load_lora_weights(lora_path, adapter_name=adapter_name)

# Set the LoRA weight in range [0., 1.]
pipe.set_adapters(adapter_name, adapter_weight)

prompt = "a prompt for the model"

image = pipe(
    prompt,
    generator = torch.Generator(device="cuda").manual_seed(seed)
).images[0]
```

## Reference

- [Load adapters - Diffusers, Hugging Face](https://huggingface.co/docs/diffusers/using-diffusers/loading_adapters)
