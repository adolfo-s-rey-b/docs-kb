[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html)

Collapse Sidebar Expand Sidebar

additive\_chi2\_kernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#additive-chi2-kernel "Link to this heading")

============================================================================================================================================================================

sklearn.metrics.pairwise.additive\_chi2\_kernel(_X_, _Y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1761)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "Link to this definition")

Compute the additive chi-squared kernel between observations in X and Y.

The chi-squared kernel is computed between each pair of rows in X and Y. X and Y have to be non-negative. This kernel is most commonly applied to histograms.

The chi-squared kernel is given by:

k(x, y) = -Sum \[(x - y)^2 / (x + y)\]

Copy to clipboard

It can be interpreted as a weighted difference per entry.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#chi2-kernel)
.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features)

A feature array.

**Y**array-like of shape (n\_samples\_Y, n\_features), default=None

An optional second feature array. If `None`, uses `Y=X`.

Returns:

**kernel**array-like of shape (n\_samples\_X, n\_samples\_Y)

The kernel matrix.

See also

[`chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html#sklearn.metrics.pairwise.chi2_kernel "sklearn.metrics.pairwise.chi2_kernel")

The exponentiated version of the kernel, which is usually preferable.

[`sklearn.kernel_approximation.AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")

A Fourier approximation to this kernel.

Notes

As the negative of a distance, this kernel is only conditionally positive definite.

References

*   Zhang, J. and Marszalek, M. and Lazebnik, S. and Schmid, C. Local features and kernels for classification of texture and object categories: A comprehensive study International Journal of Computer Vision 2007 [https://hal.archives-ouvertes.fr/hal-00171412/document](https://hal.archives-ouvertes.fr/hal-00171412/document)
    

Examples

\>>> from sklearn.metrics.pairwise import additive\_chi2\_kernel
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> additive\_chi2\_kernel(X, Y)
array(\[\[-1., -2.\],\
       \[-2., -1.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)