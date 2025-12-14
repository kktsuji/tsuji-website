---
title: "Prompting Medical Large Vision-Language Models to Diagnose Pathologies by Visual Question Answering"
description: ""
date: 2024-08-07T09:00:00+09:00
lastmod:
draft: false
---

Title: Prompting Medical Large Vision-Language Models to Diagnose Pathologies by Visual Question Answering

Authors: Danfeng Guo, Demetri Terzopoulos

Published: Jul 31 2024

Link: [https://arxiv.org/abs/2407.21368](https://arxiv.org/abs/2407.21368)

Summary:

- 著者らは医療用大規模vision-languageモデル（LVLM）におけるハルシネーションを低減し、visual question answering（VQA）タスクを改善するための2つのプロンプト手法を導入した：
  1. 質問クエリに詳細な病理学的説明を提供する。
  2. 参考意見として予測結果を質問クエリに提供する「weak learner」を導入する。
- 提案手法はMIMIC-CXR-JPGとChexpertデータセットにおいて診断F1スコアを最大0.27改善した。

Summary（Microsoft Copilot生成）：

要約は次の通り：

- **Introduction**: 本論文は医療画像からの病理診断に焦点を当てた医療Visual Question Answering（VQA）タスクにおけるLarge Vision-Language Models（LVLM）の応用について議論している。

- **Challenges**: LVLMはハルシネーション問題に悩まされ、不均衡な訓練データのためにマイノリティ病理に苦しんでいる。

- **Methods**: 2つのプロンプト戦略が提案されている：病理の詳細な説明を提供することと、VQAパフォーマンスを改善するためにweak learnerモデルを使用すること。

- **Novelties**: 本研究はハルシネーションを低減し診断精度を向上させるための費用対効果の高いプロンプト戦略を導入している。

- **Results**: 提案された手法は診断F1スコアを大幅に改善し、最大増加量は0.27である。

- **Performances**: これらの戦略はRecallを約0.07向上させ、偽陰性予測を削減する。

- **Limitations**: これらの戦略は極端にデータが希少な病理に対しては効果が低い。

- **Discussion**: 将来の研究では、希少なカテゴリを扱うためのRetrieval Augmented Generation（RAG）のような戦略を探求できる。
