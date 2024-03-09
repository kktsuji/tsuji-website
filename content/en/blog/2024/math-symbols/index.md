---
title: 'Definition of Mathematical Symbols'
slug: 'math-symbols'
description: 'Some of the mathematical symbols are presented with their meanings, ways of reading, and LaTeX commands. The rest will be added later continuously.'
date: 2024-03-08T08:57:04+09:00
math: true
draft: false
---

On this page, some of the mathematical symbols are presented with their meanings, ways of reading, and LaTeX commands. The rest will be added later continuously.

## Set theory

### $\in, \ni, \notin, \notni$ (set membership)

Set membership represents the relationship between a set $A$ and its element $x$[^1] [^2].

* $x \in A$: 
  * $x$ is an element of the set $A$. $x$ belongs to the set $A$. $x$ is in the set $A$.
* $x \ni A$:
  * The set $A$ contains $x$ as an element.
* $x \notin A$:
  * $x$ is not an element of the set $A$.
  * This can also be written as $\neg(x \in A)$ (see "[$\neg$ logical negation](#neg-logical-negation)").

LaTeX commands:

* $\in$, ``\in``
* $\ni$ , ``\ni``
* $\notin$, ``\notin``
* $\notni$ , ``\notni``

On the machine learning context, set membership is used like below:

*If a sample $x$ in a training dataset $C$ ($C \in x$) takes binary values ($x \in \lbrace 0, 1 \rbrace$), the logistic function is often used as a loss function.*

### $\subset, \supset, \subseteq, \supseteq, \subsetneq, \supsetneq, \not\subset, \not\supset$ (set inclusion)

Set inclusion represents the relationship between a set $A$ and a set $B$. **Note:** There are two ways to use these symbols depends on contexts[^1] [^2] [^3].

* Subset:
  * $A \subset B$: $A$ is included in $B$, and possibly is equal to $B$, which means every elements of $A$ is included in $B$.
  * This can be written as $\forall A, x \in A \Rightarrow x \in B$ (see "[$\forall$ universal quantification](#forall-universal-quantification)", "[$\Rightarrow$ material conditional](#rightarrow-material-conditional)").
* Proper subset:
  * $A \subset B$: $A$ is not equal to $B$, and every elements of $A$ belongs to $B$.
  * It is equal to $A \ne B \wedge \forall A, x \in A \Rightarrow x \in B$ (see "[$\wedge$ logical and](#wedge-logical-and)").

LaTeX commands:

* $\subset$, ``\subset``
* $\supset$ , ``\supset``
* $\subseteq$, ``\subseteq``
* $\supseteq$, ``\supseteq``
* $\subsetneq$, ``\subsetneq``
* $\supsetneq$, `\supsetneq`
* $\not\subset$, ``\not\subset``
* $\not\supset$, ``\not\supset``

## Basic logic

### $\neg$ (logical negation)

$\neg$: ``\neg``

### $\forall$ (universal quantification)

### $\Rightarrow$ (material conditional)

### $\wedge$ (logical and)

[^1]: [wikipedia.org/wiki/glossary_of_mathematical_symbols](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)

[^2]: [jp.wikipedia.org/wiki/list_of_mathematical_symbols](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%AD%A6%E8%A8%98%E5%8F%B7%E3%81%AE%E8%A1%A8)

[^3]: [jp.wikipedia.org/wiki/subset](https://ja.wikipedia.org/wiki/%E9%83%A8%E5%88%86%E9%9B%86%E5%90%88)
