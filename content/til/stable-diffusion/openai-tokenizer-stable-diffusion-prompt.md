---
title: "OpenAI's Tokenizer for Stable Diffusion Prompts"
description: ""
date: 2025-09-07T16:00:00+09:00
lastmod:
draft: false
---

## OpenAI's Tokenizer for Stable Diffusion Prompts

[OpenAI's tokenizer](https://platform.openai.com/tokenizer) can be used to analyze how prompts for Stable Diffusion are tokenized.

It is useful to find the LoRA's trigger words and how many tokens are used for a given trigger word.

For example, the prompt:

- `xyz`: 1 token: `xyz`
- `1girl`: 2 tokens: `1`, `girl`
- `jGlt`: 3 tokens: `j`, `G`, `lt`
- `[xyz]`: 3 tokens: `[`, `xyz`, `]`
