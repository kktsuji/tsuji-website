---
title: 'Put C++ Const Type Qualifier After the Type'
description: ''
date: 2024-10-01T9:00:00+09:00
lastmod: 
draft: false
---

**Best Pratice:** Put `const` type qualifier at the right side of a type you want to decorate.

```cpp
int var: // var is an int
int const var: // var is a const int

int * ptr; // ptr is a pointer to an int
int const * ptr; // ptr is a pointer to a const int
int * const ptr; // prt is a const pointer to an int
int const * const ptr; // ptr is a const pointer to const an int

int ** ptr; // ptr is a pointer to a pointer to an int
int const ** ptr; // ptr is a pointer to a pointer to a const int
int * const * ptr; // ptr is a pointer to a const pointer to an int
int ** const ptr; // ptr is a const pointer to a pointer to an int
int const * const * const ptr; // ptr is a const pointer to a const pointer to const an int
```

C++'s `const` type qualifier first applys to the left of it [1]. If [1] has none, then it decorates the right side [2].

```cpp
[1] const [2]
```

The followings means the same thing:

```cpp
int const var:
const int var: // same meaning
```

But if you want to apply `const` to a pointer, it gets complicated.

```cpp
const int * ptr; // decorates right: ptr is a pointer to a const int
int const * ptr: // decorates left: ptr is a pointer to an const int
int * const ptr: // decorates left: ptr is a const pointer to an int
```

Of cource, these correctly work. But it looks ugly if there are both styles in your source code.

The simple solution is to apply `const` to the only right side of a type, which means use only [1] style.

If you have a clear coding rule, your code is easier to understand, even when written in complex syntax like this.

```cpp
int const ** const ptr; // ptr is a const pointer to a pointer to a const int
```

Note: When you contribute open source projects or company's code, it's better to follow the writing style of existing code and the coding rules of the project.

Reference:

- [https://stackoverflow.com/questions/20656539/const-before-or-after-the-type](https://stackoverflow.com/questions/20656539/const-before-or-after-the-type)
