[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.cluster.contingency_matrix.html)

Collapse Sidebar Expand Sidebar

contingency\_matrix[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#contingency-matrix "Link to this heading")

====================================================================================================================================================================

sklearn.metrics.cluster.contingency\_matrix(_labels\_true_, _labels\_pred_, _\*_, _eps\=None_, _sparse\=False_, _dtype\=<class 'numpy.int64'>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L96)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#sklearn.metrics.cluster.contingency_matrix "Link to this definition")

Build a contingency matrix describing the relationship between labels.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#contingency-matrix)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

**eps**float, default=None

If a float, that value is added to all values in the contingency matrix. This helps to stop NaN propagation. If `None`, nothing is adjusted.

**sparse**bool, default=False

If `True`, return a sparse CSR contingency matrix. If `eps` is not `None` and `sparse` is `True` will raise ValueError.

Added in version 0.18.

**dtype**numeric type, default=np.int64

Output dtype. Ignored if `eps` is not `None`.

Added in version 0.24.

Returns:

**contingency**{array-like, sparse}, shape=\[n\_classes\_true, n\_classes\_pred\]

Matrix C such that Ci,j is the number of samples in true class i and in predicted class j. If `eps is None`, the dtype of this array will be integer unless set otherwise with the `dtype` argument. If `eps` is given, the dtype will be float. If `sparse=True` will be a sparse CSR contingency.

Examples

\>>> from sklearn.metrics.cluster import contingency\_matrix
\>>> labels\_true \= \[0, 0, 1, 1, 2, 2\]
\>>> labels\_pred \= \[1, 0, 2, 1, 0, 2\]
\>>> contingency\_matrix(labels\_true, labels\_pred)
array(\[\[1, 1, 0\],\
       \[0, 1, 1\],\
       \[1, 0, 1\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)