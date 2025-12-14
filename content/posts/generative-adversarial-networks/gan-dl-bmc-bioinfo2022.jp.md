---
title: "GAN-DL for Dataset RxRx19a, BMC Bioinformatics2022"
description: 'COVID-19に感染したヒト細胞の蛍光顕微鏡画像で構成される公開データセットRxRx19aの分析のために"GAN-DL"と呼ばれるdeep learning技術を提案した論文のまとめ。'
date: 2024-04-17T08:03:26+09:00
lastmod:
draft: false
---

この記事では、Mascolini _et. al._ によって書かれたdeep learning技術GAN-DL[^1]を提案した論文を紹介します。

（この記事の図は論文[^1]からの引用です）

## 論文の概要

- 著者らはNVIDIAのStyleGAN2アーキテクチャ[^2]に基づく"Generative Adversarial Network Discriminator Learner（GAN-DL）[^1]"と呼ばれる自己教師あり学習フレームワークを提案しました。
- GAN-DLはCOVID-19に感染したヒト細胞の蛍光顕微鏡画像で構成される公開データセットRxRx19a[^3]を使用して訓練されました。
- 訓練されたGAN-DLのdiscriminatorの特徴は分類などの下流タスクに適用されました。
- いくつかの先行研究の手法を使用してGAN-DLの性能を評価しました。

## 他の研究より優れている点は？

- 画像のアノテーションが不要です。
  - いくつかの関連研究[^4] [^5]はembeddingデータを生成するために対象データセットのラベルが必要です。
  - 一方、GAN-DLはラベルやアノテーションなしで動作します。
- 自己教師あり学習です。
  - Baseline（後述）は従来のtransfer learningに基づいています。
  - GAN-DLは自己教師あり学習フレームワークです。

![img](https://img.tsuji.tech/gan-dl-bmc-bioinfo2022-0.jpg)

![img](https://img.tsuji.tech/gan-dl-bmc-bioinfo2022-1.jpg)

## 重要なポイントは？

- RxRx19aデータセットを用いたpre-text taskにStyleGan2学習が使用されました。
- discriminatorの特徴はいくつかの下流タスクを解決するために使用される新しい表現空間を提供しました。

## GAN-DLネットワークの詳細

- GAN-DLはStyleGAN2のインスタンスです。
  - 完全接続マッピングネットワークは元の8層から3層に削減するよう簡略化されました。
  - サイズが512のstyleベクトルが潜在空間に使用されます。
  - 両方のネットワークの画像に最も近い畳み込み層のフィルタサイズを5にします（入力画像は5チャンネルですが、RGBチャンネルではありません）。
- 訓練時間:
  - コアあたり16GBのRAMを持つTPU v3-8ノードで24時間。
  - 単一のTesla V100で48時間。

## 比較対象

### Baseline

- Cuccarese _et al._[^10]によるRxRx19aのためのtransfer learningベースの画像embeddingがGAN-DL著者[^1]の論文で評価baselineとして使用されました。
- そのembedding（1024次元ベクトル、画像ごとに1つのベクトル）はImageNet[^13]で事前訓練されたDenseNet[^14] CNNアーキテクチャを使用して生成されます。
  - 初期畳み込み層は512 x 512 x 5にリサイズされます。
  - Global average poolingを使用して最終的な特徴マップを長さ2208のベクトルに抽出します。
  - 次元1024の完全接続層が画像のembeddingとして追加されます。
  - Softmax activationとArcFace Activation[^12]がembedding層の2つの別々の分類層に使用されます。
- BaselineはRxRx1データセット[^11]（約300GBのアノテーション付き顕微鏡画像）を使用して初期訓練されました。
- その下流タスクはRxRx19aデータセットで何かを行うことです。
- Baselineのembeddingデータは利用可能ですが、ソースコードと訓練済みモデルは利用できません。
- GAN-DL著者[^1]はこの論文でbaselineとして利用可能なembeddedデータ[^10]を使用しました。

### DenseNet CNN

- GAN-DL著者[^1]は別のDenseNet CNNネットワークを実装しました。
- DenseNetはRGB画像を受け入れることができますが、RxRx1の画像は6チャンネルでRxRx19aは5チャンネルです。したがって著者[^1]はbaselineのアーキテクチャ[^10]を再現するために2つの方法を採用しました:
  1. ImageNet-collapsed戦略: 訓練可能な畳み込み層（カーネルサイズ1）がRGB事前訓練ネットワークの最初の層として追加され、蛍光画像のチャンネル数を1チャンネルのグレースケール画像に削減し、その後1チャンネルデータを各3チャンネルに複製して疑似RGB画像を生成します。追加された層は与えられた下流タスクのfine-tuningを通じて学習されます（Adamオプティマイザー、学習率0.001、わずか数エポック）。
  2. ImageNet-concatenated戦略: 蛍光画像の各チャンネルを1チャンネル画像に分離し、それぞれネットワークに入力されます。Embeddingサイズは5120（1024 x 5）です。

### Convolutional autoencoder（ConvAE[^15]）

- ConvAEはRxRx19aで訓練されました。
- 著者[^1]はWallace _et al_[^16]を参照してこのネットワークを実装しました。
- アーキテクチャは以下の2つを追加することで修正されました:
  1. StyleGan2のgeneratorで使用される残差接続スキーム。
  2. ImageNetで事前訓練されたResNet50[^17]を使用して生成された知覚損失関数。
- 最後の層がembeddingとして使用されます（サイズは1024）。

## RxRx19aデータセットの準備

- RxRx19aデータセット（305,520枚の蛍光顕微鏡画像、高さ: 1024、幅: 1024、5チャンネル）から2つの対照群が作成されました。
  1. 感染していない細胞から生成された条件培地調製物（Mock）。
  2. in vitroで活性SARS-CoV-2ウイルスに感染し、化合物で処理されていない細胞で構成されるもの。
- 対照画像の75%が訓練に使用され、25%がテストに使用されました（ランダムに分割）。
- クラスの不均衡はクラス頻度に反比例して正規化されました（クラス内の画像数について言及されていますか？）。
- 対照群外は用量反応評価に使用されましたが、下流タスクの訓練には使用されませんでした。
- 著者らはRxRx19aとRxRx1のプレート間分散を除去するための正規化を含む標準的な後処理[^10]を使用しました。

## 下流タスクを解決する能力の評価

### 1. 対照分類と3. 細胞モデル分類

Linear support vector machine（SVN）がGAN-DLのstyleベクトルと競合他社のembeddingsを使用した分類タスクに適用されます。

- Baselineが最高のパフォーマンスです。
- GAN-DLはbaselineよりわずかに性能が低いですが、DenseNetやConvAEよりもはるかに優れています。

### 2. 用量反応モデリング

- 省略。

### ゼロショット表現学習

- RxRx19aで学習したGAN-DLのembeddingはRxRx1でのゼロショット表現学習タスクに適用されました。
- BaselineはRxRx1を使用して事前訓練されたため、この実験には使用されませんでした。
- ソフトマージンlinear SVMがGAN-DLのembeddingの上に構築されました（何を言っているのでしょうか？）。
- SVMは入力RxRx1データを4つのクラスに分類しました。
- GAN-DLはヒト臍帯静脈内皮細胞（HUVEC）画像を除いてDenseNetやConvAEよりも優れた性能を示しました。

## 何が議論されていたか？

- GAN-DL著者[^1]は、baselineが提案手法GAN-DLよりも分類タスクにおいて一般的により正確であると述べました。しかし、GAN-DLの他のタスクへの再利用可能性が利点であると述べられています。Baselineはラベル付きの大規模データセットRxRx1で訓練されましたが、GAN-DLは訓練フェーズでアノテーションやラベルを必要としません。
- 著者らはConvAEの表現能力がDenseNetよりも低いのは、autoencoderの高品質画像を生成する能力が制限されているためだと推測しています。

## ソースコードは利用可能か？

- 利用できません。
- しかし、著者らはGAN-DLの結果であるembeddingデータを公開しています。

## データセットは利用可能か？

- はい。

## 学んだこと

- NVIDIAのStyleGan2[^2]はWasserstein Generative Adversarial Networks（W-GANs）[^6]ファミリーです。
- Goldsborough _et al._ は生物学的画像（蛍光顕微鏡）に自己教師あり表現学習（SSRL）タスクを適用した最初の研究[^7]を発表しましたが、著者[^1]によると結果は良くありませんでした。
- GANのdiscriminatorを特徴抽出器として使用する元のアイデアはRadford _et al._[^8]によって示されました。
- StyleGAN2はmode collapse現象[^6] [^9]に耐性があることが提案されました。
- W-GANsはGANsの訓練における2つの問題に耐性があります。
  1. Mode collapse
  - GANネットワークはデータのサブセットのみを学習します。
  - 崩壊した分布は単一の画像または離散的な画像セットを生成します。
  - これはモデルが特定のサブセットに大きく過学習していることを意味します。
  - discriminatorは局所最小値にトラップされ、generatorはこのdiscriminatorのために同じ画像を生成します。
  2. 収束の欠如
  - generatorまたはdiscriminatorのいずれかの改善速度が他のネットワークよりもあまりにも速く、相互改善が妨げられます。
- W-GANsは古典的なdiscriminatorモデルをWasserstein距離ベースのモデルに置き換えることでこれらの問題を軽減できます。このモデルは与えられた画像の現実性をスコア化します。
- StyleGAN2はW-GANのインスタンスであり、両方のネットワークに残差接続を適用します。
- 高品質な画像を生成する能力（= 訓練データの特徴をよく抽出する能力）は、その事前訓練された特徴を下流タスクに適用する際に他の下流タスクを解決する能力につながります。

## 次に読むべき論文は？

- StyleGan2[^2]
- W-GAN[^6]
- Goldsborough _et al._（生物学的画像に自己教師あり表現学習タスクを適用した最初の論文）[^7]

[^1]: Alessio Mascolini, Dario Cardamone, Francesco Ponzio, Santa Di Cataldo and Elisa Ficarra. Exploiting generative self-supervised learning for the assessment of biological images with lack of annotations. _BMC Bioinformatics_, 23, 295, 2022. [doi.org/10.1186/s12859-022-04845-1](https://doi.org/10.1186/s12859-022-04845-1).

[^2]: Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen and Timo Aila. Analyzing and Improving the Image Quality of StyleGAN. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_, pages 8110–19, 2020. [doi:10.1109/CVPR42600.2020.00813](https://doi.ieeecomputersociety.org/10.1109/CVPR42600.2020.00813) or [arXiv:1912.04958](https://arxiv.org/abs/1912.04958). ([Github repository](https://github.com/NVlabs/stylegan2)).

[^3]: Recursion. RxRx19a dataset. [https://www.rxrx.ai/rxrx19a](https://www.rxrx.ai/rxrx19a), 2020.

[^4]: Dylan Zhuangand Ali K. Ibrahim. Deep Learning for Drug Discovery: A Study of Identifying High Efficacy Drug Compounds Using a Cascade Transfer Learning Approach. _Applied Sciences_. 2021;11(17):7772, 2021. [doi:10.3390/app11177772](https://doi.org/10.3390/app11177772).

[^5]: M. Sadegh Saberian, Kathleen P. Moriarty, Andrea D. Olmstead, Christian Hallgrimson, François Jean, Ivan R. Nabi, Maxwell W. Libbrecht and Ghassan Hamarneh. DEEMD: Drug Efficacy Estimation Against SARS-CoV-2 Based on Cell Morphology With Deep Multiple Instance Learning. _Medical Image Computing and Computer Assisted Intervention – MICCAI 2023_, vol.14227, pp.676, 2023. [doi:10.1109/TMI.2022.3178523](https://ieeexplore.ieee.org/document/9783182)

[^6]: Martin Arjovsky, Soumith Chintala and Léon Bottou. Wasserstein GAN. In _Proceedings of the 34th International Conference on Machine Learning_, PMLR 70:214-223, 2017. [link](https://proceedings.mlr.press/v70/arjovsky17a.html) or [arXiv:1701.07875](https://arxiv.org/abs/1701.07875)

[^7]: Peter Goldsborough, Nick Pawlowski, Juan C Caicedo, Shantanu Singh and Anne E Carpenter. CytoGAN: Generative Modeling of Cell Images. BioRxiv 2017. [doi:10.1101/227645](https://doi.org/10.1101/227645).

[^8]: Alec Radford, Luke Metz and Soumith Chintala. Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks. _arXiv preprint [arxiv:1511.06434](https://arxiv.org/abs/1511.06434)_.

[^9]: Mingyang Zhang, Maoguo Gong, Yishun Mao, Jun Li and Yue Wu. Unsupervised Feature Extraction in Hyperspectral Images Based on Wasserstein Generative Adversarial Network. _IEEE Transactions on Geoscience and Remote Sensing_, vol.57, no.5, pp.2669-2688, 2019. [doi:10.1109/TGRS.2018.2876123](https://ieeexplore.ieee.org/document/8527649).

[^10]: Michael F. Cuccarese et al. Functional immune mapping with deep-learning enabled phenomics applied to immunomodulatory and COVID-19 drug discovery, BioRxiv 2020. [doi:10.1101/2020.08.02.233064](https://www.biorxiv.org/content/10.1101/2020.08.02.233064v2).

[^11]: Recursion. RxRx1 dataset. [https://www.rxrx.ai/rxrx1](https://www.rxrx.ai/rxrx1), 2019.

[^12]: Jiankang Deng, Jia Guo, Niannan Xue and Stefanos Zafeiriou. ArcFace: Additive Angular Margin Loss for Deep Face Recognition. _2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_, pp.4685-4694, 2019. [doi:10.1109/CVPR.2019.00482](https://ieeexplore.ieee.org/document/8953658).

[^13]: ImageNet. [https://www.image-net.org/](https://www.image-net.org/).

[^14]: Gao Huang, Zhuang Liu, Laurens van der Maaten and Kilian Q. Weinberger. Densely Connected Convolutional Networks. _arXiv preprint [arxiv:1608.06993](https://arxiv.org/abs/1608.06993)_. ([Github repository](https://github.com/liuzhuang13/DenseNet)).

[^15]: Dong Jin Ji, Jinsol Park and Dong-Ho Cho. ConvAE: A New Channel Autoencoder Based on Convolutional Layers and Residual Connections. _IEEE Communications Letters_, vol.23, no.10, pp.1769-1772, 2019. [doi:10.1109/LCOMM.2019.2930287](https://ieeexplore.ieee.org/abstract/document/8768327).

[^16]: Bram Wallace and Bharath Hariharan. Extending and Analyzing Self-Supervised Learning Across Domains. _Computer Vision – ECCV 2020. Lecture Notes in Computer Science_, vol.12371, Springer, 2020. [doi:/10.1007/978-3-030-58574-7_43](https://doi.org/10.1007/978-3-030-58574-7_43)

[^17]: Gustav Grund Pihlgren, Fredrik Sandin and Marcus Liwicki. Improving Image Autoencoder Embeddings with Perceptual Loss. _arXiv preprint [arxiv:2001.03444](https://arxiv.org/abs/2001.03444)_.
