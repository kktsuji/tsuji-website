---
title: "stable-diffusion-webui-wd14-taggerのモデル"
description: ""
date: 2025-02-02T18:00:00+09:00
lastmod:
draft: false
---

## stable-diffusion-webui-wd14-taggerのモデル

[picobyte/stable-diffusion-webui-wd14-tagger](https://github.com/picobyte/stable-diffusion-webui-wd14-tagger)[^1]は、画像のタグを推定するために2つのモデルを使用します：

1. [KichangKim/DeepDanbooru](https://github.com/KichangKim/DeepDanbooru?tab=readme-ov-file)：Danbooruの画像で学習されたアニメスタイルの女の子の画像タグ推定モデル。
2. [SmilingWolf/wd-v1-4-moat-tagger](https://huggingface.co/SmilingWolf/wd-v1-4-moat-tagger-v2)：レーティング、キャラクター、一般的なタグをサポート。こちらもDanbooruの画像で学習されています。

[^1]: アーカイブされたプロジェクト[toriato/stable-diffusion-webui-wd14-tagger](https://github.com/toriato/stable-diffusion-webui-wd14-tagger)からフォークされました。
