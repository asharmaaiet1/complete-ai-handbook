# Mathematical Foundations

## Learning objectives

By the end of this guide, you should be able to:

- Read simple equations and identify what each variable represents.
- Use functions, powers, and logarithms in basic calculations.
- Explain how these ideas appear in model formulas and loss calculations.

**Difficulty:** Beginner  
**Prerequisites:** Basic arithmetic.  
**Role in the path:** Refresh these ideas before or alongside the core AI subjects.

## Overview

This guide covers the small set of school-level ideas that appear repeatedly in technical explanations. The goal is fluency with notation and relationships, not advanced algebra or proof writing.

## Topics Covered

### Numbers and expressions

- Fractions, ratios, percentages, and unit changes.
- Negative numbers, absolute value, order of operations, and simplifying expressions.
- Powers, roots, and scientific notation.
- Logarithms as the inverse of exponentiation; common and natural logarithms.

### Equations and functions

- Rearranging and solving linear equations; reading simple inequalities.
- Variables, input-output functions, domain, and range.
- Linear, quadratic, exponential, and logarithmic functions.
- Reading coordinate graphs, slope, and the meaning of a function's scale.

### Summation and notation

- Sigma notation as a compact way to add a sequence of values.
- Subscripts for identifying individual data points or model parameters.
- The difference between a constant, a measured value, and a value a model learns.

## Learn the idea

Math notation is a shorter way to describe a calculation. A variable is a name for a value that may change. A function is a repeatable rule: give it an input, and it returns an output. This is also a useful way to think about a model: it receives data and produces a result.

An equation says that two expressions have the same value. You can rearrange it as long as you do the same operation to both sides. A logarithm asks a reverse question to a power: `log₂(8) = 3` because `2³ = 8`. Logs are useful when values grow quickly or when multiplying many probabilities would produce tiny numbers.

## Example in AI: turning inputs into a score

A simple prediction system might combine two measurements into a score. Imagine a practice tool uses `score = 2 × completed exercises + 1` as a made-up readiness score. A learner who completed 3 exercises gets `2 × 3 + 1 = 7`. If the tool shows a score of 11, rearranging the equation tells us that it corresponds to 5 exercises. This example shows why variables, functions, and rearranging equations help us read model formulas. Real systems learn their rules from data rather than using this hand-written rule.

## Try it

For `score = 3 × examples + 2`, what score do 4 examples produce?

??? success "Check your answer"
    `3 × 4 + 2 = 14`.

## AI Applications

Ratios help interpret class balance and accuracy. Functions describe how inputs map to predictions. Exponentials and logarithms appear in probabilities, log loss, and numerical routines. Summation notation often represents the total loss over a dataset. Being able to rearrange an equation makes it easier to understand what a model is computing.

## Recommended References

- [OpenStax College Algebra 2e](https://openstax.org/details/books/college-algebra-2e/) — free textbook; use selected chapters on functions, exponents, and logarithms.
- [OpenStax Precalculus 2e](https://openstax.org/details/books/precalculus-2e) — free textbook for functions and graphs; broader than this guide requires.
- [Khan Academy: Algebra](https://www.khanacademy.org/math/algebra) — free, beginner-friendly practice for equations and expressions.

---

[← Previous: Mathematics for AI overview](index.md) · [Next: Linear Algebra →](02-linear-algebra.md)
