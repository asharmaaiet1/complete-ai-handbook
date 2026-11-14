# Numerical Methods and Computational Mathematics

**Difficulty:** Intermediate  
**Prerequisites:** Mathematical foundations, linear algebra, and basic programming; calculus helps for numerical differentiation.

## Overview

Computers store and calculate finite approximations to real numbers. Numerical mathematics studies how those approximations affect answers and how to choose algorithms that remain useful and stable.

## Topics Covered

### Finite precision

- Floating-point numbers and rounding error.
- Overflow, underflow, and cancellation when subtracting nearly equal values.
- Stable alternatives such as log-sum-exp for calculations involving exponentials.

### Problem sensitivity and algorithm behavior

- Conditioning: how sensitive the mathematical problem is to small input changes.
- Stability: how much error an algorithm adds while computing an answer.
- The distinction matters: a stable algorithm cannot remove sensitivity inherent in a problem.

### Computation for AI

- Solving linear systems without explicitly computing a matrix inverse.
- Approximation, iterative algorithms, and stopping tolerances.
- Finite-difference checks for derivatives and their limitations.
- Accumulation of rounding error in long sums and low-precision calculations.
- Scaling inputs and choosing sensible units.

## Learn the idea

Computers have a limited number of bits to represent numbers, so many real values are stored as nearby approximations. Small rounding differences are normal. Problems arise when an algorithm amplifies them, when a value is too large or too small to represent, or when nearly equal numbers are subtracted and useful digits disappear.

Two ideas help diagnose numerical problems. Conditioning describes how sensitive the question itself is to small input changes. Stability describes whether the chosen calculation adds much extra error. A sensitive problem can challenge even a careful algorithm; a stable method avoids making it worse than necessary.

## Example in AI: keeping probability calculations stable

AI classifiers often turn model scores into probabilities with softmax, which uses exponentials. Very large scores can overflow a computer's number range. For scores `[1000, 1001]`, subtract the largest score first to get `[-1, 0]`; this does not change the final softmax probabilities, but keeps the exponentials manageable. The resulting probabilities are about `[0.269, 0.731]`. This numerical trick is useful when model scores become large. A separate everyday sign of finite precision is that `0.1 + 0.2` may display as `0.30000000000000004`, since those decimals are approximated in binary storage.

## Try it

Why can a computer show a tiny difference when adding decimal values such as `0.1` and `0.2`?

??? success "Check your answer"
    These decimals are approximated in binary floating-point storage, so the stored values are not exact.

## AI Applications

Numerical issues can turn mathematically valid formulas into unreliable code. They affect softmax, probability calculations, linear algebra, gradient checking, and training with low-precision arithmetic. Recognizing these issues helps diagnose NaNs, unstable losses, and results that vary unexpectedly across hardware or settings.

## Recommended References

- [Fundamentals of Numerical Computation](https://fncbook.com/) — free online textbook with Python, Julia, and MATLAB versions; select chapters on floating point, linear systems, and conditioning.
- [MIT OpenCourseWare 18.335J: Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/) — deeper university material in numerical linear algebra and computational methods.
- [NumPy: Linear algebra](https://numpy.org/doc/stable/reference/routines.linalg.html) — practical reference for common numerical linear algebra operations in Python.

---

[← Previous: Discrete Mathematics and Graph Theory](08-discrete-mathematics.md) · [Next: Advanced AI Mathematics →](10-advanced-ai-mathematics.md)
