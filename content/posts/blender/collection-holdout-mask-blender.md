---
title: "Use Collection as Holdout Mask in Blender"
description: ""
date: 2025-03-01T18:00:00+09:00
lastmod:
draft: false
---

## Use Collection as Holdout Mask in Blender

In this post, I'll use two objects in Blender for an example of holdout. The Suzanne object places in front of the camera, and the plane object places behind the Suzanne object. I'll use the Suzanne object as a holdout mask to make a hole in the plane object. Then I'll composite the rendered image with a background color to confirm the hole.

### 1. Create Objects

Put objects in the 3d Viewport like the following image.

![img](https://img.tsuji.tech/collection-holdout-mask-blender-0.jpg)

### 2. Collection Settings

Create a new collection and move the Suzanne object to the collection in the Outliner. Then, enable the Holdout option in the collection settings. If there is no Holdout option icon in the collection settings, check the filter icon in the Outliner.

![img](https://img.tsuji.tech/collection-holdout-mask-blender-1.jpg)

Camera perspective view in the 3D Viewport (shortcut is "0" key) is useful to confirm that holdout is enable.

![img](https://img.tsuji.tech/collection-holdout-mask-blender-2.jpg)

### 3. Composite Settings

Go to the Compositing workspace and enable the Use Nodes option. Then, add RGB node and Alpha Over node. Connect them as the following image.

![img](https://img.tsuji.tech/collection-holdout-mask-blender-3.jpg)

### 4. Render

Render the image. You can see the holdout mask effect.

![img](https://img.tsuji.tech/collection-holdout-mask-blender-4.jpg)
