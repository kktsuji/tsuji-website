---
title: "BlenderでCollectionをHoldout Maskとして使用する"
description: ""
date: 2025-03-01T18:00:00+09:00
lastmod:
draft: false
---

## BlenderでCollectionをHoldout Maskとして使用する

この記事では、Blenderで2つのオブジェクトを使ってholdoutの例を示す。Suzanneオブジェクトをカメラの前に配置し、planeオブジェクトをSuzanneオブジェクトの後ろに配置する。Suzanneオブジェクトをholdout maskとして使用してplaneオブジェクトに穴を開ける。次に、レンダリングされた画像を背景色と合成して穴を確認する。

### 1. オブジェクトの作成

以下の画像のように3d Viewportにオブジェクトを配置する。

![img](https://img.tsuji.tech/collection-holdout-mask-blender-0.jpg)

### 2. Collectionの設定

新しいcollectionを作成し、OutlinerでSuzanneオブジェクトをそのcollectionに移動する。次に、collectionの設定でHoldoutオプションを有効にする。collectionの設定にHoldoutオプションのアイコンがない場合は、Outlinerのfilterアイコンを確認する。

![img](https://img.tsuji.tech/collection-holdout-mask-blender-1.jpg)

3D Viewportのカメラ視点ビュー（ショートカットは"0"キー）は、holdoutが有効であることを確認するのに便利である。

![img](https://img.tsuji.tech/collection-holdout-mask-blender-2.jpg)

### 3. Compositeの設定

CompositingワークスペースへGOし、Use Nodesオプションを有効にする。次に、RGBノードとAlpha Overノードを追加する。以下の画像のように接続する。

![img](https://img.tsuji.tech/collection-holdout-mask-blender-3.jpg)

### 4. レンダリング

画像をレンダリングする。holdout maskの効果を確認できる。

![img](https://img.tsuji.tech/collection-holdout-mask-blender-4.jpg)
