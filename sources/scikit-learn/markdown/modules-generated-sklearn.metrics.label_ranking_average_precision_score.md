[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html)

Collapse Sidebar Expand Sidebar

label\_ranking\_average\_precision\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#label-ranking-average-precision-score "Link to this heading")

========================================================================================================================================================================================================================

sklearn.metrics.label\_ranking\_average\_precision\_score(_y\_true_, _y\_score_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1375)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "Link to this definition")

Compute ranking-based average precision.

Label ranking average precision (LRAP) is the average over each ground truth label assigned to each sample, of the ratio of true vs. total labels with lower score.

This metric is used in multilabel ranking problem, where the goal is to give better rank to the labels associated to each sample.

The obtained score is always strictly greater than 0 and the best value is 1.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#label-ranking-average-precision)
.

Parameters:

**y\_true**{array-like, sparse matrix} of shape (n\_samples, n\_labels)

True binary labels in [label indicator format](https://scikit-learn.org/stable/glossary.html#term-label-indicator-format)
.

**y\_score**array-like of shape (n\_samples, n\_labels)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Added in version 0.20.

Returns:

**score**float

Ranking-based average precision score.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import label\_ranking\_average\_precision\_score
\>>> y\_true \= np.array(\[\[1, 0, 0\], \[0, 0, 1\]\])
\>>> y\_score \= np.array(\[\[0.75, 0.5, 1\], \[1, 0.2, 0.1\]\])
\>>> label\_ranking\_average\_precision\_score(y\_true, y\_score)
0.416

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)