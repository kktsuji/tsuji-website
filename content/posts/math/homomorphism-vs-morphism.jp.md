---
title: "Homomorphism v.s. Morphism"
description: ""
date: 2024-12-14T9:00:00+09:00
lastmod:
draft: false
math: true
---

Microsoft Copilotによって生成:

## HomomorphismとMorphismの違い

数学において、**homomorphism**と**morphism**は代数的構造間の構造保存写像を記述するために使用される概念であるが、わずかに異なる文脈で使用される。

### Homomorphism

**Homomorphism**は群、環、またはベクトル空間のような代数的構造に適用される特定のタイプのmorphismである。これは同じタイプの2つの構造間の写像であり、それらの構造上で定義された演算を保存する。例えば、$ f $が2つの群$ G $と$ H $の間のhomomorphismである場合、$ G $のすべての要素$ a $と$ b $に対して：

$$ f(ab) = f(a)f(b) $$

これは、$ G $における演算（加法や乗法など）が写像$ f $の下で$ H $において保存されることを意味する。

### Morphism

**Morphism**は圏論において圏内のオブジェクト間の写像を記述するために使用されるより一般的な用語である。圏は代数的構造だけでなく、様々な構造を含むことができる。Morphismは圏によって定義された特定の性質を満たさなければならないが、これらの性質は大きく異なる可能性がある。本質的に、すべてのhomomorphismはmorphismであるが、すべてのmorphismがhomomorphismであるわけではない。

### 主な違い

1. **範囲**: Homomorphismは代数的構造に特有であり、morphismは圏論のより広い文脈で使用される。
2. **保存**: Homomorphismは特に代数的演算を保存するが、morphismはそれらが属する圏によって定義された構造を保存する。
3. **使用法**: Homomorphismは群論、環論、線形代数などの分野で使用される。Morphismは多くの異なるタイプの数学的構造を包含できる圏論で使用される。

## 参考文献

- [Homomorphism - Wiki](https://en.wikipedia.org/wiki/Homomorphism)
- [math.libretexts.org](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/First-Semester_Abstract_Algebra%3A_A_Structural_Approach_%28Sklar%29/03%3A_Homomorphisms_and_Isomorphisms/3.02%3A_Definitions_of_Homomorphisms_and_Isomorphisms).
