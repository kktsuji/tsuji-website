---
title: 'WSL Config Files'
description: ''
date: 2024-11-15T09:00:00+09:00
lastmod:
draft: false
---

Two types of config files:

- ``.wslconfig``: Global settings of all WSL2 distributions.
  - ``C://Users/user/.wslconfig``: on Windows
  - ``/mnt/c/Users/user/.wslconfig``: on WSL
- ``wsl.conf``: Local settings of each distribution of WSL1 and WSL2.
  - ``/etc/wsl.conf``: on WSL

Reference:

- [Advanced settings configuration in WSL - Microsoft](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
