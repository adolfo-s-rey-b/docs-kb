[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.fbeta_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.fbeta_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.fbeta_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.fbeta_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.fbeta_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.fbeta_score.html)

Collapse Sidebar Expand Sidebar

fbeta\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#fbeta-score "Link to this heading")

=======================================================================================================================================

sklearn.metrics.fbeta\_score(_y\_true_, _y\_pred_, _\*_, _beta_, _labels\=None_, _pos\_label\=1_, _average\='binary'_, _sample\_weight\=None_, _zero\_division\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L1623)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "Link to this definition")

Compute the F-beta score.

The F-beta score is the weighted harmonic mean of precision and recall, reaching its optimal value at 1 and its worst value at 0.

The `beta` parameter represents the ratio of recall importance to precision importance. `beta > 1` gives more weight to recall, while `beta < 1` favors precision. For example, `beta = 2` makes recall twice as important as precision, while `beta = 0.5` does the opposite. Asymptotically, `beta -> +inf` considers only recall, and `beta -> 0` only precision.

The formula for F-beta score is:

Fβ\=(1+β2)tp(1+β2)tp+fp+β2fn

Where tp is the number of true positives, fp is the number of false positives, and fn is the number of false negatives.

Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 targets is achieved by treating [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 data as a collection of binary problems, one for each label. For the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 case, setting `average='binary'` will return F-beta score for `pos_label`. If `average` is not `'binary'`, `pos_label` is ignored and F-beta score for both classes are computed, then averaged or both returned (when `average=None`). Similarly, for [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 targets, F-beta score for all `labels` are either returned or averaged depending on the `average` parameter. Use `labels` specify the set of labels to calculate F-beta score for.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) target values. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Estimated targets as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**beta**float

Determines the weight of recall in the combined score.

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

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**zero\_division**{“warn”, 0.0, 1.0, np.nan}, default=”warn”

Sets the value to return when there is a zero division, i.e. when all predictions and labels are negative.

Notes:

*   If set to “warn”, this acts like 0, but a warning is also raised.
    
*   If set to `np.nan`, such values will be excluded from the average.
    

Added in version 1.3: `np.nan` option was added.

Returns:

**fbeta\_score**float (if average is not None) or array of float, shape = \[n\_unique\_labels\]

F-beta score of the positive class in binary classification or weighted average of the F-beta score of each class for the multiclass task.

See also

[`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")

Compute the precision, recall, F-score, and support.

[`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")

Compute a confusion matrix for each class or sample.

Notes

When `true positive + false positive + false negative == 0`, f-score returns 0.0 and raises `UndefinedMetricWarning`. This behavior can be modified by setting `zero_division`.

F-beta score is not implemented as a named scorer that can be passed to the `scoring` parameter of cross-validation tools directly: it requires to be wrapped with [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
 so as to specify the value of `beta`. See examples for details.

References

\[1\]

R. Baeza-Yates and B. Ribeiro-Neto (2011). Modern Information Retrieval. Addison Wesley, pp. 327-328.

\[2\]

[Wikipedia entry for the F1-score](https://en.wikipedia.org/wiki/F1_score)
.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import fbeta\_score
\>>> y\_true \= \[0, 1, 2, 0, 1, 2\]
\>>> y\_pred \= \[0, 2, 1, 0, 0, 1\]
\>>> fbeta\_score(y\_true, y\_pred, average\='macro', beta\=0.5)
0.238
\>>> fbeta\_score(y\_true, y\_pred, average\='micro', beta\=0.5)
0.33
\>>> fbeta\_score(y\_true, y\_pred, average\='weighted', beta\=0.5)
0.238
\>>> fbeta\_score(y\_true, y\_pred, average\=None, beta\=0.5)
array(\[0.71, 0.        , 0.        \])
\>>> y\_pred\_empty \= \[0, 0, 0, 0, 0, 0\]
\>>> fbeta\_score(
...     y\_true,
...     y\_pred\_empty,
...     average\="macro",
...     zero\_division\=np.nan,
...     beta\=0.5,
... )
0.128

Copy to clipboard

In order to use `fbeta_scorer` as a scorer, a callable scorer objects needs to be created first with [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
, passing the value for the `beta` parameter.

\>>> from sklearn.metrics import fbeta\_score, make\_scorer
\>>> ftwo\_scorer \= make\_scorer(fbeta\_score, beta\=2)
\>>> from sklearn.model\_selection import GridSearchCV
\>>> from sklearn.svm import LinearSVC
\>>> grid \= GridSearchCV(
...     LinearSVC(dual\="auto"),
...     param\_grid\={'C': \[1, 10\]},
...     scoring\=ftwo\_scorer,
...     cv\=5
... )

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)