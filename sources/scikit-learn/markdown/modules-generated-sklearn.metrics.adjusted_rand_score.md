[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.adjusted_rand_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.adjusted_rand_score.html)

Collapse Sidebar Expand Sidebar

adjusted\_rand\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#adjusted-rand-score "Link to this heading")

================================================================================================================================================================

sklearn.metrics.adjusted\_rand\_score(_labels\_true_, _labels\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L353)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "Link to this definition")

Rand index adjusted for chance.

The Rand Index computes a similarity measure between two clusterings by considering all pairs of samples and counting pairs that are assigned in the same or different clusters in the predicted and true clusterings.

The raw RI score is then “adjusted for chance” into the ARI score using the following scheme:

ARI \= (RI \- Expected\_RI) / (max(RI) \- Expected\_RI)

Copy to clipboard

The adjusted Rand index is thus ensured to have a value close to 0.0 for random labeling independently of the number of clusters and samples and exactly 1.0 when the clusterings are identical (up to a permutation). The adjusted Rand index is bounded below by -0.5 for especially discordant clusterings.

ARI is a symmetric measure:

adjusted\_rand\_score(a, b) \== adjusted\_rand\_score(b, a)

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#adjusted-rand-score)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

Returns:

**ARI**float

Similarity score between -0.5 and 1.0. Random labelings have an ARI close to 0.0. 1.0 stands for perfect match.

See also

[`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")

Adjusted Mutual Information.

References

\[Hubert1985\]

L. Hubert and P. Arabie, Comparing Partitions, Journal of Classification 1985 [https://link.springer.com/article/10.1007%2FBF01908075](https://link.springer.com/article/10.1007%2FBF01908075)

\[Steinley2004\]

D. Steinley, Properties of the Hubert-Arabie adjusted Rand index, Psychological Methods 2004

\[wk\]

[https://en.wikipedia.org/wiki/Rand\_index#Adjusted\_Rand\_index](https://en.wikipedia.org/wiki/Rand_index#Adjusted_Rand_index)

\[Chacon\]

[Minimum adjusted Rand index for two clusterings of a given size, 2022, J. E. Chacón and A. I. Rastrojo](https://doi.org/10.1007/s11634-022-00491-w)

Examples

Perfectly matching labelings have a score of 1 even

\>>> from sklearn.metrics.cluster import adjusted\_rand\_score
\>>> adjusted\_rand\_score(\[0, 0, 1, 1\], \[0, 0, 1, 1\])
1.0
\>>> adjusted\_rand\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

Labelings that assign all classes members to the same clusters are complete but may not always be pure, hence penalized:

\>>> adjusted\_rand\_score(\[0, 0, 1, 2\], \[0, 0, 1, 1\])
0.57

Copy to clipboard

ARI is symmetric, so labelings that have pure clusters with members coming from the same classes but unnecessary splits are penalized:

\>>> adjusted\_rand\_score(\[0, 0, 1, 1\], \[0, 0, 1, 2\])
0.57

Copy to clipboard

If classes members are completely split across different clusters, the assignment is totally incomplete, hence the ARI is very low:

\>>> adjusted\_rand\_score(\[0, 0, 0, 0\], \[0, 1, 2, 3\])
0.0

Copy to clipboard

ARI may take a negative value for especially discordant labelings that are a worse choice than the expected value of random labels:

\>>> adjusted\_rand\_score(\[0, 0, 1, 1\], \[0, 1, 0, 1\])
\-0.5

Copy to clipboard

See [Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#sphx-glr-auto-examples-cluster-plot-adjusted-for-chance-measures-py)
 for a more detailed example.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_thumb.png)

[Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html)

Adjustment for chance in clustering performance evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)

[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)

Demo of affinity propagation clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

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