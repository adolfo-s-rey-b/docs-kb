[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.compute_optics_graph.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.compute_optics_graph.html)

Collapse Sidebar Expand Sidebar

compute\_optics\_graph[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#compute-optics-graph "Link to this heading")

===================================================================================================================================================================

sklearn.cluster.compute\_optics\_graph(_X_, _\*_, _min\_samples_, _max\_eps_, _metric_, _p_, _metric\_params_, _algorithm_, _leaf\_size_, _n\_jobs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_optics.py#L444)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#sklearn.cluster.compute_optics_graph "Link to this definition")

Compute the OPTICS reachability graph.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#optics)
.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features), or (n\_samples, n\_samples) if metric=’precomputed’

A feature array, or array of distances between samples if metric=’precomputed’.

**min\_samples**int > 1 or float between 0 and 1

The number of samples in a neighborhood for a point to be considered as a core point. Expressed as an absolute number or a fraction of the number of samples (rounded to be at least 2).

**max\_eps**float, default=np.inf

The maximum distance between two samples for one to be considered as in the neighborhood of the other. Default value of `np.inf` will identify clusters across all scales; reducing `max_eps` will result in shorter run times.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Any metric from scikit-learn or scipy.spatial.distance can be used.

If metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays as input and return one value indicating the distance between them. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string. If metric is “precomputed”, X is assumed to be a distance matrix and must be square.

Valid values for metric are:

*   from scikit-learn: \[‘cityblock’, ‘cosine’, ‘euclidean’, ‘l1’, ‘l2’, ‘manhattan’\]
    
*   from scipy.spatial.distance: \[‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘correlation’, ‘dice’, ‘hamming’, ‘jaccard’, ‘kulsinski’, ‘mahalanobis’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’\]
    

See the documentation for scipy.spatial.distance for details on these metrics.

Note

`'kulsinski'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

**p**float, default=2

Parameter for the Minkowski metric from [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    .
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    .
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to `fit` method. (default)
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf size passed to [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 or [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Returns:

**ordering\_**array of shape (n\_samples,)

The cluster ordered list of sample indices.

**core\_distances\_**array of shape (n\_samples,)

Distance at which each sample becomes a core point, indexed by object order. Points which will never be core have a distance of inf. Use `clust.core_distances_[clust.ordering_]` to access in cluster order.

**reachability\_**array of shape (n\_samples,)

Reachability distances per sample, indexed by object order. Use `clust.reachability_[clust.ordering_]` to access in cluster order.

**predecessor\_**array of shape (n\_samples,)

Point that a sample was reached from, indexed by object order. Seed points have a predecessor of -1.

References

\[1\]

Ankerst, Mihael, Markus M. Breunig, Hans-Peter Kriegel, and Jörg Sander. “OPTICS: ordering points to identify the clustering structure.” ACM SIGMOD Record 28, no. 2 (1999): 49-60.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import compute\_optics\_graph
\>>> X \= np.array(\[\[1, 2\], \[2, 5\], \[3, 6\],\
...               \[8, 7\], \[8, 8\], \[7, 3\]\])
\>>> ordering, core\_distances, reachability, predecessor \= compute\_optics\_graph(
...     X,
...     min\_samples\=2,
...     max\_eps\=np.inf,
...     metric\="minkowski",
...     p\=2,
...     metric\_params\=None,
...     algorithm\="auto",
...     leaf\_size\=30,
...     n\_jobs\=None,
... )
\>>> ordering
array(\[0, 1, 2, 5, 3, 4\])
\>>> core\_distances
array(\[3.16, 1.41, 1.41, 1.        , 1.        ,\
       4.12\])
\>>> reachability
array(\[       inf, 3.16, 1.41, 4.12, 1.        ,\
       5.        \])
\>>> predecessor
array(\[-1,  0,  1,  5,  3,  2\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)