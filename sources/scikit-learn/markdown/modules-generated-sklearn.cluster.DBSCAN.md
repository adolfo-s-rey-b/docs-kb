[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.DBSCAN.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.DBSCAN.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.DBSCAN.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.DBSCAN.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.DBSCAN.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.DBSCAN.html)

Collapse Sidebar Expand Sidebar

DBSCAN[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#dbscan "Link to this heading")

=======================================================================================================================

class sklearn.cluster.DBSCAN(_eps\=0.5_, _\*_, _min\_samples\=5_, _metric\='euclidean'_, _metric\_params\=None_, _algorithm\='auto'_, _leaf\_size\=30_, _p\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_dbscan.py#L201)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "Link to this definition")

Perform DBSCAN clustering from vector array or distance matrix.

DBSCAN - Density-Based Spatial Clustering of Applications with Noise. Finds core samples of high density and expands clusters from them. This algorithm is particularly good for data which contains clusters of similar density and can find clusters of arbitrary shape.

Unlike K-means, DBSCAN does not require specifying the number of clusters in advance and can identify outliers as noise points.

This implementation has a worst case memory complexity of O(n2), which can occur when the `eps` param is large and `min_samples` is low, while the original DBSCAN only uses linear memory. For further details, see the Notes below.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
.

Parameters:

**eps**float, default=0.5

The maximum distance between two samples for one to be considered as in the neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. This is the most important DBSCAN parameter to choose appropriately for your data set and distance function. Smaller values generally lead to more clusters.

**min\_samples**int, default=5

The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself. If `min_samples` is set to a higher value, DBSCAN will find denser clusters, whereas if it is set to a lower value, the found clusters will be more sparse.

**metric**str, or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string or callable, it must be one of the options allowed by [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
 for its metric parameter. If metric is “precomputed”, X is assumed to be a distance matrix and must be square. X may be a [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
, in which case only “nonzero” elements may be considered neighbors for DBSCAN.

Added in version 0.17: metric _precomputed_ to accept precomputed sparse matrix.

**metric\_params**dict, default=None

Additional keyword arguments for the metric function.

Added in version 0.19.

**algorithm**{‘auto’, ‘ball\_tree’, ‘kd\_tree’, ‘brute’}, default=’auto’

The algorithm to be used by the NearestNeighbors module to compute pointwise distances and find nearest neighbors. ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.fit "sklearn.cluster.DBSCAN.fit")
 method. See [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 documentation for details.

**leaf\_size**int, default=30

Leaf size passed to BallTree or cKDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

**p**float, default=None

The power of the Minkowski metric to be used to calculate distance between points. If None, then `p=2` (equivalent to the Euclidean distance). When p=1, this is equivalent to Manhattan distance.

**n\_jobs**int, default=None

The number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**core\_sample\_indices\_**ndarray of shape (n\_core\_samples,)

Indices of core samples.

**components\_**ndarray of shape (n\_core\_samples, n\_features)

Copy of each core sample found by training.

**labels\_**ndarray of shape (n\_samples,)

Cluster labels for each point in the dataset given to fit(). Noisy samples are given the label -1. Non-negative integers indicate cluster membership.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")

A similar clustering at multiple values of eps. Our implementation is optimized for memory usage.

Notes

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

\>>> from sklearn.cluster import DBSCAN
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 2\], \[2, 2\], \[2, 3\],\
...               \[8, 7\], \[8, 8\], \[25, 80\]\])
\>>> clustering \= DBSCAN(eps\=3, min\_samples\=2).fit(X)
\>>> clustering.labels\_
array(\[ 0,  0,  0,  1,  1, -1\])
\>>> clustering
DBSCAN(eps=3, min\_samples=2)

Copy to clipboard

For an example, see [Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)
.

For a comparison of DBSCAN with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_dbscan.py#L393)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.fit "Link to this definition")

Perform DBSCAN clustering from features, or distance matrix.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or (n\_samples, n\_samples)

Training instances to cluster, or distances between instances if `metric='precomputed'`. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weight of each sample, such that a sample with a weight of at least `min_samples` is by itself a core sample; a sample with a negative weight may inhibit its eps-neighbor from being core. Note that weights are absolute, and default to 1.

Returns:

**self**object

Returns a fitted instance of self.

fit\_predict(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_dbscan.py#L478)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.fit_predict "Link to this definition")

Compute clusters from a data or distance matrix and predict labels.

This method fits the model and returns the cluster labels in a single step. It is equivalent to calling fit(X).labels\_.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or (n\_samples, n\_samples)

Training instances to cluster, or distances between instances if `metric='precomputed'`. If a sparse matrix is provided, it will be converted into a sparse `csr_matrix`.

**y**Ignored

Not used, present here for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weight of each sample, such that a sample with a weight of at least `min_samples` is by itself a core sample; a sample with a negative weight may inhibit its eps-neighbor from being core. Note that weights are absolute, and default to 1.

Returns:

**labels**ndarray of shape (n\_samples,)

Cluster labels. Noisy samples are given the label -1. Non-negative integers indicate cluster membership.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster._dbscan.DBSCAN")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)