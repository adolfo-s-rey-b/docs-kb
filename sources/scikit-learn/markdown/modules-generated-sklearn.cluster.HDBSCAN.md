[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.cluster.HDBSCAN.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.cluster.HDBSCAN.html)

Collapse Sidebar Expand Sidebar

HDBSCAN[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#hdbscan "Link to this heading")

==========================================================================================================================

class sklearn.cluster.HDBSCAN(_min\_cluster\_size\=5_, _min\_samples\=None_, _cluster\_selection\_epsilon\=0.0_, _max\_cluster\_size\=None_, _metric\='euclidean'_, _metric\_params\=None_, _alpha\=1.0_, _algorithm\='auto'_, _leaf\_size\=40_, _n\_jobs\=None_, _cluster\_selection\_method\='eom'_, _allow\_single\_cluster\=False_, _store\_centers\=None_, _copy\='warn'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_hdbscan/hdbscan.py#L423)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "Link to this definition")

Cluster data using hierarchical density-based clustering.

HDBSCAN - Hierarchical Density-Based Spatial Clustering of Applications with Noise. Performs [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
 over varying epsilon values and integrates the result to find a clustering that gives the best stability over epsilon. This allows HDBSCAN to find clusters of varying densities (unlike [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
), and be more robust to parameter selection. Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hdbscan)
.

Added in version 1.3.

Parameters:

**min\_cluster\_size**int, default=5

The minimum number of samples in a group for that group to be considered a cluster; groupings smaller than this size will be left as noise.

**min\_samples**int, default=None

The parameter `k` used to calculate the distance between a point `x_p` and its k-th nearest neighbor. When `None`, defaults to `min_cluster_size`.

**cluster\_selection\_epsilon**float, default=0.0

A distance threshold. Clusters below this value will be merged. See [\[5\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#r6f313792b2b7-5)
 for more information.

**max\_cluster\_size**int, default=None

A limit to the size of clusters returned by the `"eom"` cluster selection algorithm. There is no limit when `max_cluster_size=None`. Has no effect if `cluster_selection_method="leaf"`.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array.

*   If metric is a string or callable, it must be one of the options allowed by [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     for its metric parameter.
    
*   If metric is “precomputed”, X is assumed to be a distance matrix and must be square.
    

**metric\_params**dict, default=None

Arguments passed to the distance metric.

**alpha**float, default=1.0

A distance scaling parameter as used in robust single linkage. See [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#r6f313792b2b7-3)
 for more information.

**algorithm**{“auto”, “brute”, “kd\_tree”, “ball\_tree”}, default=”auto”

Exactly which algorithm to use for computing core distances; By default this is set to `"auto"` which attempts to use a [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
 tree if possible, otherwise it uses a [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
 tree. Both `"kd_tree"` and `"ball_tree"` algorithms use the [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 estimator.

If the `X` passed during `fit` is sparse or `metric` is invalid for both [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
 and [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
, then it resolves to use the `"brute"` algorithm.

**leaf\_size**int, default=40

Leaf size for trees responsible for fast nearest neighbour queries when a KDTree or a BallTree are used as core-distance algorithms. A large dataset size and small `leaf_size` may induce excessive memory usage. If you are running out of memory consider increasing the `leaf_size` parameter. Ignored for `algorithm="brute"`.

**n\_jobs**int, default=None

Number of jobs to run in parallel to calculate distances. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**cluster\_selection\_method**{“eom”, “leaf”}, default=”eom”

The method used to select clusters from the condensed tree. The standard approach for HDBSCAN\* is to use an Excess of Mass (`"eom"`) algorithm to find the most persistent clusters. Alternatively you can instead select the clusters at the leaves of the tree – this provides the most fine grained and homogeneous clusters.

**allow\_single\_cluster**bool, default=False

By default HDBSCAN\* will not produce a single cluster, setting this to True will override this and allow single cluster results in the case that you feel this is a valid result for your dataset.

**store\_centers**str, default=None

Which, if any, cluster centers to compute and store. The options are:

*   `None` which does not compute nor store any centers.
    
*   `"centroid"` which calculates the center by taking the weighted average of their positions. Note that the algorithm uses the euclidean metric and does not guarantee that the output will be an observed data point.
    
*   `"medoid"` which calculates the center by taking the point in the fitted data which minimizes the distance to all other points in the cluster. This is slower than “centroid” since it requires computing additional pairwise distances between points of the same cluster but guarantees the output is an observed data point. The medoid is also well-defined for arbitrary metrics, and does not depend on a euclidean metric.
    
*   `"both"` which computes and stores both forms of centers.
    

**copy**bool, default=False

If `copy=True` then any time an in-place modifications would be made that would overwrite data passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, a copy will first be made, guaranteeing that the original data will be unchanged. Currently, it only applies when `metric="precomputed"`, when passing a dense array or a CSR sparse matrix and when `algorithm="brute"`.

Changed in version 1.10: The default value for `copy` will change from `False` to `True` in version 1.10.

Attributes:

**labels\_**ndarray of shape (n\_samples,)

Cluster labels for each point in the dataset given to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Outliers are labeled as follows:

*   Noisy samples are given the label -1.
    
*   Samples with infinite elements (+/- np.inf) are given the label -2.
    
*   Samples with missing data are given the label -3, even if they also have infinite elements.
    

**probabilities\_**ndarray of shape (n\_samples,)

The strength with which each sample is a member of its assigned cluster.

*   Clustered samples have probabilities proportional to the degree that they persist as part of the cluster.
    
*   Noisy samples have probability zero.
    
*   Samples with infinite elements (+/- np.inf) have probability 0.
    
*   Samples with missing data have probability `np.nan`.
    

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

**centroids\_**ndarray of shape (n\_clusters, n\_features)

A collection containing the centroid of each cluster calculated under the standard euclidean metric. The centroids may fall “outside” their respective clusters if the clusters themselves are non-convex.

Note that `n_clusters` only counts non-outlier clusters. That is to say, the `-1, -2, -3` labels for the outlier clusters are excluded.

**medoids\_**ndarray of shape (n\_clusters, n\_features)

A collection containing the medoid of each cluster calculated under the whichever metric was passed to the `metric` parameter. The medoids are points in the original cluster which minimize the average distance to all other points in that cluster under the chosen metric. These can be thought of as the result of projecting the `metric`\-based centroid back onto the cluster.

Note that `n_clusters` only counts non-outlier clusters. That is to say, the `-1, -2, -3` labels for the outlier clusters are excluded.

See also

[`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")

Density-Based Spatial Clustering of Applications with Noise.

[`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")

Ordering Points To Identify the Clustering Structure.

[`Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")

Memory-efficient, online-learning algorithm.

Notes

The `min_samples` parameter includes the point itself, whereas the implementation in [scikit-learn-contrib/hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
 does not. To get the same results in both versions, the value of `min_samples` here must be 1 greater than the value used in [scikit-learn-contrib/hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
.

References

\[1\]

[Campello, R. J., Moulavi, D., & Sander, J. Density-based clustering based on hierarchical density estimates.](https://doi.org/10.1007/978-3-642-37456-2_14)

\[2\]

[Campello, R. J., Moulavi, D., Zimek, A., & Sander, J. Hierarchical density estimates for data clustering, visualization, and outlier detection.](https://doi.org/10.1145/2733381)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#id2)\
\]

[Chaudhuri, K., & Dasgupta, S. Rates of convergence for the cluster tree.](https://papers.nips.cc/paper/2010/hash/b534ba68236ba543ae44b22bd110a1d6-Abstract.html)

\[4\]

[Moulavi, D., Jaskowiak, P.A., Campello, R.J., Zimek, A. and Sander, J. Density-Based Clustering Validation.](https://epubs.siam.org/doi/pdf/10.1137/1.9781611973440.96)

\[[5](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#id1)\
\]

[Malzer, C., & Baum, M. “A Hybrid Approach To Hierarchical Density-based Cluster Selection.”](https://arxiv.org/abs/1911.02282)
.

Examples

\>>> import numpy as np
\>>> from sklearn.cluster import HDBSCAN
\>>> from sklearn.datasets import load\_digits
\>>> X, \_ \= load\_digits(return\_X\_y\=True)
\>>> hdb \= HDBSCAN(copy\=True, min\_cluster\_size\=20)
\>>> hdb.fit(X)
HDBSCAN(copy=True, min\_cluster\_size=20)
\>>> hdb.labels\_.shape \== (X.shape\[0\],)
True
\>>> np.unique(hdb.labels\_).tolist()
\[-1, 0, 1, 2, 3, 4, 5, 6, 7\]

Copy to clipboard

dbscan\_clustering(_cut\_distance_, _min\_cluster\_size\=5_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_hdbscan/hdbscan.py#L967)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.dbscan_clustering "Link to this definition")

Return clustering given by DBSCAN without border points.

Return clustering that would be equivalent to running DBSCAN\* for a particular cut\_distance (or epsilon) DBSCAN\* can be thought of as DBSCAN without the border points. As such these results may differ slightly from `cluster.DBSCAN` due to the difference in implementation over the non-core points.

This can also be thought of as a flat clustering derived from constant height cut through the single linkage tree.

This represents the result of selecting a cut value for robust single linkage clustering. The `min_cluster_size` allows the flat clustering to declare noise points (and cluster smaller than `min_cluster_size`).

Parameters:

**cut\_distance**float

The mutual reachability distance cut value to use to generate a flat clustering.

**min\_cluster\_size**int, default=5

Clusters smaller than this value with be called ‘noise’ and remain unclustered in the resulting flat clustering.

Returns:

**labels**ndarray of shape (n\_samples,)

An array of cluster labels, one per datapoint. Outliers are labeled as follows:

*   Noisy samples are given the label -1.
    
*   Samples with infinite elements (+/- np.inf) are given the label -2.
    
*   Samples with missing data are given the label -3, even if they also have infinite elements.
    

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_hdbscan/hdbscan.py#L697)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.fit "Link to this definition")

Find clusters based on hierarchical density-based clustering.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or ndarray of shape (n\_samples, n\_samples)

A feature array, or array of distances between samples if `metric='precomputed'`.

**y**None

Ignored.

Returns:

**self**object

Returns self.

fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/cluster/_hdbscan/hdbscan.py#L902)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.fit_predict "Link to this definition")

Cluster X and return the associated cluster labels.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features), or ndarray of shape (n\_samples, n\_samples)

A feature array, or array of distances between samples if `metric='precomputed'`.

**y**None

Ignored.

Returns:

**y**ndarray of shape (n\_samples,)

Cluster labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)