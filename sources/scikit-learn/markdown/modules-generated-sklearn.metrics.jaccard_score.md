[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.jaccard_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.jaccard_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.jaccard_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.jaccard_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.jaccard_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.jaccard_score.html)

Collapse Sidebar Expand Sidebar

jaccard\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#jaccard-score "Link to this heading")

=============================================================================================================================================

sklearn.metrics.jaccard\_score(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _pos\_label\=1_, _average\='binary'_, _sample\_weight\=None_, _zero\_division\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L1041)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "Link to this definition")

Jaccard similarity coefficient score.

The Jaccard index \[1\], or Jaccard similarity coefficient, defined as the size of the intersection divided by the size of the union of two label sets, is used to compare set of predicted labels for a sample to the corresponding set of labels in `y_true`.

Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 targets is achieved by treating [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 data as a collection of binary problems, one for each label. For the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 case, setting `average='binary'` will return the Jaccard similarity coefficient for `pos_label`. If `average` is not `'binary'`, `pos_label` is ignored and scores for both classes are computed, then averaged or both returned (when `average=None`). Similarly, for [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 targets, scores for all `labels` are either returned or averaged depending on the `average` parameter. Use `labels` specify the set of labels to calculate the score for.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#jaccard-similarity-score)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) labels. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Predicted labels, as returned by a classifier. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**labels**array-like of shape (n\_classes,), default=None

The set of labels to include when `average != 'binary'`, and their order if `average is None`. Labels present in the data can be excluded, for example in multiclass classification to exclude a “negative class”. Labels not present in the data can be included and will be “assigned” 0 samples. For multilabel targets, labels are column indices. By default, all labels in `y_true` and `y_pred` are used in sorted order.

**pos\_label**int, float, bool or str, default=1

The class to report if `average='binary'` and the data is binary, otherwise this parameter is ignored. For multiclass or multilabel targets, set `labels=[pos_label]` and `average != 'binary'` to report metrics for one label only.

**average**{‘micro’, ‘macro’, ‘samples’, ‘weighted’, ‘binary’} or None, default=’binary’

If `None`, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:

`'binary'`:

Only report results for the class specified by `pos_label`. This is applicable only if targets (`y_{true,pred}`) are binary.

`'micro'`:

Calculate metrics globally by counting the total true positives, false negatives and false positives.

`'macro'`:

Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.

`'weighted'`:

Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance.

`'samples'`:

Calculate metrics for each instance, and find their average (only meaningful for multilabel classification).

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**zero\_division**{“warn”, 0.0, 1.0, np.nan}, default=”warn”

Sets the value to return when there is a zero division, i.e. when there are no negative values in predictions and labels. If set to “warn”, this acts like 0, but a warning is also raised.

Added in version 0.24.

Returns:

**score**float or ndarray of shape (n\_unique\_labels,), dtype=np.float64

The Jaccard score. When `average` is not `None`, a single scalar is returned.

See also

[`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")

Function for calculating the accuracy score.

[`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")

Function for calculating the F1 score.

[`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")

Function for computing a confusion matrix for each class or sample.

Notes

[`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
 may be a poor metric if there are no positives for some samples or classes. Jaccard is undefined if there are no true or predicted labels, and our implementation will return a score of 0 with a warning.

References

\[1\]

[Wikipedia entry for the Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)
.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import jaccard\_score
\>>> y\_true \= np.array(\[\[0, 1, 1\],\
...                    \[1, 1, 0\]\])
\>>> y\_pred \= np.array(\[\[1, 1, 1\],\
...                    \[1, 0, 0\]\])

Copy to clipboard

In the binary case:

\>>> jaccard\_score(y\_true\[0\], y\_pred\[0\])
0.6666

Copy to clipboard

In the 2D comparison case (e.g. image similarity):

\>>> jaccard\_score(y\_true, y\_pred, average\="micro")
0.6

Copy to clipboard

In the multilabel case:

\>>> jaccard\_score(y\_true, y\_pred, average\='samples')
0.5833
\>>> jaccard\_score(y\_true, y\_pred, average\='macro')
0.6666
\>>> jaccard\_score(y\_true, y\_pred, average\=None)
array(\[0.5, 0.5, 1. \])

Copy to clipboard

In the multiclass case:

\>>> y\_pred \= \[0, 2, 1, 2\]
\>>> y\_true \= \[0, 1, 2, 2\]
\>>> jaccard\_score(y\_true, y\_pred, average\=None)
array(\[1. , 0. , 0.33\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)