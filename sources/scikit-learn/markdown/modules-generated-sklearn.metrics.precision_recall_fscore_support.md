[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.precision_recall_fscore_support.html)

Collapse Sidebar Expand Sidebar

precision\_recall\_fscore\_support[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#precision-recall-fscore-support "Link to this heading")

=====================================================================================================================================================================================================

sklearn.metrics.precision\_recall\_fscore\_support(_y\_true_, _y\_pred_, _\*_, _beta\=1.0_, _labels\=None_, _pos\_label\=1_, _average\=None_, _warn\_for\=('precision', 'recall', 'f-score')_, _sample\_weight\=None_, _zero\_division\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L1939)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "Link to this definition")

Compute precision, recall, F-measure and support for each class.

The precision is the ratio `tp / (tp + fp)` where `tp` is the number of true positives and `fp` the number of false positives. The precision is intuitively the ability of the classifier not to label a negative sample as positive.

The recall is the ratio `tp / (tp + fn)` where `tp` is the number of true positives and `fn` the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.

The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F-beta score reaches its best value at 1 and worst score at 0.

The F-beta score weights recall more than precision by a factor of `beta`. `beta == 1.0` means recall and precision are equally important.

The support is the number of occurrences of each class in `y_true`.

Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 targets is achieved by treating [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 data as a collection of binary problems, one for each label. For the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 case, setting `average='binary'` will return metrics for `pos_label`. If `average` is not `'binary'`, `pos_label` is ignored and metrics for both classes are computed, then averaged or both returned (when `average=None`). Similarly, for [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 targets, metrics for all `labels` are either returned or averaged depending on the `average` parameter. Use `labels` specify the set of labels to calculate metrics for.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) target values. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Estimated targets as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**beta**float, default=1.0

The strength of recall versus precision in the F-score.

**labels**array-like, default=None

The set of labels to include when `average != 'binary'`, and their order if `average is None`. Labels present in the data can be excluded, for example in multiclass classification to exclude a “negative class”. Labels not present in the data can be included and will be “assigned” 0 samples. For multilabel targets, labels are column indices. By default, all labels in `y_true` and `y_pred` are used in sorted order.

Changed in version 0.17: Parameter `labels` improved for multiclass problem.

**pos\_label**int, float, bool or str, default=1

The class to report if `average='binary'` and the data is binary, otherwise this parameter is ignored. For multiclass or multilabel targets, set `labels=[pos_label]` and `average != 'binary'` to report metrics for one label only.

**average**{‘micro’, ‘macro’, ‘samples’, ‘weighted’, ‘binary’} or None, default=’binary’

This parameter is required for multiclass/multilabel targets. If `None`, the metrics for each class are returned. Otherwise, this determines the type of averaging performed on the data:

`'binary'`:

Only report results for the class specified by `pos_label`. This is applicable only if targets (`y_{true,pred}`) are binary.

`'micro'`:

Calculate metrics globally by counting the total true positives, false negatives and false positives.

`'macro'`:

Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.

`'weighted'`:

Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.

`'samples'`:

Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
).

**warn\_for**list, tuple or set, for internal use

This determines which warnings will be made in the case that this function is being used to return only one of its metrics.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**zero\_division**{“warn”, 0.0, 1.0, np.nan}, default=”warn”

Sets the value to return when there is a zero division:

*   recall: when there are no positive labels
    
*   precision: when there are no positive predictions
    
*   f-score: both
    

Notes:

*   If set to “warn”, this acts like 0, but a warning is also raised.
    
*   If set to `np.nan`, such values will be excluded from the average.
    

Added in version 1.3: `np.nan` option was added.

Returns:

**precision**float (if average is not None) or array of float, shape = \[n\_unique\_labels\]

Precision score.

**recall**float (if average is not None) or array of float, shape = \[n\_unique\_labels\]

Recall score.

**fbeta\_score**float (if average is not None) or array of float, shape = \[n\_unique\_labels\]

F-beta score.

**support**None (if average is not None) or array of int, shape = \[n\_unique\_labels\]

The number of occurrences of each label in `y_true`.

Notes

When `true positive + false positive == 0`, precision is undefined. When `true positive + false negative == 0`, recall is undefined. When `true positive + false negative + false positive == 0`, f-score is undefined. In such cases, by default the metric will be set to 0, and `UndefinedMetricWarning` will be raised. This behavior can be modified with `zero_division`.

References

\[1\]

[Wikipedia entry for the Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
.

\[2\]

[Wikipedia entry for the F1-score](https://en.wikipedia.org/wiki/F1_score)
.

\[3\]

[Discriminative Methods for Multi-labeled Classification Advances in Knowledge Discovery and Data Mining (2004), pp. 22-30 by Shantanu Godbole, Sunita Sarawagi](http://www.godbole.net/shantanu/pubs/multilabelsvm-pakdd04.pdf)
.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import precision\_recall\_fscore\_support
\>>> y\_true \= np.array(\['cat', 'dog', 'pig', 'cat', 'dog', 'pig'\])
\>>> y\_pred \= np.array(\['cat', 'pig', 'dog', 'cat', 'cat', 'dog'\])
\>>> precision\_recall\_fscore\_support(y\_true, y\_pred, average\='macro')
(0.222, 0.333, 0.267, None)
\>>> precision\_recall\_fscore\_support(y\_true, y\_pred, average\='micro')
(0.33, 0.33, 0.33, None)
\>>> precision\_recall\_fscore\_support(y\_true, y\_pred, average\='weighted')
(0.222, 0.333, 0.267, None)

Copy to clipboard

It is possible to compute per-label precisions, recalls, F1-scores and supports instead of averaging:

\>>> precision\_recall\_fscore\_support(y\_true, y\_pred, average\=None,
... labels\=\['pig', 'dog', 'cat'\])
(array(\[0.        , 0.        , 0.66\]),
 array(\[0., 0., 1.\]), array(\[0. , 0. , 0.8\]),
 array(\[2, 2, 2\]))

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)