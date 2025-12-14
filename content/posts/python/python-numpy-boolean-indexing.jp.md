---
title: "PythonのNumpyブーリアンインデックス"
description: ""
date: 2024-12-19T18:00:00+09:00
lastmod:
draft: false
---

## ブーリアン配列インデックス

```python
import numpy as np

# Create a 2D array
array_2d = np.array([[0, -1, 2], [-3, 4, -5]])

# Replace elements less than or equal to 0 with 0
array_2d[array_2d <= 0] = 0

print(array_2d)
# [[0 0 2]
#  [0 4 0]]
```

## リファレンス

- [Numpyユーザーガイド](https://numpy.org/doc/stable/user/basics.indexing.html)
