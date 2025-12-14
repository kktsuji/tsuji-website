---
title: "テキストから画像生成のための豊富な人間フィードバック、CVPR2024最優秀論文賞"
description: ""
date: 2024-06-29T15:01:22+09:00
lastmod:
draft: false
---

## 概要

論文：Liang et al., Rich Human Feedback for Text-to-Image Generation（[cvpr2024 open access](https://openaccess.thecvf.com/content/CVPR2024/papers/Liang_Rich_Human_Feedback_for_Text-to-Image_Generation_CVPR_2024_paper.pdf)または[arxiv](https://arxiv.org/abs/2312.10240)）。

本論文は[CVPR2024最優秀論文賞受賞者](https://cvpr.thecvf.com/Conferences/2024/News/Awards)の1つである。

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-0.jpg)

（この記事の図表は元論文から引用）

## 論文の新規性

- 以下の3つの情報で構成される「Rich Human Feedback on 18K generated images」（RichHF-18K）と呼ばれる新しいデータセットを提案した：
  1. ポイントアノテーション：生成画像内の不自然な領域、アーティファクト領域、テキストと画像の不一致部分。
  2. ラベル付けされたプロンプト単語：プロンプト内の欠落または誤表現された概念の単語。
  3. 4つのスコア：生成画像の妥当性、テキストと画像の整合性、美的評価、総合評価。
- RichHR-18Kデータセットは[GitHubリポジトリ](https://github.com/google-research/google-research/tree/master/richhf_18k)で公開されている。
- ViTとT5Xに基づく「Rich Automatic Human Feedback」（RAHF）と呼ばれる新しいマルチモーダルtransformerアーキテクチャも提案した。これは、プロンプトと対応するプロンプトを使用して生成された画像のペアを入力として受け取り、（1）入力画像内の不自然さと不一致領域のヒートマップ、（2）入力のスコア、（3）入力プロンプト内の不一致単語を予測する。
- 予測されたスコアによる既存モデルのファインチューニングや、予測されたヒートマップとスコアによるインペインティングタスクなど、RAHFが他のタスクを改善する能力を示した。

## 性能評価手法

- RAHFの性能をResNet-50、PickScore、CLIPと比較して評価した。
- スコア評価にはPearson線形相関係数（PLCC）、Spearmanランク相関係数（SRCC）が使用される。ヒートマップには平均二乗誤差（MSE）、CC、KLD、SIM、NSS、AUC-Juddが利用される。テキスト評価にはPrecision、Recall、F1スコアが使用される。
- 元のMuseとRAHFスコアでファインチューニングされたMuseによって、どちらの生成画像が優れているかを人間が評価した。

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-1.jpg)

![img](https://img.tsuji.tech/richhf-18k-cvpr2024-2.jpg)

## 考察

- HARFはほとんどの指標で他のモデルを上回る性能を示した。
- 不一致ヒートマップの評価においてHARFがResNet-50より劣っていた理由は、グラウンドトゥルース領域の定義が不十分であったためである可能性がある。
- 人間による定量評価では、50%以上のサンプルにおいて、ファインチューニングされたMuseが元のものよりも有意にまたはわずかに優れていると判断された結果が示された。
- RichHF-18KデータセットとHARFモデルを活用する方法は数多くあると言及した。

## 学んだこと

- AIは他のAIモデルの訓練に利用される（Museのファインチューニング用の入力プロンプトは他のLLMモデルPaLM2によって生成された）。
- トップレベルの研究は成果を示すだけでなく、AI研究者のための将来の研究方向も示す。
