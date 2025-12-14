---
title: "Pythonにおけるパッケージとスクリプトの名前の競合"
description: ""
date: 2025-04-18T09:00:00+09:00
lastmod:
draft: false
---

## 名前の競合

Pythonスクリプトの名前は、スクリプト内で使用しているパッケージの名前と同じであってはなりません。そうでないと、競合が発生します。

```bash
pip install numpy
```

次に、`numpy.py`という名前のスクリプトを作成します。

```python
import numpy as np
print(np.array([1, 2, 3]))
```

スクリプトを実行すると、エラーが発生します。

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

スクリプト`numpy.py`は、競合を避けるために`execute_numpy.py`のように名前を変更する必要があります。
