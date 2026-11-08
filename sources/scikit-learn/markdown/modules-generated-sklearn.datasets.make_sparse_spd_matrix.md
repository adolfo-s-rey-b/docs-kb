[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html)

Collapse Sidebar Expand Sidebar

make\_sparse\_spd\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#make-sparse-spd-matrix "Link to this heading")

===========================================================================================================================================================================

sklearn.datasets.make\_sparse\_spd\_matrix(_n\_dim\=1_, _\*_, _alpha\=0.95_, _norm\_diag\=False_, _smallest\_coef\=0.1_, _largest\_coef\=0.9_, _sparse\_format\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L1739)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "Link to this definition")

Generate a sparse symmetric definite positive matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_dim**int, default=1

The size of the random matrix to generate.

Changed in version 1.4: Renamed from `dim` to `n_dim`.

**alpha**float, default=0.95

The probability that a coefficient is zero (see notes). Larger values enforce more sparsity. The value should be in the range 0 and 1.

**norm\_diag**bool, default=False

Whether to normalize the output matrix to make the leading diagonal elements all 1.

**smallest\_coef**float, default=0.1

The value of the smallest coefficient between 0 and 1.

**largest\_coef**float, default=0.9

The value of the largest coefficient between 0 and 1.

**sparse\_format**str, default=None

String representing the output sparse format, such as ‘csc’, ‘csr’, etc. If `None`, return a dense numpy ndarray.

Added in version 1.4.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**prec**ndarray or sparse matrix of shape (dim, dim)

The generated matrix. If `sparse_format=None`, this would be an ndarray. Otherwise, this will be a sparse matrix of the specified format.

See also

[`make_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#sklearn.datasets.make_spd_matrix "sklearn.datasets.make_spd_matrix")

Generate a random symmetric, positive-definite matrix.

Notes

The sparsity is actually imposed on the cholesky factor of the matrix. Thus alpha does not translate directly into the filling fraction of the matrix itself.

Examples

\>>> from sklearn.datasets import make\_sparse\_spd\_matrix
\>>> make\_sparse\_spd\_matrix(n\_dim\=4, norm\_diag\=False, random\_state\=42)
array(\[\[1., 0., 0., 0.\],\
       \[0., 1., 0., 0.\],\
       \[0., 0., 1., 0.\],\
       \[0., 0., 0., 1.\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

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