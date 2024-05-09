---
title: 'Python Matplotlib インターフェース'
slug: 'python-matplotlib-interfaces'
description: 'python matplotlib のインターフェースについての Today I learned ポスト。'
date: 2024-04-02T21:47:42+09:00
lastmod: 
math: false
draft: false
---

## Reference

詳細は [公式 quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html) と [API interfaces](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html) を参照.

## Preparation

```bash
pip install -U pip
pip install matplotlib
```

## Coding style

Matplotlib には2種類のインターフェースが存在する。

* オブジェクト指向スタイル
  * もしくは、「オブジェクト指向インターフェース」、「明示的インターフェース」とも呼ばれる。
* pyplot スタイル
  * もしくは、「pyplot インターフェース」、「黙示的インターフェース」とも呼ばれる。
  * Python のインタラクティブモードやシンプルで短いスクリプト向け。

### オブジェクト指向スタイル

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# Option 1
fig, ax = plt.subplots()
ax.plot(data_x, data_y)

# Option 2 (option 1 と同じ)
fig = plt.figure()
ax = fig.subplots()
ax.plot(data_x, data_y)
```

### pyplot スタイル

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# Same as the OO-style
plt.plot(data_x, data_y)
```

![python-matplotlib-interfaces-img0](https://github.com/kktsuji/tsuji-website/assets/31529355/556b6e04-36b4-4dcc-9b1d-05630a8d0ded)

## Figure オブジェクトに複数の Axes オブジェクトが存在する場合

もし ``Figure`` オブジェクトが複数の ``Axes`` オブジェクトを保つ場合、黙示的な pyplot スタイルは実装が複雑となる。これはバグの温床となる可能性がある。

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# 黙示的インターフェース
# 1x2 行列で並んだの2つの Axes オブジェクトが Figure に生成される。
# pyplot インターフェースは、1つ目の axes を指す.
plt.subplot(1, 2, 1)
plt.plot(data_x, data_y)

# 2つ目へスイッチ
plt.subplot(1, 2, 2)
plt.plot(np.flipud(data_x), data_y) # x軸を反転

# 最初の axes へ軸ラベルのような何らかの要素を追加する場合、
# インターフェースの切り替えが必要
plt.subplot(1, 2, 1)
plt.xlabel('X-axis 0')

# 再度切り替える
plt.subplot(1, 2, 2)
plt.xlabel('X-axis 1')

# もしくは、以下の書き方も可能
for i in range(1, 3):
    plt.subplot(1, 2, i)
    plt.xlabel(f'X-axis {i- 1}')
```

一方、明示的なオブジェクト指向スタイルはよりシンプルに同じことを実装可能。

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# 明示的スタイル
fig, axs = plt.subplots(1, 2)

axs[0].plot(data_x, data_y)
axs[1].plot(np.flipud(data_x), data_y) # x軸を反転

axs[0].set_xlabel('X-axis 0')
axs[1].set_xlabel('X-axis 1')

# 同様に以下で書ける
for i in range(2):
    axs[i].set_xlabel(f'X-axis {i}')
```

![python-matplotlib-interfaces-img1](https://github.com/kktsuji/tsuji-website/assets/31529355/95d7a0e0-21e9-4474-b624-e2d5a0c7b8bf)

## 明示的インターフェースにおける "subplots()"

```python
import matplotlib.pyplot as plt

# fig: Figure オブジェクトのインスタンス
# ax: fig 上に描画される axex オブジェクトのインスタンス
fig, ax = plt.subplots()

# fig: Figure オブジェクトのインスタンス
# ax: fig 上に描画される 3x2 で並んだ axes オブジェクトのインスタンスのリスト
fig, axs = plt.subplots(3, 2)
```