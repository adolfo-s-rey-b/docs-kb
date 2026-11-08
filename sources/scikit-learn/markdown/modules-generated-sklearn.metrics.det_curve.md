[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.det_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.det_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.det_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.det_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.det_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.det_curve.html)

Collapse Sidebar Expand Sidebar

det\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#det-curve "Link to this heading")

=================================================================================================================================

sklearn.metrics.det\_curve(_y\_true_, _y\_score_, _pos\_label\=None_, _sample\_weight\=None_, _drop\_intermediate\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L302)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "Link to this definition")

Compute Detection Error Tradeoff (DET) for different probability thresholds.

Note: Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 classification tasks, via one-vs-rest or one-vs-one, is not implemented.

The DET curve is used for evaluation of ranking and error tradeoffs in binary classification tasks.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#det-curve)
.

Added in version 0.24.

Changed in version 1.7: An arbitrary threshold at infinity is added to represent a classifier that always predicts the negative class, i.e. `fpr=0` and `fnr=1`, unless `fpr=0` is already reached at a finite threshold.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True binary labels. If labels are not either {-1, 1} or {0, 1}, then pos\_label should be explicitly given.

**y\_score**array-like of shape of (n\_samples,)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=False

Whether to drop thresholds where true positives (tp) do not change from the previous or subsequent threshold. All points with the same tp value have the same `fnr` and thus same y coordinate.

Added in version 1.7.

Returns:

**fpr**ndarray of shape (n\_thresholds,)

False positive rate (FPR) such that element i is the false positive rate of predictions with score >= thresholds\[i\]. This is occasionally referred to as false acceptance probability or fall-out.

**fnr**ndarray of shape (n\_thresholds,)

False negative rate (FNR) such that element i is the false negative rate of predictions with score < thresholds\[i\]. This is occasionally referred to as false rejection or miss rate.

**thresholds**ndarray of shape (n\_thresholds,)

Increasing thresholds on the decision function (either `predict_proba` or `decision_function`) used to compute FPR and FNR.

Changed in version 1.7: An arbitrary threshold at infinity is added for the case `fpr=0` and `fnr=1`.

See also

[`DetCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")

Plot DET curve given an estimator and some data.

[`DetCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")

Plot DET curve given the true and predicted labels.

[`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")

DET curve visualization.

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall curve.

[`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

For binary classification, compute true negative, false positive, false negative and true positive counts per threshold.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import det\_curve
\>>> y\_true \= np.array(\[0, 0, 1, 1\])
\>>> y\_scores \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> fpr, fnr, thresholds \= det\_curve(y\_true, y\_scores)
\>>> fpr
array(\[0.5, 0.5, 0. \])
\>>> fnr
array(\[0. , 0.5, 0.5\])
\>>> thresholds
array(\[0.35, 0.4 , 0.8 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)