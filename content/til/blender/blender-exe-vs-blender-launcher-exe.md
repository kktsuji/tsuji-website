---
title: 'blender.exe vs. blender-launcher.exe'
description: ''
date: 2024-11-29T9:00:00+09:00
lastmod: 
draft: false
---

There are two types of ``.exe`` files in blender portable (``.zip``) version.

- ``blender.exe``: The main execution file. The terminal window continues to appear while the blender app is running.
- ``blender-launcher.exe``: The wrapper of ``blender.exe`` to hide the terminal window. All command lien parameters will be passed to ``blender.exe``.

Results:

- ``blender.exe`` and ``blender-launcher.exe`` are functionally identical.
- Use ``blender-launcher.exe`` if you want to hide the terminal window while using blender app.

References:

- [Win: Add launcher to hide the console window flash - blender.org](https://projects.blender.org/blender/blender/commit/f3944cf503966a93a124e389d9232d7f833c0077)
- [Runnin Blender.exe vs. Blender-launcher.exe - blender.stackexchange.com](https://blender.stackexchange.com/questions/252438/runnin-blender-exe-vs-blender-launcher-exe)
