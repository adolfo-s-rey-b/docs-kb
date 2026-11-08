[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.RegressorMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.RegressorMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.RegressorMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.RegressorMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.RegressorMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.RegressorMixin.html)

Collapse Sidebar Expand Sidebar

RegressorMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#regressormixin "Link to this heading")

============================================================================================================================================

class sklearn.base.RegressorMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L631)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "Link to this definition")

Mixin class for all regression estimators in scikit-learn.

This mixin defines the following functionality:

*   set estimator type to `"regressor"` through the `estimator_type` tag;
    
*   `score` method that default to [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    .
    
*   enforce that `fit` requires `y` to be passed through the `requires_y` tag, which is done by setting the regressor type tag.
    

Read more in the [User Guide](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)
.

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, RegressorMixin
\>>> \# Mixin classes should always be on the left-hand side for a correct MRO
\>>> class MyEstimator(RegressorMixin, BaseEstimator):
...     def \_\_init\_\_(self, \*, param\=1):
...         self.param \= param
...     def fit(self, X, y\=None):
...         self.is\_fitted\_ \= True
...         return self
...     def predict(self, X):
...         return np.full(shape\=X.shape\[0\], fill\_value\=self.param)
\>>> estimator \= MyEstimator(param\=0)
\>>> X \= np.array(\[\[1, 2\], \[2, 3\], \[3, 4\]\])
\>>> y \= np.array(\[\-1, 0, 1\])
\>>> estimator.fit(X, y).predict(X)
array(\[0, 0, 0\])
\>>> estimator.score(X, y)
0.0

Copy to clipboard

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin.score "Link to this definition")

Return [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)
 on test data.

The coefficient of determination, R2, is defined as (1−uv), where u is the residual sum of squares `((y_true - y_pred)** 2).sum()` and v is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of `y`, disregarding the input features, would get a R2 score of 0.0.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples. For some estimators this may be a precomputed kernel matrix or a list of generic objects instead with shape `(n_samples, n_samples_fitted)`, where `n_samples_fitted` is the number of samples used in the fitting for the estimator.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True values for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

R2 of `self.predict(X)` w.r.t. `y`.

Notes

The R2 score used when calling `score` on a regressor uses `multioutput='uniform_average'` from version 0.23 to keep consistent with default value of [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
. This influences the `score` method of all the multioutput regressors (except for [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
).

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)