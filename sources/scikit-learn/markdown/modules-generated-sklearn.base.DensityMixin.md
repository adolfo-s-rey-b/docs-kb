[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.DensityMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.DensityMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.DensityMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.DensityMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.DensityMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.DensityMixin.html)

Collapse Sidebar Expand Sidebar

DensityMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#densitymixin "Link to this heading")

======================================================================================================================================

class sklearn.base.DensityMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1069)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#sklearn.base.DensityMixin "Link to this definition")

Mixin class for all density estimators in scikit-learn.

This mixin defines the following functionality:

*   sets estimator type to `"density_estimator"` through the `estimator_type` tag;
    
*   `score` method that default that do no-op.
    

Examples

\>>> from sklearn.base import DensityMixin
\>>> class MyEstimator(DensityMixin):
...     def fit(self, X, y\=None):
...         self.is\_fitted\_ \= True
...         return self
\>>> estimator \= MyEstimator()
\>>> hasattr(estimator, "score")
True

Copy to clipboard

score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1094)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#sklearn.base.DensityMixin.score "Link to this definition")

Return the score of the model on the data `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**score**float

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)