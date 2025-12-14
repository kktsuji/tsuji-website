---
title: "機械学習向けのGPUリソース"
description: ""
date: 2024-07-27T15:43:49+09:00
lastmod:
draft: false
---

## 無料のリソース

### 大学の研究室

- メリット：
  - 最も簡単で柔軟な手段。
  - 使用するにあたりマニュアルやサポートがあると思われる。
- デメリット：
  - GPUの質は研究室の予算に依存する。
  - 繁忙期には、リソースが空くまで待つ必要がある可能性がある。
  - プロジェクトの再現性が低くなる可能性がある。ソースコードを公開する場合、ドキュメンテーションを慎重に作成する必要がある。

### GoogleのTPU Research Cloud

[TPU Research Cloud](https://sites.research.google/trc/about/)は研究者へ無料でクラウドの計算リソースを提供している。

- メリット：
  - Tensor Processing Unit (TPU)を無料で使用できる。
- デメリット：
  - TPUへの30日間の無料アクセスには、事前の申請と承認が必要。
  - TPUは無料だが、データセットのストレージなど、他のGoogle Cloud Platformサービスは有料。
  - Pytorch (Meta製) も使用できるが、TPUにおいてはTensorFlow（Google製）の方が性能が優れていると言われている。これは、TensorFlowがTPUをネイティブにサポートしているためである。

### Google Colab（無料プラン）

[Google Colab](https://colab.research.google.com/).

- メリット：
  - プロジェクトの再現性が高い。
- デメリット：
  - 無料枠はマシンパワーが弱く、かつ時間制限がある。

## 有料のリソース

### 自分自身のGPU

- メリット：
  - 一度GPUを購入すると、電気代以外は無料。
  - いつでも利用可能。
- デメリット：
  - GPUは時代遅れになりやすい（進化が早いため）。
  - GPUの稼働率が低い場合、クラウドサービスのオンデマンド利用に比べ、費用対効果が低くなる可能性がある。
  - GPUが故障する可能性がある。
  - ソースコードの再現性が低くなる可能性がある。

### クラウドサービス

様々なサービスが存在するため、コストを比較し利用する。

- [Google Colab（有料プラン）](https://colab.research.google.com/)
- [GCP (Google Cloud Platform)](https://console.cloud.google.com/welcome)
- [AWS (Amazon Web Service)](https://aws.amazon.com/)
- [Microsoft Azure](https://portal.azure.com/)
- など
