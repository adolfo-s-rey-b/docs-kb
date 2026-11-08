[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.TheilSenRegressor.html)

Collapse Sidebar Expand Sidebar

TheilSenRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#theilsenregressor "Link to this heading")

=============================================================================================================================================================

class sklearn.linear\_model.TheilSenRegressor(_\*_, _fit\_intercept\=True_, _max\_subpopulation\=10000.0_, _n\_subsamples\=None_, _max\_iter\=300_, _tol\=0.001_, _random\_state\=None_, _n\_jobs\=None_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_theil_sen.py#L207)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "Link to this definition")

Theil-Sen Estimator: robust multivariate regression model.

The algorithm calculates least square solutions on subsets with size n\_subsamples of the samples in X. Any value of n\_subsamples between the number of features and samples leads to an estimator with a compromise between robustness and efficiency. Since the number of least square solutions is “n\_samples choose n\_subsamples”, it can be extremely large and can therefore be limited with max\_subpopulation. If this limit is reached, the subsets are chosen randomly. In a final step, the spatial median (or L1 median) is calculated of all least square solutions.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#theil-sen-regression)
.

Parameters:

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations.

**max\_subpopulation**int, default=1e4

Instead of computing with a set of cardinality ‘n choose k’, where n is the number of samples and k is the number of subsamples (at least number of features), consider only a stochastic subpopulation of a given maximal size if ‘n choose k’ is larger than max\_subpopulation. For other than small problem sizes this parameter will determine memory usage and runtime if n\_subsamples is not changed. Note that the data type should be int but floats such as 1e4 can be accepted too.

**n\_subsamples**int, default=None

Number of samples to calculate the parameters. This is at least the number of features (plus 1 if fit\_intercept=True) and the number of samples as a maximum. A lower number leads to a higher breakdown point and a low efficiency while a high number leads to a low breakdown point and a high efficiency. If None, take the minimum number of subsamples leading to maximal robustness. If n\_subsamples is set to n\_samples, Theil-Sen is identical to least squares.

**max\_iter**int, default=300

Maximum number of iterations for the calculation of spatial median.

**tol**float, default=1e-3

Tolerance when calculating spatial median.

**random\_state**int, RandomState instance or None, default=None

A random number generator instance to define the state of the random permutations generator. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int, default=None

Number of CPUs to use during the cross validation. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**bool, default=False

Verbose mode when fitting the model.

Attributes:

**coef\_**ndarray of shape (n\_features,)

Coefficients of the regression model (median of distribution).

**intercept\_**float

Estimated intercept of regression model.

**breakdown\_**float

Approximated breakdown point.

**n\_iter\_**int

Number of iterations needed for the spatial median.

**n\_subpopulation\_**int

Number of combinations taken into account from ‘n choose k’, where n is the number of samples and k is the number of subsamples.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")

Linear regression model that is robust to outliers.

[`RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")

RANSAC (RANdom SAmple Consensus) algorithm.

[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")

Fitted by minimizing a regularized empirical loss with SGD.

References

*   Theil-Sen Estimators in a Multiple Linear Regression Model, 2009 Xin Dang, Hanxiang Peng, Xueqin Wang and Heping Zhang [http://home.olemiss.edu/~xdang/papers/MTSE.pdf](http://home.olemiss.edu/~xdang/papers/MTSE.pdf)
    

Examples

\>>> from sklearn.linear\_model import TheilSenRegressor
\>>> from sklearn.datasets import make\_regression
\>>> X, y \= make\_regression(
...     n\_samples\=200, n\_features\=2, noise\=4.0, random\_state\=0)
\>>> reg \= TheilSenRegressor(random\_state\=0).fit(X, y)
\>>> reg.score(X, y)
0.9884
\>>> reg.predict(X\[:1,\])
array(\[-31.5871\])

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_theil_sen.py#L391)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.fit "Link to this definition")

Fit linear model.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Training data.

**y**ndarray of shape (n\_samples,)

Target values.

Returns:

**self**returns an instance of self.

Fitted `TheilSenRegressor` estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L301)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.score "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model._theil_sen.TheilSenRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)