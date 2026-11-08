[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.top_k_accuracy_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.top_k_accuracy_score.html)

Collapse Sidebar Expand Sidebar

top\_k\_accuracy\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#top-k-accuracy-score "Link to this heading")

====================================================================================================================================================================

sklearn.metrics.top\_k\_accuracy\_score(_y\_true_, _y\_score_, _\*_, _k\=2_, _normalize\=True_, _sample\_weight\=None_, _labels\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L2069)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "Link to this definition")

Top-k Accuracy classification score.

This metric computes the number of times where the correct label is among the top `k` labels predicted (ranked by predicted scores). Note that the multilabel case isn’t covered here.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#top-k-accuracy-score)

Parameters:

**y\_true**array-like of shape (n\_samples,)

True labels.

**y\_score**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Target scores. These can be either probability estimates or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). The binary case expects scores with shape (n\_samples,) while the multiclass case expects scores with shape (n\_samples, n\_classes). In the multiclass case, the order of the class scores must correspond to the order of `labels`, if provided, or else to the numerical or lexicographical order of the labels in `y_true`. If `y_true` does not contain all the labels, `labels` must be provided.

**k**int, default=2

Number of most likely outcomes considered to find the correct label.

**normalize**bool, default=True

If `True`, return the fraction of correctly classified samples. Otherwise, return the number of correctly classified samples.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If `None`, all samples are given the same weight.

**labels**array-like of shape (n\_classes,), default=None

Multiclass only. List of labels that index the classes in `y_score`. If `None`, the numerical or lexicographical order of the labels in `y_true` is used. If `y_true` does not contain all the labels, `labels` must be provided.

Returns:

**score**float

The top-k accuracy score. The best performance is 1 with `normalize == True` and the number of samples with `normalize == False`.

See also

[`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")

Compute the accuracy score. By default, the function will return the fraction of correct predictions divided by the total number of predictions.

Notes

In cases where two or more labels are assigned equal predicted scores, the labels with the highest indices will be chosen first. This might impact the result if the correct label falls after the threshold because of that.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import top\_k\_accuracy\_score
\>>> y\_true \= np.array(\[0, 1, 2, 2\])
\>>> y\_score \= np.array(\[\[0.5, 0.2, 0.2\],  \# 0 is in top 2\
...                     \[0.3, 0.4, 0.2\],  \# 1 is in top 2\
...                     \[0.2, 0.4, 0.3\],  \# 2 is in top 2\
...                     \[0.7, 0.2, 0.1\]\]) \# 2 isn't in top 2
\>>> top\_k\_accuracy\_score(y\_true, y\_score, k\=2)
0.75
\>>> \# Not normalizing gives the number of "correctly" classified samples
\>>> top\_k\_accuracy\_score(y\_true, y\_score, k\=2, normalize\=False)
3.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)