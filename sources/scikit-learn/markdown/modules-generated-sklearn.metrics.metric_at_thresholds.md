[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.metric_at_thresholds.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.metric_at_thresholds.html)

Collapse Sidebar Expand Sidebar

metric\_at\_thresholds[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#metric-at-thresholds "Link to this heading")

===================================================================================================================================================================

sklearn.metrics.metric\_at\_thresholds(_y\_true_, _y\_score_, _metric\_func_, _\*_, _sample\_weight\=None_, _metric\_params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L2250)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#sklearn.metrics.metric_at_thresholds "Link to this definition")

Compute `metric_func` per threshold for [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 data.

Aids visualization of metric values across thresholds when tuning the [decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html#threshold-tuning)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/classification_threshold.html#metric-at-thresholds)
.

Added in version 1.9.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target labels.

**y\_score**array-like of shape (n\_samples,)

Continuous prediction scores, either estimated probabilities of the positive class or output of a [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
.

**metric\_func**callable

The metric function to use. It will be called as `metric_func(y_true, y_pred, **metric_params)`, where `y_pred` are thresholded predictions, internally computed as `y_pred = (y_score >= threshold)`. The output should be a single numeric or a collection where each element has the same size.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If not `None`, will be passed to `metric_func`.

**metric\_params**dict, default=None

Parameters to pass to `metric_func`.

Returns:

**metric\_values**ndarray of shape (n\_thresholds,) or (n\_thresholds, \*n\_outputs)

The scores associated with each threshold. If `metric_func` returns a collection (e.g., a tuple of floats), the output would be a 2D array of shape (n\_thresholds, \*n\_outputs).

**thresholds**ndarray of shape (n\_thresholds,)

The thresholds used to compute the scores.

See also

[`confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")

Compute binary confusion matrix per threshold.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall pairs for different probability thresholds.

[`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")

Compute error rates for different probability thresholds.

[`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")

Compute Receiver operating characteristic (ROC) curve.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import accuracy\_score, metric\_at\_thresholds
\>>> y\_true \= np.array(\[0, 0, 1, 1\])
\>>> y\_score \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> metric\_values, thresholds \= metric\_at\_thresholds(
...     y\_true, y\_score, accuracy\_score)
\>>> thresholds
array(\[0.8 , 0.4 , 0.35, 0.1 \])
\>>> metric\_values
array(\[0.75, 0.5 , 0.75, 0.5 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)