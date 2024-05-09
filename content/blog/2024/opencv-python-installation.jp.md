---
title: 'opencv-python インストール方法'
slug: 'opencv-python-installation'
description: 'opencv-python のインストール方法についての Today I learned ポスト。'
date: 2024-03-31T16:42:17+09:00
lastmod: 
math: false
draft: false
---

## Reference

詳細は [公式 GitHub リポジトリ](https://github.com/opencv/opencv-python) を参照。

## Preparation

もし実行環境に古いバージョン、もしくは手動でインストールしたバージョン（ただし、``pip`` を用いずにインストールしたものを指す）が存在する場合、コンフリクトを避けるために事前にアンインストールが必要。

また、``pip`` >= 19.3 でない場合はアップグレードを行う。

```bash
pip -V
pip install -U pip
```

## Installation

``pip`` によるインストールには4つのオプションがある。

**Note:** 4つのうち1つのみ選択可能。1つの環境に2つ以上のオプションが同時にインストールされている場合は、``pip uninstall opencv-python`` のようにアンインストールが必要。これは、4つのパッケージ全てが同じ名前空間 ``cv2`` を使用するためである。

標準的なデスクトップ環境の場合 (Windows, macOS, ほぼ全ての GNU/Linux ディストリビューション)：

```bash
# 1. Main modules package
pip install opencv-python

# 2. Full package (contains both main modules and contrib/extra modules)
pip install opencv-contrib-python
```

サーバー（ヘッドレス）環境の場合 (Docker, クラウド環境など, また GUI ライブラリへの依存がない場合)：

```bash
# 3. Headless main modules package
pip install opencv-python-headless

# 4. Headless full package (contains both main modules and contrib/extra modules)
opencv-contrib-python-headless
```