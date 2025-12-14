---
title: "Benefits of Log-Likelihood in Maximum Likelihood Estimation"
description: ""
date: 2025-10-20T18:00:00+09:00
lastmod:
draft: false
math: true
---

## Log-Likelihood

The likelihood of observed data $ D = \{x_0, x_1, \ldots, x_n\} $ in a probability model represents the probability that the data is generated from the model. The likelihood function is defined as follows:

$ L(\theta; D) = P(D | \theta) = \prod\_{i=0}^{n} P(x_i | \theta) $

Where $ \theta $ represents the parameters of the model and $ P(x_i | \theta) $ is the probability of observing data point $ x_i $ given the parameters $ \theta $.

Log-likelihood is the natural logarithm of the likelihood function:

$ \log L(\theta; D) = \sum\_{i=0}^{n} \log P(x_i | \theta) $

## Benefits of Log-Likelihood

### 1.Lower Computational Cost

The derivative of a product is obtained as follows:

$ (f \cdot g)' = f' \cdot g + f \cdot g' $

On the other hand, the derivative of a sum is obtained as follows:

$ (f + g)' = f' + g' $

When calculating the gradient of the likelihood function, the product rule must be applied, which can be computationally expensive, especially for large datasets. In contrast, the log-likelihood function allows us to use the sum rule, which is computationally more efficient.

### 2.Numerical Stability

When multiplying many small probabilities togather, the result can become extremely small, leading to numerical underflow. By taking the logarithm of the likelihood, we convert the product of probabilities into a sum of log-probabilities, which helps to maintain numerical stability and prevents underflow.

If the underflow occurs, the likelihood can be approximated as follows:

$ L(\theta; D) \approx 0 $

Which leads to the gradient equal to zero and stops the learning process.

### 3.Algorithmic Optimization

Many optimization algorithms, such as gradient descent, work more efficiently with sums rather than products.

- Easier to compute gradients and Hessians.
- Parallelization of computations.
- Numerical stability during calculations.
- Simplified implementation of optimization algorithms.
