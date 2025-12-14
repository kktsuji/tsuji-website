---
title: "Convert 1-channel Numpy Ndarray to 3-channel"
description: ""
date: 2025-02-21T22:00:00+09:00
lastmod:
draft: false
---

## By Using List or Tuple

This conversion can be used to convert a 1-channel grayscale image to a 3-channel RGB image.

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

## By Using copy()

```python
import numpy as np

one_ch = np.arange(0, 6).reshape((2, 3))

copies = [one_ch.copy() for _ in range(3)]
three_ch = np.stack(copies, axis=-1)
```
