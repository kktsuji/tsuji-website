---
title: "Stable DiffusionプロンプトのためのOpenAI Tokenizer"
description: ""
date: 2025-09-07T16:00:00+09:00
lastmod:
draft: false
---

## OpenAIのTokenizerでStable Diffusionプロンプトを解析する

[OpenAIのtokenizer](https://platform.openai.com/tokenizer)を使用して、Stable Diffusionのプロンプトがどのようにトークン化されるかを分析できます。

LoRAのトリガーワードを見つけたり、特定のトリガーワードに使用されるトークン数を確認するのに便利です。

例えば、プロンプトは以下のようにトークン化されます：

- `xyz`：1トークン：`xyz`
- `1girl`：2トークン：`1`、`girl`
- `jGlt`：3トークン：`j`、`G`、`lt`
- `[xyz]`：3トークン：`[`、`xyz`、`]`
