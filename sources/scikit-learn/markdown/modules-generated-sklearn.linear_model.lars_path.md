[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.lars_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.lars_path.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.lars_path.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.lars_path.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.lars_path.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.lars_path.html)

Collapse Sidebar Expand Sidebar

lars\_path[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#lars-path "Link to this heading")

======================================================================================================================================

sklearn.linear\_model.lars\_path(_X_, _y_, _Xy\=None_, _\*_, _Gram\=None_, _max\_iter\=500_, _alpha\_min\=0_, _method\='lar'_, _copy\_X\=True_, _eps\=np.float64(2.220446049250313e-16)_, _copy\_Gram\=True_, _verbose\=0_, _return\_path\=True_, _return\_n\_iter\=False_, _positive\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_least_angle.py#L47)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "Link to this definition")

Compute Least Angle Regression or Lasso path using the LARS algorithm.

The optimization objective for the case method=’lasso’ is:

(1 / (2 \* n\_samples)) \* ||y \- Xw||^2\_2 + alpha \* ||w||\_1

Copy to clipboard

in the case of method=’lar’, the objective function is only known in the form of an implicit equation (see discussion in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#r2391cff0bbde-1)
).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression)
.

Parameters:

**X**None or ndarray of shape (n\_samples, n\_features)

Input data. If X is `None`, Gram must also be `None`. If only the Gram matrix is available, use `lars_path_gram` instead.

**y**None or ndarray of shape (n\_samples,)

Input targets.

**Xy**array-like of shape (n\_features,), default=None

`Xy = X.T @ y` that can be precomputed. It is useful only when the Gram matrix is precomputed.

**Gram**None, ‘auto’, bool, ndarray of shape (n\_features, n\_features), default=None

Precomputed Gram matrix `X.T @ X`, if `'auto'`, the Gram matrix is precomputed from the given X, if there are more samples than features.

**max\_iter**int, default=500

Maximum number of iterations to perform, set to infinity for no limit.

**alpha\_min**float, default=0

Minimum correlation along the path. It corresponds to the regularization parameter `alpha` in the Lasso.

**method**{‘lar’, ‘lasso’}, default=’lar’

Specifies the returned model. Select `'lar'` for Least Angle Regression, `'lasso'` for the Lasso.

**copy\_X**bool, default=True

If `False`, `X` is overwritten.

**eps**float, default=np.finfo(float).eps

The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Unlike the `tol` parameter in some iterative optimization-based algorithms, this parameter does not control the tolerance of the optimization.

**copy\_Gram**bool, default=True

If `False`, `Gram` is overwritten.

**verbose**int, default=0

Controls output verbosity.

**return\_path**bool, default=True

If `True`, returns the entire path, else returns only the last point of the path.

**return\_n\_iter**bool, default=False

Whether to return the number of iterations.

**positive**bool, default=False

Restrict coefficients to be >= 0. This option is only allowed with method ‘lasso’. Note that the model coefficients will not converge to the ordinary-least-squares solution for small values of alpha. Only coefficients up to the smallest alpha value (`alphas_[alphas_ > 0.].min()` when fit\_path=True) reached by the stepwise Lars-Lasso algorithm are typically in congruence with the solution of the coordinate descent `lasso_path` function.

Returns:

**alphas**ndarray of shape (n\_alphas + 1,)

Maximum of covariances (in absolute value) at each iteration. `n_alphas` is either `max_iter`, `n_features`, or the number of nodes in the path with `alpha >= alpha_min`, whichever is smaller.

**active**ndarray of shape (n\_alphas,)

Indices of active variables at the end of the path.

**coefs**ndarray of shape (n\_features, n\_alphas + 1)

Coefficients along the path.

**n\_iter**int

Number of iterations run. Returned only if `return_n_iter` is set to True.

See also

[`lars_path_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html#sklearn.linear_model.lars_path_gram "sklearn.linear_model.lars_path_gram")

Compute LARS path in the sufficient stats mode.

[`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")

Compute Lasso path with coordinate descent.

[`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")

Lasso model fit with Least Angle Regression a.k.a. Lars.

[`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")

Least Angle Regression model a.k.a. LAR.

[`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")

Cross-validated Lasso, using the LARS algorithm.

[`LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")

Cross-validated Least Angle Regression model.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Sparse coding.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#id1)\
\]

“Least Angle Regression”, Efron et al. [http://statweb.stanford.edu/~tibs/ftp/lars.pdf](http://statweb.stanford.edu/~tibs/ftp/lars.pdf)

\[2\]

[Wikipedia entry on the Least-angle regression](https://en.wikipedia.org/wiki/Least-angle_regression)

\[3\]

[Wikipedia entry on the Lasso](https://en.wikipedia.org/wiki/Lasso_(statistics))

Examples

\>>> from sklearn.linear\_model import lars\_path
\>>> from sklearn.datasets import make\_regression
\>>> X, y, true\_coef \= make\_regression(
...    n\_samples\=100, n\_features\=5, n\_informative\=2, coef\=True, random\_state\=0
... )
\>>> true\_coef
array(\[ 0.        ,  0.        ,  0.        , 97.9, 45.7\])
\>>> alphas, \_, estimated\_coef \= lars\_path(X, y)
\>>> alphas.shape
(3,)
\>>> estimated\_coef
array(\[\[ 0.     ,  0.     ,  0.     \],\
       \[ 0.     ,  0.     ,  0.     \],\
       \[ 0.     ,  0.     ,  0.     \],\
       \[ 0.     , 46.96, 97.99\],\
       \[ 0.     ,  0.     , 45.70\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)