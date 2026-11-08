[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.precision_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.precision_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.precision_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.precision_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.precision_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.precision_score.html)

Collapse Sidebar Expand Sidebar

precision\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#precision-score "Link to this heading")

===================================================================================================================================================

sklearn.metrics.precision\_score(_y\_true_, _y\_pred_, _\*_, _labels\=None_, _pos\_label\=1_, _average\='binary'_, _sample\_weight\=None_, _zero\_division\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L2479)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "Link to this definition")

Compute the precision.

The precision is the ratio `tp / (tp + fp)` where `tp` is the number of true positives and `fp` the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.

The best value is 1 and the worst value is 0.

Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 targets is achieved by treating [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 data as a collection of binary problems, one for each label. For the [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 case, setting `average='binary'` will return precision for `pos_label`. If `average` is not `'binary'`, `pos_label` is ignored and precision for both classes are computed, then averaged or both returned (when `average=None`). Similarly, for [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 and [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 targets, precision for all `labels` are either returned or averaged depending on the `average` parameter. Use `labels` specify the set of labels to calculate precision for.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) target values. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Estimated targets as returned by a classifier. Sparse matrix is only supported when targets are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

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

Sets the value to return when there is a zero division.

Notes:

*   If set to “warn”, this acts like 0, but a warning is also raised.
    
*   If set to `np.nan`, such values will be excluded from the average.
    

Added in version 1.3: `np.nan` option was added.

Returns:

**precision**float (if average is not None) or array of float of shape (n\_unique\_labels,)

Precision of the positive class in binary classification or weighted average of the precision of each class for the multiclass task.

See also

[`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")

Compute precision, recall, F-measure and support for each class.

[`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")

Compute the ratio `tp / (tp + fn)` where `tp` is the number of true positives and `fn` the number of false negatives.

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot precision-recall curve given an estimator and some data.

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot precision-recall curve given binary class predictions.

[`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")

Compute a confusion matrix for each class or sample.

Notes

When `true positive + false positive == 0`, precision returns 0 and raises `UndefinedMetricWarning`. This behavior can be modified with `zero_division`.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import precision\_score
\>>> y\_true \= \[0, 1, 2, 0, 1, 2\]
\>>> y\_pred \= \[0, 2, 1, 0, 0, 1\]
\>>> precision\_score(y\_true, y\_pred, average\='macro')
0.22
\>>> precision\_score(y\_true, y\_pred, average\='micro')
0.33
\>>> precision\_score(y\_true, y\_pred, average\='weighted')
0.22
\>>> precision\_score(y\_true, y\_pred, average\=None)
array(\[0.66, 0.        , 0.        \])
\>>> y\_pred \= \[0, 0, 0, 0, 0, 0\]
\>>> precision\_score(y\_true, y\_pred, average\=None)
array(\[0.33, 0.        , 0.        \])
\>>> precision\_score(y\_true, y\_pred, average\=None, zero\_division\=1)
array(\[0.33, 1.        , 1.        \])
\>>> precision\_score(y\_true, y\_pred, average\=None, zero\_division\=np.nan)
array(\[0.33,        nan,        nan\])

Copy to clipboard

\>>> \# multilabel classification
\>>> y\_true \= \[\[0, 0, 0\], \[1, 1, 1\], \[0, 1, 1\]\]
\>>> y\_pred \= \[\[0, 0, 0\], \[1, 1, 1\], \[1, 1, 0\]\]
\>>> precision\_score(y\_true, y\_pred, average\=None)
array(\[0.5, 1. , 1. \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)