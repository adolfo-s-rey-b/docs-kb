[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.graphical_lasso.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.graphical_lasso.html)

Collapse Sidebar Expand Sidebar

graphical\_lasso[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#graphical-lasso "Link to this heading")

======================================================================================================================================================

sklearn.covariance.graphical\_lasso(_emp\_cov_, _alpha_, _\*_, _mode\='cd'_, _tol\=0.0001_, _enet\_tol\=0.0001_, _max\_iter\=100_, _verbose\=False_, _return\_costs\=False_, _eps\=np.float64(2.220446049250313e-16)_, _return\_n\_iter\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_graph_lasso.py#L228)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "Link to this definition")

L1-penalized covariance estimator.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#sparse-inverse-covariance)
.

Changed in version v0.20: graph\_lasso has been renamed to graphical\_lasso

Parameters:

**emp\_cov**array-like of shape (n\_features, n\_features)

Empirical covariance from which to compute the covariance estimate.

**alpha**float

The regularization parameter: the higher alpha, the more regularization, the sparser the inverse covariance. Range is (0, inf\].

**mode**{‘cd’, ‘lars’}, default=’cd’

The Lasso solver to use: coordinate descent or LARS. Use LARS for very sparse underlying graphs, where p > n. Elsewhere prefer cd which is more numerically stable.

**tol**float, default=1e-4

The tolerance to declare convergence: if the dual gap goes below this value, iterations are stopped. Range is (0, inf\].

**enet\_tol**float, default=1e-4

The tolerance for the elastic net solver used to calculate the descent direction. This parameter controls the accuracy of the search direction for a given column update, not of the overall parameter estimate. Only used for mode=’cd’. Range is (0, inf\].

**max\_iter**int, default=100

The maximum number of iterations.

**verbose**bool, default=False

If verbose is True, the objective function and dual gap are printed at each iteration.

**return\_costs**bool, default=False

If return\_costs is True, the objective function and dual gap at each iteration are returned.

**eps**float, default=eps

The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Default is `np.finfo(np.float64).eps`.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

Returns:

**covariance**ndarray of shape (n\_features, n\_features)

The estimated covariance matrix.

**precision**ndarray of shape (n\_features, n\_features)

The estimated (sparse) precision matrix.

**costs**list of (objective, dual\_gap) pairs

The list of values of the objective function and the dual gap at each iteration. Returned only if return\_costs is True.

**n\_iter**int

Number of iterations. Returned only if `return_n_iter` is set to True.

See also

[`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")

Sparse inverse covariance estimation with an l1-penalized estimator.

[`GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")

Sparse inverse covariance with cross-validated choice of the l1 penalty.

Notes

The algorithm employed to solve this problem is the GLasso algorithm, from the Friedman 2008 Biostatistics paper. It is the same algorithm as in the R `glasso` package.

One possible difference with the `glasso` R package is that the diagonal coefficients are not penalized.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_sparse\_spd\_matrix
\>>> from sklearn.covariance import empirical\_covariance, graphical\_lasso
\>>> true\_cov \= make\_sparse\_spd\_matrix(n\_dim\=3,random\_state\=42)
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.multivariate\_normal(mean\=np.zeros(3), cov\=true\_cov, size\=3)
\>>> emp\_cov \= empirical\_covariance(X, assume\_centered\=True)
\>>> emp\_cov, \_ \= graphical\_lasso(emp\_cov, alpha\=0.05)
\>>> emp\_cov
array(\[\[ 1.687,  0.212, -0.209\],\
       \[ 0.212,  0.221, -0.0817\],\
       \[-0.209, -0.0817, 0.232\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)