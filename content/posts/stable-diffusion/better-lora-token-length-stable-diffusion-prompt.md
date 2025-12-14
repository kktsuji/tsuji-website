---
title: "Better LoRA Token Length in Stable Diffusion Prompts"
description: ""
date: 2025-10-17T8:30:00+09:00
lastmod:
draft: false
---

Supported to generated contents by Claude Sonnet 4.

## Better LoRA Token Length in Stable Diffusion Prompts

The fewer tokens for LoRA (Low-Rank Adaptation) trigger words in Stable Diffusion prompts, the better the performance.

- 1 token:
  - Lower learning complexity
  - More efficient training
  - Probably conflict to other tokens which means existing concepts
- 2 tokens:
  - Balanced learning complexity
  - Moderate training efficiency
  - Reduced conflict with existing concepts
- 3 tokens or more:
  - Higher learning complexity
  - Less efficient training
  - Fewer conflicts with existing concepts
