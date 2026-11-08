[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html)

Collapse Sidebar Expand Sidebar

pair\_confusion\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#pair-confusion-matrix "Link to this heading")

==============================================================================================================================================================================

sklearn.metrics.cluster.pair\_confusion\_matrix(_labels\_true_, _labels\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L188)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#sklearn.metrics.cluster.pair_confusion_matrix "Link to this definition")

Pair confusion matrix arising from two clusterings.

The pair confusion matrix C computes a 2 by 2 similarity matrix between two clusterings by considering all pairs of samples and counting pairs that are assigned into the same or into different clusters under the true and predicted clusterings [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#r9ca8fd06d29a-1)
.

Considering a pair of samples that is clustered together a positive pair, then as in binary classification the count of true negatives is C00, false negatives is C10, true positives is C11 and false positives is C01.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#pair-confusion-matrix)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

Returns:

**C**ndarray of shape (2, 2), dtype=np.int64

The contingency matrix.

See also

[`sklearn.metrics.rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "sklearn.metrics.rand_score")

Rand Score.

[`sklearn.metrics.adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")

Adjusted Rand Score.

[`sklearn.metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")

Adjusted Mutual Information.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#id1)\
\]

[Hubert, L., Arabie, P. “Comparing partitions.” Journal of Classification 2, 193–218 (1985).](https://doi.org/10.1007/BF01908075)

Examples

Perfectly matching labelings have all non-zero entries on the diagonal regardless of actual label values:

\>>> from sklearn.metrics.cluster import pair\_confusion\_matrix
\>>> pair\_confusion\_matrix(\[0, 0, 1, 1\], \[1, 1, 0, 0\])
array(\[\[8, 0\],\
       \[0, 4\]\]...

Copy to clipboard

Labelings that assign all classes members to the same clusters are complete but may be not always pure, hence penalized, and have some off-diagonal non-zero entries:

\>>> pair\_confusion\_matrix(\[0, 0, 1, 2\], \[0, 0, 1, 1\])
array(\[\[8, 2\],\
       \[0, 2\]\]...

Copy to clipboard

Note that the matrix is not symmetric.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)