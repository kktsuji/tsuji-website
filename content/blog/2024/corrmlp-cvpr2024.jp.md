---
title: 'CorrMLP: 相関を考慮した MLP に基づく coarse-to-fine 位置合わせ, CVPR2024'
description: 'CorrMLP を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-25T20:26:48+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Meng et al., Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Meng_Correlation-aware_Coarse-to-fine_MLPs_for_Deformable_Medical_Image_Registration_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2406.00123)).

![img](https://img.tsuji.tech/corrmlp-cvpr2024-0.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-1.jpg)

(本ポストの図と表は論文からの引用である)

## 論文の新規性

* Self-attention を用いない多層パーセプトロン (MLP, multi-layer perceptron) は、計算コストとメモリ使用量の点で効率的な手法の一つであるが、帰納バイアスを考慮しない。
* この問題を解決するために、著者らは 相関を考慮した MLP に基づく (CorrMLP, correlation-aware MLP-based) 位置合わせ手法を提案した。
* CNN に基づく階層的特徴抽出エンコーダと、相関を考慮した粗から詳細への位置合わせデコーダ  (correlation-aware coarse-to-fine registration) の2つがポイントである。
* 後段のデコーダの相関考慮型マルチウィンドウ MLP (CMW-MLP, Correlation-aware multi-window MLP) ブロックは、前段のエンコーダで抽出された複数サイズの特徴量を扱うため、CorrMLP はフル解像度の画像における詳細かつ広域な特徴量を使用することが可能となる。
* CorrMLP は、画像位置合わせのための局所的な非線形変形と広範囲変形の両方を解決することができる。

## 性能評価手法

* CorrMLPは他の手法 (SyN, NifyReg, VoxelMorph, Swin-CoxelMorph, TransMorph, TransMatch, LapIRN, ULAE-net, Dual-PRNet++, SDHNet, NICE-Net, NICE-Trans) と比較された。
* データセット：ADNI, ABIDE, ADHD, IXI, Mindboggle, Buckner（患者の脳の 3D 画像位置合わせ向け）、ACDC（患者の心臓の 4D 画像位置合わせ向け）。

![img](https://img.tsuji.tech/corrmlp-cvpr2024-2.jpg)

![img](https://img.tsuji.tech/corrmlp-cvpr2024-3.jpg)

## 議論

* CorrMLP は、DSC と NJD の指標において、他の手法（トランスフォーマ、CNN、MLP）よりも優れたパフォーマンスを示した。
* CorrMLP の最高性能のためには、画像レベルとステップレベルの相関が両方必要である。

## 学んだこと

* CorrMLP において、帰納バイアスは、CNN（前者のエンコーダー）とグローバル平均プーリング（後者のデコーダー）の組み合わせによって実装されている（と私は予想する）。
* MLP は帰納バイアスを考慮しない。
* トランスフォーマは画像中の広範囲な特徴を捉える能力を持つ。しかし、計算量とメモリ消費量を減らすため、ダウンサンプリングされた特徴が一般的に使用されるため、入力画像サイズのきめ細かいかつ広域な特徴を扱うのは難しい。
