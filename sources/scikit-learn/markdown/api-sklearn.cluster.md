[Skip to main content](https://scikit-learn.org/stable/api/sklearn.cluster.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.cluster.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.cluster.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.cluster.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.cluster.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.cluster.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.cluster.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.cluster.html)

Collapse Sidebar Expand Sidebar

sklearn.cluster[#](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "Link to this heading")

===========================================================================================================================

Popular unsupervised clustering algorithms.

**User guide.** See the [Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering)
 and [Biclustering](https://scikit-learn.org/stable/modules/biclustering.html#biclustering)
 sections for further details.

|     |     |
| --- | --- |
| [`AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation") | Perform Affinity Propagation Clustering of data. |
| [`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering") | Agglomerative Clustering. |
| [`Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch") | Implements the BIRCH clustering algorithm. |
| [`BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans") | Bisecting K-Means clustering. |
| [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN") | Perform DBSCAN clustering from vector array or distance matrix. |
| [`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration") | Agglomerate features. |
| [`HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN") | Cluster data using hierarchical density-based clustering. |
| [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans") | K-Means clustering. |
| [`MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift") | Mean shift clustering using a flat kernel. |
| [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans") | Mini-Batch K-Means clustering. |
| [`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS") | Estimate clustering structure from vector array. |
| [`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering") | Spectral biclustering (Kluger, 2003) [\[R2af9f5762274-1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#r2af9f5762274-1)<br>. |
| [`SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering") | Apply clustering to a projection of the normalized Laplacian. |
| [`SpectralCoclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering") | Spectral Co-Clustering algorithm (Dhillon, 2001) [\[R0dd0f3306ba7-1\]](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#r0dd0f3306ba7-1)<br>. |
| [`affinity_propagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#sklearn.cluster.affinity_propagation "sklearn.cluster.affinity_propagation") | Perform Affinity Propagation Clustering of data. |
| [`cluster_optics_dbscan`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "sklearn.cluster.cluster_optics_dbscan") | Perform DBSCAN extraction for an arbitrary epsilon. |
| [`cluster_optics_xi`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html#sklearn.cluster.cluster_optics_xi "sklearn.cluster.cluster_optics_xi") | Automatically extract clusters according to the Xi-steep method. |
| [`compute_optics_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#sklearn.cluster.compute_optics_graph "sklearn.cluster.compute_optics_graph") | Compute the OPTICS reachability graph. |
| [`dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan") | Perform DBSCAN clustering from vector array or distance matrix. |
| [`estimate_bandwidth`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "sklearn.cluster.estimate_bandwidth") | Estimate the bandwidth to use with the mean-shift algorithm. |
| [`k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means") | Perform K-means clustering algorithm. |
| [`kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus") | Init n\_clusters seeds according to k-means++. |
| [`mean_shift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#sklearn.cluster.mean_shift "sklearn.cluster.mean_shift") | Perform mean shift clustering of data using a flat kernel. |
| [`spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering") | Apply clustering to a projection of the normalized Laplacian. |
| [`ward_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "sklearn.cluster.ward_tree") | Ward clustering based on a Feature matrix. |