---
title: "Epochs vs. Global Steps in Training AI Models"
description: ""
date: 2025-10-25T12:00:00+09:00
lastmod:
math: true
draft: false
---

## Epochs

- One complete pass through the entire training dataset
- If you have 100 training samples and set batch size to 1, 1 epoch means the model processes all 100 samples once
- If you have 100 training samples and set batch size to 10, it takes 10 iterations to complete 1 epoch

## Global Steps

- One global step refers to a single update of the model's parameters (weights update)
- Typically, one global step corresponds to processing a single batch, since the model’s weights are usually updated after each batch.
- The number of global steps depends on the batch size and the number of epochs

## Relationship Between Epochs and Global Steps

The relationship can be summarized with the formula:

$$
\text{Global Steps} = \frac{\text{Number of Samples}}{\text{Batch Size}} \times \text{Number of Epochs}
$$

If the dataset size is not divisible by the batch size (or you count the final partial batch), use the ceiling:

$$
\text{Global Steps} = \left\lceil\frac{\text{Number of Samples}}{\text{Batch Size}}\right\rceil \times \text{Number of Epochs}
$$

(Behavior can vary if a framework drops the last partial batch)
