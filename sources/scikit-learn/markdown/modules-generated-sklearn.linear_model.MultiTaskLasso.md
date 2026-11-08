[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.MultiTaskLasso.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.MultiTaskLasso.html)

Collapse Sidebar Expand Sidebar

MultiTaskLasso[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#multitasklasso "Link to this heading")

====================================================================================================================================================

class sklearn.linear\_model.MultiTaskLasso(_alpha\=1.0_, _\*_, _fit\_intercept\=True_, _copy\_X\=True_, _max\_iter\=1000_, _tol\=0.0001_, _warm\_start\=False_, _random\_state\=None_, _selection\='cyclic'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L2868)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "Link to this definition")

Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.

The optimization objective for Lasso is:

(1 / (2 \* n\_samples)) \* ||Y \- XW||^2\_Fro + alpha \* ||W||\_21

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of norm of each row.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso)
.

Parameters:

**alpha**float, default=1.0

Constant that multiplies the L1/L2 term. Defaults to 1.0.

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (i.e. data is expected to be centered).

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

**max\_iter**int, default=1000

The maximum number of iterations.

**tol**float, default=1e-4

The tolerance for the optimization: if the updates are smaller or equal to `tol`, the optimization code checks the dual gap for optimality and continues until it is smaller or equal to `tol`.

**warm\_start**bool, default=False

When set to `True`, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**random\_state**int, RandomState instance, default=None

The seed of the pseudo random number generator that selects a random feature to update. Used when `selection` == ‘random’. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**selection**{‘cyclic’, ‘random’}, default=’cyclic’

If set to ‘random’, a random coefficient is updated every iteration rather than looping over features sequentially by default. This (setting to ‘random’) often leads to significantly faster convergence especially when tol is higher than 1e-4.

Attributes:

**coef\_**ndarray of shape (n\_targets, n\_features)

Parameter vector (W in the cost function formula). Note that `coef_` stores the transpose of `W`, `W.T`.

**intercept\_**ndarray of shape (n\_targets,)

Independent term in decision function.

**n\_iter\_**int

Number of iterations run by the coordinate descent solver to reach the specified tolerance.

**dual\_gap\_**ndarray of shape (n\_alphas,)

The dual gaps at the end of the optimization for each alpha.

**eps\_**float

The tolerance scaled scaled by the variance of the target `y`.

`sparse_coef_`sparse matrix of shape (n\_features,) or (n\_targets, n\_features)

Sparse representation of the fitted `coef_`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

Linear Model trained with L1 prior as regularizer (aka the Lasso).

[`MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")

Multi-task L1 regularized linear model with built-in cross-validation.

[`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")

Multi-task L1/L2 ElasticNet with built-in cross-validation.

Notes

The algorithm used to fit the model is coordinate descent.

To avoid unnecessary memory duplication the X and y arguments of the fit method should be directly passed as Fortran-contiguous numpy arrays.

Examples

\>>> from sklearn import linear\_model
\>>> clf \= linear\_model.MultiTaskLasso(alpha\=0.1)
\>>> clf.fit(\[\[0, 1\], \[1, 2\], \[2, 4\]\], \[\[0, 0\], \[1, 1\], \[2, 3\]\])
MultiTaskLasso(alpha=0.1)
\>>> print(clf.coef\_)
\[\[0.         0.60809415\]\
\[0.         0.94592424\]\]
\>>> print(clf.intercept\_)
\[-0.41888636 -0.87382323\]

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L2717)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.fit "Link to this definition")

Fit MultiTaskElasticNet model with coordinate descent.

Parameters:

**X**{ndarray, sparse matrix, sparse array} of shape (n\_samples, n\_features)

Data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication.

Note that large sparse matrices and arrays requiring `int64` indices are not accepted.

**y**ndarray of shape (n\_samples, n\_targets)

Target. Will be cast to X’s dtype if necessary.

**sample\_weight**float or array-like of shape (n\_samples,), default=None

Sample weights. Internally, the `sample_weight` vector will be rescaled to sum to `n_samples`.

Added in version 1.9.

Returns:

**self**object

Fitted estimator.

Notes

Coordinate descent is an algorithm that considers each column of data at a time hence it will automatically convert the X input as a Fortran-contiguous numpy array if necessary.

To avoid memory re-allocation it is advised to allocate the initial data in memory directly using that format.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

static path(_X_, _y_, _\*_, _l1\_ratio\=0.5_, _eps\=0.001_, _n\_alphas\='deprecated'_, _alphas\='warn'_, _precompute\='auto'_, _Xy\=None_, _copy\_X\=True_, _coef\_init\=None_, _verbose\=False_, _return\_n\_iter\=False_, _positive\=False_, _check\_input\=True_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L449)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.path "Link to this definition")

Compute elastic net path with coordinate descent.

The elastic net optimization function varies for mono and multi-outputs.

For mono-output tasks it is:

1 / (2 \* n\_samples) \* ||y \- Xw||^2\_2
+ alpha \* l1\_ratio \* ||w||\_1
+ 0.5 \* alpha \* (1 \- l1\_ratio) \* ||w||^2\_2

Copy to clipboard

For multi-output tasks it is:

1 / (2 \* n\_samples) \* ||Y \- XW||\_Fro^2
+ alpha \* l1\_ratio \* ||W||\_21
+ 0.5 \* alpha \* (1 \- l1\_ratio) \* ||W||\_Fro^2

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of L2-norm of each row (task) (i=feature, j=task)

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication. If `y` is mono-output then `X` can be sparse.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**l1\_ratio**float, default=0.5

Number between 0 and 1 passed to elastic net (scaling between l1 and l2 penalties). `l1_ratio=1` corresponds to the Lasso.

**eps**float, default=1e-3

Length of the path. `eps=1e-3` means that `alpha_min / alpha_max = 1e-3`.

**n\_alphas**int, default=100

Number of alphas along the regularization path.

**alphas**array-like, default=None

List of alphas where to compute the models. If None alphas are set automatically.

**precompute**‘auto’, bool or array-like of shape (n\_features, n\_features), default=’auto’

Whether to use a precomputed Gram matrix to speed up calculations. If set to `'auto'` let us decide. The Gram matrix can also be passed as argument.

**Xy**array-like of shape (n\_features,) or (n\_features, n\_targets), default=None

Xy = np.dot(X.T, y) that can be precomputed. It is useful only when the Gram matrix is precomputed.

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

**coef\_init**array-like of shape (n\_features, ), default=None

The initial values of the coefficients.

**verbose**bool or int, default=False

Amount of verbosity.

**return\_n\_iter**bool, default=False

Whether to return the number of iterations or not.

**positive**bool, default=False

If set to True, forces coefficients to be positive. (Only allowed when `y.ndim == 1`).

**check\_input**bool, default=True

If set to False, the input validation checks are skipped (including the Gram matrix when provided). It is assumed that they are handled by the caller.

**\*\*params**kwargs

Keyword arguments passed to the coordinate descent solver.

Returns:

**alphas**ndarray of shape (n\_alphas,)

The alphas along the path where models are computed.

**coefs**ndarray of shape (n\_features, n\_alphas) or (n\_targets, n\_features, n\_alphas)

Coefficients along the path.

**dual\_gaps**ndarray of shape (n\_alphas,)

The dual gaps at the end of the optimization for each alpha.

**n\_iters**list of int

The number of iterations taken by the coordinate descent optimizer to reach the specified tolerance for each alpha. (Is returned when `return_n_iter` is set to True).

See also

[`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")

Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer.

[`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")

Multi-task L1/L2 ElasticNet with built-in cross-validation.

[`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")

Linear regression with combined L1 and L2 priors as regularizer.

[`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")

Elastic Net model with iterative fitting along a regularization path.

Notes

For an example, see [examples/linear\_model/plot\_lasso\_lasso\_lars\_elasticnet\_path.py](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#sphx-glr-auto-examples-linear-model-plot-lasso-lasso-lars-elasticnet-path-py)
.

The underlying coordinate descent solver uses gap safe screening rules to speedup fitting time, see [User Guide on coordinate descent](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent)
.

Examples

\>>> from sklearn.linear\_model import enet\_path
\>>> from sklearn.datasets import make\_regression
\>>> X, y, true\_coef \= make\_regression(
...    n\_samples\=100, n\_features\=5, n\_informative\=2, coef\=True, random\_state\=0
... )
\>>> true\_coef
array(\[ 0.        ,  0.        ,  0.        , 97.9, 45.7\])
\>>> alphas, estimated\_coef, \_ \= enet\_path(X, y, alphas\=3)
\>>> alphas.shape
(3,)
\>>> estimated\_coef
 array(\[\[ 0.,  0.787,  0.568\],\
        \[ 0.,  1.120,  0.620\],\
        \[-0., -2.129, -1.128\],\
        \[ 0., 23.046, 88.939\],\
        \[ 0., 10.637, 41.566\]\])

Copy to clipboard

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [MultiTaskLasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model._coordinate_descent.MultiTaskLasso")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [MultiTaskLasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model._coordinate_descent.MultiTaskLasso")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)