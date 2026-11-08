[Skip to main content](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/dbscan-function.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/dbscan-function.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/dbscan-function.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/dbscan-function.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/dbscan-function.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/dbscan-function.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/dbscan-function.html)

Collapse Sidebar Expand Sidebar

dbscan[#](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#dbscan "Link to this heading")

================================================================================================================

sklearn.cluster.dbscan(_X_, _eps\=0.5_, _\*_, _min\_samples\=5_, _metric\='minkowski'_, _metric\_params\=None_, _algorithm\='auto'_, _leaf\_size\=30_, _p\=2_, _sample\_weight\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_dbscan.py#L22)
[#](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "Link to this definition")

Perform DBSCAN clustering from vector array or distance matrix.

This function is a wrapper around `DBSCAN`, suitable for quick, standalone clustering tasks. For estimator-based workflows, where estimator attributes or pipeline integration is required, prefer `DBSCAN`.

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a density-based clustering algorithm that groups together points that are closely packed while marking points in low-density regions as outliers.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
.

Parameters:

**X**{array-like, scipy sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

A feature array, or array of distances between samples if `metric='precomputed'`. When using precomputed distances, X must be a square symmetric matrix.

**eps**float, default=0.5

The maximum distance between two samples for one to be considered as in the neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. This is the most important DBSCAN parameter to choose appropriately for your data set and distance function. Smaller values result in more clusters, while larger values result in fewer, larger clusters.

**min\_samples**int, default=5

The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself. Higher values yield fewer, denser clusters, while lower values yield more, sparser clusters.

**metric**str or callable, default=’minkowski’

The metric to use when calculating distance between instances in a feature array. If metric is a string or callable, it must be one of the options allowed by [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
 for its metric parameter. If metric is “precomputed”, X is assumed to be a distance matrix and must be square during fit. X may be a [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
, in which case only “nonzero” elements may be considered neighbors.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

Added in version 0.19.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

The algorithm to be used by the NearestNeighbors module to compute pointwise distances and find nearest neighbors. ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to `fit` method. See [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 documentation for details.

**leaf\_size**int, default=30

Leaf size passed to BallTree or cKDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem. Generally, smaller leaf sizes lead to faster queries but slower construction.

**p**float, default=2

Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used. This parameter is expected to be positive.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weight of each sample, such that a sample with a weight of at least `min_samples` is by itself a core sample; a sample with negative weight may inhibit its eps-neighbor from being core. Note that weights are absolute, and default to 1.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details. If precomputed distances are used, parallel execution is not available and thus n\_jobs will have no effect.

Returns:

**core\_samples**ndarray of shape (n\_core\_samples,)

Indices of core samples.

**labels**ndarray of shape (n\_samples,)

Cluster labels for each point. Noisy samples are given the label -1. Non-negative integers indicate cluster membership.

See also

[`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")

An estimator interface for this clustering algorithm.

[`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")

A similar estimator interface clustering at multiple values of eps. Our implementation is optimized for memory usage.

Notes

For an example, see [Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)
.

This implementation bulk-computes all neighborhood queries, which increases the memory complexity to O(n.d) where d is the average number of neighbors, while original DBSCAN had memory complexity O(n). It may attract a higher memory complexity when querying these nearest neighborhoods, depending on the `algorithm`.

One way to avoid the query complexity is to pre-compute sparse neighborhoods in chunks using [`NearestNeighbors.radius_neighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors_graph "sklearn.neighbors.NearestNeighbors.radius_neighbors_graph")
 with `mode='distance'`, then using `metric='precomputed'` here.

Another way to reduce memory and computation time is to remove (near-)duplicate points and use `sample_weight` instead.

[`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
 provides a similar clustering with lower memory usage.

References

Ester, M., H. P. Kriegel, J. Sander, and X. Xu, [“A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise”](https://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf)
. In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996

Schubert, E., Sander, J., Ester, M., Kriegel, H. P., & Xu, X. (2017). [“DBSCAN revisited, revisited: why and how you should (still) use DBSCAN.”](https://doi.org/10.1145/3068335)
 ACM Transactions on Database Systems (TODS), 42(3), 19.

Examples

\>>> from sklearn.cluster import dbscan
\>>> X \= \[\[1, 2\], \[2, 2\], \[2, 3\], \[8, 7\], \[8, 8\], \[25, 80\]\]
\>>> core\_samples, labels \= dbscan(X, eps\=3, min\_samples\=2)
\>>> core\_samples
array(\[0, 1, 2, 3, 4\])
\>>> labels
array(\[ 0,  0,  0,  1,  1, -1\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)