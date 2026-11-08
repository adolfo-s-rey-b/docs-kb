[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.GraphicalLassoCV.html)

Collapse Sidebar Expand Sidebar

GraphicalLassoCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#graphicallassocv "Link to this heading")

========================================================================================================================================================

class sklearn.covariance.GraphicalLassoCV(_\*_, _alphas\=4_, _n\_refinements\=4_, _cv\=None_, _tol\=0.0001_, _enet\_tol\=0.0001_, _max\_iter\=100_, _mode\='cd'_, _n\_jobs\=None_, _verbose\=False_, _eps\=np.float64(2.220446049250313e-16)_, _assume\_centered\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_graph_lasso.py#L720)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "Link to this definition")

Sparse inverse covariance w/ cross-validated choice of the l1 penalty.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#sparse-inverse-covariance)
.

Changed in version v0.20: GraphLassoCV has been renamed to GraphicalLassoCV

Parameters:

**alphas**int or array-like of shape (n\_alphas,), dtype=float, default=4

If an integer is given, it fixes the number of points on the grids of alpha to be used. If a list is given, it gives the grid to be used. See the notes in the class docstring for more details. Range is \[1, inf) for an integer. Range is (0, inf\] for an array-like of floats.

**n\_refinements**int, default=4

The number of times the grid is refined. Not used if explicit values of alphas are passed. Range is \[1, inf).\
\
**cv**int, cross-validation generator or iterable, default=None\
\
Determines the cross-validation splitting strategy. Possible inputs for cv are:\
\
*   None, to use the default 5-fold cross-validation,\
    \
*   integer, to specify the number of folds,\
    \
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)\
    ,\
    \
*   an iterable yielding (train, test) splits as arrays of indices.\
    \
\
For integer/None inputs [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")\
 is used.\
\
Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)\
 for the various cross-validation strategies that can be used here.\
\
Changed in version 0.20: `cv` default value if None changed from 3-fold to 5-fold.\
\
**tol**float, default=1e-4\
\
The tolerance to declare convergence: if the dual gap goes below this value, iterations are stopped. Range is (0, inf\].

**enet\_tol**float, default=1e-4

The tolerance for the elastic net solver used to calculate the descent direction. This parameter controls the accuracy of the search direction for a given column update, not of the overall parameter estimate. Only used for mode=’cd’. Range is (0, inf\].

**max\_iter**int, default=100

Maximum number of iterations.

**mode**{‘cd’, ‘lars’}, default=’cd’

The Lasso solver to use: coordinate descent or LARS. Use LARS for very sparse underlying graphs, where number of features is greater than number of samples. Elsewhere prefer cd which is more numerically stable.

**n\_jobs**int, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Changed in version v0.20: `n_jobs` default changed from 1 to None

**verbose**bool, default=False

If verbose is True, the objective function and duality gap are printed at each iteration.

**eps**float, default=eps

The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Default is `np.finfo(np.float64).eps`.

Added in version 1.3.

**assume\_centered**bool, default=False

If True, data are not centered before computation. Useful when working with data whose mean is almost, but not exactly zero. If False, data are centered before computation.

Attributes:

**location\_**ndarray of shape (n\_features,)

Estimated location, i.e. the estimated mean.

**covariance\_**ndarray of shape (n\_features, n\_features)

Estimated covariance matrix.

**precision\_**ndarray of shape (n\_features, n\_features)

Estimated precision matrix (inverse covariance).

**costs\_**list of (objective, dual\_gap) pairs

The list of values of the objective function and the dual gap at each iteration. Returned only if return\_costs is True.

Added in version 1.3.

**alpha\_**float

Penalization parameter selected.

**cv\_results\_**dict of ndarrays

A dict with keys:

alphasndarray of shape (n\_alphas,)

All penalization parameters explored.

split(k)\_test\_scorendarray of shape (n\_alphas,)

Log-likelihood score on left-out data across (k)th fold.

Added in version 1.0.

mean\_test\_scorendarray of shape (n\_alphas,)

Mean of scores over the folds.

Added in version 1.0.

std\_test\_scorendarray of shape (n\_alphas,)

Standard deviation of scores over the folds.

Added in version 1.0.

**n\_iter\_**int

Number of iterations run for the optimal alpha.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")

L1-penalized covariance estimator.

[`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")

Sparse inverse covariance estimation with an l1-penalized estimator.

Notes

The search for the optimal penalization parameter (`alpha`) is done on an iteratively refined grid: first the cross-validated scores on a grid are computed, then a new refined grid is centered around the maximum, and so on.

One of the challenges which is faced here is that the solvers can fail to converge to a well-conditioned estimate. The corresponding values of `alpha` then come out as missing values, but the optimum may be close to these missing values.

In `fit`, once the best parameter `alpha` is found through cross-validation, the model is fit again using the entire training set.

Examples

\>>> import numpy as np
\>>> from sklearn.covariance import GraphicalLassoCV
\>>> true\_cov \= np.array(\[\[0.8, 0.0, 0.2, 0.0\],\
...                      \[0.0, 0.4, 0.0, 0.0\],\
...                      \[0.2, 0.0, 0.3, 0.1\],\
...                      \[0.0, 0.0, 0.1, 0.7\]\])
\>>> np.random.seed(0)
\>>> X \= np.random.multivariate\_normal(mean\=\[0, 0, 0, 0\],
...                                   cov\=true\_cov,
...                                   size\=200)
\>>> cov \= GraphicalLassoCV().fit(X)
\>>> np.around(cov.covariance\_, decimals\=3)
array(\[\[0.816, 0.051, 0.22 , 0.017\],\
       \[0.051, 0.364, 0.018, 0.036\],\
       \[0.22 , 0.018, 0.322, 0.094\],\
       \[0.017, 0.036, 0.094, 0.69 \]\])
\>>> np.around(cov.location\_, decimals\=3)
array(\[0.073, 0.04 , 0.038, 0.143\])

Copy to clipboard

For an example comparing [`sklearn.covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
, [`sklearn.covariance.ledoit_wolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf")
 shrinkage and the empirical covariance on high-dimensional gaussian data, see [Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#sphx-glr-auto-examples-covariance-plot-sparse-cov-py)
.

error\_norm(_comp\_cov_, _norm\='frobenius'_, _scaling\=True_, _squared\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L290)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.error_norm "Link to this definition")

Compute the Mean Squared Error between two covariance estimators.

Parameters:

**comp\_cov**array-like of shape (n\_features, n\_features)

The covariance to compare with.

**norm**{“frobenius”, “spectral”}, default=”frobenius”

The type of norm used to compute the error. Available error types: - ‘frobenius’ (default): sqrt(tr(A^t.A)) - ‘spectral’: sqrt(max(eigenvalues(A^t.A)) where A is the error `(comp_cov - self.covariance_)`.

**scaling**bool, default=True

If True (default), the squared error norm is divided by n\_features. If False, the squared error norm is not rescaled.

**squared**bool, default=True

Whether to compute the squared error norm or the error norm. If True (default), the squared error norm is returned. If False, the error norm is returned.

Returns:

**result**float

The Mean Squared Error (in the sense of the Frobenius norm) between `self` and `comp_cov` covariance estimators.

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_graph_lasso.py#L945)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.fit "Link to this definition")

Fit the GraphicalLasso covariance model to X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data from which to compute the covariance estimate.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*params**dict, default=None

Parameters to be passed to the CV splitter and the cross\_val\_score function.

Added in version 1.5: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_graph_lasso.py#L1132)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L217)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.get_precision "Link to this definition")

Getter for the precision matrix.

Returns:

**precision\_**array-like of shape (n\_features, n\_features)

The precision matrix associated to the current covariance object.

mahalanobis(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.mahalanobis "Link to this definition")

Compute the squared Mahalanobis distances of given observations.

For a detailed example of how outliers affects the Mahalanobis distance, see [Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#sphx-glr-auto-examples-covariance-plot-mahalanobis-distances-py)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The observations, the Mahalanobis distances of the which we compute. Observations are assumed to be drawn from the same distribution than the data used in fit.

Returns:

**dist**ndarray of shape (n\_samples,)

Squared Mahalanobis distances of the observations.

score(_X\_test_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L259)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.score "Link to this definition")

Compute the log-likelihood of `X_test` under the estimated Gaussian model.

The Gaussian model is defined by its mean and covariance matrix which are represented respectively by `self.location_` and `self.covariance_`.

Parameters:

**X\_test**array-like of shape (n\_samples, n\_features)

Test data of which we compute the likelihood, where `n_samples` is the number of samples and `n_features` is the number of features. `X_test` is assumed to be drawn from the same distribution than the data used in fit (including centering).

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**res**float

The log-likelihood of `X_test` with `self.location_` and `self.covariance_` as estimators of the Gaussian model mean and covariance matrix respectively.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)