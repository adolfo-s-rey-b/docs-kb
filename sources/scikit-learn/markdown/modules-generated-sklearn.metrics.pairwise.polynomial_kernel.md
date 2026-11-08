[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html)

Collapse Sidebar Expand Sidebar

polynomial\_kernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#polynomial-kernel "Link to this heading")

==================================================================================================================================================================

sklearn.metrics.pairwise.polynomial\_kernel(_X_, _Y\=None_, _degree\=3_, _gamma\=None_, _coef0\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "Link to this definition")

Compute the polynomial kernel between X and Y.

K(X, Y) = (gamma <X, Y> + coef0) ^ degree

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#polynomial-kernel)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

A feature array.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. If `None`, uses `Y=X`.

**degree**float, default=3

Kernel degree.

**gamma**float, default=None

Coefficient of the vector inner product. If None, defaults to 1.0 / n\_features.

**coef0**float, default=1

Constant offset added to scaled inner product.

Returns:

**kernel**ndarray of shape (n\_samples\_X, n\_samples\_Y)

The polynomial kernel.

Examples

\>>> from sklearn.metrics.pairwise import polynomial\_kernel
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> polynomial\_kernel(X, Y, degree\=2)
array(\[\[1.     , 1.     \],\
       \[1.77, 2.77\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)