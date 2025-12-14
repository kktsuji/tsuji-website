---
title: "数学における実数R"
description: ""
date: 2025-08-23T9:00:00+09:00
lastmod:
draft: false
math: true
---

## 実数 $ \mathbb{R} $

記号$ \mathbb{R} $（または$ R $）は、すべての実数の集合を表す。

- LaTeXコマンド: `\mathbb{R}`

### 有理数 $ \mathbb{Q} $

- 整数: $ \mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\} \subset \mathbb{Q} $
- 分数: $ \frac{a}{b} $ ここで$ a, b \in \mathbb{Z} $かつ$ b \neq 0 $
- 有限小数: 例: $ 0.5, 1.75, -2.0 $
- 循環小数: 例: $ 0.333\ldots, 0.123123\ldots $

### 無理数

- 非循環、非有限小数: 例: $ \sqrt{2}, \pi, e $

### 非実数

- 複素数: $ \mathbb{C} = \{ a + bi \mid a, b \in \mathbb{R}, i = \sqrt{-1} \} $
- 虚数: 例: $ 3i, -2i $
- 無限大: 例: $ +\infty, -\infty $

注記:

```text
複素数
├── 実数: a + 0i（実部 ≠ 0）
└── 虚数:（虚部 ≠ 0）
    ├── 純虚数: 0 + bi
    └── 非実複素数: a + bi（a≠0、b≠0）
```

## 次元$ D $を伴う場合

記号$ \mathbb{R}^D $は、$ D $次元空間におけるすべての実数の集合を表す。

例:

- $ \mathbb{R}^1 $: 1次元空間（直線）。
- $ \mathbb{R}^2 $: 2次元空間（平面、座標(x, y)）。
- $ \mathbb{R}^3 $: 3次元空間（空間、座標(x, y, z)）。
- $ \mathbb{R}^D $: $ D $次元空間（座標($ x_1, x_2, \ldots, x_D $)）。
