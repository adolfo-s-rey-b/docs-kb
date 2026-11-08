[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.silhouette_samples.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.silhouette_samples.html)

Collapse Sidebar Expand Sidebar

silhouette\_samples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#silhouette-samples "Link to this heading")

============================================================================================================================================================

sklearn.metrics.silhouette\_samples(_X_, _labels_, _\*_, _metric\='euclidean'_, _\*\*kwds_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_unsupervised.py#L203)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "Link to this definition")

Compute the Silhouette Coefficient for each sample.

The Silhouette Coefficient is a measure of how well samples are clustered with samples that are similar to themselves. Clustering models with a high Silhouette Coefficient are said to be dense, where samples in the same cluster are similar to each other, and well separated, where samples in different clusters are not very similar to each other.

The Silhouette Coefficient is calculated using the mean intra-cluster distance (`a`) and the mean nearest-cluster distance (`b`) for each sample. The Silhouette Coefficient for a sample is `(b - a) / max(a, b)`. Note that Silhouette Coefficient is only defined if number of labels is 2 `<= n_labels <= n_samples - 1`.

This function returns the Silhouette Coefficient for each sample.

The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_a, n\_samples\_a) if metric == “precomputed” or (n\_samples\_a, n\_features) otherwise

An array of pairwise distances between samples, or a feature array. If a sparse matrix is provided, CSR format should be favoured avoiding an additional copy.

**labels**array-like of shape (n\_samples,)

Label values for each sample.

**metric**str or callable, default=’euclidean’

The metric to use when calculating distance between instances in a feature array. If metric is a string, it must be one of the options allowed by [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
. If `X` is the distance array itself, use “precomputed” as the metric. Precomputed distance matrices must have 0 along the diagonal.

**\*\*kwds**optional keyword parameters

Any further parameters are passed directly to the distance function. If using a `scipy.spatial.distance` metric, the parameters are still metric dependent. See the scipy docs for usage examples.

Returns:

**silhouette**array-like of shape (n\_samples,)

Silhouette Coefficients for each sample.

References

\[1\]

[Peter J. Rousseeuw (1987). “Silhouettes: a Graphical Aid to the Interpretation and Validation of Cluster Analysis”. Computational and Applied Mathematics 20: 53-65.](https://www.sciencedirect.com/science/article/pii/0377042787901257)

\[2\]

[Wikipedia entry on the Silhouette Coefficient](https://en.wikipedia.org/wiki/Silhouette_(clustering))

Examples

\>>> from sklearn.metrics import silhouette\_samples
\>>> from sklearn.datasets import make\_blobs
\>>> from sklearn.cluster import KMeans
\>>> X, y \= make\_blobs(n\_samples\=50, random\_state\=42)
\>>> kmeans \= KMeans(n\_clusters\=3, random\_state\=42)
\>>> labels \= kmeans.fit\_predict(X)
\>>> silhouette\_samples(X, labels)
array(\[...\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)