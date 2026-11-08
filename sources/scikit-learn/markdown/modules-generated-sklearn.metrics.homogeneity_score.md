[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.homogeneity_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.homogeneity_score.html)

Collapse Sidebar Expand Sidebar

homogeneity\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#homogeneity-score "Link to this heading")

=========================================================================================================================================================

sklearn.metrics.homogeneity\_score(_labels\_true_, _labels\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L566)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "Link to this definition")

Homogeneity metric of a cluster labeling given a ground truth.

A clustering result satisfies homogeneity if all of its clusters contain only data points which are members of a single class.

This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.

This metric is not symmetric: switching `label_true` with `label_pred` will return the [`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")
 which will be different in general.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#homogeneity-completeness)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

Returns:

**homogeneity**float

Score between 0.0 and 1.0. 1.0 stands for perfectly homogeneous labeling.

See also

[`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")

Completeness metric of cluster labeling.

[`v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")

V-Measure (NMI with arithmetic mean option).

References

\[1\]

[Andrew Rosenberg and Julia Hirschberg, 2007. V-Measure: A conditional entropy-based external cluster evaluation measure](https://aclweb.org/anthology/D/D07/D07-1043.pdf)

Examples

Perfect labelings are homogeneous:

\>>> from sklearn.metrics.cluster import homogeneity\_score
\>>> homogeneity\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

Non-perfect labelings that further split classes into more clusters can be perfectly homogeneous:

\>>> print("%.6f" % homogeneity\_score(\[0, 0, 1, 1\], \[0, 0, 1, 2\]))
1.000000
\>>> print("%.6f" % homogeneity\_score(\[0, 0, 1, 1\], \[0, 1, 2, 3\]))
1.000000

Copy to clipboard

Clusters that include samples from different classes do not make for an homogeneous labeling:

\>>> print("%.6f" % homogeneity\_score(\[0, 0, 1, 1\], \[0, 1, 0, 1\]))
0.0...
\>>> print("%.6f" % homogeneity\_score(\[0, 0, 1, 1\], \[0, 0, 0, 0\]))
0.0...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

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