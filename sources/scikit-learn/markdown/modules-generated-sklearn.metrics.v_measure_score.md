[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

v\_measure\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#v-measure-score "Link to this heading")

====================================================================================================================================================

sklearn.metrics.v\_measure\_score(_labels\_true_, _labels\_pred_, _\*_, _beta\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L718)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "Link to this definition")

V-measure cluster labeling given a ground truth.

This score is identical to [`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
 with the `'arithmetic'` option for averaging.

The V-measure is the harmonic mean between homogeneity and completeness:

v \= (1 + beta) \* homogeneity \* completeness
     / (beta \* homogeneity + completeness)

Copy to clipboard

This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.

This metric is furthermore symmetric: switching `label_true` with `label_pred` will return the same score value. This can be useful to measure the agreement of two independent label assignments strategies on the same dataset when the real ground truth is not known.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#homogeneity-completeness)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

**beta**float, default=1.0

Ratio of weight attributed to `homogeneity` vs `completeness`. If `beta` is greater than 1, `completeness` is weighted more strongly in the calculation. If `beta` is less than 1, `homogeneity` is weighted more strongly.

Returns:

**v\_measure**float

Score between 0.0 and 1.0. 1.0 stands for perfectly complete labeling.

See also

[`homogeneity_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")

Homogeneity metric of cluster labeling.

[`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")

Completeness metric of cluster labeling.

[`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")

Normalized Mutual Information.

References

\[1\]

[Andrew Rosenberg and Julia Hirschberg, 2007. V-Measure: A conditional entropy-based external cluster evaluation measure](https://aclweb.org/anthology/D/D07/D07-1043.pdf)

Examples

Perfect labelings are both homogeneous and complete, hence have score 1.0:

\>>> from sklearn.metrics.cluster import v\_measure\_score
\>>> v\_measure\_score(\[0, 0, 1, 1\], \[0, 0, 1, 1\])
1.0
\>>> v\_measure\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

Labelings that assign all classes members to the same clusters are complete but not homogeneous, hence penalized:

\>>> print("%.6f" % v\_measure\_score(\[0, 0, 1, 2\], \[0, 0, 1, 1\]))
0.8
\>>> print("%.6f" % v\_measure\_score(\[0, 1, 2, 3\], \[0, 0, 1, 1\]))
0.67

Copy to clipboard

Labelings that have pure clusters with members coming from the same classes are homogeneous but un-necessary splits harm completeness and thus penalize V-measure as well:

\>>> print("%.6f" % v\_measure\_score(\[0, 0, 1, 1\], \[0, 0, 1, 2\]))
0.8
\>>> print("%.6f" % v\_measure\_score(\[0, 0, 1, 1\], \[0, 1, 2, 3\]))
0.67

Copy to clipboard

If classes members are completely split across different clusters, the assignment is totally incomplete, hence the V-Measure is null:

\>>> print("%.6f" % v\_measure\_score(\[0, 0, 0, 0\], \[0, 1, 2, 3\]))
0.0

Copy to clipboard

Clusters that include samples from totally different classes totally destroy the homogeneity of the labeling, hence:

\>>> print("%.6f" % v\_measure\_score(\[0, 0, 1, 1\], \[0, 0, 0, 0\]))
0.0

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

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

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

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