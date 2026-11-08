[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html)

Collapse Sidebar Expand Sidebar

euclidean\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#euclidean-distances "Link to this heading")

========================================================================================================================================================================

sklearn.metrics.pairwise.euclidean\_distances(_X_, _Y\=None_, _\*_, _Y\_norm\_squared\=None_, _squared\=False_, _X\_norm\_squared\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L258)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "Link to this definition")

Compute the distance matrix between each pair from a feature array X and Y.

For efficiency reasons, the euclidean distance between a pair of row vector x and y is computed as:

dist(x, y) \= sqrt(dot(x, x) \- 2 \* dot(x, y) + dot(y, y))

Copy to clipboard

This formulation has two advantages over other ways of computing distances. First, it is computationally efficient when dealing with sparse data. Second, if one argument varies but the other remains unchanged, then `dot(x, x)` and/or `dot(y, y)` can be pre-computed.

However, this is not the most precise way of doing this computation, because this equation potentially suffers from “catastrophic cancellation”. Also, the distance matrix returned by this function may not be exactly symmetric as required by, e.g., [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 functions.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, n\_features)

An array where each row is a sample and each column is a feature.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, n\_features), default=None

An array where each row is a sample and each column is a feature. If `None`, method uses `Y=X`.

**Y\_norm\_squared**array-like of shape (n\_samples\_Y,) or (n\_samples\_Y, 1) or (1, n\_samples\_Y), default=None

Pre-computed dot-products of vectors in Y (e.g., `(Y**2).sum(axis=1)`) May be ignored in some cases, see the note below.

**squared**bool, default=False

Return squared Euclidean distances.

**X\_norm\_squared**array-like of shape (n\_samples\_X,) or (n\_samples\_X, 1) or (1, n\_samples\_X), default=None

Pre-computed dot-products of vectors in X (e.g., `(X**2).sum(axis=1)`) May be ignored in some cases, see the note below.

Returns:

**distances**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Returns the distances between the row vectors of `X` and the row vectors of `Y`.

See also

[`paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances")

Distances between pairs of elements of X and Y.

Notes

To achieve a better accuracy, `X_norm_squared` and `Y_norm_squared` may be unused if they are passed as `np.float32`.

Examples

\>>> from sklearn.metrics.pairwise import euclidean\_distances
\>>> X \= \[\[0, 1\], \[1, 1\]\]
\>>> \# distance between rows of X
\>>> euclidean\_distances(X, X)
array(\[\[0., 1.\],\
       \[1., 0.\]\])
\>>> \# get distance to origin
\>>> euclidean\_distances(X, \[\[0, 0\]\])
array(\[\[1.        \],\
       \[1.41421356\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)