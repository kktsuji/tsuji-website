---
title: "C++のconst型修飾子を型の後に置く"
description: ""
date: 2024-10-01T9:00:00+09:00
lastmod:
draft: false
---

**ベストプラクティス：** `const`型修飾子を、修飾したい型の右側に置きます。

```cpp
int var: // varはint型
int const var: // varはconst int型

int * ptr; // ptrはintへのポインター
int const * ptr; // ptrはconst intへのポインター
int * const ptr; // prtはintへのconstポインター
int const * const ptr; // ptrはconst intへのconstポインター

int ** ptr; // ptrはintへのポインターへのポインター
int const ** ptr; // ptrはconst intへのポインターへのポインター
int * const * ptr; // ptrはintへのconstポインターへのポインター
int ** const ptr; // ptrはintへのポインターへのconstポインター
int const * const * const ptr; // ptrはconst intへのconstポインターへのconstポインター
```

C++の`const`型修飾子はまずその左側に適用されます[1]。[1]が存在しない場合は、右側を修飾します[2]。

```cpp
[1] const [2]
```

以下は同じ意味です：

```cpp
int const var:
const int var: // 同じ意味
```

しかし、ポインターに`const`を適用したい場合は複雑になります。

```cpp
const int * ptr; // 右側を修飾：ptrはconst intへのポインター
int const * ptr: // 左側を修飾：ptrはconst intへのポインター
int * const ptr: // 左側を修飾：ptrはintへのconstポインター
```

もちろん、これらは正しく動作します。しかし、ソースコードに両方のスタイルがある場合は見苦しくなります。

シンプルな解決策は、型の右側のみに`const`を適用することです。つまり、[1]スタイルのみを使用します。

明確なコーディング規則があれば、このような複雑な構文で書かれている場合でも、コードは理解しやすくなります。

```cpp
int const ** const ptr; // ptrはconst intへのポインターへのconstポインター
```

注：オープンソースプロジェクトや会社のコードに貢献する場合は、既存のコードの書き方やプロジェクトのコーディング規則に従う方が良いです。

参考文献：

- [https://stackoverflow.com/questions/20656539/const-before-or-after-the-type](https://stackoverflow.com/questions/20656539/const-before-or-after-the-type)
