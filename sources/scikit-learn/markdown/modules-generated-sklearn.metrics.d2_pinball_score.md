[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.d2_pinball_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.d2_pinball_score.html)

Collapse Sidebar Expand Sidebar

d2\_pinball\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#d2-pinball-score "Link to this heading")

=======================================================================================================================================================

sklearn.metrics.d2\_pinball\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _alpha\=0.5_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1698)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "Link to this definition")

D2 regression score function, fraction of pinball loss explained.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A model that always uses the empirical alpha-quantile of `y_true` as constant prediction, disregarding the input features, gets a D2 score of 0.0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#d2-score)
.

Added in version 1.1.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**alpha**float, default=0.5

Slope of the pinball deviance. It determines the quantile level alpha for which the pinball deviance and also D2 are optimal. The default `alpha=0.5` is equivalent to `d2_absolute_error_score`.

**multioutput**{‘raw\_values’, ‘uniform\_average’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output values. Array-like value defines weights used to average scores.

‘raw\_values’ :

Returns a full set of errors in case of multioutput input.

‘uniform\_average’ :

Scores of all outputs are averaged with uniform weight.

Returns:

**score**float or ndarray of floats

The D2 score with a pinball deviance or ndarray of scores if `multioutput='raw_values'`.

Notes

Like R2, D2 score may be negative (it need not actually be the square of a quantity D).

This metric is not well-defined for a single point and will return a NaN value if n\_samples is less than two.

This metric is not a built-in [string name scorer](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
 to use along with tools such as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 or [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
. Instead, you can [create a scorer object](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-adapt-metric)
 using [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
, with any desired parameter settings. See the `Examples` section for details.

References

\[1\]

Eq. (7) of [Koenker, Roger; Machado, José A. F. (1999). “Goodness of Fit and Related Inference Processes for Quantile Regression”](https://doi.org/10.1080/01621459.1999.10473882)

\[2\]

Eq. (3.11) of Hastie, Trevor J., Robert Tibshirani and Martin J. Wainwright. “Statistical Learning with Sparsity: The Lasso and Generalizations.” (2015). [https://hastie.su.domains/StatLearnSparsity/](https://hastie.su.domains/StatLearnSparsity/)

Examples

\>>> from sklearn.metrics import d2\_pinball\_score
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[1, 3, 3\]
\>>> d2\_pinball\_score(y\_true, y\_pred)
0.5
\>>> d2\_pinball\_score(y\_true, y\_pred, alpha\=0.9)
0.666...
\>>> d2\_pinball\_score(y\_true, y\_pred, alpha\=0.1)
\-1.999...
\>>> d2\_pinball\_score(y\_true, y\_true, alpha\=0.1)
1.0

Copy to clipboard

Creating a scorer object with [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
:

\>>> import numpy as np
\>>> from sklearn.metrics import make\_scorer
\>>> from sklearn.model\_selection import GridSearchCV
\>>> from sklearn.linear\_model import QuantileRegressor
\>>> X \= np.array(\[\[1\], \[2\], \[3\], \[4\]\])
\>>> y \= np.array(\[2.5, 0.0, 2, 8\])
\>>> pinball\_95\_scorer \= make\_scorer(d2\_pinball\_score, alpha\=0.95)
\>>> grid \= GridSearchCV(
...     QuantileRegressor(quantile\=0.95),
...     param\_grid\={"fit\_intercept": \[True, False\]},
...     scoring\=pinball\_95\_scorer,
...     cv\=2,
... ).fit(X, y)
\>>> grid.best\_params\_
{'fit\_intercept': True}

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)