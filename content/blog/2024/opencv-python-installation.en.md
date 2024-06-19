---
title: 'opencv-python Installation'
description: 'Today I Learned post about how to install opencv-python.'
date: 2024-03-31T16:42:17+09:00
lastmod: 
math: false
draft: false
---

## Reference

For more details, see [official github repository](https://github.com/opencv/opencv-python).

## Preparation

If previous or other opencv version (= not installed via ``pip``) are installed in the environment, please uninstall it to avoid conflict.

Upgrade ``pip`` version if it's lower than the minimum supported version 19.3.

```bash
pip -V
pip install -U pip
```

## Installation

There are four options to install opencv-python via pip.

**Note:** only one option can be chosen. If multiple diifferent packages are installed simultaneously in a single environment, the extra ones should be uninstalled with like ``pip uninstall opencv-python``. This is because all 4 packages use same namespace ``cv2``.

For standard desktop environments (Windows, macOS, almost any GNU/Linux distribution):

```bash
# 1. Main modules package
pip install opencv-python

# 2. Full package (contains both main modules and contrib/extra modules)
pip install opencv-contrib-python
```

For server (headless) environments (such as Docker, cloud environments etc., no GUI library dependencies):

```bash
# 3. Headless main modules package
pip install opencv-python-headless

# 4. Headless full package (contains both main modules and contrib/extra modules)
opencv-contrib-python-headless
```