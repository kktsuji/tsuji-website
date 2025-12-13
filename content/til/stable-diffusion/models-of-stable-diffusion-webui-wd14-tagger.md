---
title: "Models of stable-diffusion-webui-wd14-tagger"
description: ""
date: 2025-02-02T18:00:00+09:00
lastmod:
draft: false
---

## Models of stable-diffusion-webui-wd14-tagger

[picobyte/stable-diffusion-webui-wd14-tagger](https://github.com/picobyte/stable-diffusion-webui-wd14-tagger)[^1] uses two models to estimate the tags of an image:

1. [KichangKim/DeepDanbooru](https://github.com/KichangKim/DeepDanbooru?tab=readme-ov-file): an anime-style girl image tag estimation model trained on Danbooru images.
2. [SmilingWolf/wd-v1-4-moat-tagger](https://huggingface.co/SmilingWolf/wd-v1-4-moat-tagger-v2): Supports ratings, characters and general tags. Also trained on Danbooru images.

[^1]: Forked from archived project [toriato/stable-diffusion-webui-wd14-tagger](https://github.com/toriato/stable-diffusion-webui-wd14-tagger).
