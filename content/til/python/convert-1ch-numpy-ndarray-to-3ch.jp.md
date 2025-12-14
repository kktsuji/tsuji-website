---
title: "1チャンネルのNumpy Ndarrayを3チャンネルに変換する"
description: ""
date: 2025-02-21T22:00:00+09:00
lastmod:
draft: false
---

## ListまたはTupleを使用する

この変換は、1チャンネルのグレースケール画像を3チャンネルのRGB画像に変換するために使用できます。

```python
import numpy as np

# Create a 1ch ndarray
one_ch = np.arange(0, 6).reshape((2, 3))

print(one_ch)
# [[0 1 2]
#  [3 4 5]]

print(one_ch.shape)
# (2, 3)
# [[0 1 2]


# Convert 1ch to 3ch by using list
three_ch = np.stack([one_ch] * 3, axis=-1)
# or by using tuple
three_ch = np.stack((one_ch,) * 3, axis=-1)

print(three_ch)
# [[[0 0 0]
#   [1 1 1]
#   [2 2 2]]

#  [[3 3 3]
#   [4 4 4]
#   [5 5 5]]]

print(three_ch.shape)
# (2, 3, 3)
```

## copy()を使用する

```python
import numpy as np

one_ch = np.arange(0, 6).reshape((2, 3))

copies = [one_ch.copy() for _ in range(3)]
three_ch = np.stack(copies, axis=-1)
```
