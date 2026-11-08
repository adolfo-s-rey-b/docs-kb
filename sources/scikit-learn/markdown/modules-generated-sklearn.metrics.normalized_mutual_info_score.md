[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)

Collapse Sidebar Expand Sidebar

normalized\_mutual\_info\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#normalized-mutual-info-score "Link to this heading")

============================================================================================================================================================================================

sklearn.metrics.normalized\_mutual\_info\_score(_labels\_true_, _labels\_pred_, _\*_, _average\_method\='arithmetic'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L1076)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "Link to this definition")

Normalized Mutual Information between two clusterings.

Normalized Mutual Information (NMI) is a normalization of the Mutual Information (MI) score to scale the results between 0 (no mutual information) and 1 (perfect correlation). In this function, mutual information is normalized by some generalized mean of `H(labels_true)` and `H(labels_pred))`, defined by the `average_method`.

This measure is not adjusted for chance. Therefore [`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
 might be preferred.

This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.

This metric is furthermore symmetric: switching `label_true` with `label_pred` will return the same score value. This can be useful to measure the agreement of two independent label assignments strategies on the same dataset when the real ground truth is not known.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mutual-info-score)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets.

**labels\_pred**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets.

**average\_method**{‘min’, ‘geometric’, ‘arithmetic’, ‘max’}, default=’arithmetic’

How to compute the normalizer in the denominator.

Added in version 0.20.

Changed in version 0.22: The default value of `average_method` changed from ‘geometric’ to ‘arithmetic’.

Returns:

**nmi**float

Score between 0.0 and 1.0 in normalized nats (based on the natural logarithm). 1.0 stands for perfectly complete labeling.

See also

[`v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")

V-Measure (NMI with arithmetic mean option).

[`adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")

Adjusted Rand Index.

[`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")

Adjusted Mutual Information (adjusted against chance).

Examples

Perfect labelings are both homogeneous and complete, hence have score 1.0:

\>>> from sklearn.metrics.cluster import normalized\_mutual\_info\_score
\>>> normalized\_mutual\_info\_score(\[0, 0, 1, 1\], \[0, 0, 1, 1\])
1.0
\>>> normalized\_mutual\_info\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

If classes members are completely split across different clusters, the assignment is totally in-complete, hence the NMI is null:

\>>> normalized\_mutual\_info\_score(\[0, 0, 0, 0\], \[0, 1, 2, 3\])
0.0

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_thumb.png)

[Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html)

Adjustment for chance in clustering performance evaluation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)