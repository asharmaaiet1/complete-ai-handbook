# Probability Theory

**Difficulty:** Beginner to intermediate  
**Prerequisites:** Mathematical foundations; fractions and basic algebra.

## Overview

Probability gives a consistent way to reason about uncertain outcomes. AI systems use it to represent uncertain predictions, model random data, and describe how evidence changes what is plausible.

## Topics Covered

### Events and relationships

- Outcomes, sample spaces, events, and complements.
- Addition and multiplication rules for probabilities.
- Conditional probability: probability of an event given another event.
- Independence: when learning one event does not change the probability of another.
- Bayes' rule: updating a probability using new evidence.

### Random variables and distributions

- Random variables as numerical descriptions of uncertain outcomes.
- Discrete and continuous distributions.
- Bernoulli, categorical, binomial, and normal distributions.
- Expected value as a long-run average; variance and standard deviation as measures of spread.
- Joint, marginal, and conditional distributions.

## Learn the idea

Probability is a number from 0 to 1 that describes how likely an event is under a model of uncertainty. Zero means impossible in that model; one means certain. If a fair coin is tossed, heads has probability `1/2`. After several tosses, the chance of a particular sequence can be found by multiplying probabilities when the tosses are independent.

Conditional probability asks about an event after some information is known. The chance of rain given dark clouds can differ from the chance of rain on any day. Bayes' rule reverses the direction of a conditional question: it helps update the chance of a cause after observing evidence. The result depends on how common the cause was before the evidence.

## Example in AI: describing an uncertain prediction

Suppose an image model is choosing between two labels: cat and dog. It assigns probabilities `0.7` to cat and `0.3` to dog. These numbers describe the model's uncertainty under its learned probability estimates; they do not guarantee that the image is a cat or that the estimates are well calibrated. Probability is useful when an application must represent uncertainty, compare possible outcomes, or decide whether to ask a person for help. For a simple chance calculation, two fair coin tosses have outcomes `HH`, `HT`, `TH`, and `TT`; exactly one head occurs in 2 of 4 outcomes, so its probability is `1/2`.

## Try it

What is the probability of getting two heads in two fair tosses?

??? success "Check your answer"
    Only `HH` works, so the probability is `1/4`.

## AI Applications

Classification models often produce scores that are interpreted or calibrated as probabilities. Bayesian reasoning describes how a prior belief and observed evidence combine. Sampling-based algorithms use random draws to estimate quantities that are difficult to calculate exactly. Probability distributions also describe latent variables and generated outputs.

## Recommended References

- [Harvard Statistics 110: Probability](https://stat110.hsites.harvard.edu/) — course materials and a free online version of the accompanying book.
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive visual introductions to probability and statistics.
- [OpenStax Introductory Statistics 2e](https://openstax.org/details/books/introductory-statistics-2e) — free text for introductory probability and statistical reasoning.

---

[← Previous: Calculus](03-calculus.md) · [Next: Statistics →](05-statistics.md)
