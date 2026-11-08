[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.AgglomerativeClustering.html)

Collapse Sidebar Expand Sidebar

AgglomerativeClustering[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#agglomerativeclustering "Link to this heading")

==========================================================================================================================================================================

class sklearn.cluster.AgglomerativeClustering(_n\_clusters\=2_, _\*_, _metric\='euclidean'_, _memory\=None_, _connectivity\=None_, _compute\_full\_tree\='auto'_, _linkage\='ward'_, _distance\_threshold\=None_, _compute\_distances\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L780)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "Link to this definition")

Agglomerative Clustering.

Recursively merges pair of clusters of sample data; uses linkage distance.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
.

Parameters:

**n\_clusters**int or None, default=2

The number of clusters to find. It must be `None` if `distance_threshold` is not `None`.

**metric**str or callable, default=”euclidean”

Metric used to compute the linkage. Can be “euclidean”, “l1”, “l2”, “manhattan”, “cosine”, or “precomputed”. If linkage is “ward”, only “euclidean” and “l2” are accepted. If “precomputed”, a distance matrix is needed as input for the fit method. If connectivity is None, linkage is “single” and metric is not “precomputed” any valid pairwise distance metric can be assigned.

For an example of agglomerative clustering with different metrics, see [Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html#sphx-glr-auto-examples-cluster-plot-agglomerative-clustering-metrics-py)
.

Added in version 1.2.

**memory**str or object with the joblib.Memory interface, default=None

Used to cache the output of the computation of the tree. By default, no caching is done. If a string is given, it is the path to the caching directory.

**connectivity**array-like, sparse matrix, or callable, default=None

Connectivity matrix. Defines for each sample the neighboring samples following a given structure of the data. This can be a connectivity matrix itself or a callable that transforms the data into a connectivity matrix, such as derived from `kneighbors_graph`. Default is `None`, i.e, the hierarchical clustering algorithm is unstructured.

For an example of connectivity matrix using [`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
, see [Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#sphx-glr-auto-examples-cluster-plot-ward-structured-vs-unstructured-py)
.

**compute\_full\_tree**‘auto’ or bool, default=’auto’

Stop early the construction of the tree at `n_clusters`. This is useful to decrease computation time if the number of clusters is not small compared to the number of samples. This option is useful only when specifying a connectivity matrix. Note also that when varying the number of clusters and using caching, it may be advantageous to compute the full tree. It must be `True` if `distance_threshold` is not `None`. By default `compute_full_tree` is “auto”, which is equivalent to `True` when `distance_threshold` is not `None` or that `n_clusters` is inferior to the maximum between 100 or `0.02 * n_samples`. Otherwise, “auto” is equivalent to `False`.

**linkage**{‘ward’, ‘complete’, ‘average’, ‘single’}, default=’ward’

Which linkage criterion to use. The linkage criterion determines which distance to use between sets of observation. The algorithm will merge the pairs of cluster that minimize this criterion.

*   ‘ward’ minimizes the variance of the clusters being merged.
    
*   ‘average’ uses the average of the distances of each observation of the two sets.
    
*   ‘complete’ or ‘maximum’ linkage uses the maximum distances between all observations of the two sets.
    
*   ‘single’ uses the minimum of the distances between all observations of the two sets.
    

Added in version 0.20: Added the ‘single’ option

For examples comparing different `linkage` criteria, see [Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html#sphx-glr-auto-examples-cluster-plot-linkage-comparison-py)
.

**distance\_threshold**float, default=None

The linkage distance threshold at or above which clusters will not be merged. If not `None`, `n_clusters` must be `None` and `compute_full_tree` must be `True`.

Added in version 0.21.

**compute\_distances**bool, default=False

Computes distances between clusters even if `distance_threshold` is not used. This can be used to make dendrogram visualization, but introduces a computational and memory overhead.

Added in version 0.24.

For an example of dendrogram visualization, see [Plot Hierarchical Clustering Dendrogram](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html#sphx-glr-auto-examples-cluster-plot-agglomerative-dendrogram-py)
.

Attributes:

**n\_clusters\_**int

The number of clusters found by the algorithm. If `distance_threshold=None`, it will be equal to the given `n_clusters`.

**labels\_**ndarray of shape (n\_samples)

Cluster labels for each point.

**n\_leaves\_**int

Number of leaves in the hierarchical tree.

**n\_connected\_components\_**int

The estimated number of connected components in the graph.

Added in version 0.21: `n_connected_components_` was added to replace `n_components_`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**children\_**array-like of shape (n\_samples-1, 2)

The children of each non-leaf node. Values less than `n_samples` correspond to leaves of the tree which are the original samples. A node `i` greater than or equal to `n_samples` is a non-leaf node and has children `children_[i - n_samples]`. Alternatively at the i-th iteration, children\[i\]\[0\] and children\[i\]\[1\] are merged to form node `n_samples + i`.

**distances\_**array-like of shape (n\_nodes-1,)

Distances between nodes in the corresponding place in `children_`. Only computed if `distance_threshold` is used or `compute_distances` is set to `True`.

See also

[`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")

Agglomerative clustering but for features instead of samples.

[`ward_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "sklearn.cluster.ward_tree")

Hierarchical clustering with ward linkage.

Examples

\>>> from sklearn.cluster import AgglomerativeClustering
\>>> import numpy as np
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\],\
...               \[4, 2\], \[4, 4\], \[4, 0\]\])
\>>> clustering \= AgglomerativeClustering().fit(X)
\>>> clustering
AgglomerativeClustering()
\>>> clustering.labels\_
array(\[1, 1, 1, 0, 0, 0\])

Copy to clipboard

For a comparison of Agglomerative clustering with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L972)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering.fit "Link to this definition")

Fit the hierarchical clustering from features, or distance matrix.

Parameters:

**X**array-like, shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training instances to cluster, or distances between instances if `metric='precomputed'`.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**self**object

Returns the fitted instance.

fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_agglomerative.py#L1096)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering.fit_predict "Link to this definition")

Fit and return the result of each sample’s clustering assignment.

In addition to fitting, this method also return the result of the clustering assignment for each sample in the training set.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training instances to cluster, or distances between instances if `metric='precomputed'`.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**labels**ndarray of shape (n\_samples,)

Cluster labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_dendrogram_thumb.png)

[Plot Hierarchical Clustering Dendrogram](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html)

Plot Hierarchical Clustering Dendrogram

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)