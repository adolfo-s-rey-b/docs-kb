[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.davies_bouldin_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.davies_bouldin_score.html)

Collapse Sidebar Expand Sidebar

davies\_bouldin\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#davies-bouldin-score "Link to this heading")

===================================================================================================================================================================

sklearn.metrics.davies\_bouldin\_score(_X_, _labels_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_unsupervised.py#L406)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#sklearn.metrics.davies_bouldin_score "Link to this definition")

Compute the Davies-Bouldin score.

The score is defined as the average similarity measure of each cluster with its most similar cluster, where similarity is the ratio of within-cluster distances to between-cluster distances. Thus, clusters which are farther apart and less dispersed will result in a better score.

The minimum score is zero, with lower values indicating better clustering.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#davies-bouldin-index)
.

Added in version 0.20.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

A list of `n_features`\-dimensional data points. Each row corresponds to a single data point.

**labels**array-like of shape (n\_samples,)

Predicted labels for each sample.

Returns:

score: float

The resulting Davies-Bouldin score.

References

\[1\]

Davies, David L.; Bouldin, Donald W. (1979). [“A Cluster Separation Measure”](https://ieeexplore.ieee.org/document/4766909)
. IEEE Transactions on Pattern Analysis and Machine Intelligence. PAMI-1 (2): 224-227

Examples

\>>> from sklearn.metrics import davies\_bouldin\_score
\>>> X \= \[\[0, 1\], \[1, 1\], \[3, 4\]\]
\>>> labels \= \[0, 0, 1\]
\>>> davies\_bouldin\_score(X, labels)
0.12...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)