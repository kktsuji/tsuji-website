---
title: '病理組織画像生成のための拡散確率モデル, WACV2023'
description: "病理組織画像を生成するための拡散確率モデルを提案した論文のまとめ"
date: 2024-05-20T8:50:00+09:00
lastmod: 
math: false
draft: false
---

本ポストは、Moghadamらによる論文[^1] "A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images" を紹介する。

(本ポストの図や表は論文[^1]からの引用である)

## 論文の概要

- 著者ら[^1]は、病理組織画像に拡散確率モデル (Diffusion Probabilistic Model) を適用し、高品質な合成画像を作成した。
- 論文の目的：
    - 病理組織画像を合成して生成するための拡散確率モデルの有用性を探る。
    - 拡散モデルの性能を他の生成AIモデルと比較する。
- 著者らによれば、本論文は病理組織画像に拡散モデルを導入した最初の研究である。
- 著者らは、Dhariwal ら[^10]によって提案されたU-netベースの拡散モデルアーキテクチャを病理組織画像の生成タスクに適用した。

![img](https://img.tsuji.tech/diffusion-histopathology-images-wacv2023-0.jpg)

## どの点が他より優れているか？

- 性能：
    - 提案する拡散モデルは、ProGanと比較して、すべての指標（IS, FID, sFID, Improved Precision and Recall）で優れている。
    - 拡散モデルによって合成された画像は、特定の細胞タイプの特徴を持つ。
- 実験方法：
    - 病理医 (Pathologist) が本研究へ参加し、実画像と拡散モデルによる合成画像を識別する実験を行った。

## 提案されたアーキテクチャ

- 本提案手法のバックボーンは、Dhariwal *ら*[^10]によって改良されたUnetベースのモデルに似たニューラルネットワークである。
    - これ[^10]は、Ho ら[^17]による拡散モデルの Unet モデルから着想を得ている。
    - このモデルは3種類の画像の解像度を使用し、画像の局所的な特徴と大域的な特徴を扱うことができる。
- 合成画像上のチェッカーボックスやエイリアシングのようなアーティファクトを低減するために、BIGGAN の downsampling/upsampling residual ブロック[^5]を用いる。
    - このようなアーティファクトは、特に病理組織画像にとっては致命的なノイズであるため。
- Embedding layer は拡散ネットワークにタイムステップを注入するために使用される。
    - すべてのタイムステップはモデルの全重みにアクセスできる。
- 画像の遺伝子型 (Genotypes) は、分離された埋め込み層での学習に利用される。

## 性能評価

- 病理組織画像を生成するために、2つのネットワークを使用した。
    - 提案手法（拡散モデル[^1]に基づくもの）。
    - 関連研究[^24]のネットワーク（ProGAN[^20]を利用しているもの）。
        - 著者らは、Miyato ら[^28]が提案した cGAN を参考に、ProGAN を若干修正した。
- 2人の病理医による、2つのネットワークによって合成された画像の評価。


## データセット


- Cancer Genome Atlas（TCGA）アーカイブのデータセット[^15]。
    - 低悪性度癌の3つの主要な genomic subtypes の344の全スライド画像（WSI）。
    - 画像サイズは100K x 100Kピクセル。
- アノテーション：
    - 各スライド画像は、著者ら[^1]のアノテーションツールを用いて、専門の病理医によりピクセル単位でアノテーションされている。これらのアノテーションは一般に公開される予定であるとのこと。
- パッチ
    - 各スライドから 512x512 ピクセルの腫瘍パッチを最大100個まで切り出して作成する。
    - これらのパッチは 128x128 のサイズにスケーリングされる。
    - パッチ総数は 33,777枚（128x128）。

## 結果

### 合成生成画像のクオリティ


- 主観的評価：
    - 提案手法で生成された合成画像は、ProGANで生成された合成画像よりも高画質であった（Fig.5）。
- Inception Score (IS), Frechet Inception Distance (FID), sFID
    - 表2より、Inception Score と sFID は拡散モデルの方が優れている。
    - 著者らは、提案する拡散モデルは、3つの指標において ProGAN より優れていると述べている。
    - また、FID と sFID は ProGAN よりも低い値を示しており、拡散モデルは ProGAN よりもロバストに知覚特徴を生成できることが分かる。

![img](https://img.tsuji.tech/diffusion-histopathology-images-wacv2023-1.jpg)

![img](https://img.tsuji.tech/diffusion-histopathology-images-wacv2023-2.jpg)

- Improved Precision and Recall Metrics[^22]
    - Inproved Recall: 実データの特徴量が、生成結果のデータ特徴の多様体 (Manifold) に含まれる割合。
    - Improved Precision: 上記の実データと生成結果のデータを入れ替えたもの。
    - 提案された拡散モデルは、ProGAN の結果よりも両方の指標で良い結果を示した。

![img](https://img.tsuji.tech/diffusion-histopathology-images-wacv2023-3.jpg)

![img](https://img.tsuji.tech/diffusion-histopathology-images-wacv2023-4.jpg)

### Pathologist による評価


- 著者らは、実画像と合成画像から同数の画像を選択した。
- 2人の病理医にそれらの画像のみを見せ、それぞれの画像について2つの質問を行った：
    1. この画像は本物か、それともAIによる偽物か、どちらだと思いますか？
    2. その答えにどの程度の確信度がありますか？
- 著者らは、提案した拡散モデルによって合成された画像は、実画像に極めて類似していると結論づけた：
    - 病理医は合成画像から本物画像を識別できなかった。
    - 合成画像を識別する際の信頼度が低かった。

## 視覚的な観察

- 拡散モデルは特定の細胞タイプの特徴を持つ画像を生成できるが、ProGan の画像は特徴が不明瞭である。つまり、拡散モデルは、各細胞に固有の特徴も学習することが可能であることが示唆されている。

## 個人的に学んだこと (What I Learned)

- 拡散モデルのメリット
    - 安定した学習、モデルのスケーリングが容易、分布のカバー率が高い。
    - 安定性が高い：
        - ノイズ除去ステップと入力画像に対する強い条件により、データ分布が柔らかくなる。
    - より多様な画像：
        - 分布のカバー率が高い。
    - オーバーフィッティングが少ない[^42]。
- GAN のデメリット：
    - この論文によれば、モデル崩壊と不安定性がデメリット。
        - 複雑な潜在空間から、画像を直接生成する点。
        - 識別器のオーバーフィッティングが起こりやすい点[^42]。
    - これらの原因により、ネットワークが不適当になったり、希少な条件や不均衡なデータセットからサンプルを生成したりする。
- Inception score (IS)[^21]:
    - IS はカルバック・ライブラー (Kullback-Leibler) ダイバージェンスを用いて2つの確率分布の差を測定することで定義される。
    - ある論文[^3]では、IS は ImageNet 以外のデータセットを用いて学習した生成モデルには適さない可能性があると述べられている。
- Frechet inception distance (FID)[^37]:
    - FIDは、訓練データセットの分布と合成データの分布を比較するための指標である。
    - FID値が低いということは、２つの分布が類似していることを意味する。
    - FID は Inception-V3 潜在空間を利用する。
    - 両データは inception V3 モデルに入力され、“pool_3 layer” の平均と標準偏差が FID の計算に用いられる。
- sFID[^37]:
    - FIDの修正版。
    - FDIは空間情報を圧縮する "pool_3 Layer "を使用するため、空間的な不均質性に対する感度が低い。
    - 一方、sFDIは中間層の初期チャネルを用いる。つまり、sFDI は状況によっては FDI よりも空間的類似性の情報を抽出することができる[^30]。
    
[^1]: Puria Azadi Moghadam, Sanne Van Dalen, Karina C. Martin, Jochen Lennerz, Stephen Yip, Hossein Farahani and Ali Bashashati. A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images. *2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*, pages 1999-2008, 2023. [doi.org/10.1109/WACV56688.2023.00204](https://doi.ieeecomputersociety.org/10.1109/WACV56688.2023.00204) or [arXiv:2209.13167](https://arxiv.org/abs/2209.13167).

[^3]: Shane Barratt and Rishi Sharma. A Note on the Inception Score. *arXiv preprint [arxiv:1801.01973](https://arxiv.org/abs/1801.01973)*.

[^5]: Andrew Brock, Jeff Donahue and Karen Simonyan. Large Scale GAN Training for High Fidelity Natural Image Synthesis. *arXiv preprint [arxiv:1809.11096](https://arxiv.org/abs/1809.11096)*.

[^10]: Prafulla Dhariwal and Alex Nichol. Diffusion Models Beat GANs on Image Synthesis. *arXiv preprint [arxiv:2105.05233](https://arxiv.org/abs/2105.05233)*.

[^15]: Robert L. Grossman, Allison P. Heath, Vincent Ferretti, Harold E. Varmus, Douglas R. Lowy, Warren A. Kibbe, and Louis M. Staudt. Toward a shared vision for cancer genomic data. New England Journal of Medicine, 375(12):1109– 1112, 2016. [doi.org/10.1056/NEJMp1607591](https://www.nejm.org/doi/full/10.1056/NEJMp1607591).

[^17]: Jonathan Ho, Ajay Jain and Pieter Abbeel. Denoising Diffusion Probabilistic Models. *arXiv preprint [arxiv:2006.11239](https://arxiv.org/abs/2006.11239)*.

[^20]: Tero Karras, Timo Aila, Samuli Laine and Jaakko Lehtinen. Progressive Growing of GANs for Improved Quality, Stability, and Variation. *arXiv preprint [arxiv:1710.10196](https://arxiv.org/abs/1710.10196)*.

[^21]: Tuomas Kynkäänniemi, Tero Karras, Miika Aittala, Timo Aila and Jaakko Lehtinen. The Role of ImageNet Classes in Fréchet Inception Distance. *arXiv preprint [arxiv:2203.06026](https://arxiv.org/abs/2203.06026)*.

[^22]: Tuomas Kynka¨anniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Improved precision and recall metric for assessing generative models. Advances in Neural Information Processing Systems, 32, 2019. [link](https://proceedings.neurips.cc/paper/2019/hash/0234c510bc6d908b28c70ff313743079-Abstract.html)

[^24]: Adrian B Levine, Jason Peng, David Farnell, Mitchell Nursey, Yiping Wang, Julia R Naso, Hezhen Ren, Hossein Farahani, Colin Chen, Derek Chiu, et al. Synthesis of diagnostic quality cancer pathology images by generative adversarial networks. The Journal of pathology, 252(2):178–188, 2020. [doi.org/10.1002/path.5509](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.5509).

[^28]: Takeru Miyato and Masanori Koyama. cGANs with Projection Discriminator. *arXiv preprint [arxiv:1802.05637](https://arxiv.org/abs/1802.05637)*.

[^30]: Charlie Nash, Jacob Menick, Sander Dieleman and Peter W. Battaglia. Generating Images with Sparse Representations. *arXiv preprint [arxiv:2103.03841](https://arxiv.org/abs/2103.03841)*.

[^35]: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved techniques for training gans. Advances in neural information processing systems, 29, 2016.

[^37]: Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2818–2826, 2016.

[^42]: Zhisheng Xiao, Karsten Kreis, and Arash Vahdat. Tackling the generative learning trilemma with denoising diffusion gans. In International Conference on Learning Representations, 2021.