---
title: "AIモデル訓練におけるEpoch vs. Global Steps"
description: ""
date: 2025-10-25T12:00:00+09:00
lastmod:
math: true
draft: false
---

## Epochs

- 訓練データセット全体を1回完全にパスすること
- 100個の訓練サンプルがあり、batch sizeを1に設定した場合、1 epochはモデルが全100サンプルを1回処理することを意味する
- 100個の訓練サンプルがあり、batch sizeを10に設定した場合、1 epochを完了するのに10回のiterationsが必要

## Global Steps

- 1 global stepはモデルのパラメータ（weights update）の1回の更新を指す
- 通常、1 global stepは単一batchの処理に対応する。なぜならモデルのweightsは通常各batch後に更新されるため
- global stepsの数はbatch sizeとepochs数に依存する

## EpochsとGlobal Stepsの関係

この関係は次の式で要約できる：

$$
\text{Global Steps} = \frac{\text{Number of Samples}}{\text{Batch Size}} \times \text{Number of Epochs}
$$

データセットサイズがbatch sizeで割り切れない場合（または最後の部分的なbatchをカウントする場合）、ceilingを使用する：

$$
\text{Global Steps} = \left\lceil\frac{\text{Number of Samples}}{\text{Batch Size}}\right\rceil \times \text{Number of Epochs}
$$

（frameworkが最後の部分的なbatchを削除する場合、動作が異なる可能性がある）
