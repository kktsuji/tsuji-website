---
title: "Rotate Python Numpy NDArray"
description: ""
date: 2024-11-20T09:00:00+09:00
lastmod:
draft: false
---

## Numpy rot90()

```python
# Interactive mode
python

>>> import numpy as n

# Create an array
>>> np.array([0, 1, 2])
array([0, 1, 2])

# An array of 2x3
>>> tmp = np.array([[0, 1, 2], [3, 4, 5]])

>>> tmp
array([[0, 1, 2],
       [3, 4, 5]])

# Rotate ndarray 90 degrees in the counterclockwise direction
>>> np.rot90(tmp)
array([[2, 5],
       [1, 4],
       [0, 3]])

# Option k: number of rotations (90 * k)
>>> np.rot90(tmp, k=2)
array([[5, 4, 3],
       [2, 1, 0]])
```

## OpenCV rotate()

```python
# Interactive mode
python

>>> import cv2

>>> img = cv2.imread('path_to_image.jpg')

# Rotate image (ndarray) 90 degrees in the clockwise direction
#   - cv2.ROTATE_90_CLOCKWISE
#   - cv2.ROTATE_90_COUNTERCLOCKWISE
#   - cv2.ROTATE_180
>>> cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
```

References:

- [numpy.rot90()](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html)
- [cv2.rotate()](https://docs.opencv.org/4.0.1/d2/de8/group__core__array.html#ga4ad01c0978b0ce64baa246811deeac24)
