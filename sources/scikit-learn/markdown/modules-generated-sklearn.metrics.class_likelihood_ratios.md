[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.class_likelihood_ratios.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.class_likelihood_ratios.html)

Collapse Sidebar Expand Sidebar

class\_likelihood\_ratios[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#class-likelihood-ratios "Link to this heading")

============================================================================================================================================================================

sklearn.metrics.class\_likelihood\_ratios(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _sample\_weight\=None_, _replace\_undefined\_by\=nan_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L2221)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "Link to this definition")

Compute binary classification positive and negative likelihood ratios.

The positive likelihood ratio is `LR+ = sensitivity / (1 - specificity)` where the sensitivity or recall is the ratio `tp / (tp + fn)` and the specificity is `tn / (tn + fp)`. The negative likelihood ratio is `LR- = (1 - sensitivity) / specificity`. Here `tp` is the number of true positives, `fp` the number of false positives, `tn` is the number of true negatives and `fn` the number of false negatives. Both class likelihood ratios can be used to obtain post-test probabilities given a pre-test probability.

`LR+` ranges from 1.0 to infinity. A `LR+` of 1.0 indicates that the probability of predicting the positive class is the same for samples belonging to either class; therefore, the test is useless. The greater `LR+` is, the more a positive prediction is likely to be a true positive when compared with the pre-test probability. A value of `LR+` lower than 1.0 is invalid as it would indicate that the odds of a sample being a true positive decrease with respect to the pre-test odds.

`LR-` ranges from 0.0 to 1.0. The closer it is to 0.0, the lower the probability of a given sample to be a false negative. A `LR-` of 1.0 means the test is useless because the odds of having the condition did not change after the test. A value of `LR-` greater than 1.0 invalidates the classifier as it indicates an increase in the odds of a sample belonging to the positive class after being classified as negative. This is the case when the classifier systematically predicts the opposite of the true label.

A typical application in medicine is to identify the positive/negative class to the presence/absence of a disease, respectively; the classifier being a diagnostic test; the pre-test probability of an individual having the disease can be the prevalence of such disease (proportion of a particular population found to be affected by a medical condition); and the post-test probabilities would be the probability that the condition is truly present given a positive test result.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#class-likelihood-ratios)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) target values. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Estimated targets as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**labels**array-like, default=None

List of labels to index the matrix. This may be used to select the positive and negative classes with the ordering `labels=[negative_class, positive_class]`. If `None` is given, those that appear at least once in `y_true` or `y_pred` are used in sorted order.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**replace\_undefined\_by**np.nan, 1.0, or dict, default=np.nan

Sets the return values for LR+ and LR- when there is a division by zero. Can take the following values:

*   `np.nan` to return `np.nan` for both `LR+` and `LR-`
    
*   `1.0` to return the worst possible scores: `{"LR+": 1.0, "LR-": 1.0}`
    
*   a dict in the format `{"LR+": value_1, "LR-": value_2}` where the values can be non-negative floats, `np.inf` or `np.nan` in the range of the likelihood ratios. For example, `{"LR+": 1.0, "LR-": 1.0}` can be used for returning the worst scores, indicating a useless model, and `{"LR+": np.inf, "LR-": 0.0}` can be used for returning the best scores, indicating a useful model.
    

If a division by zero occurs, only the affected metric is replaced with the set value; the other metric is calculated as usual.

Added in version 1.7.

Returns:

**(positive\_likelihood\_ratio, negative\_likelihood\_ratio)**tuple of float

A tuple of two floats, the first containing the positive likelihood ratio (LR+) and the second the negative likelihood ratio (LR-).

Warns:

Raises [`UndefinedMetricWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.UndefinedMetricWarning.html#sklearn.exceptions.UndefinedMetricWarning "sklearn.exceptions.UndefinedMetricWarning")
 when `y_true` and

`y_pred` lead to the following conditions:

*   The number of false positives is 0: positive likelihood ratio is undefined.
    
*   The number of true negatives is 0: negative likelihood ratio is undefined.
    
*   The sum of true positives and false negatives is 0 (no samples of the positive class are present in `y_true`): both likelihood ratios are undefined.
    

For the first two cases, an undefined metric can be defined by setting the `replace_undefined_by` param.

References

\[1\]

[Wikipedia entry for the Likelihood ratios in diagnostic testing](https://en.wikipedia.org/wiki/Likelihood_ratios_in_diagnostic_testing)
.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import class\_likelihood\_ratios
\>>> class\_likelihood\_ratios(\[0, 1, 0, 1, 0\], \[1, 1, 0, 0, 0\])
(1.5, 0.75)
\>>> y\_true \= np.array(\["non-cat", "cat", "non-cat", "cat", "non-cat"\])
\>>> y\_pred \= np.array(\["cat", "cat", "non-cat", "non-cat", "non-cat"\])
\>>> class\_likelihood\_ratios(y\_true, y\_pred)
(1.33, 0.66)
\>>> y\_true \= np.array(\["non-zebra", "zebra", "non-zebra", "zebra", "non-zebra"\])
\>>> y\_pred \= np.array(\["zebra", "zebra", "non-zebra", "non-zebra", "non-zebra"\])
\>>> class\_likelihood\_ratios(y\_true, y\_pred)
(1.5, 0.75)

Copy to clipboard

To avoid ambiguities, use the notation `labels=[negative_class, positive_class]`

\>>> y\_true \= np.array(\["non-cat", "cat", "non-cat", "cat", "non-cat"\])
\>>> y\_pred \= np.array(\["cat", "cat", "non-cat", "non-cat", "non-cat"\])
\>>> class\_likelihood\_ratios(y\_true, y\_pred, labels\=\["non-cat", "cat"\])
(1.5, 0.75)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_thumb.png)

[Class Likelihood Ratios to measure classification performance](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html)

Class Likelihood Ratios to measure classification performance

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)