[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html)

Collapse Sidebar Expand Sidebar

pairwise\_distances\_argmin\_min[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#pairwise-distances-argmin-min "Link to this heading")

===============================================================================================================================================================================================

sklearn.metrics.pairwise\_distances\_argmin\_min(_X_, _Y_, _\*_, _axis\=1_, _metric\='euclidean'_, _metric\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L698)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "Link to this definition")

Compute minimum distances between one point and a set of points.

This function computes for each row in X, the index of the row of Y which is closest (according to the specified distance). The minimal distances are also returned.

This is mostly equivalent to calling:

(pairwise\_distances(X, Y\=Y, metric\=metric).argmin(axis\=axis),
 pairwise\_distances(X, Y\=Y, metric\=metric).min(axis\=axis))

Copy to clipboard

but uses much less memory, and is faster for large arrays.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

Array containing points.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features)

Array containing points.

**axis**int, default=1

Axis along which the argmin and distances are to be computed.

**metric**str or callable, default=’euclidean’

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

**argmin**ndarray

Y\[argmin\[i\], :\] is the row in Y that is closest to X\[i, :\].

**distances**ndarray

The array of minimum distances. `distances[i]` is the distance between the i-th row in X and the argmin\[i\]-th row in Y.

See also

[`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")

Distances between every pair of samples of X and Y.

[`pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")

Same as `pairwise_distances_argmin_min` but only returns the argmins.

Examples

\>>> from sklearn.metrics.pairwise import pairwise\_distances\_argmin\_min
\>>> X \= \[\[0, 0, 0\], \[1, 1, 1\]\]
\>>> Y \= \[\[1, 0, 0\], \[1, 1, 0\]\]
\>>> argmin, distances \= pairwise\_distances\_argmin\_min(X, Y)
\>>> argmin
array(\[0, 1\])
\>>> distances
array(\[1., 1.\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)