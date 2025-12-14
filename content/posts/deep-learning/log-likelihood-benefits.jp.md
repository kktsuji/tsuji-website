---
title: "Maximum Likelihood EstimationにおけるLog-Likelihoodの利点"
description: ""
date: 2025-10-20T18:00:00+09:00
lastmod:
draft: false
math: true
---

## Log-Likelihood

確率モデルにおける観測データ$ D = \{x_0, x_1, \ldots, x_n\} $のlikelihoodは、データがモデルから生成される確率を表す。Likelihood関数は次のように定義される：

$ L(\theta; D) = P(D | \theta) = \prod\_{i=0}^{n} P(x_i | \theta) $

ここで、$ \theta $はモデルのパラメータを表し、$ P(x_i | \theta) $はパラメータ$ \theta $が与えられたときにデータポイント$ x_i $を観測する確率である。

Log-likelihoodはlikelihood関数の自然対数である：

$ \log L(\theta; D) = \sum\_{i=0}^{n} \log P(x_i | \theta) $

## Log-Likelihoodの利点

### 1. 計算コストの削減

積の微分は次のように得られる：

$ (f \cdot g)' = f' \cdot g + f \cdot g' $

一方、和の微分は次のように得られる：

$ (f + g)' = f' + g' $

Likelihood関数の勾配を計算する際、積の法則を適用する必要があり、特に大規模なデータセットでは計算コストが高くなる可能性がある。対照的に、log-likelihood関数では和の法則を使用でき、計算効率が向上する。

### 2. 数値的安定性

多くの小さな確率を乗算すると、結果が極めて小さくなり、数値アンダーフローが発生する可能性がある。Likelihoodの対数を取ることで、確率の積をlog確率の和に変換し、数値的安定性を維持し、アンダーフローを防ぐのに役立つ。

アンダーフローが発生すると、likelihoodは次のように近似できる：

$ L(\theta; D) \approx 0 $

これにより勾配がゼロに等しくなり、学習プロセスが停止する。

### 3. アルゴリズム最適化

Gradient descentなどの多くの最適化アルゴリズムは、積よりも和でより効率的に動作する。

- 勾配とHessiansの計算が容易になる
- 計算の並列化
- 計算中の数値的安定性
- 最適化アルゴリズムの実装の簡素化
