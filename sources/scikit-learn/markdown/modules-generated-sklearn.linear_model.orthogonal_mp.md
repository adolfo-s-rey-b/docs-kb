[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.orthogonal_mp.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.orthogonal_mp.html)

Collapse Sidebar Expand Sidebar

orthogonal\_mp[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#orthogonal-mp "Link to this heading")

==================================================================================================================================================

sklearn.linear\_model.orthogonal\_mp(_X_, _y_, _\*_, _n\_nonzero\_coefs\=None_, _tol\=None_, _precompute\=False_, _copy\_X\=True_, _return\_path\=False_, _return\_n\_iter\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_omp.py#L291)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#sklearn.linear_model.orthogonal_mp "Link to this definition")

Orthogonal Matching Pursuit (OMP).

Solves `n_targets` Orthogonal Matching Pursuit problems. Each instance of the problem fits a linear model with constraints imposed on the number of non-zero coefficients (i.e. the ell0 pseudo-norm) using `n_nonzero_coefs`:

argminw||y−Xw||22 subject to ||w||0≤nnonzero\_coefs

When parametrized by error using the parameter `tol`:

argminw||w||0 subject to ||y−Xw||22≤tol

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#omp)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data. Columns are assumed to have unit norm.

**y**ndarray of shape (n\_samples,) or (n\_samples, n\_targets)

Input targets.

**n\_nonzero\_coefs**int, default=None

Maximum number of non-zero entries in the solution. If None (by default) this value is set to 10% of n\_features.

**tol**float, default=None

Maximum squared norm of the residual. If not None, overrides n\_nonzero\_coefs.

**precompute**‘auto’ or bool, default=False

Whether to perform precomputations. Improves performance when n\_targets or n\_samples is very large.

**copy\_X**bool, default=True

Whether the design matrix X must be copied by the algorithm. A false value is only helpful if X is already Fortran-ordered, otherwise a copy is made anyway.

**return\_path**bool, default=False

Whether to return every value of the nonzero coefficients along the forward path. Useful for cross-validation.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

Returns:

**coef**ndarray of shape (n\_features,) or (n\_features, n\_targets)

Coefficients of the OMP solution. If `return_path=True`, this contains the whole coefficient path. In this case its shape is (n\_features, n\_features) or (n\_features, n\_targets, n\_features) and iterating over the last axis generates coefficients in increasing order of active features.

**n\_iters**array-like or int

Number of active features across every target. Returned only if `return_n_iter` is set to True.

See also

[`OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")

Orthogonal Matching Pursuit model.

[`orthogonal_mp_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#sklearn.linear_model.orthogonal_mp_gram "sklearn.linear_model.orthogonal_mp_gram")

Solve OMP problems using Gram matrix and the product X.T \* y.

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Sparse coding.

Notes

Orthogonal matching pursuit was introduced in S. Mallat, Z. Zhang, Matching pursuits with time-frequency dictionaries, IEEE Transactions on Signal Processing, Vol. 41, No. 12. (December 1993), pp. 3397-3415. ([https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf](https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf)
)

This implementation is based on Rubinstein, R., Zibulevsky, M. and Elad, M., Efficient Implementation of the K-SVD Algorithm using Batch Orthogonal Matching Pursuit Technical Report - CS Technion, April 2008. [https://www.cs.technion.ac.il/~ronrubin/Publications/KSVD-OMP-v2.pdf](https://www.cs.technion.ac.il/~ronrubin/Publications/KSVD-OMP-v2.pdf)

Examples

\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.linear\_model import orthogonal\_mp
\>>> X, y \= make\_regression(noise\=4, random\_state\=0)
\>>> coef \= orthogonal\_mp(X, y)
\>>> coef.shape
(100,)
\>>> X\[:1,\] @ coef
array(\[-78.68\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)