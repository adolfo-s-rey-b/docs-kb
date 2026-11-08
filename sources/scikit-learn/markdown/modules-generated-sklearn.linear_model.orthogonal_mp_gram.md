[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html)

Collapse Sidebar Expand Sidebar

orthogonal\_mp\_gram[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#orthogonal-mp-gram "Link to this heading")

==================================================================================================================================================================

sklearn.linear\_model.orthogonal\_mp\_gram(_Gram_, _Xy_, _\*_, _n\_nonzero\_coefs\=None_, _tol\=None_, _norms\_squared\=None_, _copy\_Gram\=True_, _copy\_Xy\=True_, _return\_path\=False_, _return\_n\_iter\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_omp.py#L473)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#sklearn.linear_model.orthogonal_mp_gram "Link to this definition")

Gram Orthogonal Matching Pursuit (OMP).

Solves `n_targets` Orthogonal Matching Pursuit problems using only the precomputed Gram matrix `X.T * X` and the product `X.T * y`. This implementation efficiently computes the solution using the Cholesky decomposition.

Each instance of the problem fits a linear model with constraints imposed on the number of non-zero coefficients (i.e. the ℓ0 pseudo-norm) using `n_nonzero_coefs` or on the error using the parameter `tol`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#omp)
.

Parameters:

**Gram**array-like of shape (n\_features, n\_features)

Gram matrix of the input data: `X.T * X`.

**Xy**array-like of shape (n\_features,) or (n\_features, n\_targets)

Input targets multiplied by `X`: `X.T * y`.

**n\_nonzero\_coefs**int, default=None

Maximum number of non-zero entries in the solution. If `None` (by default) this value is set to 10% of n\_features.

**tol**float, default=None

Maximum squared norm of the residual. If not `None`, overrides `n_nonzero_coefs`.

**norms\_squared**array-like of shape (n\_targets,), default=None

Squared L2 norms of the lines of `y`. Required if `tol` is not None.

**copy\_Gram**bool, default=True

Whether the gram matrix must be copied by the algorithm. A `False` value is only helpful if it is already Fortran-ordered, otherwise a copy is made anyway.

**copy\_Xy**bool, default=True

Whether the covariance vector `Xy` must be copied by the algorithm. If `False`, it may be overwritten.

**return\_path**bool, default=False

Whether to return every value of the nonzero coefficients along the forward path. Useful for cross-validation.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

Returns:

**coef**ndarray of shape (n\_features,) or (n\_features, n\_targets)

Coefficients of the OMP solution. If `return_path=True`, this contains the whole coefficient path. In this case its shape is `(n_features, n_features)` or `(n_features, n_targets, n_features)` and iterating over the last axis yields coefficients in increasing order of active features.

**n\_iters**list or int

Number of active features across every target. Returned only if `return_n_iter` is set to True.

See also

[`OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")

Orthogonal Matching Pursuit model (OMP).

[`orthogonal_mp`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#sklearn.linear_model.orthogonal_mp "sklearn.linear_model.orthogonal_mp")

Solves n\_targets Orthogonal Matching Pursuit problems.

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Generic sparse coding. Each column of the result is the solution to a Lasso problem.

Notes

Orthogonal matching pursuit was introduced in G. Mallat, Z. Zhang, Matching pursuits with time-frequency dictionaries, IEEE Transactions on Signal Processing, Vol. 41, No. 12. (December 1993), pp. 3397-3415. ([https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf](https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf)
)

This implementation is based on Rubinstein, R., Zibulevsky, M. and Elad, M., Efficient Implementation of the K-SVD Algorithm using Batch Orthogonal Matching Pursuit Technical Report - CS Technion, April 2008. [https://www.cs.technion.ac.il/~ronrubin/Publications/KSVD-OMP-v2.pdf](https://www.cs.technion.ac.il/~ronrubin/Publications/KSVD-OMP-v2.pdf)

Examples

\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.linear\_model import orthogonal\_mp\_gram
\>>> X, y \= make\_regression(noise\=4, random\_state\=0)
\>>> coef \= orthogonal\_mp\_gram(X.T @ X, X.T @ y)
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