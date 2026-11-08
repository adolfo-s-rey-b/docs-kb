[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.log_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.log_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.log_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.log_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.log_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.log_loss.html)

Collapse Sidebar Expand Sidebar

log\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#log-loss "Link to this heading")

==============================================================================================================================

sklearn.metrics.log\_loss(_y\_true_, _y\_proba\=None_, _\*_, _normalize\=True_, _sample\_weight\=None_, _labels\=None_, _y\_pred\='deprecated'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3310)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "Link to this definition")

Log loss, aka logistic loss or cross-entropy loss.

This is the loss function used in (multinomial) logistic regression and extensions of it such as neural networks, defined as the negative log-likelihood of a logistic model that returns `y_proba` probabilities for its training data `y_true`. The log loss is only defined for two or more labels. For a single sample with true label y∈{0,1} and a probability estimate p\=Pr(y\=1), the log loss is:

Llog(y,p)\=−(ylog⁡(p)+(1−y)log⁡(1−p))

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)
.

Parameters:

**y\_true**array-like or label indicator matrix

Ground truth (correct) labels for n\_samples samples.

**y\_proba**array-like of float, shape = (n\_samples, n\_classes) or (n\_samples,)

Predicted probabilities, as returned by a classifier’s predict\_proba method. If `y_proba.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. The labels in `y_proba` are assumed to be ordered alphabetically, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

`y_proba` values are clipped to `[eps, 1-eps]` where `eps` is the machine precision for `y_proba`’s dtype.

Added in version 1.9: `y_pred` was renamed to `y_proba`.

**normalize**bool, default=True

If true, return the mean loss per sample. Otherwise, return the sum of the per-sample losses.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**labels**array-like, default=None

If not provided, labels will be inferred from y\_true. If `labels` is `None` and `y_pred` has shape (n\_samples,) the labels are assumed to be binary and are inferred from `y_true`.

Added in version 0.18.

**y\_pred**array-like of float, shape = (n\_samples, n\_classes) or (n\_samples,)

Predicted probabilities, as returned by a classifier’s predict\_proba method. If `y_pred.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. The labels in `y_pred` are assumed to be ordered alphabetically, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

`y_pred` values are clipped to `[eps, 1-eps]` where `eps` is the machine precision for `y_pred`’s dtype.

Deprecated since version 1.9: `y_pred` was deprecated in favor of `y_proba` in v1.9 and will be removed in v1.11.

Returns:

**loss**float

Log loss, aka logistic loss or cross-entropy loss.

Notes

The logarithm used is the natural logarithm (base-e).

References

C.M. Bishop (2006). [Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
. Springer, p. 209.

Examples

\>>> from sklearn.metrics import log\_loss
\>>> log\_loss(\["spam", "ham", "ham", "spam"\],
...          \[\[.1, .9\], \[.9, .1\], \[.8, .2\], \[.35, .65\]\])
0.21616

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_thumb.png)

[Gradient Boosting Out-of-Bag estimates](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)

Gradient Boosting Out-of-Bag estimates

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_thumb.png)

[Probabilistic predictions with Gaussian process classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)

Probabilistic predictions with Gaussian process classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)