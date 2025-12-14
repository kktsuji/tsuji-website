---
title: "C++論理ANDとORの短絡評価"
description: ""
date: 2024-09-28T18:30:00+09:00
lastmod:
draft: false
---

C++の論理AND演算子`&&`と論理OR演算子`||`は短絡評価です。

- `&&`：最初のオペランドが条件を**満たさない**場合（== `false`）、2番目のオペランドは評価されません。
- `||`：最初のオペランドが条件を**満たす**場合（== `true`）、2番目のオペランドは評価されません。

```cpp
const auto x = 1;

if ((x > 1) && (x < 10)) { // (x > 1)がfalseの場合、(x < 10)は無視されます
    ...
}

if ((x > 0) || (x < 10)) { // (x > 0)がtrueの場合、(x < 10)は無視されます
    ...
}
```

このシステムを使用して、以下のようなコードを書くことができます：

```cpp
assert ((!(myclass = getInstance(key))) || !myclass->isValid());

// 以下と同等です：
myclass = getInstance(key);
if (myclass != NULL) assert(!myclass->isValid())
```

個人的には、2番目の書き方の方が読みやすいと感じますが。

参考文献：

- [https://en.wikipedia.org/wiki/Short-circuit_evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)
- [https://en.cppreference.com/w/cpp/language/operator_logical](https://en.cppreference.com/w/cpp/language/operator_logical)
