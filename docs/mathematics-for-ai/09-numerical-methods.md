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

## AI Applications

Numerical issues can turn mathematically valid formulas into unreliable code. They affect softmax, probability calculations, linear algebra, gradient checking, and training with low-precision arithmetic. Recognizing these issues helps diagnose NaNs, unstable losses, and results that vary unexpectedly across hardware or settings.

## Recommended References

- [Fundamentals of Numerical Computation](https://fncbook.com/) — free online textbook with Python, Julia, and MATLAB versions; select chapters on floating point, linear systems, and conditioning.
- [MIT OpenCourseWare 18.335J: Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/) — deeper university material in numerical linear algebra and computational methods.
- [NumPy: Linear algebra](https://numpy.org/doc/stable/reference/routines.linalg.html) — practical reference for common numerical linear algebra operations in Python.

---

[← Previous: Discrete Mathematics and Graph Theory](08-discrete-mathematics.md) · [Next: Advanced AI Mathematics →](10-advanced-ai-mathematics.md)
