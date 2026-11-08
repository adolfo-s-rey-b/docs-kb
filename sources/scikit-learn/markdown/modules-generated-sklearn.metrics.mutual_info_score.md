[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

mutual\_info\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#mutual-info-score "Link to this heading")

==========================================================================================================================================================

sklearn.metrics.mutual\_info\_score(_labels\_true_, _labels\_pred_, _\*_, _contingency\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L822)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "Link to this definition")

Mutual Information between two clusterings.

The Mutual Information is a measure of the similarity between two labels of the same data. Where |Ui| is the number of the samples in cluster Ui and |Vj| is the number of the samples in cluster Vj, the Mutual Information between clusterings U and V is given as:

MI(U,V)\=∑i\=1|U|∑j\=1|V||Ui∩Vj|Nlog⁡N|Ui∩Vj||Ui||Vj|

This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.

This metric is furthermore symmetric: switching U (i.e `label_true`) with V (i.e. `label_pred`) will return the same score value. This can be useful to measure the agreement of two independent label assignments strategies on the same dataset when the real ground truth is not known.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#mutual-info-score)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets, called U in the above formula.

**labels\_pred**array-like of shape (n\_samples,)

A clustering of the data into disjoint subsets, called V in the above formula.

**contingency**{array-like, sparse matrix} of shape (n\_classes\_true, n\_classes\_pred), default=None

A contingency matrix given by the [`contingency_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#sklearn.metrics.cluster.contingency_matrix "sklearn.metrics.cluster.contingency_matrix")
 function. If value is `None`, it will be computed, otherwise the given value is used, with `labels_true` and `labels_pred` ignored.

Returns:

**mi**float

Mutual information, a non-negative value, measured in nats using the natural logarithm.

See also

[`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")

Adjusted against chance Mutual Information.

[`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")

Normalized Mutual Information.

Notes

The logarithm used is the natural logarithm (base-e).

Examples

\>>> from sklearn.metrics import mutual\_info\_score
\>>> labels\_true \= \[0, 1, 1, 0, 1, 0\]
\>>> labels\_pred \= \[0, 1, 0, 0, 1, 1\]
\>>> mutual\_info\_score(labels\_true, labels\_pred)
0.0566

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

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