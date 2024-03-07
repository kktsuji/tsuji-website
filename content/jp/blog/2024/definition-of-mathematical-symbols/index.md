---
title: '数学記号の定義'
slug: 'definition of mathematical symbols'
description: '数学記号の定義をまとめます。'
date: 2024-03-06T08:57:04+09:00
math: true
draft: false
---

## はじめに

数学記号の定義をまとめます。記号の意味に加え、英語の読み方、LaTeXのコマンドも記載します。随時更新して追記していきます。


## 集合論 (set theory)

### $\in$, $\ni$ (set membership)

集合 $S$ が要素（元）$x$ を含むことを意味する。$\in$ は含む、in, belongs to と読む[^1] [^2]。

* $x \in S$: 
  * 要素（元）$x$ は集合 $S$ に属する、$x$ は $S$ に含まれる
  * $x$ is an element of the set $S$, $x$ belongs to the set $S$, $x$ is in the set $S$
* $x \ni S$:
  * 集合 $S$ は要素（元）$x$ を含む、$x$ は $S$ の要素である
  * The set $S$ contains $x$ as an element

LaTeX コマンドは以下。

* $\in$, ``\in``
* $\ni$ , ``\ni``

機械学習の文脈では、以下のような記述で用いられることがある。

> 学習データセット $C$ のあるサンプル $x$ ($C \in x$) が値として 2値を取る ($x \in \lbrace 0, 1 \rbrace$) 場合、損失関数としてロジスティック関数を用いることが多い。


## 更新履歴

None for now.

[^1]: [wikipedia.org/wiki/Glossary_of_mathematical_symbols](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)

[^2]: [wikipedia.org/wiki/数学記号の表](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E8%A8%98%E5%8F%B7%E3%81%AE%E8%A1%A8)
