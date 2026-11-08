[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.brier_score_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.brier_score_loss.html)

Collapse Sidebar Expand Sidebar

brier\_score\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#brier-score-loss "Link to this heading")

=======================================================================================================================================================

sklearn.metrics.brier\_score\_loss(_y\_true_, _y\_proba_, _\*_, _sample\_weight\=None_, _pos\_label\=None_, _labels\=None_, _scale\_by\_half\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L3702)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "Link to this definition")

Compute the Brier score loss.

The smaller the Brier score loss, the better, hence the naming with “loss”. The Brier score measures the mean squared difference between the predicted probability and the actual outcome. The Brier score is a strictly proper scoring rule.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#brier-score-loss)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True targets.

**y\_proba**array-like of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted probabilities. If `y_proba.shape = (n_samples,)` the probabilities provided are assumed to be that of the positive class. If `y_proba.shape = (n_samples, n_classes)` the columns in `y_proba` are assumed to correspond to the labels in alphabetical order, as done by [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**pos\_label**int, float, bool or str, default=None

Label of the positive class when `y_proba.shape = (n_samples,)`. If not provided, `pos_label` will be inferred in the following manner:

*   if `y_true` in {-1, 1} or {0, 1}, `pos_label` defaults to 1;
    
*   else if `y_true` contains string, an error will be raised and `pos_label` should be explicitly specified;
    
*   otherwise, `pos_label` defaults to the greater label, i.e. `np.unique(y_true)[-1]`.
    

**labels**array-like of shape (n\_classes,), default=None

Class labels when `y_proba.shape = (n_samples, n_classes)`. If not provided, labels will be inferred from `y_true`.

Added in version 1.7.

**scale\_by\_half**bool or “auto”, default=”auto”

When True, scale the Brier score by 1/2 to lie in the \[0, 1\] range instead of the \[0, 2\] range. The default “auto” option implements the rescaling to \[0, 1\] only for binary classification (as customary) but keeps the original \[0, 2\] range for multiclass classification.

Added in version 1.7.

Returns:

**score**float

Brier score loss.

Notes

For N observations labeled from C possible classes, the Brier score is defined as:

1N∑i\=1N∑c\=1C(yic−p^ic)2

where yic is 1 if observation `i` belongs to class `c`, otherwise 0 and p^ic is the predicted probability for observation `i` to belong to class `c`. The Brier score then ranges between \[0,2\].

In binary classification tasks the Brier score is usually divided by two and then ranges between \[0,1\]. It can be alternatively written as:

1N∑i\=1N(yi−p^i)2

where yi is the binary target and p^i is the predicted probability of the positive class.

References

\[1\]

[Wikipedia entry for the Brier score](https://en.wikipedia.org/wiki/Brier_score)
.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import brier\_score\_loss
\>>> y\_true \= np.array(\[0, 1, 1, 0\])
\>>> y\_true\_categorical \= np.array(\["spam", "ham", "ham", "spam"\])
\>>> y\_prob \= np.array(\[0.1, 0.9, 0.8, 0.3\])
\>>> brier\_score\_loss(y\_true, y\_prob)
0.0375
\>>> brier\_score\_loss(y\_true, 1\-y\_prob, pos\_label\=0)
0.0375
\>>> brier\_score\_loss(y\_true\_categorical, y\_prob, pos\_label\="ham")
0.0375
\>>> brier\_score\_loss(y\_true, np.array(y\_prob) \> 0.5)
0.0
\>>> brier\_score\_loss(y\_true, y\_prob, scale\_by\_half\=False)
0.075
\>>> brier\_score\_loss(
...    \["eggs", "ham", "spam"\],
...    \[\[0.8, 0.1, 0.1\], \[0.2, 0.7, 0.1\], \[0.2, 0.2, 0.6\]\],
...    labels\=\["eggs", "ham", "spam"\]
... )
0.146

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)