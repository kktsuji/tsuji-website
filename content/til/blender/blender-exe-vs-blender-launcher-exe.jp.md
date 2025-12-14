---
title: "blender.exe vs. blender-launcher.exe"
description: ""
date: 2024-11-29T9:00:00+09:00
lastmod:
draft: false
---

blenderのportable（`.zip`）版には2種類の`.exe`ファイルがある。

- `blender.exe`：メインの実行ファイル。blenderアプリの実行中、ターミナルウィンドウが表示され続ける。
- `blender-launcher.exe`：`blender.exe`のwrapperでターミナルウィンドウを非表示にする。すべてのコマンドラインパラメータは`blender.exe`に渡される。

結果：

- `blender.exe`と`blender-launcher.exe`は機能的に同一である。
- blenderアプリの使用中にターミナルウィンドウを非表示にしたい場合は`blender-launcher.exe`を使用する。

参考文献：

- [Win: Add launcher to hide the console window flash - blender.org](https://projects.blender.org/blender/blender/commit/f3944cf503966a93a124e389d9232d7f833c0077)
- [Runnin Blender.exe vs. Blender-launcher.exe - blender.stackexchange.com](https://blender.stackexchange.com/questions/252438/runnin-blender-exe-vs-blender-launcher-exe)
