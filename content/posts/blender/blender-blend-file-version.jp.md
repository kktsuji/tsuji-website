---
title: "Blender .blendファイルのバージョン"
description: ""
date: 2024-11-22T9:00:00+09:00
lastmod:
draft: false
---

1. `blender.exe`を実行
2. `*.blend`ファイルを開く
3. BlenderのGUIでScriptingタブを開く
4. 以下のpythonコマンドを実行：

```python
import bpy
bpy.data.version
```
