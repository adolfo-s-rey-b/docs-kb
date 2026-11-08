[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.LarsCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LarsCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.LarsCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LarsCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LarsCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LarsCV.html)

Collapse Sidebar Expand Sidebar

LarsCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#larscv "Link to this heading")

============================================================================================================================

class sklearn.linear\_model.LarsCV(_\*_, _fit\_intercept\=True_, _verbose\=False_, _max\_iter\=500_, _precompute\='auto'_, _cv\=None_, _max\_n\_alphas\=1000_, _n\_jobs\=None_, _eps\=np.float64(2.220446049250313e-16)_, _copy\_X\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L1518)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "Link to this definition")

Cross-validated Least Angle Regression model.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression)
.

Parameters:

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (i.e. data is expected to be centered).

**verbose**bool or int, default=False

Sets the verbosity amount.

**max\_iter**int, default=500

Maximum number of iterations to perform.

**precompute**bool, ‘auto’ or array-like , default=’auto’

Whether to use a precomputed Gram matrix to speed up calculations. If set to `'auto'` let us decide. The Gram matrix cannot be passed as argument since we will use only subsets of X.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross-validation,
    
*   integer, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**max\_n\_alphas**int, default=1000

The maximum number of points on the path used to compute the residuals in the cross-validation.

**n\_jobs**int or None, default=None

Number of CPUs to use during the cross validation. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**eps**float, default=np.finfo(float).eps

The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Unlike the `tol` parameter in some iterative optimization-based algorithms, this parameter does not control the tolerance of the optimization.

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

Attributes:

**active\_**list of length n\_alphas or list of such lists

Indices of active variables at the end of the path. If this is a list of lists, the outer list length is `n_targets`.

**coef\_**array-like of shape (n\_features,)

parameter vector (w in the formulation formula)

**intercept\_**float

independent term in decision function

**coef\_path\_**array-like of shape (n\_features, n\_alphas)

the varying values of the coefficients along the path

**alpha\_**float

the estimated regularization parameter alpha

**alphas\_**array-like of shape (n\_alphas,)

the different values of alpha along the path

**cv\_alphas\_**array-like of shape (n\_cv\_alphas,)

all the values of alpha along the path for the different folds

**mse\_path\_**array-like of shape (n\_folds, n\_cv\_alphas)

the mean square error on left-out for each fold along the path (alpha values given by `cv_alphas`)

**n\_iter\_**array-like or int

the number of iterations run by Lars with the optimal alpha.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")

Compute Lasso path with coordinate descent.

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

Linear Model trained with L1 prior as regularizer (aka the Lasso).

[`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

Lasso linear model with iterative fitting along a regularization path.

[`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")

Lasso model fit with Least Angle Regression a.k.a. Lars.

[`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")

Lasso model fit with Lars using BIC or AIC for model selection.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Sparse coding.

Notes

In `fit`, once the best parameter `alpha` is found through cross-validation, the model is fit again using the entire training set.

Examples

\>>> from sklearn.linear\_model import LarsCV
\>>> from sklearn.datasets import make\_regression
\>>> X, y \= make\_regression(n\_samples\=200, noise\=4.0, random\_state\=0)
\>>> reg \= LarsCV(cv\=5).fit(X, y)
\>>> reg.score(X, y)
0.9996
\>>> reg.alpha\_
np.float64(0.2961)
\>>> reg.predict(X\[:1,\])
array(\[154.3996\])

Copy to clipboard

fit(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L1700)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.fit "Link to this definition")

Fit the model using X, y as training data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,)

Target values.

**\*\*params**dict, default=None

Parameters to be passed to the CV splitter.

Added in version 1.4: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Returns an instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L1813)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.score "Link to this definition")

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

set\_fit\_request() → [LarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model._least_angle.LarsCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.set_fit_request "Link to this definition")

No-op.

Calling this method has no effect.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LarsCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model._least_angle.LarsCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV.set_score_request "Link to this definition")

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)