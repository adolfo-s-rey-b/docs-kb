[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.precision_recall_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.precision_recall_curve.html)

Collapse Sidebar Expand Sidebar

precision\_recall\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#precision-recall-curve "Link to this heading")

=========================================================================================================================================================================

sklearn.metrics.precision\_recall\_curve(_y\_true_, _y\_score_, _\*_, _pos\_label\=None_, _sample\_weight\=None_, _drop\_intermediate\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1049)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "Link to this definition")

Compute precision-recall pairs for different probability thresholds.

Note: Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 classification tasks, via one-vs-rest or one-vs-one, is not implemented.

The precision is the ratio `tp / (tp + fp)` where `tp` is the number of true positives and `fp` the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.

The recall is the ratio `tp / (tp + fn)` where `tp` is the number of true positives and `fn` the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.

The last precision and recall values are 1. and 0. respectively and do not have a corresponding threshold. This ensures that the graph starts on the y axis.

The first precision and recall values are precision=class balance and recall=1.0 which corresponds to a classifier that always predicts the positive class.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True binary labels. If labels are not either {-1, 1} or {0, 1}, then pos\_label should be explicitly given.

**y\_score**array-like of shape (n\_samples,)

Target scores, can either be probability estimates of the positive class, or non-thresholded measure of decisions (as returned by `decision_function` on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. When `pos_label=None`, if y\_true is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=False

Whether to drop some suboptimal thresholds which would not appear on a plotted precision-recall curve. This is useful in order to create lighter precision-recall curves.

Added in version 1.3.

Returns:

**precision**ndarray of shape (n\_thresholds + 1,)

Precision values such that element i is the precision of predictions with score >= thresholds\[i\] and the last element is 1.

**recall**ndarray of shape (n\_thresholds + 1,)

Decreasing recall values such that element i is the recall of predictions with score >= thresholds\[i\] and the last element is 0.

**thresholds**ndarray of shape (n\_thresholds,)

Increasing thresholds on the decision function used to compute precision and recall where `n_thresholds = len(np.unique(y_score))`.

See also

[`PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")

Plot Precision Recall Curve given a binary classifier.

[`PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")

Plot Precision Recall Curve using predictions from a binary classifier.

[`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")

Compute average precision from prediction scores.

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

For binary classification, compute true negative, false positive, false negative and true positive counts per threshold.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import precision\_recall\_curve
\>>> y\_true \= np.array(\[0, 0, 1, 1\])
\>>> y\_scores \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> precision, recall, thresholds \= precision\_recall\_curve(
...     y\_true, y\_scores)
\>>> precision
array(\[0.5       , 0.66666667, 0.5       , 1.        , 1.        \])
\>>> recall
array(\[1. , 1. , 0.5, 0.5, 0. \])
\>>> thresholds
array(\[0.1 , 0.35, 0.4 , 0.8 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

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