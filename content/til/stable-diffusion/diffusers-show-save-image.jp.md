---
title: "Diffusersで画像を表示・保存する"
description: ""
date: 2025-02-23T9:00:00+09:00
lastmod:
draft: false
---

## 画像を表示・保存する

```python
from diffusers import StableDiffusionPipeline

model_id = "./my-model.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    model_id,
    torch_dtype=torch.float16)
pipe.to("cuda")

prompt = "a prompt for the model"
image = pipe(prompt).images[0]

# 画像を表示
image.show()

# 画像を保存
image.save("output.png")

# 画像を保存する別の方法
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
```
