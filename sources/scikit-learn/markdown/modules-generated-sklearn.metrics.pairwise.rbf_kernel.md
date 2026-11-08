[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)

Collapse Sidebar Expand Sidebar

rbf\_kernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#rbf-kernel "Link to this heading")

=============================================================================================================================================

sklearn.metrics.pairwise.rbf\_kernel(_X_, _Y\=None_, _gamma\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1571)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "Link to this definition")

Compute the rbf (gaussian) kernel between X and Y.

K(x, y) = exp(-gamma ||x-y||^2)

Copy to clipboard

for each pair of rows x in X and y in Y.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#rbf-kernel)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

A feature array.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. If `None`, uses `Y=X`.

**gamma**float, default=None

If None, defaults to 1.0 / n\_features.

Returns:

**kernel**ndarray of shape (n\_samples\_X, n\_samples\_Y)

The RBF kernel.

Examples

\>>> from sklearn.metrics.pairwise import rbf\_kernel
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> rbf\_kernel(X, Y)
array(\[\[0.71, 0.51\],\
       \[0.51, 0.71\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)