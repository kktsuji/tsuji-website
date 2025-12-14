---
title: "Training StepsにおけるDynamic Weights"
description: ""
date: 2025-10-21T09:00:00+09:00
lastmod:
draft: false
math: true
---

## Training中のDynamic Weights

Training stepsにわたってdynamic weightsを計算する方法は多数ある。

Linear: $w_t = w \cdot \frac{t}{T}$

Cosine: $w_t = w \cdot \frac{1 - \cos(\frac{\pi t}{T})}{2}$

Power: $w_t = w \cdot \left(\frac{t}{T}\right)^a$

Exponential: $w = w \cdot \left(1 - e^{-\frac{t}{T/4}}\right)$

ここで：

- $w_t$: training step $t$でのweight
- $w$: 最大weight
- $T$: 総training steps
- $a$: power factor

![img](https://img.tsuji.tech/dynamic-weights-over-training-steps-0.jpg)

## サンプルコード

GitHub gistをクローンする：

```bash
git clone https://gist.github.com/07666bb618956213b812c1b357485391.git
```

または次のコードスニペットを使用する：

```python
import numpy as np
import matplotlib.pyplot as plt


def _get_function_dynamic_weight_method(method: str):
    if method == "linear":
        return lambda step, total_steps, base_weight: base_weight * (step / total_steps)
    elif method == "cosine":
        return (
            lambda step, total_steps, base_weight: base_weight
            / 2
            * (1 - np.cos(np.pi * step / total_steps))
        )
    elif method == "power":
        return lambda step, total_steps, base_weight, a=2: base_weight * (
            (step / total_steps) ** a
        )
    elif method == "exponential":
        return lambda step, total_steps, base_weight: base_weight * (
            1 - np.exp(-step / (total_steps / 4))
        )
    else:
        raise ValueError(f"Unknown method: {method}")


def _calculate_dynamic_weight(
    method: str,
    base_weight: float,
    total_steps: int,
    a: float = 2,
):
    weight_func = _get_function_dynamic_weight_method(method)
    steps = np.arange(total_steps + 1)
    weights = (
        [weight_func(step, total_steps, base_weight, a) for step in steps]
        if method == "power"
        else [weight_func(step, total_steps, base_weight) for step in steps]
    )

    return weights


if __name__ == "__main__":
    linear_weights = _calculate_dynamic_weight(
        method="linear", base_weight=1.0, total_steps=100
    )
    cosine_weights = _calculate_dynamic_weight(
        method="cosine", base_weight=1.0, total_steps=100
    )
    power_weights = _calculate_dynamic_weight(
        method="power", base_weight=1.0, total_steps=100
    )
    exponential_weights = _calculate_dynamic_weight(
        method="exponential", base_weight=1.0, total_steps=100
    )

    plt.figure(figsize=(10, 6))
    plt.plot(linear_weights, label="Linear", color="blue")
    plt.plot(cosine_weights, label="Cosine", color="orange")
    plt.plot(power_weights, label="Power", color="green")
    plt.plot(exponential_weights, label="Exponential", color="red")
    plt.title("Dynamic Weights Over Training Steps")
    plt.xlabel("Training Steps")
    plt.ylabel("Weight")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("dynamic_weights.jpg", bbox_inches="tight")
    plt.show()
```
