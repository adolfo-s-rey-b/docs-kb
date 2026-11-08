[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.ClusterMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.ClusterMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.ClusterMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.ClusterMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.ClusterMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.ClusterMixin.html)

Collapse Sidebar Expand Sidebar

ClusterMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#clustermixin "Link to this heading")

======================================================================================================================================

class sklearn.base.ClusterMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L719)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin "Link to this definition")

Mixin class for all cluster estimators in scikit-learn.

*   set estimator type to `"clusterer"` through the `estimator_type` tag;
    
*   `fit_predict` method returning the cluster labels associated to each sample.
    

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, ClusterMixin
\>>> class MyClusterer(ClusterMixin, BaseEstimator):
...     def fit(self, X, y\=None):
...         self.labels\_ \= np.ones(shape\=(len(X),), dtype\=np.int64)
...         return self
\>>> X \= \[\[1, 2\], \[2, 3\], \[3, 4\]\]
\>>> MyClusterer().fit\_predict(X)
array(\[1, 1, 1\])

Copy to clipboard

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L745)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin.fit_predict "Link to this definition")

Perform clustering on `X` and returns cluster labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**labels**ndarray of shape (n\_samples,), dtype=np.int64

Cluster labels.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)