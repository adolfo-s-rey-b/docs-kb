[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.OPTICS.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.OPTICS.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.OPTICS.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.OPTICS.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.OPTICS.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.OPTICS.html)

Collapse Sidebar Expand Sidebar

OPTICS[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#optics "Link to this heading")

=======================================================================================================================

class sklearn.cluster.OPTICS(_\*_, _min\_samples\=5_, _max\_eps\=inf_, _metric\='minkowski'_, _p\=2_, _metric\_params\=None_, _cluster\_method\='xi'_, _eps\=None_, _xi\=0.05_, _predecessor\_correction\=True_, _min\_cluster\_size\=None_, _algorithm\='auto'_, _leaf\_size\=30_, _memory\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_optics.py#L33)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "Link to this definition")

Estimate clustering structure from vector array.

OPTICS (Ordering Points To Identify the Clustering Structure), closely related to DBSCAN, finds core samples of high density and expands clusters from them [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#r2c55e37003fe-1)
. Unlike DBSCAN, it keeps cluster hierarchy for a variable neighborhood radius. Better suited for usage on large datasets than the current scikit-learn implementation of DBSCAN.

Clusters are then extracted from the cluster-order using a DBSCAN-like method (cluster\_method = ‘dbscan’) or an automatic technique proposed in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#r2c55e37003fe-1)
 (cluster\_method = ‘xi’).

This implementation deviates from the original OPTICS by first performing k-nearest-neighborhood searches on all points to identify core sizes of all points (instead of computing neighbors while looping through points). Reachability distances to only unprocessed points are then computed, to construct the cluster order, similar to the original OPTICS. Note that we do not employ a heap to manage the expansion candidates, so the time complexity will be O(n^2).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#optics)
.

Parameters:

**min\_samples**int > 1 or float between 0 and 1, default=5

The number of samples in a neighborhood for a point to be considered as a core point. Also, up and down steep regions can’t have more than `min_samples` consecutive non-steep points. Expressed as an absolute number or a fraction of the number of samples (rounded to be at least 2).

**max\_eps**float, default=np.inf

The maximum distance between two samples for one to be considered as in the neighborhood of the other. Default value of `np.inf` will identify clusters across all scales; reducing `max_eps` will result in shorter run times.

**metric**str or callable, default=’minkowski’

Metric to use for distance computation. Any metric from scikit-learn or [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 can be used.

If `metric` is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays as input and return one value indicating the distance between them. This works for Scipy’s metrics, but is less efficient than passing the metric name as a string. If metric is “precomputed”, `X` is assumed to be a distance matrix and must be square.

Valid values for metric are:

*   from scikit-learn: \[‘cityblock’, ‘cosine’, ‘euclidean’, ‘l1’, ‘l2’, ‘manhattan’\]
    
*   from scipy.spatial.distance: \[‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘correlation’, ‘dice’, ‘hamming’, ‘jaccard’, ‘kulsinski’, ‘mahalanobis’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’\]
    

Sparse matrices are only supported by scikit-learn metrics. See [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance "(in SciPy v1.18.0)")
 for details on these metrics.

Note

`'kulsinski'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

**p**float, default=2

Parameter for the Minkowski metric from [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. When p = 1, this is equivalent to using manhattan\_distance (l1), and euclidean\_distance (l2) for p = 2. For arbitrary p, minkowski\_distance (l\_p) is used.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

**cluster\_method**{‘xi’, ‘dbscan’}, default=’xi’

The extraction method used to extract clusters using the calculated reachability and ordering.

**eps**float, default=None

The maximum distance between two samples for one to be considered as in the neighborhood of the other. By default it assumes the same value as `max_eps`. Used only when `cluster_method='dbscan'`.

**xi**float between 0 and 1, default=0.05

Determines the minimum steepness on the reachability plot that constitutes a cluster boundary. For example, an upwards point in the reachability plot is defined by the ratio from one point to its successor being at most 1-xi. Used only when `cluster_method='xi'`.

**predecessor\_correction**bool, default=True

Correct clusters according to the predecessors calculated by OPTICS [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#r2c55e37003fe-2)
. This parameter has minimal effect on most datasets. Used only when `cluster_method='xi'`.

**min\_cluster\_size**int > 1 or float between 0 and 1, default=None

Minimum number of samples in an OPTICS cluster, expressed as an absolute number or a fraction of the number of samples (rounded to be at least 2). If `None`, the value of `min_samples` is used instead. Used only when `cluster_method='xi'`.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

Algorithm used to compute the nearest neighbors:

*   ‘ball\_tree’ will use [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    .
    
*   ‘kd\_tree’ will use [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
    .
    
*   ‘brute’ will use a brute-force search.
    
*   ‘auto’ (default) will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.fit "sklearn.cluster.OPTICS.fit")
     method.
    

Note: fitting on sparse input will override the setting of this parameter, using brute force.

**leaf\_size**int, default=30

Leaf size passed to [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 or [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**memory**str or object with the joblib.Memory interface, default=None

Used to cache the output of the computation of the tree. By default, no caching is done. If a string is given, it is the path to the caching directory.

**n\_jobs**int, default=None

The number of parallel jobs to run for neighbors search. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**labels\_**ndarray of shape (n\_samples,)

Cluster labels for each point in the dataset given to fit(). Noisy samples and points which are not included in a leaf cluster of `cluster_hierarchy_` are labeled as -1.

**reachability\_**ndarray of shape (n\_samples,)

Reachability distances per sample, indexed by object order. Use `clust.reachability_[clust.ordering_]` to access in cluster order.

**ordering\_**ndarray of shape (n\_samples,)

The cluster ordered list of sample indices.

**core\_distances\_**ndarray of shape (n\_samples,)

Distance at which each sample becomes a core point, indexed by object order. Points which will never be core have a distance of inf. Use `clust.core_distances_[clust.ordering_]` to access in cluster order.

**predecessor\_**ndarray of shape (n\_samples,)

Point that a sample was reached from, indexed by object order. Seed points have a predecessor of -1.

**cluster\_hierarchy\_**ndarray of shape (n\_clusters, 2)

The list of clusters in the form of `[start, end]` in each row, with all indices inclusive. The clusters are ordered according to `(end, -start)` (ascending) so that larger clusters encompassing smaller clusters come after those smaller ones. Since `labels_` does not reflect the hierarchy, usually `len(cluster_hierarchy_) > np.unique(optics.labels_)`. Please also note that these indices are of the `ordering_`, i.e. `X[ordering_][start:end + 1]` form a cluster. Only available when `cluster_method='xi'`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")

A similar clustering for a specified neighborhood radius (eps). Our implementation is optimized for runtime.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#id2)
)

Ankerst, Mihael, Markus M. Breunig, Hans-Peter Kriegel, and Jörg Sander. “OPTICS: ordering points to identify the clustering structure.” ACM SIGMOD Record 28, no. 2 (1999): 49-60.

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#id3)\
\]

Schubert, Erich, Michael Gertz. “Improving the Cluster Structure Extracted from OPTICS Plots.” Proc. of the Conference “Lernen, Wissen, Daten, Analysen” (LWDA) (2018): 318-329.

Examples

\>>> from sklearn.cluster import OPTICS
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 2\], \[2, 5\], \[3, 6\],\
...               \[8, 7\], \[8, 8\], \[7, 3\]\])
\>>> clustering \= OPTICS(min\_samples\=2).fit(X)
\>>> clustering.labels\_
array(\[0, 0, 0, 1, 1, 1\])

Copy to clipboard

For a more detailed example see [Demo of OPTICS clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html#sphx-glr-auto-examples-cluster-plot-optics-py)
.

For a comparison of OPTICS with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_optics.py#L300)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.fit "Link to this definition")

Perform OPTICS clustering.

Extracts an ordered list of points and reachability distances, and performs initial clustering using `max_eps` distance specified at OPTICS object instantiation.

Parameters:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features), or (n\_samples, n\_samples) if metric=’precomputed’

A feature array, or array of distances between samples if metric=’precomputed’. If a sparse matrix is provided, it will be converted into CSR format.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns a fitted instance of self.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L745)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.fit_predict "Link to this definition")

Perform clustering on `X` and returns cluster labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**labels**ndarray of shape (n\_samples,), dtype=np.int64

Cluster labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_optics_thumb.png)

[Demo of OPTICS clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html)

Demo of OPTICS clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)