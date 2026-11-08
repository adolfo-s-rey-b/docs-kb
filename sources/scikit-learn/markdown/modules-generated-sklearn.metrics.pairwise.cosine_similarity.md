[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)

Collapse Sidebar Expand Sidebar

cosine\_similarity[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#cosine-similarity "Link to this heading")

==================================================================================================================================================================

sklearn.metrics.pairwise.cosine\_similarity(_X_, _Y\=None_, _dense\_output\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1695)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "Link to this definition")

Compute cosine similarity between samples in X and Y.

Cosine similarity, or the cosine kernel, computes similarity as the normalized dot product of X and Y:

K(X, Y) = <X, Y> / (||X||\*||Y||)

Copy to clipboard

On L2-normalized data, this function is equivalent to linear\_kernel.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

Input data.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

Input data. If `None`, the output will be the pairwise similarities between all samples in `X`.

**dense\_output**bool, default=True

Whether to return dense output even when the input is sparse. If `False`, the output is sparse if both input arrays are sparse.

Added in version 0.17: parameter `dense_output` for dense output.

Returns:

**similarities**ndarray or sparse matrix of shape (n\_samples\_X, n\_samples\_Y)

Returns the cosine similarity between samples in X and Y.

Examples

\>>> from sklearn.metrics.pairwise import cosine\_similarity
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> cosine\_similarity(X, Y)
array(\[\[0.   , 0.   \],\
       \[0.577, 0.816\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_thumb.png)

[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)

Plot classification boundaries with different SVM Kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)