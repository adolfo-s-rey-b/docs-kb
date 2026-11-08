[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html)

Collapse Sidebar Expand Sidebar

sigmoid\_kernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sigmoid-kernel "Link to this heading")

=========================================================================================================================================================

sklearn.metrics.pairwise.sigmoid\_kernel(_X_, _Y\=None_, _gamma\=None_, _coef0\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1506)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sklearn.metrics.pairwise.sigmoid_kernel "Link to this definition")

Compute the sigmoid kernel between X and Y.

K(X, Y) = tanh(gamma <X, Y> + coef0)

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#sigmoid-kernel)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

A feature array.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. If `None`, uses `Y=X`.

**gamma**float, default=None

Coefficient of the vector inner product. If None, defaults to 1.0 / n\_features.

**coef0**float, default=1

Constant offset added to scaled inner product.

Returns:

**kernel**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Sigmoid kernel between two arrays.

Examples

\>>> from sklearn.metrics.pairwise import sigmoid\_kernel
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> sigmoid\_kernel(X, Y)
array(\[\[0.76, 0.76\],\
       \[0.87, 0.93\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)