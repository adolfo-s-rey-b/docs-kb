[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html)

Collapse Sidebar Expand Sidebar

confusion\_matrix\_at\_thresholds[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#confusion-matrix-at-thresholds "Link to this heading")

==================================================================================================================================================================================================

sklearn.metrics.confusion\_matrix\_at\_thresholds(_y\_true_, _y\_score_, _\*_, _pos\_label\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L924)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "Link to this definition")

Calculate [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 confusion matrix terms per classification threshold.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
.

Added in version 1.8.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True targets of binary classification.

**y\_score**array-like of shape (n\_samples,)

Estimated probabilities or output of a decision function.

**pos\_label**int, float, bool or str, default=None

The label of the positive class.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**tns**ndarray of shape (n\_thresholds,)

A count of true negatives, at index `i` being the number of negative samples assigned a `score < thresholds[i]`.

**fps**ndarray of shape (n\_thresholds,)

A count of false positives, at index `i` being the number of negative samples assigned a `score >= thresholds[i]`. The total number of negative samples is equal to `fps[-1]`.

**fns**ndarray of shape (n\_thresholds,)

A count of false negatives, at index `i` being the number of positive samples assigned a `score < thresholds[i]`.

**tps**ndarray of shape (n\_thresholds,)

An increasing count of true positives, at index `i` being the number of positive samples assigned a `score >= thresholds[i]`. The total number of positive samples is equal to `tps[-1]`.

**thresholds**ndarray of shape (n\_thresholds,)

Decreasing score values.

See also

[`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

Compute classification matrix to evaluate the accuracy of a classifier.

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall curve.

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute Detection error tradeoff (DET) curve.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import confusion\_matrix\_at\_thresholds
\>>> y\_true \= np.array(\[0., 0., 1., 1.\])
\>>> y\_score \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> tns, fps, fns, tps, thresholds \= confusion\_matrix\_at\_thresholds(y\_true, y\_score)
\>>> tns
array(\[2., 1., 1., 0.\])
\>>> fps
array(\[0., 1., 1., 2.\])
\>>> fns
array(\[1., 1., 0., 0.\])
\>>> tps
array(\[1., 1., 2., 2.\])
\>>> thresholds
array(\[0.8 , 0.4 , 0.35, 0.1 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_confusion_matrix_thumb.png)

[Evaluate the performance of a classifier with Confusion Matrix](https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

Evaluate the performance of a classifier with Confusion Matrix

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)