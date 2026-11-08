[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.QuantileRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.QuantileRegressor.html)

Collapse Sidebar Expand Sidebar

QuantileRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#quantileregressor "Link to this heading")

=============================================================================================================================================================

class sklearn.linear\_model.QuantileRegressor(_\*_, _quantile\=0.5_, _alpha\=1.0_, _fit\_intercept\=True_, _solver\='highs'_, _solver\_options\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_quantile.py#L20)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "Link to this definition")

Linear regression model that predicts conditional quantiles.

The linear [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 optimizes the pinball loss for a desired `quantile` and is robust to outliers.

This model uses an L1 regularization like [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#quantile-regression)
.

Added in version 1.0.

Parameters:

**quantile**float, default=0.5

The quantile that the model tries to predict. It must be strictly between 0 and 1. If 0.5 (default), the model predicts the 50% quantile, i.e. the median.

**alpha**float, default=1.0

Regularization constant that multiplies the L1 penalty term.

**fit\_intercept**bool, default=True

Whether or not to fit the intercept.

**solver**{‘highs-ds’, ‘highs-ipm’, ‘highs’, ‘interior-point’, ‘revised simplex’}, default=’highs’

Method used by [`scipy.optimize.linprog`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog "(in SciPy v1.18.0)")
 to solve the linear programming formulation.

It is recommended to use the highs methods because they are the fastest ones. Solvers “highs-ds”, “highs-ipm” and “highs” support sparse input data and, in fact, always convert to sparse csc.

From `scipy>=1.11.0`, “interior-point” is not available anymore.

Changed in version 1.4: The default of `solver` changed to `"highs"` in version 1.4.

**solver\_options**dict, default=None

Additional parameters passed to [`scipy.optimize.linprog`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog "(in SciPy v1.18.0)")
 as options. If `None` and if `solver='interior-point'`, then `{"lstsq": True}` is passed to [`scipy.optimize.linprog`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog "(in SciPy v1.18.0)")
 for the sake of stability.

Attributes:

**coef\_**array of shape (n\_features,)

Estimated coefficients for the features.

**intercept\_**float

The intercept of the model, aka bias term.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

The actual number of iterations performed by the solver.

See also

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

The Lasso is a linear model that estimates sparse coefficients with l1 regularization.

[`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")

Linear regression model that is robust to outliers.

Examples

\>>> from sklearn.linear\_model import QuantileRegressor
\>>> import numpy as np
\>>> n\_samples, n\_features \= 10, 2
\>>> rng \= np.random.RandomState(0)
\>>> y \= rng.randn(n\_samples)
\>>> X \= rng.randn(n\_samples, n\_features)
\>>> \# the two following lines are optional in practice
\>>> from sklearn.utils.fixes import sp\_version, parse\_version
\>>> reg \= QuantileRegressor(quantile\=0.8).fit(X, y)
\>>> np.mean(y <= reg.predict(X))
np.float64(0.8)

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_quantile.py#L142)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.fit "Link to this definition")

Fit the model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**self**object

Returns self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L301)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.score "Link to this definition")

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

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model._quantile.QuantileRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model._quantile.QuantileRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor.set_score_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `score` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `score`.

Returns:

**self**object

The updated object.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_thumb.png)

[Quantile regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)

Quantile regression

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)