---
title: "PythonのMatplotlibインターフェース"
description: "PythonのMatplotlibインターフェースについてのメモ。"
date: 2024-04-02T21:47:42+09:00
lastmod:
draft: false
---

## リファレンス

詳細は[公式クイックスタートガイド](https://matplotlib.org/stable/users/explain/quick_start.html)と[APIインターフェース](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html)を参照してください。

## 準備

```bash
pip install -U pip
pip install matplotlib
```

## コーディングスタイル

matplotlibを始めるには2つのスタイルがあります。

- オブジェクト指向（OO）スタイル
  - OOインターフェースまたは明示的インターフェースとも呼ばれます。
- pyplotスタイル
  - pyplotインターフェースまたは暗黙的インターフェースとも呼ばれます。
  - 対話モードまたは短い簡単なスクリプト用。

### OOスタイルは以下の通りです:

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# Option 1
fig, ax = plt.subplots()
ax.plot(data_x, data_y)

# Option 2 (same as option 1)
fig = plt.figure()
ax = fig.subplots()
ax.plot(data_x, data_y)
```

### pyplotスタイルは以下の通りです:

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# Same as the OO-style
plt.plot(data_x, data_y)
```

![img](https://img.tsuji.tech/python-matplotlib-interfaces-0.jpg)

## Figureオブジェクト内の複数のAxesオブジェクト

`Figure`オブジェクトが複数の`Axes`オブジェクトを持つ場合、暗黙的なpyplotスタイルは複雑です。バグを引き起こす可能性があります。

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# The implicit interface
# Two axes objects with one row and two columns
# was generated in a figure.
# The pyplot interface refers to the first axes.
plt.subplot(1, 2, 1)
plt.plot(data_x, data_y)

# Switch to the second one.
plt.subplot(1, 2, 2)
plt.plot(np.flipud(data_x), data_y) # Invert x-axis

# The interface needs to switch to the first axes again
# when adding some elements like a xlabel to it.
plt.subplot(1, 2, 1)
plt.xlabel('X-axis 0')

# Switch again
plt.subplot(1, 2, 2)
plt.xlabel('X-axis 1')

# Other way of writing
for i in range(1, 3):
    plt.subplot(1, 2, i)
    plt.xlabel(f'X-axis {i- 1}')
```

一方、明示的なOOインターフェースは同じことを行うのがはるかに簡単です。

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# The explicit style
fig, axs = plt.subplots(1, 2)

axs[0].plot(data_x, data_y)
axs[1].plot(np.flipud(data_x), data_y) # Invert x-axis

axs[0].set_xlabel('X-axis 0')
axs[1].set_xlabel('X-axis 1')

# Other way
for i in range(2):
    axs[i].set_xlabel(f'X-axis {i}')
```

![img](https://img.tsuji.tech/python-matplotlib-interfaces-1.jpg)

## 明示的インターフェースにおける「subplots()」

```python
import matplotlib.pyplot as plt

# fig: a instance of the Figure object
# ax: a instance of the Axes object in the fig
fig, ax = plt.subplots()

# fig: a instance of the Figure object
# ax: a list of the Axes objects with 3 rows and 2 columns in the fig
fig, axs = plt.subplots(3, 2)
```
