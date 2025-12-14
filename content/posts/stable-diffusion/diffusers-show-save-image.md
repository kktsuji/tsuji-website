---
title: "Show and Save Image from Diffusers"
description: ""
date: 2025-02-23T9:00:00+09:00
lastmod:
draft: false
---

## Show and Save Image

```python
from diffusers import StableDiffusionPipeline

model_id = "./my-model.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    model_id,
    torch_dtype=torch.float16)
pipe.to("cuda")

prompt = "a prompt for the model"
image = pipe(prompt).images[0]

# Show the image
image.show()

# Save the image
image.save("output.png")

# Other way to save the image
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
```
