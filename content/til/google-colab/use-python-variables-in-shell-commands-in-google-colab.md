---
title: 'Use Python Variables in Shell Commands in Google Colab'
description: 
date: 2025-02-03T20:00:00+09:00
lastmod: 
draft: false
---

## Use Python Variables in Shell Commands in Google Colab

```python
file_path = '/content/sample.txt'
!echo "Hello, World!" > {file_path}
!cat {file_path}
```
