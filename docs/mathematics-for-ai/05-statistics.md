# Statistics

**Difficulty:** Beginner to intermediate  
**Prerequisites:** Mathematical foundations and introductory probability.

## Overview

Statistics helps us learn from samples and describe how uncertain our conclusions are. It is not just a set of formulas: good statistical reasoning also asks how data was collected and whether the evidence supports the claim.

## Topics Covered

### Describe data

- Mean, median, quantiles, range, variance, and standard deviation.
- Tables, histograms, and scatter plots; association is not by itself evidence of causation.
- Outliers, missing values, and the effect of measurement choices.

### Learn from samples

- Population, sample, sampling variation, and sampling bias.
- Estimators and the distinction between bias and variability.
- Confidence intervals as procedures with long-run coverage, not as a probability assigned to one fixed interval.
- Hypothesis tests, p-values, and why statistical significance is not the same as practical importance.
- Bootstrap and randomization ideas as resampling tools.

### Evaluate evidence

- Correlation and simple regression as summaries of relationships, with assumptions and limitations.
- Train, validation, and test sets as a way to separate model fitting from evaluation.
- Data leakage, class imbalance, and uncertainty in reported metrics.

## Learn the idea

Statistics helps us describe the data we have and judge how much it tells us about data we have not seen. A mean uses every value, so an unusually large value can pull it upward. A median is the middle value after sorting and is less affected by extreme values.

A sample is only part of a larger group, so a result can vary depending on which examples were selected. A larger sample often gives a steadier estimate, but it cannot fix a biased collection process. In machine learning, keeping test examples separate from training helps estimate performance on new cases. If information from the test set influences training, the estimate is no longer independent.

## Example in AI: checking model errors

After testing a model, suppose its prediction errors on four examples are `[2, 4, 4, 10]` units. The mean error is `(2 + 4 + 4 + 10) / 4 = 5`, while the median is 4. The one large error pulls the mean upward more than the median. Both summaries help: the mean reflects the total average impact, while the median describes a more typical case. Statistics is useful when comparing models because one score alone can hide unusual failures or variation across examples.

## Try it

What is the median of `[1, 3, 8]`?

??? success "Check your answer"
    The values are already sorted; the middle value is 3.

## AI Applications

Statistics informs experiment design, dataset summaries, model evaluation, and uncertainty reporting. It helps distinguish a real improvement from noise and exposes sampling or measurement problems. Statistical reasoning is essential when deciding whether a model result is likely to hold beyond the examples used to develop it.

## Recommended References

- [OpenIntro Statistics](https://www.openintro.org/book/os/) — free textbook, datasets, and supporting materials for introductory statistics.
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive explanations of distributions, inference, and regression.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — reference material for methods and statistical practice; more detailed than a first introduction.

---

[← Previous: Probability Theory](04-probability-theory.md) · [Next: Optimization Mathematics →](06-optimization.md)
