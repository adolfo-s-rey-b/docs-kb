[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.fowlkes_mallows_score.html)

Collapse Sidebar Expand Sidebar

fowlkes\_mallows\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#fowlkes-mallows-score "Link to this heading")

======================================================================================================================================================================

sklearn.metrics.fowlkes\_mallows\_score(_labels\_true_, _labels\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L1188)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "Link to this definition")

Measure the similarity of two clusterings of a set of points.

Added in version 0.18.

The Fowlkes-Mallows index (FMI) is defined as the geometric mean of the precision and recall:

FMI \= TP / sqrt((TP + FP) \* (TP + FN))

Copy to clipboard

Where `TP` is the number of **True Positive** (i.e. the number of pairs of points that belong to the same cluster in both `labels_true` and `labels_pred`), `FP` is the number of **False Positive** (i.e. the number of pairs of points that belong to the same cluster in `labels_pred` but not in `labels_true`) and `FN` is the number of **False Negative** (i.e. the number of pairs of points that belong to the same cluster in `labels_true` but not in `labels_pred`).

The score ranges from 0 to 1. A high value indicates a good similarity between two clusters.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#fowlkes-mallows-scores)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets.

**labels\_pred**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets.

Returns:

**score**float

The resulting Fowlkes-Mallows score.

References

\[1\]

[E. B. Fowkles and C. L. Mallows, 1983. “A method for comparing two hierarchical clusterings”. Journal of the American Statistical Association](https://www.tandfonline.com/doi/abs/10.1080/01621459.1983.10478008)

\[2\]

[Wikipedia entry for the Fowlkes-Mallows Index](https://en.wikipedia.org/wiki/Fowlkes-Mallows_index)

Examples

Perfect labelings are both homogeneous and complete, hence have score 1.0:

\>>> from sklearn.metrics.cluster import fowlkes\_mallows\_score
\>>> fowlkes\_mallows\_score(\[0, 0, 1, 1\], \[0, 0, 1, 1\])
1.0
\>>> fowlkes\_mallows\_score(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
1.0

Copy to clipboard

If classes members are completely split across different clusters, the assignment is totally random, hence the FMI is null:

\>>> fowlkes\_mallows\_score(\[0, 0, 0, 0\], \[0, 1, 2, 3\])
0.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)