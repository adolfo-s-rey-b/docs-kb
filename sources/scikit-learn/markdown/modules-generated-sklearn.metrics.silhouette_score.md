[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.silhouette_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.silhouette_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.silhouette_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.silhouette_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.silhouette_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.silhouette_score.html)

Collapse Sidebar Expand Sidebar

silhouette\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#silhouette-score "Link to this heading")

======================================================================================================================================================

sklearn.metrics.silhouette\_score(_X_, _labels_, _\*_, _metric\='euclidean'_, _sample\_size\=None_, _random\_state\=None_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_unsupervised.py#L49)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "Link to this definition")

Compute the mean Silhouette Coefficient of all samples.

The Silhouette Coefficient is calculated using the mean intra-cluster distance (`a`) and the mean nearest-cluster distance (`b`) for each sample. The Silhouette Coefficient for a sample is `(b - a) / max(a, b)`. To clarify, `b` is the distance between a sample and the nearest cluster that the sample is not a part of. Note that Silhouette Coefficient is only defined if number of labels is `2 <= n_labels <= n_samples - 1`.

This function returns the mean Silhouette Coefficient over all samples. To obtain the values for each sample, use [`silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
.

The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_a, n\_samples\_a) if metric == “precomputed” or (n\_samples\_a, n\_features) otherwise

An array of pairwise distances between samples, or a feature array.

**labels**array-like of shape (n\_samples,)

Predicted labels for each sample.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. If `X` is the distance array itself, use `metric="precomputed"`.

**sample\_size**int, default=None

The size of the sample to use when computing the Silhouette Coefficient on a random subset of the data. If `sample_size is None`, no sampling is used.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for selecting a subset of samples. Used when `sample_size is not None`. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**\*\*kwds**optional keyword parameters

Any further parameters are passed directly to the distance function. If using a scipy.spatial.distance metric, the parameters are still metric dependent. See the scipy docs for usage examples.

Returns:

**silhouette**float

Mean Silhouette Coefficient for all samples.

References

\[1\]

[Peter J. Rousseeuw (1987). “Silhouettes: a Graphical Aid to the Interpretation and Validation of Cluster Analysis”. Computational and Applied Mathematics 20: 53-65.](https://www.sciencedirect.com/science/article/pii/0377042787901257)

\[2\]

[Wikipedia entry on the Silhouette Coefficient](https://en.wikipedia.org/wiki/Silhouette_(clustering))

Examples

\>>> from sklearn.datasets import make\_blobs
\>>> from sklearn.cluster import KMeans
\>>> from sklearn.metrics import silhouette\_score
\>>> X, y \= make\_blobs(random\_state\=42)
\>>> kmeans \= KMeans(n\_clusters\=2, random\_state\=42)
\>>> silhouette\_score(X, kmeans.fit\_predict(X))
0.49...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)

[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)

Demo of affinity propagation clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)