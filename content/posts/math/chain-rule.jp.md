---
title: "微分におけるChain Rule"
description: ""
date: 2025-10-22T7:00:00+09:00
lastmod:
draft: false
math: true
---

## Chain Rule

2つの微分可能な関数$g(x)$と$u(x)$がある場合、それらの合成関数$f(x) = g(u(x))$の導関数はchain ruleによって与えられる：

$$\frac{df}{dx} = \frac{dg}{du} \cdot \frac{du}{dx}$$

または

$$f'(x) = g'(u(x)) \cdot u'(x)$$
