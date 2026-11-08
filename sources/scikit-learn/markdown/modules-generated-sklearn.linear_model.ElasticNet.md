[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.ElasticNet.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.ElasticNet.html)

Collapse Sidebar Expand Sidebar

ElasticNet[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#elasticnet "Link to this heading")

========================================================================================================================================

class sklearn.linear\_model.ElasticNet(_alpha\=1.0_, _\*_, _l1\_ratio\=0.5_, _fit\_intercept\=True_, _precompute\=False_, _max\_iter\=1000_, _copy\_X\=True_, _tol\=0.0001_, _warm\_start\=False_, _positive\=False_, _random\_state\=None_, _selection\='cyclic'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L884)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "Link to this definition")

Linear regression with combined L1 and L2 priors as regularizer.

Minimizes the objective function:

12nsamples⋅‖y−Xw‖22+α⋅l1\_ratio⋅‖w‖1+0.5⋅α⋅(1−l1\_ratio)⋅‖w‖22

If you are interested in controlling the L1 and L2 penalty separately, keep in mind that this is equivalent to:

a⋅‖w‖1+0.5⋅b⋅‖w‖22

where:

α\=a+b,l1\_ratio\=aa+b

The parameter l1\_ratio corresponds to alpha in the glmnet R package while alpha corresponds to the lambda parameter in glmnet. Specifically, l1\_ratio = 1 is the lasso penalty. Currently, l1\_ratio <= 0.01 is not reliable, unless you supply your own sequence of alpha.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
.

Parameters:

**alpha**float, default=1.0

Constant that multiplies the penalty terms. Defaults to 1.0. See the notes for the exact mathematical meaning of this parameter. `alpha = 0` is equivalent to an ordinary least square, solved by the [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 object. For numerical reasons, using `alpha = 0` with the `Lasso` object is not advised. Given this, you should use the [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 object.

**l1\_ratio**float, default=0.5

The ElasticNet mixing parameter, with `0 <= l1_ratio <= 1`. For `l1_ratio = 0` the penalty is an L2 penalty. `For l1_ratio = 1` it is an L1 penalty. For `0 < l1_ratio < 1`, the penalty is a combination of L1 and L2.

**fit\_intercept**bool, default=True

Whether the intercept should be estimated or not. If `False`, the data is assumed to be already centered.

**precompute**bool or array-like of shape (n\_features, n\_features), default=False

Whether to use a precomputed Gram matrix to speed up calculations. The Gram matrix can also be passed as argument. For sparse input this option is always `False` to preserve sparsity. Check [an example on how to use a precomputed Gram Matrix in ElasticNet](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html#sphx-glr-auto-examples-linear-model-plot-elastic-net-precomputed-gram-matrix-with-weighted-samples-py)
 for details.

**max\_iter**int, default=1000

The maximum number of iterations.

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

**tol**float, default=1e-4

The tolerance for the optimization: if the updates are smaller or equal to `tol`, the optimization code checks the dual gap for optimality and continues until it is smaller or equal to `tol`, see Notes below.

**warm\_start**bool, default=False

When set to `True`, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**positive**bool, default=False

When set to `True`, forces the coefficients to be positive.

**random\_state**int, RandomState instance, default=None

The seed of the pseudo random number generator that selects a random feature to update. Used when `selection` == ‘random’. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**selection**{‘cyclic’, ‘random’}, default=’cyclic’

If set to ‘random’, a random coefficient is updated every iteration rather than looping over features sequentially by default. This (setting to ‘random’) often leads to significantly faster convergence especially when tol is higher than 1e-4.

Attributes:

**coef\_**ndarray of shape (n\_features,) or (n\_targets, n\_features)

Parameter vector (w in the cost function formula).

`sparse_coef_`sparse matrix of shape (n\_features,) or (n\_targets, n\_features)

Sparse representation of the fitted `coef_`.

**intercept\_**float or ndarray of shape (n\_targets,)

Independent term in decision function.

**n\_iter\_**list of int

Number of iterations run by the coordinate descent solver to reach the specified tolerance.

**dual\_gap\_**float or ndarray of shape (n\_targets,)

Given param alpha, the dual gaps at the end of the optimization, same shape as each observation of y.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")

Elastic net model with best model selection by cross-validation.

[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")

Implements elastic net regression with incremental training.

[`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

Implements logistic regression with elastic net penalty (`SGDClassifier(loss="log_loss", penalty="elasticnet")`).

Notes

To avoid unnecessary memory duplication the X argument of the fit method should be directly passed as a Fortran-contiguous numpy array.

The precise stopping criteria based on `tol` are the following: First, check that that maximum coordinate update, i.e. maxj|wjnew−wjold| is smaller or equal to `tol` times the maximum absolute coefficient, maxj|wj|. If so, then additionally check whether the dual gap is smaller or equal to `tol` times ||y||22/nsamples.

The underlying coordinate descent solver uses gap safe screening rules to speedup fitting time, see [User Guide on coordinate descent](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent)
.

Examples

\>>> from sklearn.linear\_model import ElasticNet
\>>> from sklearn.datasets import make\_regression

Copy to clipboard

\>>> X, y \= make\_regression(n\_features\=2, random\_state\=0)
\>>> regr \= ElasticNet(random\_state\=0)
\>>> regr.fit(X, y)
ElasticNet(random\_state=0)
\>>> print(regr.coef\_)
\[18.83816048 64.55968825\]
\>>> print(regr.intercept\_)
1.451
\>>> print(regr.predict(\[\[0, 0\]\]))
\[1.451\]

Copy to clipboard

*   [L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-auto-examples-linear-model-plot-lasso-and-elasticnet-py)
     showcases ElasticNet alongside Lasso and ARD Regression for sparse signal recovery in the presence of noise and feature correlation.
    

fit(_X_, _y_, _sample\_weight\=None_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L1096)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.fit "Link to this definition")

Fit model with coordinate descent.

Parameters:

**X**{ndarray, sparse matrix, sparse array} of shape (n\_samples, n\_features)

Data.

Note that large sparse matrices and arrays requiring `int64` indices are not accepted.

**y**ndarray of shape (n\_samples,) or (n\_samples, n\_targets)

Target. Will be cast to X’s dtype if necessary.

**sample\_weight**float or array-like of shape (n\_samples,), default=None

Sample weights. Internally, the `sample_weight` vector will be rescaled to sum to `n_samples`.

Added in version 0.23.

**check\_input**bool, default=True

Allow to bypass several input checking. Don’t use this parameter unless you know what you do.

Returns:

**self**object

Fitted estimator.

Notes

Coordinate descent is an algorithm that considers each column of data at a time hence it will automatically convert the X input as a Fortran-contiguous numpy array if necessary.

To avoid memory re-allocation it is advised to allocate the initial data in memory directly using that format.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

static path(_X_, _y_, _\*_, _l1\_ratio\=0.5_, _eps\=0.001_, _n\_alphas\='deprecated'_, _alphas\='warn'_, _precompute\='auto'_, _Xy\=None_, _copy\_X\=True_, _coef\_init\=None_, _verbose\=False_, _return\_n\_iter\=False_, _positive\=False_, _check\_input\=True_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L449)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.path "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model._coordinate_descent.ElasticNet")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model._coordinate_descent.ElasticNet")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_elastic_net_precomputed_gram_matrix_with_weighted_samples_thumb.png)

[Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)

Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)