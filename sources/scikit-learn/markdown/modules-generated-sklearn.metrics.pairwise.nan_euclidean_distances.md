[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html)

Collapse Sidebar Expand Sidebar

nan\_euclidean\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#nan-euclidean-distances "Link to this heading")

=====================================================================================================================================================================================

sklearn.metrics.pairwise.nan\_euclidean\_distances(_X_, _Y\=None_, _\*_, _squared\=False_, _missing\_values\=nan_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L430)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "Link to this definition")

Calculate the euclidean distances in the presence of missing values.

Compute the euclidean distance between each pair of samples in X and Y, where Y=X is assumed if Y=None. When calculating the distance between a pair of samples, this formulation ignores feature coordinates with a missing value in either sample and scales up the weight of the remaining coordinates:

dist(x,y) = sqrt(weight \* sq. distance from present coordinates)

Copy to clipboard

where:

weight = Total # of coordinates / # of present coordinates

Copy to clipboard

For example, the distance between `[3, na, na, 6]` and `[1, na, 4, 5]` is:

42((3−1)2+(6−5)2)

If all the coordinates are missing or if there are no common present coordinates then NaN is returned for that pair.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Added in version 0.22.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features)

An array where each row is a sample and each column is a feature.

**Y**array-like of shape (n\_samples\_Y, n\_features), default=None

An array where each row is a sample and each column is a feature. If `None`, method uses `Y=X`.

**squared**bool, default=False

Return squared Euclidean distances.

**missing\_values**np.nan, float or int, default=np.nan

Representation of missing value.

**copy**bool, default=True

Make and use a deep copy of X and Y (if Y exists).

Returns:

**distances**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Returns the distances between the row vectors of `X` and the row vectors of `Y`.

See also

[`paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances")

Distances between pairs of elements of X and Y.

References

*   John K. Dixon, “Pattern Recognition with Partly Missing Data”, IEEE Transactions on Systems, Man, and Cybernetics, Volume: 9, Issue: 10, pp. 617 - 621, Oct. 1979. [http://ieeexplore.ieee.org/abstract/document/4310090/](http://ieeexplore.ieee.org/abstract/document/4310090/)
    

Examples

\>>> from sklearn.metrics.pairwise import nan\_euclidean\_distances
\>>> nan \= float("NaN")
\>>> X \= \[\[0, 1\], \[1, nan\]\]
\>>> nan\_euclidean\_distances(X, X) \# distance between rows of X
array(\[\[0.        , 1.41421356\],\
       \[1.41421356, 0.        \]\])

Copy to clipboard

\>>> \# get distance to origin
\>>> nan\_euclidean\_distances(X, \[\[0, 0\]\])
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