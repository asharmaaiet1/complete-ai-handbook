# Calculus

## Learning objectives

By the end of this guide, you should be able to:

- Explain a derivative as a measure of local change.
- Describe what a gradient tells us about a function with several inputs.
- Explain why derivatives help a model adjust its parameters during training.

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

## Learn the idea

A derivative describes how quickly a value changes near a chosen point. If a small change in a parameter causes a large change in the loss, the derivative has a large magnitude. A positive derivative means increasing the parameter raises the value locally; a negative one means it lowers it.

For a function with many inputs, the gradient collects one derivative for each input. It points toward the direction of fastest increase. To reduce a loss, training usually moves a little in the opposite direction. The chain rule helps find how a change travels through several linked calculations, which is why it is central to training layered models.

## Example in AI: deciding how to adjust a model

During training, a model compares a prediction with the right answer and gets a loss. To see how a parameter affects that loss, use the simple example `L(w) = (w − 3)²`. Its derivative is `2(w − 3)`. At `w = 1`, the derivative is `−4`, which tells us that a small increase in `w` should reduce the loss nearby. With a step size of `0.1`, an update gives `w = 1 − 0.1 × (−4) = 1.4`; the loss falls from 4 to 2.56. Derivatives are useful here because they tell training which direction to try. This simple curve is only an illustration; real model losses can be more complex.

## Try it

For `L(w) = (w − 3)²`, what is the derivative at `w = 2`?

??? success "Check your answer"
    The derivative is `2(w − 3)`, so at 2 it is `−2`.

## AI Applications

Training often changes parameters to reduce a loss. Derivatives estimate how a small parameter change affects that loss. The chain rule lets a deep network pass this information backward through its layers. Integration appears in continuous probability and some generative models; most beginners can postpone detailed integration techniques.

## Recommended References

- [MIT OpenCourseWare 18.01SC: Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — free self-study course with lectures and practice.
- [MIT OpenCourseWare 18.02SC: Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) — use selected material on partial derivatives, gradients, and the chain rule.
- [3Blue1Brown: Calculus](https://www.3blue1brown.com/topics/calculus) — visual introduction to limits, derivatives, and integrals.

---

[← Previous: Linear Algebra](02-linear-algebra.md) · [Next: Probability Theory →](04-probability-theory.md)
