[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.rand_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.rand_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.rand_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.rand_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.rand_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.rand_score.html)

Collapse Sidebar Expand Sidebar

rand\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#rand-score "Link to this heading")

====================================================================================================================================

sklearn.metrics.rand\_score(_labels\_true_, _labels\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L273)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "Link to this definition")

Rand index.

The Rand Index computes a similarity measure between two clusterings by considering all pairs of samples and counting pairs that are assigned in the same or different clusters in the predicted and true clusterings [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#rbedd61930922-1)
 [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#rbedd61930922-2)
.

The raw RI score [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#rbedd61930922-3)
 is:

RI = (number of agreeing pairs) / (number of pairs)

Copy to clipboard

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#rand-score)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

Returns:

**RI**float

Similarity score between 0.0 and 1.0, inclusive, 1.0 stands for perfect match.

See also

[`adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")

Adjusted Rand Score.

[`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")

Adjusted Mutual Information.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#id1)\
\]

[Hubert, L., Arabie, P. “Comparing partitions.” Journal of Classification 2, 193–218 (1985).](https://doi.org/10.1007/BF01908075)
.

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#id2)\
\]

[Wikipedia: Simple Matching Coefficient](https://en.wikipedia.org/wiki/Simple_matching_coefficient)

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#id3)\
\]

[Wikipedia: Rand Index](https://en.wikipedia.org/wiki/Rand_index)

Examples

Perfectly matching labelings have a score of 1 even

\>>> from sklearn.metrics.cluster import rand\_score
\>>> rand\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

Labelings that assign all classes members to the same clusters are complete but may not always be pure, hence penalized:

\>>> rand\_score(\[0, 0, 1, 2\], \[0, 0, 1, 1\])
0.83

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

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