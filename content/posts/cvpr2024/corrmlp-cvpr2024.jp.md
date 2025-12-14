---
title: "変形可能な医用画像レジストレーションのための相関認識粗密MLPs"
description: ""
date: 2024-06-25T20:26:48+09:00
lastmod:
draft: false
---

## 概要

論文：Meng et al., Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Meng_Correlation-aware_Coarse-to-fine_MLPs_for_Deformable_Medical_Image_Registration_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2406.00123)）。

![img](https://img.tsuji.tech/corrmlp-cvpr2024-0.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-1.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- 自己注意機構を持たない多層パーセプトロン（MLP）は計算コストとメモリ使用量の点で効率的な手法の1つであるが、帰納的バイアスを考慮していない。
- この問題を解決するために、著者らは相関認識MLPベース（CorrMLP）ネットワークと呼ばれるレジストレーション手法を提案した。
- 2つの重要なポイントは、CNNベースの階層的特徴抽出エンコーダーと、相関認識粗密レジストレーションデコーダーである。
- 後段デコーダー内の相関認識マルチウィンドウMLP（CMW-MLP）ブロックは、前段エンコーダーによって抽出された複数サイズの特徴を処理し、CorrMLPがフル解像度画像上で細粒度の長距離特徴を利用することを可能にする。
- CorrMLPは画像レジストレーションのための局所的非線形変形と広範囲変形を解決できる。

## 性能評価手法

- CorrMLPをSyN、NifyReg、VoxelMorph、Swin-CoxelMorph、TransMorph、TransMatch、LapIRN、ULAE-net、Dual-PRNet++、SDHNet、NICE-Net、NICE-Transを含む他の手法と比較した。
- データセット：3D患者間脳画像レジストレーション用にADNI、ABIDE、ADHD、IXI、Mindboggle、Buckner、4D患者内心臓画像レジストレーション用にACDC。

![img](https://img.tsuji.tech/corrmlp-cvpr2024-2.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-3.jpg)

## 考察

- CorrMLPはDSCおよびNJD指標において他の手法（transformers、CNNs、MLPs）よりも優れた性能を示した。
- CorrMLPの最良性能には、画像レベルとステップレベルの両方の相関が必要である。

## 学んだこと

- 帰納的バイアスは、CNN（前段エンコーダー）とグローバル平均プーリング（後段デコーダー）の組み合わせによって実装されていると推測される。
- MLPsは帰納的バイアスを考慮しない。
- Transformerは画像内の広範囲特徴を捉える能力を持つが、計算量とメモリ消費を削減するためにダウンサンプル特徴が一般的に使用されるため、入力画像サイズでの細粒度長距離依存関係を扱うことは困難である可能性がある。
