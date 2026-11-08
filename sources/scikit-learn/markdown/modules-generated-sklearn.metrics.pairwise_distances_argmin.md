[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise_distances_argmin.html)

Collapse Sidebar Expand Sidebar

pairwise\_distances\_argmin[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#pairwise-distances-argmin "Link to this heading")

==================================================================================================================================================================================

sklearn.metrics.pairwise\_distances\_argmin(_X_, _Y_, _\*_, _axis\=1_, _metric\='euclidean'_, _metric\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L848)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "Link to this definition")

Compute minimum distances between one point and a set of points.

This function computes for each row in X, the index of the row of Y which is closest (according to the specified distance).

This is mostly equivalent to calling:

pairwise\_distances(X, Y\=Y, metric\=metric).argmin(axis\=axis)

Copy to clipboard

but uses much less memory, and is faster for large arrays.

This function works with dense 2D arrays only.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

Array containing points.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features)

Arrays containing points.

**axis**int, default=1

Axis along which the argmin and distances are to be computed.

**metric**str or callable, default=”euclidean”

Metric to use for distance computation. Any metric from scikit-learn or [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 can be used.

If metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays as input and return one value indicating the distance between them. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string.

Distance matrices are not supported.

Valid values for metric are:

*   from scikit-learn: \[‘cityblock’, ‘cosine’, ‘euclidean’, ‘l1’, ‘l2’, ‘manhattan’, ‘nan\_euclidean’\]
    
*   from [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
    : \[‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘correlation’, ‘dice’, ‘hamming’, ‘jaccard’, ‘kulsinski’, ‘mahalanobis’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’\]
    

See the documentation for [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 for details on these metrics.

Note

`'kulsinski'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

Note

`'matching'` has been removed in SciPy 1.9 (use `'hamming'` instead).

**metric\_kwargs**dict, default=None

Keyword arguments to pass to specified metric function.

Returns:

**argmin**numpy.ndarray

Y\[argmin\[i\], :\] is the row in Y that is closest to X\[i, :\].

See also

[`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")

Distances between every pair of samples of X and Y.

[`pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")

Same as `pairwise_distances_argmin` but also returns the distances.

Examples

\>>> from sklearn.metrics.pairwise import pairwise\_distances\_argmin
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> pairwise\_distances\_argmin(X, Y)
array(\[0, 1\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)