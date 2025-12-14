---
title: "WSLの設定ファイル"
description: ""
date: 2024-11-15T09:00:00+09:00
lastmod:
draft: false
---

2種類の設定ファイル：

- `.wslconfig`：すべてのWSL2ディストリビューションのグローバル設定。
  - `C://Users/user/.wslconfig`：Windows上
  - `/mnt/c/Users/user/.wslconfig`：WSL上
- `wsl.conf`：WSL1とWSL2の各ディストリビューションのローカル設定。
  - `/etc/wsl.conf`：WSL上

参考文献：

- [Advanced settings configuration in WSL - Microsoft](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
