---
title: 'Name Conflict: Package and Script in Python'
description: ''
date: 2025-04-18T09:00:00+09:00
lastmod: 
draft: false
---

## Name Conflict

Name of Python script must not be the same as the name of the package you are using in the script. Otherwise, it will cause a conflict.

```bash
pip install numpy
```

Then, create a script named ``numpy.py``.

```python
import numpy as np
print(np.array([1, 2, 3]))
```

When you run the script, it will raise an error.

```bash
python numpy.py

# or
python -c "import numpy as np; print(np.array([1, 2, 3]))"

# Traceback (most recent call last):
#   File "/home/xxx/python-sandbox/numpy.py", line 1, in <module>
#     import numpy as np
#   File "/home/xxx/python-sandbox/numpy.py", line 3, in <module>
#     print(np.array([1, 2, 3]))
#           ^^^^^^^^
# AttributeError: partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import)
```

The script ``numpy.py`` must be renamed like ``execute_numpy.py`` to avoid the conflict.
