[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.paired_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.paired_distances.html)

Collapse Sidebar Expand Sidebar

paired\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#paired-distances "Link to this heading")

===============================================================================================================================================================

sklearn.metrics.pairwise.paired\_distances(_X_, _Y_, _\*_, _metric\='euclidean'_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L1323)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "Link to this definition")

Compute the paired distances between X and Y.

Distances are calculated between (X\[0\], Y\[0\]), (X\[1\], Y\[1\]), …, etc.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/metrics.html#metrics)
.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Array 1 for distance computation.

**Y**ndarray of shape (n\_samples, n\_features)

Array 2 for distance computation.

**metric**str or callable, default=”euclidean”

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options specified in PAIRED\_DISTANCES, including “euclidean”, “manhattan”, or “cosine”. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from `X` as input and return a value indicating the distance between them.

**\*\*kwds**dict

Unused parameters.

Returns:

**distances**ndarray of shape (n\_samples,)

Returns the distances between the row vectors of `X` and the row vectors of `Y`, where `distances[i]` is the distance between `X[i]` and `Y[i]`.

See also

[`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")

Computes the distance between every pair of samples.

Examples

\>>> from sklearn.metrics.pairwise import paired\_distances
\>>> X \= \[\[0, 1\], \[1, 1\]\]
\>>> Y \= \[\[0, 1\], \[2, 1\]\]
\>>> paired\_distances(X, Y)
array(\[0., 1.\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)