[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html)

Collapse Sidebar Expand Sidebar

adjusted\_mutual\_info\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#adjusted-mutual-info-score "Link to this heading")

======================================================================================================================================================================================

sklearn.metrics.adjusted\_mutual\_info\_score(_labels\_true_, _labels\_pred_, _\*_, _average\_method\='arithmetic'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L938)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "Link to this definition")

Adjusted Mutual Information between two clusterings.

Adjusted Mutual Information (AMI) is an adjustment of the Mutual Information (MI) score to account for chance. It accounts for the fact that the MI is generally higher for two clusterings with a larger number of clusters, regardless of whether there is actually more information shared. For two clusterings U and V, the AMI is given as:

AMI(U, V) \= \[MI(U, V) \- E(MI(U, V))\] / \[avg(H(U), H(V)) \- E(MI(U, V))\]

Copy to clipboard

This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.

This metric is furthermore symmetric: switching U (`label_true`) with V (`labels_pred`) will return the same score value. This can be useful to measure the agreement of two independent label assignments strategies on the same dataset when the real ground truth is not known.

Be mindful that this function is an order of magnitude slower than other metrics, such as the Adjusted Rand Index.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mutual-info-score)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets, called U in the above formula.

**labels\_pred**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets, called V in the above formula.

**average\_method**{‘min’, ‘geometric’, ‘arithmetic’, ‘max’}, default=’arithmetic’

How to compute the normalizer in the denominator.

Added in version 0.20.

Changed in version 0.22: The default value of `average_method` changed from ‘max’ to ‘arithmetic’.

Returns:

ami: float (upperlimited by 1.0)

The AMI returns a value of 1 when the two partitions are identical (ie perfectly matched). Random partitions (independent labellings) have an expected AMI around 0 on average hence can be negative. The value is in adjusted nats (based on the natural logarithm).

See also

[`adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")

Adjusted Rand Index.

[`mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")

Mutual Information (not adjusted for chance).

References

\[1\]

[Vinh, Epps, and Bailey, (2010). Information Theoretic Measures for Clusterings Comparison: Variants, Properties, Normalization and Correction for Chance, JMLR](http://jmlr.csail.mit.edu/papers/volume11/vinh10a/vinh10a.pdf)

\[2\]

[Wikipedia entry for the Adjusted Mutual Information](https://en.wikipedia.org/wiki/Adjusted_Mutual_Information)

Examples

Perfect labelings are both homogeneous and complete, hence have score 1.0:

\>>> from sklearn.metrics.cluster import adjusted\_mutual\_info\_score
\>>> adjusted\_mutual\_info\_score(\[0, 0, 1, 1\], \[0, 0, 1, 1\])
1.0
\>>> adjusted\_mutual\_info\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

If classes members are completely split across different clusters, the assignment is totally in-complete, hence the AMI is null:

\>>> adjusted\_mutual\_info\_score(\[0, 0, 0, 0\], \[0, 1, 2, 3\])
0.0

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)