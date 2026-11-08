[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.MetaEstimatorMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.MetaEstimatorMixin.html)

Collapse Sidebar Expand Sidebar

MetaEstimatorMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#metaestimatormixin "Link to this heading")

========================================================================================================================================================

class sklearn.base.MetaEstimatorMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1194)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "Link to this definition")

Mixin class for all meta estimators in scikit-learn.

This mixin is empty, and only exists to indicate that the estimator is a meta-estimator.

Changed in version 1.6: The `_required_parameters` is now removed and is unnecessary since tests are refactored and don’t use this anymore.

Examples

\>>> from sklearn.base import MetaEstimatorMixin
\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.linear\_model import LogisticRegression
\>>> class MyEstimator(MetaEstimatorMixin):
...     def \_\_init\_\_(self, \*, estimator\=None):
...         self.estimator \= estimator
...     def fit(self, X, y\=None):
...         if self.estimator is None:
...             self.estimator\_ \= LogisticRegression()
...         else:
...             self.estimator\_ \= self.estimator
...         return self
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> estimator \= MyEstimator().fit(X, y)
\>>> estimator.estimator\_
LogisticRegression()

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)