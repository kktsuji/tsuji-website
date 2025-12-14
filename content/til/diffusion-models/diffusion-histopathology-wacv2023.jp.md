---
title: "病理組織画像のためのDiffusion確率モデル、WACV2023"
description: "病理組織画像の合成生成のためのdiffusion確率モデルを提案した論文の要約。"
date: 2024-05-20T8:50:00+09:00
lastmod:
draft: false
---

この投稿では、Moghadam _et al_[^1]が執筆した論文「A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images」を紹介します。

（この投稿の図と表は論文[^1]からのものです）

## この論文の概要

- 著者ら[^1]はdiffusion確率モデルを病理組織画像に適用して、高品質な合成画像を生成しました。
- この論文の目標：
  - 病理組織画像を合成するためのdiffusion確率モデルの有用性を探求すること。
  - diffusionモデルのパフォーマンスを他の生成AIモデルと比較すること。
- 著者らによると、これは病理組織画像にdiffusionモデルを導入した最初の研究です。
- 著者らはDhariwal _et al._[^10]が提案したU-Netベースのdiffusionモデルアーキテクチャを病理組織画像合成タスクに適用しました。

![img](https://img.tsuji.tech/diffusion-histopathology-wacv2023-0.jpg)

## 他と比べて優れている点は？

- パフォーマンス：
  - 提案されたdiffusionモデルは、ProGanと比較してすべての指標（IS、FID、sFID、Improved PrecisionとRecall）で優れています。
  - diffusionモデルによって合成された画像は、特定の細胞タイプの特徴を持っています。
- 実験：
  - 病理医が実験に参加して、diffusionモデルによって生成された実画像と合成画像を識別しました。

## 提案されたアーキテクチャ

- 提案手法のバックボーンは、Dhariwal _et al._[^10]によって改良されたUnetベースモデルに似たニューラルネットワークです
  - これ[^10]はHo _et al._[^17]によるdiffusionモデル用のUnetモデルに触発されています。
  - このモデルは3種類の画像解像度を使用しており、画像内の局所的およびグローバルな特徴を扱うことができます。
- 合成画像上のチェッカーボックスやエイリアシングなどのアーティファクトを減らすために、BIGGANダウンサンプリング/アップサンプリング残差ブロック[^5]を使用します。
  - この種のアーティファクトは、特に病理組織画像にとって重大なノイズです。
- embedding層を使用して、timestepをdiffusionネットワークに注入します。
  - すべてのtime stepは、モデルの残りの重みにアクセスできます。
- 画像の遺伝子型は、別のembedding層を使用した学習に利用されます。

## パフォーマンス評価

- 合成病理組織画像を生成するために2つのネットワークが適用されます。
  - 提案されたdiffusionモデル[^1]に基づく提案手法。
  - 関連研究のネットワーク[^24]はProGAN[^20]を利用しました。
    - 著者らはMiyato _et al._[^28]が提案したcGANを参照してProGANをわずかに修正しました。
- 2人の病理医が2つのネットワークによって合成された画像の品質を評価します。

## データセット

- The Cancer Genome Atlas（TCGA）アーカイブ[^15]からのデータセット。
  - 3つの主要なゲノムサブタイプを代表するlow grade gloomの344枚のwhole slides images（WSI）。
  - 画像のサイズは約100K x 100Kピクセル。
- アノテーション：
  - 各スライド画像は、著者らのアノテーションツールを使用してプロの病理医によってピクセル単位でアノテーションされています。これらのアノテーションは公開される予定です。
- パッチ：
  - 各スライドから512x512ピクセルのサイズの最大100個の腫瘍パッチが収集されます。
  - これらは128x128のサイズにスケーリングされます。
  - パッチの総数は33,777枚の画像（128x128）です。

## 結果

### 合成画像の品質

- 主観的評価：
  - 著者らは、図5において提案手法によって生成された合成画像がProGANのものより高品質であると述べています。
- Inception Score（IS）、Frechet Inception Distance（FID）、sFID
  - Diffusionモデルは表2においてInception ScoreとsFIDのより良いスコアを示しています。
  - 著者らは、提案されたdiffusion手法が3つの指標でProGANを上回っていると述べています。
  - 著者らはまた、diffusionモデルがFIDとsFIDでより低い値を示しており、ProGANよりも知覚的特徴をロバストに生成できることを述べています。

![img](https://img.tsuji.tech/diffusion-histopathology-wacv2023-1.jpg)

![img](https://img.tsuji.tech/diffusion-histopathology-wacv2023-2.jpg)

- Improved PrecisionとRecall指標[^22]
  - Inproved Recall：実データの特徴が合成データ特徴の多様体に含まれている割合。
  - Improved Precision：合成データ特徴が実データ特徴の多様体に位置する割合。
  - 提案されたdiffusionモデルは、両方の指標でProGANの結果よりも優れたパフォーマンスを示しました。

![img](https://img.tsuji.tech/diffusion-histopathology-wacv2023-3.jpg)

![img](https://img.tsuji.tech/diffusion-histopathology-wacv2023-4.jpg)

### 病理医による評価

- 著者らは、実画像と合成画像から同数の画像を選択しました。
- 2人の病理医が画像を見せられ、各画像について2つの質問をされました：
  1. この画像は実際のものだと思いますか、それとも偽物だと思いますか？
  2. あなたの答えにどの程度自信がありますか？
- 著者らは、提案されたdiffusionモデルによる合成画像が実画像に非常に似ていると結論付けました：
  - 病理医は実画像と合成画像を識別できませんでした。
  - 彼らは合成画像を区別する際、信頼度が低くなりました。

## 視覚的観察

- Diffusionモデルは特定の細胞タイプの特徴を持つ画像を生成できる一方、ProGanの画像は不明確な特徴を持っており、これはdiffusionモデルが各細胞タイプの特定の特徴を学習する能力を持っていることを示唆しています。

## 学んだこと

- Diffusionモデルの利点：
  - 安定したトレーニング、容易なモデルスケーリング、優れた分布カバレッジ。
  - より高い安定性：
    - Denoisingステップと入力画像に対する強い条件が、データ分布を柔らかくします。
  - より多様な画像：
    - より優れた分布カバレッジにより。
  - 過学習が少ない[^42]。
- GANの欠点：
  - この論文によると、モード崩壊と不安定性。
    - 複雑なlatent空間から直接画像を一度に生成します。
    - discriminatorが過学習しやすい[^42]。
  - これらの原因により、ネットワークは稀な条件や不均衡なデータセットからサンプルを生成するのに不適切または困難になります。
- Inception score（IS）[^35]：
  - ISは、2つの確率分布間の差を測定するためにKullback-Leibler（KL）ダイバージェンスを使用して定義されます。
  - ある論文[^3]は、ISはImageNet以外のデータセットを使用してトレーニングされた生成モデルには適切な指標ではない可能性があると述べています。
- Frechet inception distance（FID）[^21]：
  - FIDは、トレーニングデータセットの分布と合成データの分布を比較する指標です。
  - FID値が低いということは、これらの分布が類似していることを意味します。
  - FIDはInception-V3 latent空間を利用します。
  - 両方のデータがinception V3モデルに供給され、"pool_3 layer"の平均と標準偏差がFIDの計算に利用されます。
- sFID[^37]：
  - FIDの修正版。
  - FDIは空間情報を圧縮する"pool_3 Layer"を使用するため、空間的不均一性に対する感度が低くなります。
  - 一方、sFDIは中間層からの初期チャネルを採用します。これは、sFDIが一部の状況において空間的類似性の情報をFDIよりもよく抽出できることを意味します[^30]。

[^1]: Puria Azadi Moghadam, Sanne Van Dalen, Karina C. Martin, Jochen Lennerz, Stephen Yip, Hossein Farahani and Ali Bashashati. A Morphology Focused Diffusion Probabilistic Model for Synthesis of Histopathology Images. _2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)_, pages 1999-2008, 2023. [doi.org/10.1109/WACV56688.2023.00204](https://doi.ieeecomputersociety.org/10.1109/WACV56688.2023.00204) or [arXiv:2209.13167](https://arxiv.org/abs/2209.13167).

[^3]: Shane Barratt and Rishi Sharma. A Note on the Inception Score. _arXiv preprint [arxiv:1801.01973](https://arxiv.org/abs/1801.01973)_.

[^5]: Andrew Brock, Jeff Donahue and Karen Simonyan. Large Scale GAN Training for High Fidelity Natural Image Synthesis. _arXiv preprint [arxiv:1809.11096](https://arxiv.org/abs/1809.11096)_.

[^10]: Prafulla Dhariwal and Alex Nichol. Diffusion Models Beat GANs on Image Synthesis. _arXiv preprint [arxiv:2105.05233](https://arxiv.org/abs/2105.05233)_.

[^15]: Robert L. Grossman, Allison P. Heath, Vincent Ferretti, Harold E. Varmus, Douglas R. Lowy, Warren A. Kibbe, and Louis M. Staudt. Toward a shared vision for cancer genomic data. New England Journal of Medicine, 375(12):1109– 1112, 2016. [doi.org/10.1056/NEJMp1607591](https://www.nejm.org/doi/full/10.1056/NEJMp1607591).

[^17]: Jonathan Ho, Ajay Jain and Pieter Abbeel. Denoising Diffusion Probabilistic Models. _arXiv preprint [arxiv:2006.11239](https://arxiv.org/abs/2006.11239)_.

[^20]: Tero Karras, Timo Aila, Samuli Laine and Jaakko Lehtinen. Progressive Growing of GANs for Improved Quality, Stability, and Variation. _arXiv preprint [arxiv:1710.10196](https://arxiv.org/abs/1710.10196)_.

[^21]: Tuomas Kynkäänniemi, Tero Karras, Miika Aittala, Timo Aila and Jaakko Lehtinen. The Role of ImageNet Classes in Fréchet Inception Distance. _arXiv preprint [arxiv:2203.06026](https://arxiv.org/abs/2203.06026)_.

[^22]: Tuomas Kynka¨anniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Improved precision and recall metric for assessing generative models. Advances in Neural Information Processing Systems, 32, 2019. [link](https://proceedings.neurips.cc/paper/2019/hash/0234c510bc6d908b28c70ff313743079-Abstract.html)

[^24]: Adrian B Levine, Jason Peng, David Farnell, Mitchell Nursey, Yiping Wang, Julia R Naso, Hezhen Ren, Hossein Farahani, Colin Chen, Derek Chiu, et al. Synthesis of diagnostic quality cancer pathology images by generative adversarial networks. The Journal of pathology, 252(2):178–188, 2020. [doi.org/10.1002/path.5509](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.5509).

[^28]: Takeru Miyato and Masanori Koyama. cGANs with Projection Discriminator. _arXiv preprint [arxiv:1802.05637](https://arxiv.org/abs/1802.05637)_.

[^30]: Charlie Nash, Jacob Menick, Sander Dieleman and Peter W. Battaglia. Generating Images with Sparse Representations. _arXiv preprint [arxiv:2103.03841](https://arxiv.org/abs/2103.03841)_.

[^35]: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved techniques for training gans. Advances in neural information processing systems, 29, 2016.

[^37]: Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2818–2826, 2016.

[^42]: Zhisheng Xiao, Karsten Kreis, and Arash Vahdat. Tackling the generative learning trilemma with denoising diffusion gans. In International Conference on Learning Representations, 2021.
