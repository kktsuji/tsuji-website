---
title: '数学記号の定義'
description: '数学記号の定義をまとめます。記号の意味に加え、英語の読み方、LaTeXのコマンドも記載します。随時更新して追記していきます。'
date: 2024-03-08T08:57:04+09:00
lastmod: 2024-04-20T21:55:00+09:00
math: true
draft: false
---

数学記号の定義をまとめます。記号の意味に加え、英語の読み方、LaTeXのコマンドも記載します。随時更新して追記していきます。

## 集合論 (set theory)

### $\in, \ni, \notin, \notni$ (集合と元の帰属関係, set membership)

集合 $A$ と要素 (元) $x$ の帰属関係を意味する。$\in$ は含む (in, belongs to), $\notin$ は含まない (not in) と読む[^1] [^2]。

* $x \in A$: 
  * $x$ は $A$ に属する、$x$ は $A$ に含まれる
  * $x$ is an element of the set $A$, $x$ belongs to the set $A$, $x$ is in the set $A$
* $x \ni A$:
  * $A$ は $x$ を含む、$x$ は $A$ の要素である
  * The set $A$ contains $x$ as an element
* $x \notin A$:
  * $x$ は $A$ に含まれない。
  * $\neg(x \in A)$ とも書ける (see "[$\neg$ 論理否定](#neg-%E8%AB%96%E7%90%86%E5%90%A6%E5%AE%9A-logical-negation)")

LaTeX コマンドは以下。

* $\in$, `\in`
* $\ni$ , `\ni`
* $\notin$, `\notin`
* $\notni$ , `\notni`

機械学習の文脈では、以下のような記述で用いられることがある。

> 訓練データセット $C$ のあるサンプル $x$ ($C \in x$) が値として 2値を取る ($x \in \lbrace 0, 1 \rbrace$) 場合、損失関数としてロジスティック関数を用いることが多い。

### $\subset, \supset, \subseteq, \supseteq, \subsetneq, \supsetneq, \not\subset, \not\supset$ (集合同士の包含関係, set inclusion)

集合 $A$ と集合 $B$ の包含関係を意味する。ただし、記号 "$\subset$" に関して、意味が一意に定義されておらず、文脈により以下の2つの定義のどちらかが使用される[^1] [^2] [^3]。

* 部分集合 (subset):
  * $A \subset B$: $A$ は $B$ に含まれ、かつ $A$ と $B$ が等しい ($A$ の全要素が $B$ に含まれることを意味する)
  * $\forall A, x \in A \Rightarrow x \in B$ と書ける (see "[$\forall$ 全称限量](#forall-%E5%85%A8%E7%A7%B0%E9%99%90%E9%87%8F-universal-quantification)", "[$\Rightarrow$ 論理包含](#rightarrow-%E8%AB%96%E7%90%86%E5%8C%85%E5%90%AB-material-conditional)")
* 真部分集合 (proper subset):
  * $A \subset B$: $A$ と $B$ は異なっており、かつ $A$ の全ての元が $B$ に含まれる
  * $A \ne B \wedge \forall A, x \in A \Rightarrow x \in B$ と書ける (see "[$\wedge$ 論理和](#wedge-%E8%AB%96%E7%90%86%E5%92%8C-logical-and)")

LaTeX コマンドは以下。

* $\subset$, `\subset`
* $\supset$ , `\supset`
* $\subseteq$, `\subseteq`
* $\supseteq$, `\supseteq`
* $\subsetneq$, `\subsetneq`
* $\supsetneq$, `\supsetneq`
* $\not\subset$, `\not\subset`
* $\not\supset$, `\not\supset`

## 基本論理 (basic logic)

### $\neg$ (論理否定, logical negation)

$\neg$, `\neg`

### $\forall$ (全称限量, universal quantification)

### $\Rightarrow$ (論理包含, material conditional)

### $\wedge$ (論理和, logical and)

## Equality, equivalence and similarity

### $\approx$ (ほぼ等しい)

e.g. $\pi \approx 3.14159$

LaTeX command:

* $\approx$, `\approx`

### $\sim$ (チルダ)

1. $\approx$ (ほぼ等しい) の代わり。
2. 2つの数の桁数が同じ。
3. $X \sim N(\mu, \sigma^2$, 平均 $\mu$ 分散 $\sigma^2$ の正規分布に従う乱数 $x$。

LaTeX command:

* $\sim$, `\sim`

[^1]: [wikipedia.org/wiki/glossary_of_mathematical_symbols](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)

[^2]: [wikipedia.org/wiki/数学記号の表](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E8%A8%98%E5%8F%B7%E3%81%AE%E8%A1%A8)

[^3]: [wikipedia.org/wiki/部分集合](https://ja.wikipedia.org/wiki/%E9%83%A8%E5%88%86%E9%9B%86%E5%90%88)
