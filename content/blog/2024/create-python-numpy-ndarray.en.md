---
title: 'Python Numpy Ndarray Creation'
description: 'Today I Learned post about python numpy ndarray.'
date: 2024-04-03T17:58:55+09:00
lastmod: 
math: false
draft: false
---

## Reference

For more details, see [numpy official api reference](https://numpy.org/doc/stable/reference/arrays.ndarray.html).

## Preparation

```bash
pip install -U pip
pip install numpy
```

## Creation methods

A n-dimensional array ([ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#)) is the most important and basic class in numpy. It has a constructor but its elements will not be initialized.

```python
# Interactive mode
python

>>> import numpy as n

>>> np.ndarray(3)
array([0.e+000, 5.e-324, 1.e-323]) # random values

# An array of 3x2
>>> np.ndarray((3, 2))
array([[0.0e+000, 4.9e-324],
       [9.9e-324, 1.5e-323],
       [2.0e-323, 2.5e-323]]) # random values
```


[array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array) is an useful interface to create a ndarray object. It can recieve an array object and elements will be initialized by it.


```python
# Interactive mode
python

>>> import numpy as n

# Create an array
>>> np.array([0, 1, 2])
array([0, 1, 2])

# An array of 2x3
>>> np.array([[0, 1, 2], [3, 4, 5]])
array([[0, 1, 2],
       [3, 4, 5]])

# Type provided
>>> np.array([0, 1, 2], dtype=float)
array([0., 1., 2.])
```

[zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros), [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones), [full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full) are also aften used.

zeros:
```python
# Interactive mode
python

>>> import numpy as n

# Create an array of zeros
# Default dtype is numpy.float64
>>> np.zeros(2)
array([0., 0.])

# Type provided
>>> np.zeros((2, 3), dtype=int)
array([[0, 0, 0],
       [0, 0, 0]])
```

ones:
```python
# Create an array of zeros
# Default dtype is numpy.float64
>>> np.ones(2)
array([1., 1.])

# Type provided
>>> np.ones((2, 3), dtype=np.int8)
array([[1, 1, 1],
       [1, 1, 1]], dtype=int8)
```

full:
```python
# Create an array filled with given value
>>> np.full(2, 100)
array([100, 100])

>>> np.full((2, 3), np.inf)
array([[inf, inf, inf],
       [inf, inf, inf]])

>>> np.full((2, 3), [0, 1, 2])
array([[0, 1, 2],
       [0, 1, 2]])
```

array_like interfaces ([zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like), [ones_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like) and [full_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like)) create an array with the same shape and type as a given array.

zeros_like:

```python
# Interactive mode
python

>>> import numpy as n

>>> a = np.array([0, 1, 2], dtype=np.float64)
>>> a
array([0., 1., 2.])

>>> a.dtype
dtype('float64')



>>> np.zeros_like(a)
array([0., 0., 0.])

>>> np.zeros_like(a).dtype
dtype('float64')
```

ones_like:
```python
>>> np.ones_like(a)
array([1., 1., 1.])

>>> np.ones_like(a).dtype
dtype('float64')
```

full_like:
```python
>>> np.full_like(a, 100)
array([100., 100., 100.])

>>> np.full_like(a, 100).dtype
dtype('float64')
```