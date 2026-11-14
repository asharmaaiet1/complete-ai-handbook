# Calculus

**Difficulty:** Intermediate  
**Prerequisites:** Mathematical foundations, especially functions, graphs, and algebra.  
**Useful starting point:** Learn derivatives and the chain rule first; integration can initially be studied for intuition.

## Overview

Calculus describes change and accumulation. For machine learning, the most useful part is understanding how a model's output or error changes when its parameters change.

## Topics Covered

### Change in one variable

- The idea of a limit as a value approaches a point.
- Derivative as local rate of change and slope.
- Common derivative rules, including the product and chain rules.
- Increasing, decreasing, and stationary points.

### Several variables

- Partial derivatives: change one input while holding the others fixed.
- Gradient: a vector of partial derivatives that points toward the direction of fastest local increase.
- Chain rule through nested functions; this is the core idea behind backpropagation.
- Jacobian as a table of derivatives for vector-valued functions; Hessian as second-order change information (optional).

### Accumulation

- Definite integral as accumulated quantity or area under a curve.
- Basic connection between differentiation and integration.
- Probability density as a function whose area over a range gives probability.

## AI Applications

Training often changes parameters to reduce a loss. Derivatives estimate how a small parameter change affects that loss. The chain rule lets a deep network pass this information backward through its layers. Integration appears in continuous probability and some generative models; most beginners can postpone detailed integration techniques.

## Recommended References

- [MIT OpenCourseWare 18.01SC: Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — free self-study course with lectures and practice.
- [MIT OpenCourseWare 18.02SC: Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) — use selected material on partial derivatives, gradients, and the chain rule.
- [3Blue1Brown: Calculus](https://www.3blue1brown.com/topics/calculus) — visual introduction to limits, derivatives, and integrals.

---

[← Previous: Linear Algebra](02-linear-algebra.md) · [Next: Probability Theory →](04-probability-theory.md)
