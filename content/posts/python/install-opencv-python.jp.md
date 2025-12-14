---
title: "opencv-pythonをインストールする"
description: "opencv-pythonのインストール方法についてのメモ。"
date: 2024-03-31T16:42:17+09:00
lastmod:
draft: false
---

## リファレンス

詳細は[公式GitHubリポジトリ](https://github.com/opencv/opencv-python)を参照してください。

## 準備

環境に以前のバージョンや他のopencvバージョン（`pip`経由でインストールされていないもの）がインストールされている場合は、競合を避けるためにアンインストールしてください。

サポートされている最小バージョン19.3より低い場合は、`pip`バージョンをアップグレードしてください。

```bash
pip -V
pip install -U pip
```

## インストール

pipを介してopencv-pythonをインストールするには4つのオプションがあります。

**注意:** 1つのオプションのみを選択できます。1つの環境に複数の異なるパッケージが同時にインストールされている場合は、`pip uninstall opencv-python`のようにして余分なものをアンインストールする必要があります。これは、4つのパッケージすべてが同じ名前空間`cv2`を使用するためです。

標準的なデスクトップ環境（Windows、macOS、ほとんどのGNU/Linuxディストリビューション）の場合:

```bash
# 1. Main modules package
pip install opencv-python

# 2. Full package (contains both main modules and contrib/extra modules)
pip install opencv-contrib-python
```

サーバー（ヘッドレス）環境（Docker、クラウド環境など、GUIライブラリの依存関係がない）の場合:

```bash
# 3. Headless main modules package
pip install opencv-python-headless

# 4. Headless full package (contains both main modules and contrib/extra modules)
opencv-contrib-python-headless
```
