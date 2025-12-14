---
title: "Sigmoid Function (Logistics Function)"
description: ""
date: 2024-12-05T9:00:00+09:00
lastmod:
draft: false
math: true
---

## Sigmoid Function

$ S(x) = \dfrac{1}{1 + e^{ax}} = \dfrac{\tanh(ax/2) + 1}{2} $

ここで、$ a $はgainである。

Artificial neural networkのコンテキストでは、sigmoid functionはlogistics functionの同義語である。

[Softmax function](https://tsuji.tech/softmax-function/)はsigmoid functionのone-hot arg maxの滑らかな近似である。

## Standard Sigmoid Function

$ S(x) = \dfrac{1}{1 + e^x} = \dfrac{\tanh(x/2) + 1}{2} $

ここで、gain $ a $は1である。

Standard sigmoid functionの逆関数はlogit関数である。

## Python Script

```python
import matplotlib.pyplot as plt
import numpy as np

# Sigmoid function
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# Generate x values
x = np.linspace(-10, 10, 100)

# Calculate corresponding y values
y = sigmoid(x)

# Create the plot
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.title("Sigmoid Function")
plt.grid(True)

# Save the plot to storage
plt.savefig('./sigmoid_function.jpg')

# Display the plot
plt.show()
```

![img](https://img.tsuji.tech/sigmoid_function.jpg)

## 参考文献

- [Sigmoid Function - wiki](https://en.m.wikipedia.org/wiki/Sigmoid_function)
- [Logistics Function - wiki](https://en.wikipedia.org/wiki/Logistic_function)
