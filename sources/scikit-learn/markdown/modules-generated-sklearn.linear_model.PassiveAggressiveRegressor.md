[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)

Collapse Sidebar Expand Sidebar

PassiveAggressiveRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#passiveaggressiveregressor "Link to this heading")

========================================================================================================================================================================================

class sklearn.linear\_model.PassiveAggressiveRegressor(_\*_, _C\=1.0_, _fit\_intercept\=True_, _max\_iter\=1000_, _tol\=0.001_, _early\_stopping\=False_, _validation\_fraction\=0.1_, _n\_iter\_no\_change\=5_, _shuffle\=True_, _verbose\=0_, _loss\='epsilon\_insensitive'_, _epsilon\=0.1_, _random\_state\=None_, _warm\_start\=False_, _average\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_passive_aggressive.py#L343)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "Link to this definition")

Passive Aggressive Regressor.

Deprecated since version 1.8: The whole class `PassiveAggressiveRegressor` was deprecated in version 1.8 and will be removed in 1.10. Instead use:

reg \= SGDRegressor(
    loss\="epsilon\_insensitive",
    penalty\=None,
    learning\_rate\="pa1",  \# or "pa2"
    eta0\=1.0,  \# for parameter C
)

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive)
.

Parameters:

**C**float, default=1.0

Aggressiveness parameter for the passive-aggressive algorithm, see \[1\]. For PA-I it is the maximum step size. For PA-II it regularizes the step size (the smaller `C` the more it regularizes). As a general rule-of-thumb, `C` should be small when the data is noisy.

**fit\_intercept**bool, default=True

Whether the intercept should be estimated or not. If False, the data is assumed to be already centered. Defaults to True.

**max\_iter**int, default=1000

The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the `fit` method, and not the [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.partial_fit "sklearn.linear_model.PassiveAggressiveRegressor.partial_fit")
 method.

Added in version 0.19.

**tol**float or None, default=1e-3

The stopping criterion. If it is not None, the iterations will stop when (loss > previous\_loss - tol).

Added in version 0.19.

**early\_stopping**bool, default=False

Whether to use early stopping to terminate training when validation. score is not improving. If set to True, it will automatically set aside a fraction of training data as validation and terminate training when validation score is not improving by at least tol for n\_iter\_no\_change consecutive epochs.

Added in version 0.20.

**validation\_fraction**float, default=0.1

The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1. Only used if early\_stopping is True.

Added in version 0.20.

**n\_iter\_no\_change**int, default=5

Number of iterations with no improvement to wait before early stopping.

Added in version 0.20.

**shuffle**bool, default=True

Whether or not the training data should be shuffled after each epoch.

**verbose**int, default=0

The verbosity level.

**loss**str, default=”epsilon\_insensitive”

The loss function to be used: epsilon\_insensitive: equivalent to PA-I in the reference paper. squared\_epsilon\_insensitive: equivalent to PA-II in the reference paper.

**epsilon**float, default=0.1

If the difference between the current prediction and the correct label is below this threshold, the model is not updated.

**random\_state**int, RandomState instance, default=None

Used to shuffle the training data, when `shuffle` is set to `True`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**warm\_start**bool, default=False

When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

Repeatedly calling fit or partial\_fit when warm\_start is True can result in a different solution than when calling fit a single time because of the way the data is shuffled.

**average**bool or int, default=False

When set to True, computes the averaged SGD weights and stores the result in the `coef_` attribute. If set to an int greater than 1, averaging will begin once the total number of samples seen reaches average. So average=10 will begin averaging after seeing 10 samples.

Added in version 0.19: parameter _average_ to use weights averaging in SGD.

Attributes:

**coef\_**array, shape = \[1, n\_features\] if n\_classes == 2 else \[n\_classes, n\_features\]

Weights assigned to the features.

**intercept\_**array, shape = \[1\] if n\_classes == 2 else \[n\_classes\]

Constants in decision function.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

The actual number of iterations to reach the stopping criterion.

**t\_**int

Number of weight updates performed during training. Same as `(n_iter_ * n_samples + 1)`.

See also

[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")

Linear model fitted by minimizing a regularized empirical loss with SGD.

References

Online Passive-Aggressive Algorithms <[http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf](http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf)
\> K. Crammer, O. Dekel, J. Keshat, S. Shalev-Shwartz, Y. Singer - JMLR (2006).

Examples

\>>> from sklearn.linear\_model import PassiveAggressiveRegressor
\>>> from sklearn.datasets import make\_regression

Copy to clipboard

\>>> X, y \= make\_regression(n\_features\=4, random\_state\=0)
\>>> regr \= PassiveAggressiveRegressor(max\_iter\=100, random\_state\=0,
... tol\=1e-3)
\>>> regr.fit(X, y)
PassiveAggressiveRegressor(max\_iter=100, random\_state=0)
\>>> print(regr.coef\_)
\[20.48736655 34.18818427 67.59122734 87.94731329\]
\>>> print(regr.intercept\_)
\[-0.02306214\]
\>>> print(regr.predict(\[\[0, 0, 0, 0\]\]))
\[-0.02306214\]

Copy to clipboard

densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.densify "Link to this definition")

Convert coefficient matrix to dense array format.

Converts the `coef_` member (back) to a numpy.ndarray. This is the default format of `coef_` and is required for fitting, so calling this method is only required on models that have previously been sparsified; otherwise, it is a no-op.

Returns:

self

Fitted estimator.

fit(_X_, _y_, _coef\_init\=None_, _intercept\_init\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_passive_aggressive.py#L588)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.fit "Link to this definition")

Fit linear model with Passive Aggressive algorithm.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**numpy array of shape \[n\_samples\]

Target values.

**coef\_init**array, shape = \[n\_features\]

The initial coefficients to warm-start the optimization.

**intercept\_init**array, shape = \[1\]

The initial intercept to warm-start the optimization.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_passive_aggressive.py#L555)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.partial_fit "Link to this definition")

Fit linear model with Passive Aggressive algorithm.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Subset of training data.

**y**numpy array of shape \[n\_samples\]

Subset of target values.

Returns:

**self**object

Fitted estimator.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L1697)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)

Input data.

Returns:

ndarray of shape (n\_samples,)

Predicted target values per element in X.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.score "Link to this definition")

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

set\_fit\_request(_\*_, _coef\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _intercept\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [PassiveAggressiveRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.set_fit_request "Link to this definition")

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

**coef\_init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `coef_init` parameter in `fit`.

**intercept\_init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `intercept_init` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_partial\_fit\_request() → [PassiveAggressiveRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.set_partial_fit_request "Link to this definition")

No-op.

Calling this method has no effect.

Returns:

**self**object

The updated object.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [PassiveAggressiveRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model._passive_aggressive.PassiveAggressiveRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.set_score_request "Link to this definition")

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

sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.sparsify "Link to this definition")

Convert coefficient matrix to sparse format.

Converts the `coef_` member to a scipy.sparse matrix, which for L1-regularized models can be much more memory- and storage-efficient than the usual numpy.ndarray representation.

The `intercept_` member is not converted.

Warning

This method is not supported for estimators fitted with array API inputs (i.e. when [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor.predict "sklearn.linear_model.PassiveAggressiveRegressor.predict")
 and other methods involving passing arrays may raise or return unexpected results.

Returns:

self

Fitted estimator.

Notes

For non-sparse models, i.e. when there are not many zeros in `coef_`, this may actually _increase_ memory usage, so use this method with care. A rule of thumb is that the number of zero elements, which can be computed with `(coef_ == 0).sum()`, must be more than 50% for this to provide significant benefits.

After calling this method, further fitting with the partial\_fit method (if any) will not work until you call densify.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)