---
title: 'Sigmoid Function'
description: ''
date: 2024-12-05T9:00:00+09:00
lastmod: 
draft: false
math: true
---

## Sigmoid Function

$ S(x) = \dfrac{1}{1 + e^{ax}} = \dfrac{\tanh(ax/2) + 1}{2} $

Where $ a $ is a gain.

In the context of artificial neural network, the sigmoid function is a synonym for the logistics function.

The [softmax function](https://tsuji.tech/softmax-function/) is a smooth approximation of one-hot arg max of the sigmoid function.

## Standard Sigmoid Function

$ S(x) = \dfrac{1}{1 + e^x} = \dfrac{\tanh(x/2) + 1}{2} $

Where gain $ a $ is 1.

The inverse of the standard sigmoid function is the logit function.

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

## References

- [Sigmoid Function - wiki](https://en.m.wikipedia.org/wiki/Sigmoid_function)
