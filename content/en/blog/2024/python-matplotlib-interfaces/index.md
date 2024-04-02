---
title: 'Python Matplotlib Interfaces'
slug: 'python-matplotlib-interfaces'
description: 'Today I learned post about python matplotlib interfaces.'
date: 2024-04-02T21:47:42+09:00
lastmod: 
math: false
tocOpen: true
draft: false
---

## Reference

For more details, see [official quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html) and [API interfaces](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html).

## Preparation

```bash
pip install -U pip
pip install matplotlib
```

## Coding style

There 2 styles for get starting matplotlib.

* An "object-oriented" (OO) style
  * Also called an OO interface or an explicit interface.
* A "pyplot" style
  * Also called a pyplot interface or an implicit interface.
  * For interactive mode or short simple scripts.

### The OO-style is below:

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

### The pyplot style is below:

```python
import matplotlib.pyplot as plt
import numpy as np

data_x = np.array([0, 1, 2, 3, 4])
data_y = np.array([1, 2, 3, 5, 8])

# Same as the OO-style
plt.plot(data_x, data_y)
```

## Multiple Axes opjects in a Figure object

If a ``Figure`` object has multiple ``Axes`` objects, the implicit pyplot style is complecated. It could cause bug.

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

On the other hand, the explicit OO interface is much simpler to do same thing.

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

## "subplots()" in the explicit interface

```python
import matplotlib.pyplot as plt

# fig: a instance of the Figure object
# ax: a instance of the Axes object in the fig
fig, ax = plt.subplots()

# fig: a instance of the Figure object
# ax: a list of the Axes objects with 3 rows and 2 columns in the fig
fig, axs = plt.subplots(3, 2)
```
