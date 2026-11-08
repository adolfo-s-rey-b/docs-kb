[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.average_precision_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.average_precision_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.average_precision_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.average_precision_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.average_precision_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.average_precision_score.html)

Collapse Sidebar Expand Sidebar

average\_precision\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#average-precision-score "Link to this heading")

============================================================================================================================================================================

sklearn.metrics.average\_precision\_score(_y\_true_, _y\_score_, _\*_, _average\='macro'_, _pos\_label\=1_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L118)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "Link to this definition")

Compute average precision (AP) from prediction scores.

AP summarizes a precision-recall curve as the weighted mean of precisions achieved at each threshold, with the increase in recall from the previous threshold used as the weight:

AP\=∑n(Rn−Rn−1)Pn

where Pn and Rn are the precision and recall at the nth threshold [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#rcdf8f32d7f9d-1)
. This implementation is not interpolated and is different from computing the area under the precision-recall curve with the trapezoidal rule, which uses linear interpolation and can be too optimistic.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

True binary labels, [multi-label](https://scikit-learn.org/stable/glossary.html#term-multi-label)
 indicators (as a [multilabel indicator matrix](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrix)
) or [multi-class](https://scikit-learn.org/stable/glossary.html#term-multi-class)
 labels.

**y\_score**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**average**{‘micro’, ‘samples’, ‘weighted’, ‘macro’} or None, default=’macro’

If `None`, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:

`'micro'`:

Calculate metrics globally by considering each element of the label indicator matrix as a label.

`'macro'`:

Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.

`'weighted'`:

Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).

`'samples'`:

Calculate metrics for each instance, and find their average.

Will be ignored when `y_true` is binary.

**pos\_label**int, float, bool or str, default=1

The label of the positive class. Only applied to binary `y_true`. For multilabel-indicator `y_true`, `pos_label` is fixed to 1.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**average\_precision**float

Average precision score.

See also

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall pairs for different probability thresholds.

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot the precision recall curve using an estimator and data.

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot the precision recall curve using true and predicted labels.

Notes

Changed in version 0.19: Instead of linearly interpolating between operating points, precisions are weighted by the change in recall since the last operating point.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#id1)\
\]

[Wikipedia entry for the Average precision](https://en.wikipedia.org/w/index.php?title=Information_retrieval&oldid=793358396#Average_precision)

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import average\_precision\_score
\>>> y\_true \= np.array(\[0, 0, 1, 1\])
\>>> y\_scores \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> average\_precision\_score(y\_true, y\_scores)
0.83
\>>> y\_true \= np.array(\[0, 0, 1, 1, 2, 2\])
\>>> y\_scores \= np.array(\[\
...     \[0.7, 0.2, 0.1\],\
...     \[0.4, 0.3, 0.3\],\
...     \[0.1, 0.8, 0.1\],\
...     \[0.2, 0.3, 0.5\],\
...     \[0.4, 0.4, 0.2\],\
...     \[0.1, 0.2, 0.7\],\
... \])
\>>> average\_precision\_score(y\_true, y\_scores)
0.77

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

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