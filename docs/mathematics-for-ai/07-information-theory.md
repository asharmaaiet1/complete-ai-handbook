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

## AI Applications

Cross-entropy is a common classification and language-model training loss. KL divergence appears in variational methods and distribution matching. Entropy can describe uncertainty in predictions or guide decisions such as querying a label for the most informative example. These quantities depend on the probability model and context; they are not universal measures of model quality.

## Recommended References

- [Information Theory, Inference, and Learning Algorithms by David MacKay](https://www.inference.org.uk/mackay/itila/) — author-hosted book connecting information theory with inference and learning; broad and sometimes advanced.
- [MIT OpenCourseWare 6.441: Information Theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/) — university course for deeper study; requires probability and discrete mathematics.
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive probability foundations that help prepare for information measures.

---

[← Previous: Optimization Mathematics](06-optimization.md) · [Next: Discrete Mathematics and Graph Theory →](08-discrete-mathematics.md)
