# Linear Algebra

## Learning objectives

By the end of this guide, you should be able to:

- Distinguish scalars, vectors, matrices, and tensors by their shapes.
- Calculate a simple dot product and explain what it combines.
- Describe how linear algebra represents data and model computations.

**Difficulty:** Beginner to intermediate  
**Prerequisites:** Mathematical foundations; comfort with coordinates and equations is helpful.

## Overview

Linear algebra studies vectors, matrices, and transformations between spaces. In AI, it is a language for storing collections of numbers and describing many model computations compactly.

## Topics Covered

### Essential representations

- Scalars, vectors, matrices, and tensors; a tensor is a general name for an array with one or more dimensions.
- Shape and dimension: how many values each object contains and which operations fit.
- Vector addition, scalar multiplication, dot products, and matrix multiplication.
- Transpose, identity matrix, and matrix-vector multiplication.

### Geometry and comparison

- Norms as measures of vector size and distance.
- Linear combinations, span, basis, and linear independence at an intuitive level.
- A matrix as a transformation that rotates, scales, or combines coordinates.
- Orthogonality and projection as ways to compare or separate directions.

### Useful intermediate ideas

- Eigenvectors and eigenvalues as directions preserved by a transformation and their scale factors.
- Singular value decomposition (SVD) as a factorization that exposes important directions and scales.
- Rank as the number of independent directions represented by a matrix.

## Learn the idea

A vector is an ordered list of numbers. In a dataset, one vector can hold the measurements for one example, such as `[hours studied, practice questions]`. A matrix is a grid of numbers; it can hold many examples or the weights used by a model.

The dot product combines matching entries, multiplies each pair, then adds the results. A matrix-vector product repeats this kind of calculation to create several outputs. Shapes matter: a matrix with 2 columns can combine with a vector of 2 values, and each matrix row produces one output value.

## Example in AI: combining features for a prediction

A small model might use two features to estimate whether a learner needs another practice exercise: time spent and recent mistakes. Let the input vector be `[3, 2]`, meaning 3 time units and 2 mistakes, and let the learned weights be `[2, 1]`. The dot product is `3 × 2 + 2 × 1 = 8`, one combined score for the next step. In a real model, training learns the weights, and later calculations turn the score into an output. This is where vectors and matrix multiplication are useful: they combine many features consistently for many examples.

## Try it

What is the dot product of `[1, 4]` and `[3, 2]`?

??? success "Check your answer"
    `1 × 3 + 4 × 2 = 11`.

## AI Applications

Rows and columns organize examples and features. A neural-network layer multiplies an input representation by learned weights, then applies another operation. Embeddings represent items as vectors so similarity can be compared. PCA and related methods use matrix factorizations to summarize or compress data. Understanding shapes also helps catch implementation errors.

```mermaid
flowchart LR
    X[Input vector<br/>n values] --> W[Weight matrix<br/>m by n]
    W --> Y[Output vector<br/>m values]
```

The diagram shows the shape relationship for one matrix-vector multiplication: an input with `n` values and a weight matrix with `m` rows and `n` columns produce an output with `m` values.

## Recommended References

- [MIT OpenCourseWare 18.06: Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — full university course; select lectures on vectors, matrix multiplication, subspaces, eigenvalues, and SVD.
- [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — visual intuition; pair it with exercises because videos are not a complete course.
- [Mathematics for Machine Learning](https://mml-book.github.io/) — free online book; useful for a more mathematical bridge to ML.

---

[← Previous: Mathematical Foundations](01-mathematical-foundations.md) · [Next: Calculus →](03-calculus.md)
