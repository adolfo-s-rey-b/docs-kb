[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html)

Collapse Sidebar Expand Sidebar

laplacian\_kernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#laplacian-kernel "Link to this heading")

===============================================================================================================================================================

sklearn.metrics.pairwise.laplacian\_kernel(_X_, _Y\=None_, _gamma\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1631)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "Link to this definition")

Compute the laplacian kernel between X and Y.

The laplacian kernel is defined as:

K(x, y) = exp(-gamma ||x-y||\_1)

Copy to clipboard

for each pair of rows x in X and y in Y. Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#laplacian-kernel)
.

Added in version 0.17.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

A feature array.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. If `None`, uses `Y=X`.

**gamma**float, default=None

If None, defaults to 1.0 / n\_features. Otherwise it should be strictly positive.

Returns:

**kernel**ndarray of shape (n\_samples\_X, n\_samples\_Y)

The kernel matrix.

Examples

\>>> from sklearn.metrics.pairwise import laplacian\_kernel
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> laplacian\_kernel(X, Y)
array(\[\[0.71, 0.51\],\
       \[0.51, 0.71\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)