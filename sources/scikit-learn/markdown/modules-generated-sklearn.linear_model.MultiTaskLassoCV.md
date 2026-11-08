[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html)

Collapse Sidebar Expand Sidebar

MultiTaskLassoCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#multitasklassocv "Link to this heading")

==========================================================================================================================================================

class sklearn.linear\_model.MultiTaskLassoCV(_\*_, _eps\=0.001_, _alphas\=100_, _fit\_intercept\=True_, _max\_iter\=1000_, _tol\=0.0001_, _copy\_X\=True_, _cv\=None_, _verbose\=False_, _n\_jobs\=None_, _random\_state\=None_, _selection\='cyclic'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L3230)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "Link to this definition")

Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

The optimization objective for MultiTaskLasso is:

(1 / (2 \* n\_samples)) \* ||Y \- XW||^Fro\_2 + alpha \* ||W||\_21

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of norm of each row.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso)
.

Added in version 0.15.

Parameters:

**eps**float, default=1e-3

Length of the path. `eps=1e-3` means that `alpha_min / alpha_max = 1e-3`.

**alphas**array-like or int, default=None

Values of alphas to test along the regularization path. If int, `alphas` values are generated automatically. If array-like, list of alpha values to use.

Changed in version 1.7: `alphas` accepts an integer value which removes the need to pass `n_alphas`.

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (i.e. data is expected to be centered).

**max\_iter**int, default=1000

The maximum number of iterations.

**tol**float, default=1e-4

The tolerance for the optimization: if the updates are smaller or equal to `tol`, the optimization code checks the dual gap for optimality and continues until it is smaller or equal to `tol`.

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

**cv**int, cross-validation generator or iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross-validation,
    
*   int, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For int/None inputs, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**verbose**bool or int, default=False

Amount of verbosity.

**n\_jobs**int, default=None

Number of CPUs to use during the cross validation. Note that this is used only if multiple values for l1\_ratio are given. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance, default=None

The seed of the pseudo random number generator that selects a random feature to update. Used when `selection` == ‘random’. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**selection**{‘cyclic’, ‘random’}, default=’cyclic’

If set to ‘random’, a random coefficient is updated every iteration rather than looping over features sequentially by default. This (setting to ‘random’) often leads to significantly faster convergence especially when tol is higher than 1e-4.

Attributes:

**intercept\_**ndarray of shape (n\_targets,)

Independent term in decision function.

**coef\_**ndarray of shape (n\_targets, n\_features)

Parameter vector (W in the cost function formula). Note that `coef_` stores the transpose of `W`, `W.T`.

**alpha\_**float

The amount of penalization chosen by cross validation.

**mse\_path\_**ndarray of shape (n\_alphas, n\_folds)

Mean square error for the test set on each fold, varying alpha.

**alphas\_**ndarray of shape (n\_alphas,)

The grid of alphas used for fitting.

**n\_iter\_**int

Number of iterations run by the coordinate descent solver to reach the specified tolerance for the optimal alpha.

**dual\_gap\_**float

The dual gap at the end of the optimization for the optimal alpha.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")

Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer.

[`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")

Elastic net model with best model selection by cross-validation.

[`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")

Multi-task L1/L2 ElasticNet with built-in cross-validation.

Notes

The algorithm used to fit the model is coordinate descent.

In `fit`, once the best parameter `alpha` is found through cross-validation, the model is fit again using the entire training set.

To avoid unnecessary memory duplication the `X` and `y` arguments of the `fit` method should be directly passed as Fortran-contiguous numpy arrays.

Examples

\>>> from sklearn.linear\_model import MultiTaskLassoCV
\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.metrics import r2\_score
\>>> X, y \= make\_regression(n\_targets\=2, noise\=4, random\_state\=0)
\>>> reg \= MultiTaskLassoCV(cv\=5, random\_state\=0).fit(X, y)
\>>> r2\_score(y, reg.predict(X))
0.9994
\>>> reg.alpha\_
np.float64(0.4321...)
\>>> reg.predict(X\[:1,\])
array(\[\[153.7971,  94.9015\]\])

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L1731)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.fit "Link to this definition")

Fit model with internal cross-validation and with coordinate descent.

Fit is on grid of alphas and best alpha estimated by cross-validation.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication. If y is mono-output, X can be sparse. Note that large sparse matrices and arrays requiring `int64` indices are not accepted.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**sample\_weight**float or array-like of shape (n\_samples,), default=None

Sample weights used for fitting and evaluation of the weighted mean squared error of each cv-fold. Note that the cross validated MSE that is finally used to find the best model is the unweighted mean over the (weighted) MSEs of each test fold.

**\*\*params**dict, default=None

Parameters to be passed to the CV splitter.

Added in version 1.4: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Returns an instance of fitted model.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L1997)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

static path(_X_, _y_, _\*_, _eps\=0.001_, _n\_alphas\='deprecated'_, _alphas\='warn'_, _precompute\='auto'_, _Xy\=None_, _copy\_X\=True_, _coef\_init\=None_, _verbose\=False_, _return\_n\_iter\=False_, _positive\=False_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L213)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.path "Link to this definition")

Compute Lasso path with coordinate descent.

The Lasso optimization function varies for mono and multi-outputs.

For mono-output tasks it is:

(1 / (2 \* n\_samples)) \* ||y \- Xw||^2\_2 + alpha \* ||w||\_1

Copy to clipboard

For multi-output tasks it is:

(1 / (2 \* n\_samples)) \* ||Y \- XW||^2\_Fro + alpha \* ||W||\_21

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of norm of each row.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#lasso)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication. If `y` is mono-output then `X` can be sparse.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**eps**float, default=1e-3

Length of the path. `eps=1e-3` means that `alpha_min / alpha_max = 1e-3`.

**n\_alphas**int, default=100

Number of alphas along the regularization path.

**alphas**array-like, default=None

List of alphas where to compute the models. If `None` alphas are set automatically.

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

The number of iterations taken by the coordinate descent optimizer to reach the specified tolerance for each alpha.

See also

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

The Lasso is a linear model that estimates sparse coefficients.

[`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")

Lasso model fit with Least Angle Regression a.k.a. Lars.

[`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

Lasso linear model with iterative fitting along a regularization path.

[`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")

Cross-validated Lasso using the LARS algorithm.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Estimator that can be used to transform signals into sparse linear combination of atoms from a fixed.

Notes

For an example, see [examples/linear\_model/plot\_lasso\_lasso\_lars\_elasticnet\_path.py](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#sphx-glr-auto-examples-linear-model-plot-lasso-lasso-lars-elasticnet-path-py)
.

To avoid unnecessary memory duplication the X argument of the fit method should be directly passed as a Fortran-contiguous numpy array.

Note that in certain cases, the Lars solver may be significantly faster to implement this functionality. In particular, linear interpolation can be used to retrieve model coefficients between the values output by lars\_path.

The underlying coordinate descent solver uses gap safe screening rules to speedup fitting time, see [User Guide on coordinate descent](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent)
.

Examples

Comparing lasso\_path and lars\_path with interpolation:

\>>> import numpy as np
\>>> from sklearn.linear\_model import lasso\_path
\>>> X \= np.array(\[\[1, 2, 3.1\], \[2.3, 5.4, 4.3\]\]).T
\>>> y \= np.array(\[1, 2, 3.1\])
\>>> \# Use lasso\_path to compute a coefficient path
\>>> \_, coef\_path, \_ \= lasso\_path(X, y, alphas\=\[5., 1., .5\])
\>>> print(coef\_path)
\[\[0.         0.         0.46874778\]\
 \[0.2159048  0.4425765  0.23689075\]\]

Copy to clipboard

\>>> \# Now use lars\_path and 1D linear interpolation to compute the
\>>> \# same path
\>>> from sklearn.linear\_model import lars\_path
\>>> alphas, active, coef\_path\_lars \= lars\_path(X, y, method\='lasso')
\>>> from scipy import interpolate
\>>> coef\_path\_continuous \= interpolate.interp1d(alphas\[::\-1\],
...                                             coef\_path\_lars\[:, ::\-1\])
\>>> print(coef\_path\_continuous(\[5., 1., .5\]))
\[\[0.         0.         0.46915237\]\
 \[0.2159048  0.4425765  0.23668876\]\]

Copy to clipboard

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [MultiTaskLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model._coordinate_descent.MultiTaskLassoCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [MultiTaskLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model._coordinate_descent.MultiTaskLassoCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV.set_score_request "Link to this definition")

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