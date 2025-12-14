---
title: "Short-Circuit Evaluation of C++ Logical AND OR"
description: ""
date: 2024-09-28T18:30:00+09:00
lastmod:
draft: false
---

C++'s logical AND operator `&&` and logical OR operator `||` are short-circuit evaluations.

- `&&`: If the first operand is **not satisfies** the condition (== `false`), the second one will not evaluated.
- `||`: If the first operand is **satisfies** the condition (== `true`), the second one will not evaluated.

```cpp
const auto x = 1;

if ((x > 1) && (x < 10)) { // (x > 1) is false, then (x < 10) is ignored.
    ...
}

if ((x > 0) || (x < 10)) { // (x > 0) is true, then (x < 10) is ignored.
    ...
}
```

Using this system, we can write a code like below:

```cpp
assert ((!(myclass = getInstance(key))) || !myclass->isValid());

// Equals to below:
myclass = getInstance(key);
if (myclass != NULL) assert(!myclass->isValid())
```

Personally, I feel the second writing style is easier to read, though.

References:

- [https://en.wikipedia.org/wiki/Short-circuit_evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)
- [https://en.cppreference.com/w/cpp/language/operator_logical](https://en.cppreference.com/w/cpp/language/operator_logical)
