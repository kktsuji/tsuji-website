---
title: 'RichHF-18K: 1.8万枚の画像に対する人間のフィードバックデータベース, CVPR2024 Best Paper Award'
description: 'RichHR-18K を提案する CVPR2024 の論文のサマリ。'
date: 2024-06-29T15:01:22+09:00
lastmod: 
math: false
draft: false
---

## 概要

Paper: Liang et al., Rich Human Feedback for Text-to-Image Generation ([cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Liang_Rich_Human_Feedback_for_Text-to-Image_Generation_CVPR_2024_paper.pdf) or [arxiv](https://arxiv.org/abs/2312.10240)).

この論文は [CVPR2024 best paper award](https://cvpr.thecvf.com/Conferences/2024/News/Awards) を受賞している。

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-0.jpg)

(本ポストの図と表は論文からの引用である)

## 論文の新規性

* 著者らは "RichHF-18K" (Rich Human Feedback on 18K generated images) と呼ばれる新しいデータセットを提案した。データセットは以下を含む：
  1. アノテーション：生成AIにより生成された画像中の非現実的な領域、アーチファクト領域、テキストと画像のズレ部分。
  2. ラベル付きプロンプト：生成された画像とプロンプトを比較して、欠落している、または誤って表現されている単語。
  3. 4つのスコア：生成された画像のもっともらしさ、テキストと画像の整合性、美しさ、総合評価。
* RichHR-18K データセットは [彼らの GitHub リポジトリ](https://github.com/google-research/google-research/tree/master/richhf_18k) で公開されている。
* また、ViT と T5X をベースとした "RAHF" (Rich Automatic Human Feedback) と呼ばれる新しいマルチモーダルのトランスフォーマアーキテクチャを提案した。これは、プロンプトと、それを用いて生成された画像のペアを受け取り、(1)入力画像内の非現実的な領域と、表現ミス領域のヒートマップ、(2)スコア、(3)入力プロンプト内の表現ミス単語、を予測する。
* また彼らは、RAHF で予測されたスコアを用いて既存モデルのファインチューニングを行ったり、予測されたヒートマップとスコアを用いてインペインティングを行うなど、他のタスクの改善にも有効であることを示した。

## 性能評価手法

* 彼らは ResNet-50, PickScore, CLIP と比較することで RAHF の性能を評価した。
* 評価指標として次を用いた：Pearson linear correlation coefficient (PLCC), Spearman rank correlation coefficient (SRCC) are used for score evaluation. Mean square error (MSE), CC, KLD, SIM, NSS and AUC-Judd are utilized for heatmap. Precision, Recall, F1 Score。
* 人間の判定者により、オリジナルの Muse と、RAHF のスコアによりファインチューニングされた Muse と、どちらの性能が優れているかを定性評価した。

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-1.jpg)

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-2.jpg)

## 議論

* HARF はほとんどの指標で他のモデルを上回る性能を示した。
* 表現ミスヒートマップの評価において、HARF が ResNet-50 よりも劣っていた理由は、Ground Truth 領域の定義が不十分であったためと著者らは考えている。
* 人間による定量的評価では、50%以上のサンプルで、ファインチューニングされた Muse は、オリジナルのものよりも有意に、もしくはわずかに優れていると判定された。
* RichHF-18K データセットと HARF モデルを活用する方法は数多く考えられると著者らは述べている。

## 学んだこと

* AI モデルの学習のために、別の AI モデルが活用されている（Muse のファインチューニングのための入力プロンプトは、他の LLM モデルである PaLM2 によって生成された）。
* トップレベルの研究は、著者の成果を述べるだけでなく、AI研究者全体の今後の研究の方向性も示している。
