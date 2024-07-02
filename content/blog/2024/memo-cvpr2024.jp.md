---
title: 'CVPR2024 の論文メモ'
description: 'CVPR2024 の論文メモ.'
date: 2024-07-02T07:50:00+09:00
lastmod: 
math: false
draft: false
---

本ポストでは、私の研究領域との関連が薄い CVPR2024 の論文のメモを 1つの記事にまとめる。

## Generative Image Dynamics

Paper: Li et al., Generative Image Dynamics ([project page](https://generative-dynamics.github.io/), [cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Li_Generative_Image_Dynamics_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2309.07906)).

この論文は [CVPR2024 best paper award](https://cvpr.thecvf.com/Conferences/2024/News/Awards) を受賞している。

![img](https://img.tsuji.tech/gid-cvpr2024-0.jpg)

![img](https://img.tsuji.tech/gid-cvpr2024-1.jpg)

(画像は[論文](https://openaccess.thecvf.com/content/CVPR2024/papers/Li_Generative_Image_Dynamics_CVPR_2024_paper.pdf)からの引用である)

* 著者らは、1枚の RGB画像から、動きの軌跡を含むループ動画を生成する、拡散モデルに基づく新しい手法を提案した。
* このモデルは、実際に撮影された動画から、風などによって揺れる物体の振動ダイナミクスを学習する。
* 運動はフーリエ領域のスペクトルボリュームとして扱われる。

## BioCLIP

Paper: Stevens et al., BIOCLIP: A Vision Foundation Model for the Tree of Life ([project page](https://imageomics.github.io/bioclip/), [cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Stevens_BioCLIP_A_Vision_Foundation_Model_for_the_Tree_of_Life_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2311.18803)).

この論文は [CVPR2024 best student paper award](https://cvpr.thecvf.com/Conferences/2024/News/Awards) を受賞している。

![img](https://img.tsuji.tech/bioclip-cvpr2024-0.jpg)

(画像は[論文](https://openaccess.thecvf.com/content/CVPR2024/papers/Stevens_BioCLIP_A_Vision_Foundation_Model_for_the_Tree_of_Life_CVPR_2024_paper.pdf)からの引用である)

* 著者らは、生物画像を含む新しいデータセット "TREEOFLIFE-10M" を提案した。
* また、"BIOCLIP "と呼ばれる、TREEOFLIFE-10M に基づく新しい基礎モデルを提案した。
