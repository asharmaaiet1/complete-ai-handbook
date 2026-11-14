# Information Theory

**Difficulty:** Intermediate  
**Prerequisites:** Probability distributions, logarithms, and basic summation.

## Overview

Information theory studies how to measure uncertainty and information. Its measures help compare probability distributions and explain losses used to train classification and language models.

## Topics Covered

### Uncertainty and coding

- Self-information: the surprise associated with an event, which is larger for less likely events.
- Entropy as average uncertainty in a distribution.
- Cross-entropy as the average penalty for assigning probability according to one distribution when another generated the outcomes.
- Bits and the logarithm base; changing the base changes units, not the underlying comparison.

### Comparing distributions

- Kullback–Leibler (KL) divergence as a measure of mismatch between distributions; it is not a symmetric distance.
- Mutual information as a measure of statistical dependence.
- The relationship between entropy, cross-entropy, and KL divergence.
- Perplexity as an exponentiated average log-loss measure used in language modeling; comparisons require consistent tokenization and evaluation data.

## Learn the idea

Entropy measures the average uncertainty in a probability distribution. A fair coin has one bit of entropy: before the toss, either outcome is equally possible. A coin that lands heads almost every time has less uncertainty. Entropy describes a distribution overall; it does not tell us whether a particular prediction is correct.

Cross-entropy measures how much penalty a prediction receives when an outcome occurs. Giving a likely outcome high probability leads to a small penalty. Giving the actual outcome a very low probability leads to a large one. This makes cross-entropy useful for teaching a classifier to assign higher probabilities to the correct answers.

## Example in AI: scoring a classification prediction

When a classifier predicts the chance of each label, cross-entropy can score how well those probabilities fit the answer. If the correct label receives probability `0.9`, its penalty is `−log₂(0.9)`, about `0.15` bits. If the correct label receives only `0.1`, the penalty is about `3.32` bits. The confident wrong prediction gets a much larger penalty, giving training a reason to improve its probabilities. The exact training setup may average this score across many examples.

## Try it

Which gets the larger penalty when it happens: an outcome predicted with probability `0.8` or one predicted with probability `0.2`?

??? success "Check your answer"
    Probability `0.2` gets the larger penalty because `−log₂(0.2)` is greater than `−log₂(0.8)`.

## AI Applications

Cross-entropy is a common classification and language-model training loss. KL divergence appears in variational methods and distribution matching. Entropy can describe uncertainty in predictions or guide decisions such as querying a label for the most informative example. These quantities depend on the probability model and context; they are not universal measures of model quality.

## Recommended References

- [Information Theory, Inference, and Learning Algorithms by David MacKay](https://www.inference.org.uk/mackay/itila/) — author-hosted book connecting information theory with inference and learning; broad and sometimes advanced.
- [MIT OpenCourseWare 6.441: Information Theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/) — university course for deeper study; requires probability and discrete mathematics.
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive probability foundations that help prepare for information measures.

---

[← Previous: Optimization Mathematics](06-optimization.md) · [Next: Discrete Mathematics and Graph Theory →](08-discrete-mathematics.md)
