[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.sparse_encode.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.sparse_encode.html)

Collapse Sidebar Expand Sidebar

sparse\_encode[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sparse-encode "Link to this heading")

===================================================================================================================================================

sklearn.decomposition.sparse\_encode(_X_, _dictionary_, _\*_, _gram\=None_, _cov\=None_, _algorithm\='lasso\_lars'_, _n\_nonzero\_coefs\=None_, _alpha\=None_, _copy\_cov\=True_, _init\=None_, _max\_iter\=1000_, _n\_jobs\=None_, _check\_input\=True_, _verbose\=0_, _positive\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L204)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "Link to this definition")

Sparse coding.

Each row of the result is the solution to a sparse coding problem. The goal is to find a sparse array `code` such that:

X ~= code \* dictionary

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#sparsecoder)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data matrix.

**dictionary**array-like of shape (n\_components, n\_features)

The dictionary matrix against which to solve the sparse coding of the data. Some of the algorithms assume normalized rows for meaningful output.

**gram**array-like of shape (n\_components, n\_components), default=None

Precomputed Gram matrix, `dictionary * dictionary'`.

**cov**array-like of shape (n\_components, n\_samples), default=None

Precomputed covariance, `dictionary' * X`.

**algorithm**{‘lasso\_lars’, ‘lasso\_cd’, ‘lars’, ‘omp’, ‘threshold’}, default=’lasso\_lars’

The algorithm used:

*   `'lars'`: uses the least angle regression method (`linear_model.lars_path`);
    
*   `'lasso_lars'`: uses Lars to compute the Lasso solution;
    
*   `'lasso_cd'`: uses the coordinate descent method to compute the Lasso solution (`linear_model.Lasso`). lasso\_lars will be faster if the estimated components are sparse;
    
*   `'omp'`: uses orthogonal matching pursuit to estimate the sparse solution;
    
*   `'threshold'`: squashes to zero all coefficients less than regularization from the projection `dictionary * data'`.
    

**n\_nonzero\_coefs**int, default=None

Number of nonzero coefficients to target in each column of the solution. This is only used by `algorithm='lars'` and `algorithm='omp'` and is overridden by `alpha` in the `omp` case. If `None`, then `n_nonzero_coefs=int(n_features / 10)`.

**alpha**float, default=None

If `algorithm='lasso_lars'` or `algorithm='lasso_cd'`, `alpha` is the penalty applied to the L1 norm. If `algorithm='threshold'`, `alpha` is the absolute value of the threshold below which coefficients will be squashed to zero. If `algorithm='omp'`, `alpha` is the tolerance parameter: the value of the reconstruction error targeted. In this case, it overrides `n_nonzero_coefs`. If `None`, default to 1.

**copy\_cov**bool, default=True

Whether to copy the precomputed covariance matrix; if `False`, it may be overwritten.

**init**ndarray of shape (n\_samples, n\_components), default=None

Initialization value of the sparse codes. Only used if `algorithm='lasso_cd'`.

**max\_iter**int, default=1000

Maximum number of iterations to perform if `algorithm='lasso_cd'` or `'lasso_lars'`.

**n\_jobs**int, default=None

Number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**check\_input**bool, default=True

If `False`, the input arrays X and dictionary will not be checked.

**verbose**int, default=0

Controls the verbosity; the higher, the more messages.

**positive**bool, default=False

Whether to enforce positivity when finding the encoding.

Added in version 0.20.

Returns:

**code**ndarray of shape (n\_samples, n\_components)

The sparse codes.

See also

[`sklearn.linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`sklearn.linear_model.orthogonal_mp`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#sklearn.linear_model.orthogonal_mp "sklearn.linear_model.orthogonal_mp")

Solves Orthogonal Matching Pursuit problems.

[`sklearn.linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

Train Linear Model with L1 prior as regularizer.

[`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")

Find a sparse representation of data from a fixed precomputed dictionary.

Examples

\>>> import numpy as np
\>>> from sklearn.decomposition import sparse\_encode
\>>> X \= np.array(\[\[\-1, \-1, \-1\], \[0, 0, 3\]\])
\>>> dictionary \= np.array(
...     \[\[0, 1, 0\],\
...      \[\-1, \-1, 2\],\
...      \[1, 1, 1\],\
...      \[0, 1, 1\],\
...      \[0, 2, 1\]\],
...    dtype\=np.float64
... )
\>>> sparse\_encode(X, dictionary, alpha\=1e-10)
array(\[\[ 0.,  0., -1.,  0.,  0.\],\
       \[ 0.,  1.,  1.,  0.,  0.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)