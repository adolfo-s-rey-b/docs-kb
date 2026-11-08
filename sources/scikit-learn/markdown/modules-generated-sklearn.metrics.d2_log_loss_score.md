[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.d2_log_loss_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.d2_log_loss_score.html)

Collapse Sidebar Expand Sidebar

d2\_log\_loss\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#d2-log-loss-score "Link to this heading")

===========================================================================================================================================================

sklearn.metrics.d2\_log\_loss\_score(_y\_true_, _y\_proba\=None_, _\*_, _sample\_weight\=None_, _labels\=None_, _y\_pred\='deprecated'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3859)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "Link to this definition")

D2 score function, fraction of log loss explained.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A model that always predicts the per-class proportions of `y_true`, disregarding the input features, gets a D^2 score of 0.0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#d2-score-classification)
.

Added in version 1.5.

Parameters:

**y\_true**array-like or label indicator matrix

The actuals labels for the n\_samples samples.

**y\_proba**array-like of shape (n\_samples, n\_classes) or (n\_samples,)

Predicted probabilities, as returned by a classifier’s predict\_proba method. If `y_proba.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. The labels in `y_proba` are assumed to be ordered alphabetically, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

Added in version 1.9: `y_pred` was renamed to `y_proba`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**labels**array-like, default=None

If not provided, labels will be inferred from y\_true. If `labels` is `None` and `y_pred` has shape (n\_samples,) the labels are assumed to be binary and are inferred from `y_true`.

**y\_pred**array-like of shape (n\_samples, n\_classes) or (n\_samples,)

Predicted probabilities, as returned by a classifier’s predict\_proba method. If `y_pred.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. The labels in `y_pred` are assumed to be ordered alphabetically, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

Deprecated since version 1.9: `y_pred` was deprecated in favor of `y_proba` in v1.9 and will be removed in v1.11.

Returns:

**d2**float or ndarray of floats

The D^2 score.

Notes

This is not a symmetric function.

Like R^2, D^2 score may be negative (it need not actually be the square of a quantity D).

This metric is not well-defined for a single sample and will return a NaN value if n\_samples is less than two.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)