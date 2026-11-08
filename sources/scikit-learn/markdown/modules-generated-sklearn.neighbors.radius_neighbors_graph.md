[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.radius_neighbors_graph.html)

Collapse Sidebar Expand Sidebar

radius\_neighbors\_graph[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html#radius-neighbors-graph "Link to this heading")

===========================================================================================================================================================================

sklearn.neighbors.radius\_neighbors\_graph(_X_, _radius_, _\*_, _mode\='connectivity'_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _include\_self\=False_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_graph.py#L155)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html#sklearn.neighbors.radius_neighbors_graph "Link to this definition")

Compute the (weighted) graph of Neighbors for points in X.

Neighborhoods are restricted the points at a distance lower than radius.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#unsupervised-neighbors)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Sample data.

**radius**float

Radius of neighborhoods.

**mode**{‘connectivity’, ‘distance’}, default=’connectivity’

Type of returned matrix: ‘connectivity’ will return the connectivity matrix with ones and zeros, and ‘distance’ will return the distances between neighbors according to the given metric.

**metric**str, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for valid metric values.

**p**float, default=2

Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**include\_self**bool or ‘auto’, default=False

Whether or not to mark each sample as the first nearest neighbor to itself. If ‘auto’, then True is used for mode=’connectivity’ and False for mode=’distance’.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Returns:

**A**sparse matrix of shape (n\_samples, n\_samples)

Graph where A\[i, j\] is assigned the weight of edge that connects i to j. The matrix is of CSR format.

See also

[`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")

Compute the weighted graph of k-neighbors for points in X.

Examples

\>>> X \= \[\[0\], \[3\], \[1\]\]
\>>> from sklearn.neighbors import radius\_neighbors\_graph
\>>> A \= radius\_neighbors\_graph(X, 1.5, mode\='connectivity',
...                            include\_self\=True)
\>>> A.toarray()
array(\[\[1., 0., 1.\],\
       \[0., 1., 0.\],\
       \[1., 0., 1.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)