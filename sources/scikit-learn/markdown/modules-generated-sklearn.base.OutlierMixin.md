[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.OutlierMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.OutlierMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.OutlierMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.OutlierMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.OutlierMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.OutlierMixin.html)

Collapse Sidebar Expand Sidebar

OutlierMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#outliermixin "Link to this heading")

======================================================================================================================================

class sklearn.base.OutlierMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1112)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "Link to this definition")

Mixin class for all outlier detection estimators in scikit-learn.

This mixin defines the following functionality:

*   set estimator type to `"outlier_detector"` through the `estimator_type` tag;
    
*   `fit_predict` method that default to `fit` and `predict`.
    

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, OutlierMixin
\>>> class MyEstimator(OutlierMixin):
...     def fit(self, X, y\=None):
...         self.is\_fitted\_ \= True
...         return self
...     def predict(self, X):
...         return np.ones(shape\=len(X))
\>>> estimator \= MyEstimator()
\>>> X \= np.array(\[\[1, 2\], \[2, 3\], \[3, 4\]\])
\>>> estimator.fit\_predict(X)
array(\[1., 1., 1.\])

Copy to clipboard

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1141)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin.fit_predict "Link to this definition")

Perform fit on X and returns labels for X.

Returns -1 for outliers and 1 for inliers.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**y**ndarray of shape (n\_samples,)

1 for inliers, -1 for outliers.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)