[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.roc_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.roc_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.roc_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.roc_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.roc_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.roc_curve.html)

Collapse Sidebar Expand Sidebar

roc\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#roc-curve "Link to this heading")

=================================================================================================================================

sklearn.metrics.roc\_curve(_y\_true_, _y\_score_, _\*_, _pos\_label\=None_, _sample\_weight\=None_, _drop\_intermediate\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1208)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "Link to this definition")

Compute Receiver operating characteristic (ROC).

Note: Support beyond [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 classification tasks, via one-vs-rest or one-vs-one, is not implemented.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True binary labels. If labels are not either {-1, 1} or {0, 1}, then pos\_label should be explicitly given.

**y\_score**array-like of shape (n\_samples,)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers). For [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 scores, values greater than or equal to zero should indicate the positive class.

**pos\_label**int, float, bool or str, default=None

The label of the positive class. When `pos_label=None`, if `y_true` is in {-1, 1} or {0, 1}, `pos_label` is set to 1, otherwise an error will be raised.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**drop\_intermediate**bool, default=True

Whether to drop thresholds where the resulting point is collinear with its neighbors in ROC space. This has no effect on the ROC AUC or visual shape of the curve, but reduces the number of plotted points.

Added in version 0.17: parameter _drop\_intermediate_.

Returns:

**fpr**ndarray of shape (>2,)

Increasing false positive rates such that element `i` is the false positive rate of predictions with score >= `thresholds[i]`.

**tpr**ndarray of shape (>2,)

Increasing true positive rates such that element `i` is the true positive rate of predictions with score >= `thresholds[i]`.

**thresholds**ndarray of shape (n\_thresholds,)

Decreasing thresholds on the decision function used to compute fpr and tpr. The first threshold is set to `np.inf`.

Changed in version 1.3: An arbitrary threshold at infinity (stored in `thresholds[0]`) is added to represent a classifier that always predicts the negative class, i.e. `fpr=0` and `tpr=0`.

See also

[`RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")

Plot Receiver Operating Characteristic (ROC) curve given an estimator and some data.

[`RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")

Plot Receiver Operating Characteristic (ROC) curve given the true and predicted values.

[`RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")

Plot multi-fold ROC curves given cross-validation results.

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

[`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

For binary classification, compute true negative, false positive, false negative and true positive counts per threshold.

Notes

Since the thresholds are sorted from low to high values, they are reversed upon returning them to ensure they correspond to both `fpr` and `tpr`, which are sorted in reversed order during their calculation.

References

\[1\]

[Wikipedia entry for the Receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)

\[2\]

Fawcett T. An introduction to ROC analysis\[J\]. Pattern Recognition Letters, 2006, 27(8):861-874.

Examples

\>>> import numpy as np
\>>> from sklearn import metrics
\>>> y \= np.array(\[1, 1, 2, 2\])
\>>> scores \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> fpr, tpr, thresholds \= metrics.roc\_curve(y, scores, pos\_label\=2)
\>>> fpr
array(\[0. , 0. , 0.5, 0.5, 1. \])
\>>> tpr
array(\[0. , 0.5, 0.5, 1. , 1. \])
\>>> thresholds
array(\[ inf, 0.8 , 0.4 , 0.35, 0.1 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_display_object_visualization_thumb.png)

[Visualizations with Display Objects](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html)

Visualizations with Display Objects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_det_thumb.png)

[Detection error tradeoff (DET) curve](https://scikit-learn.org/stable/auto_examples/model_selection/plot_det.html)

Detection error tradeoff (DET) curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)