---
title: 'GAN-DL for データセット RxRx19a'
slug: 'gan-dl-rxrx19a'
description: 'COVID-19 に感染したヒト細胞の蛍光顕微鏡画像からなる公開データセット RxRx19a の解析のために提案された Deep Learning 手法の１つ "GAN-DL" についての論文まとめ。'
date: 2024-04-17T08:03:26+09:00
lastmod: 
math: false
draft: false
---

この記事では、Mascoliniらによる Deep Learning 技術の１つである GAN-DL[^1] を紹介する。

(本ポストの図は論文[^1]からの引用である)

## 論文の概要

* 著者らは、NVIDIA の StyleGAN2 アーキテクチャ[^2] に基づく「Generative Adversarial Network Discriminator Learner (GAN-DL)[^1]」と呼ばれる自己教師あり学習フレームワークを提案した。
* GAN-DLは、COVID-19 に感染したヒト細胞の蛍光顕微鏡画像からなる公開データセット RxRx19a[^3] を用いて学習された。
* 学習された GAN-DL の識別器の特徴は、classification のようないくつかの下流のタスクに適用された。
* GAN-DL の性能評価には、いくつかの先行研究の手法を用いた。

## 他の手法より優れた点

* 画像のアノテーションが不要
  * いくつかの関連研究[^4] [^5] では、embedding data 生成のためにターゲットデータセットのラベルが必要。
  * 一方、GAN-DL はラベルやアノテーション無しで動作する。
* 自己教師あり学習
  * 性能比較対象の Baseline (後述) は伝統的な転移学習に基づく。
  * 対して、GAN-DL は自己教師あり学習に基づく。

![img](https://img.tsuji.tech/gan-dl-rxrx19a-0.jpg)

![img](https://img.tsuji.tech/gan-dl-rxrx19a-1.jpg)

## 重要な点

* StyleGan2 の学習と RxRx19a データセットは、pretext-task に用いられる。
* 学習した discriminator の特徴は、他のダウンストリームタスクを解くための表現空間として使用される。

## GAN-DL ネットワークの詳細

* GAN-DL は StyleGAN2 のインスタンス
  * 全結合層のネットワークを簡略化し、8層から3層に削減。
  * 潜在空間にはサイズ 512 のスタイルベクタを使用。
  * Dscriminator と Generator の両ネットワークのうち、画像に最も近い畳み込み層のフィルタサイズを5に変更（入力画像はRGB 3チャネルではなく、5チャネルの蛍光顕微鏡画像であるため）。
* 学習時間
  * コアあたり 16GIB の RAM を搭載した TPU v3-8 ノードで 24時間。
  * シングル Tesla V100 で 48時間。

## 比較対象

### Baseline

 
* Cuccareseら[^10]による RxRx19a のための転移学習ベースの embedding が、GAN-DL の著者ら[^1]による論文で評価のベースラインとして使用された。
* その embedding (1024次元ベクトル、1画像につき1ベクトル) は、ImageNet[^13] によって事前に学習された DenseNet[^14] CNN アーキテクチャを用いて生成された。
  * 最初の畳み込み層は 512 x 512 x 5 に変更された。
  * グローバル平均プーリングは、最終的な特徴マップを長さ 2208 のベクトルに抽出するために使用される。
  * 1024次元の全結合層が画像の embedding として追加される。
  * Embedding 層では、ソフトマックス活性化関数と ArcFace活性化関数[^12]を2つの別々の分類層に使用。
* ベースラインは RxRx1 データセット[^11]（約300GBのアノテーション付き顕微鏡画像）を用いて学習させた。
* このダウンストリームタスクには、RxRx19 データセットを用いる。
* ベースラインの empbedding データは利用可能であるが、ソースコードと学習済みモデルは利用できない。
* GAN-DL の著者[^1]は、上記の利用可能な embedding データ[^10]をベースラインとしている。

### DenseNet CNN

* GAN-DL の著者[^1]は、比較のために DenseNet CNN ネットワークを実装した。
* DenseNet は RGB画像を受け付けるが、RxRx1 の画像は 6チャンネル、RxRx19a は 5チャンネルである。そこで著者[^1]はベースラインのアーキテクチャ[^10]を再現するために2つの方法をとった：
  1. ImageNet-collapsed 戦略: 学習可能な畳み込み層（カーネルサイズ1）をRGBの事前学習済みネットワークの最初の層として追加し、蛍光画像のチャンネル数を1チャンネルのグレースケール画像に削減する。そして、RGBそれぞれに複製して擬似的なRGB画像を生成する。追加された層は、与えられたダウンストリームタスク（Adam オプティマイザ、学習率 0.001、数エポック）のファインチューンにより学習される。
  2. ImageNet 連結戦略: 蛍光画像の各チャンネルは1チャンネル画像に分離され、それぞれネットワークに入力される。埋め込みサイズは5120 (1024 x 5) となる。

### 伝統的なオートエンコーダ (ConvAE[^15])

* ConvAE を RxRx19a により学習する。
* GAN-DL の著者[^1]は、Wallaceら[^16]を参考にしてこのネットワークを実装した。
* アーキテクチャは以下の2つを追加することで変更した：
  1. StyleGan2 のジェネレーターで使用されている residual 接続スキーム。
  2. ImageNet で事前に学習した ResNet50[^17] を用いて生成した知覚的損失関数。
* 最後の層を embedding として使用（サイズは 1024）。

## RxRx19a dataset の準備

* RxRx19a データセットの 305,520枚の蛍光顕微鏡画像（縦：1024、横：1024、5チャネル）、2つの対照群を作成。
  1. 感染していない細胞から調製したコンディショニング培地（Mock）。
  2. 活性型 SARS-CoV-2 ウイルスに vitro感染した、化合物で処理されていない細胞。
* 画像の 75% はトレーニング用、25% はテスト用に使用（ランダムに分割）。
* クラス内の不均衡は、クラスの頻度に反比例した値を用いて正規化した（クラス内の画像数について言及されている？）。
* 対照群以外の画像は、dense-response 評価に使用したが、ダウンストリームタスクの訓練には使用しない。
* RxRx19a と RxRx1 のプレート間分散を除去するための正規化を含む標準的なポスト処理[^10]を行った。

## ダウンストリームタスクを解決する能力の評価

### 1. Controls classification および 3. Cell models clasisification

GAN-DL のスタイルベクトルと、比較対象の embedding を用いて、線形サポートベクターマシン（SVN）を分類タスクに適用。
* ベースラインが最も精度が良好。
* GAN-DL はベースラインより若干劣るが、DenseNet や ConvAE よりははるかに良好。

### 2. Dose-response modelling

* 割愛

### Zero-shot representation learning

* RxRx19a で学習した GAN-DL の埋め込みを、RxRx1 のゼロショット表現学習タスクに適用。
* ベースラインは RxRx1 を用いて事前学習を行ったため、本実験では使用しない。
* ソフトマージン線形 SVM を、GAN-DL の embedding を用いて構築した。
* SVM は RxRx1 の入力データを4つのクラスに分類した。
* GAN-DL は、ヒト臍帯静脈内皮細胞（HUVEC）画像を除いて、DenseNet や ConvAE よりも優れた性能を示した。

## 議論されたこと

* GAN-DL の著者[^1]は、分類タスクにおいて、ベースラインは提案手法である GAN-DL よりも一般的に精度が高いと述べている。しかし、GAN-DL は他のタスクに再利用できることが利点であると述べている。ベースラインはRxRx1 データセットをラベル付きで学習させたが、GAN-DL は学習段階でアノテーションやラベルを必要としないためである。
* ConvAE の表現能力は DenseNet に劣る。なぜなら、オートエンコーダが高品質な画像を生成する能力には制限があるためである。

## ソースコードは公開されているか

* GAN-DL のソースコードは公開されていない。
* しかし、著者は GAN-DL により生成された embedding データは公開している。

## データセットは公開されているか

* データセット RxRx19a, RxRx1 どちらとも公開されている。

## 私が学んだこと

* NVIDIA の StyleGan2[^2] は Wasserstein Generative Adcersarial Networks (W-GANs)[^6] の一種である。
* Goldsboroughらは、自己教師あり表現学習（SSRL）タスクを生物学的画像（蛍光顕微鏡）に適用した最初の研究[^7]を発表したが、GAN-DL の著者[^1]によると結果はあまり良くなかった。
* GAN の discriminator を特徴抽出器として使用するオリジナルのアイデアは、Radfordら[^8]によって示されている。
* StyleGAN2 はモード崩壊現象に強いことが提案されている[^6] [^9]．
* W-GAN は GAN の学習における2つの問題に強い。
  1. モード崩壊
    * GAN ネットワークはデータのサブセットのみを学習する。
    * 崩壊した分布は、単一の画像、または画像の離散的な集合を生成する。
    * これは、モデルが特定の部分集合を大きく過学習することを意味する。
    * Discriminator はローカルミニマムにトラップされ、Generotor はこの Discriminator に対して同じ画像を生成する。
  2. 収束性の欠如
    * Generator と Discriminator のどちらかの改善速度が他方のネットワークより速すぎるため、相互の改善が妨げられる。
* W-GAN はこれらの問題を軽減するため、古典的な Discriminator モデルを、与えられた画像の実在性をスコア化するWasserstein 距離に基づいたものに置き換えた。
* StyleGAN2 は W-GAN のインスタンスであり、両方のネットワークに residual connections 残差結合を適用する。
* 高品質な画像を生成する能力（＝学習データの特徴をうまく抽出する能力）は、その事前学習された特徴がダウンストリームタスクに適用されたとき、他のダウンストリームタスクを解決することにつながる。

## 次に読むべき論文

* StyleGan2[^2]
* W-GAN[^6]
* Goldsborough らの論文 (自己教師あり学習を生物学的画像に初めて適用)[^7]

[^1]: Alessio Mascolini, Dario Cardamone, Francesco Ponzio, Santa Di Cataldo and Elisa Ficarra. Exploiting generative self-supervised learning for the assessment of biological images with lack of annotations. *BMC Bioinformatics*, 23, 295, 2022. [doi.org/10.1186/s12859-022-04845-1](https://doi.org/10.1186/s12859-022-04845-1).

[^2]: Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen and Timo Aila. Analyzing and Improving the Image Quality of StyleGAN. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 8110–19, 2020. [doi:10.1109/CVPR42600.2020.00813](https://doi.ieeecomputersociety.org/10.1109/CVPR42600.2020.00813) or [arXiv:1912.04958](https://arxiv.org/abs/1912.04958). ([Github repository](https://github.com/NVlabs/stylegan2)).

[^3]: Recursion. RxRx19a dataset. [https://www.rxrx.ai/rxrx19a](https://www.rxrx.ai/rxrx19a), 2020.

[^4]: Dylan Zhuangand Ali K. Ibrahim. Deep Learning for Drug Discovery: A Study of Identifying High Efficacy Drug Compounds Using a Cascade Transfer Learning Approach. *Applied Sciences*. 2021;11(17):7772, 2021. [doi:10.3390/app11177772](https://doi.org/10.3390/app11177772).

[^5]: M. Sadegh Saberian, Kathleen P. Moriarty, Andrea D. Olmstead, Christian Hallgrimson, François Jean, Ivan R. Nabi, Maxwell W. Libbrecht and Ghassan Hamarneh. DEEMD: Drug Efficacy Estimation Against SARS-CoV-2 Based on Cell Morphology With Deep Multiple Instance Learning. *Medical Image Computing and Computer Assisted Intervention – MICCAI 2023*, vol.14227, pp.676, 2023. [doi:10.1109/TMI.2022.3178523](https://ieeexplore.ieee.org/document/9783182)

[^6]: Martin Arjovsky, Soumith Chintala and Léon Bottou. Wasserstein GAN. In *Proceedings of the 34th International Conference on Machine Learning*, PMLR 70:214-223, 2017. [link](https://proceedings.mlr.press/v70/arjovsky17a.html) or [arXiv:1701.07875](https://arxiv.org/abs/1701.07875)

[^7]: Peter Goldsborough, Nick Pawlowski, Juan C Caicedo, Shantanu Singh and Anne E Carpenter. CytoGAN: Generative Modeling of Cell Images. BioRxiv 2017. [doi:10.1101/227645](https://doi.org/10.1101/227645).

[^8]: Alec Radford, Luke Metz and Soumith Chintala. Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks. *arXiv preprint [arxiv:1511.06434](https://arxiv.org/abs/1511.06434)*.

[^9]: Mingyang Zhang, Maoguo Gong, Yishun Mao, Jun Li and Yue Wu. Unsupervised Feature Extraction in Hyperspectral Images Based on Wasserstein Generative Adversarial Network. *IEEE Transactions on Geoscience and Remote Sensing*, vol.57, no.5, pp.2669-2688, 2019. [doi:10.1109/TGRS.2018.2876123](https://ieeexplore.ieee.org/document/8527649).

[^10]: Michael F. Cuccarese et al. Functional immune mapping with deep-learning enabled phenomics applied to immunomodulatory and COVID-19 drug discovery, BioRxiv 2020. [doi:10.1101/2020.08.02.233064](https://www.biorxiv.org/content/10.1101/2020.08.02.233064v2).

[^11]: Recursion. RxRx1 dataset. [https://www.rxrx.ai/rxrx1](https://www.rxrx.ai/rxrx1), 2019.

[^12]: Jiankang Deng, Jia Guo, Niannan Xue and Stefanos Zafeiriou. ArcFace: Additive Angular Margin Loss for Deep Face Recognition. *2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pp.4685-4694, 2019. [doi:10.1109/CVPR.2019.00482](https://ieeexplore.ieee.org/document/8953658).

[^13]: ImageNet. [https://www.image-net.org/](https://www.image-net.org/).

[^14]: Gao Huang, Zhuang Liu, Laurens van der Maaten and Kilian Q. Weinberger. Densely Connected Convolutional Networks. *arXiv preprint [arxiv:1608.06993](https://arxiv.org/abs/1608.06993)*. ([Github repository](https://github.com/liuzhuang13/DenseNet)).

[^15]: Dong Jin Ji, Jinsol Park and Dong-Ho Cho. ConvAE: A New Channel Autoencoder Based on Convolutional Layers and Residual Connections. *IEEE Communications Letters*, vol.23, no.10, pp.1769-1772, 2019. [doi:10.1109/LCOMM.2019.2930287](https://ieeexplore.ieee.org/abstract/document/8768327).

[^16]: Bram Wallace and Bharath Hariharan. Extending and Analyzing Self-Supervised Learning Across Domains. *Computer Vision – ECCV 2020. Lecture Notes in Computer Science*, vol.12371, Springer, 2020. [doi:/10.1007/978-3-030-58574-7_43](https://doi.org/10.1007/978-3-030-58574-7_43)

[^17]: Gustav Grund Pihlgren, Fredrik Sandin and Marcus Liwicki. Improving Image Autoencoder Embeddings with Perceptual Loss. *arXiv preprint [arxiv:2001.03444](https://arxiv.org/abs/2001.03444)*.