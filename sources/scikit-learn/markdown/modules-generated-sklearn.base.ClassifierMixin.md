[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.ClassifierMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.ClassifierMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.ClassifierMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.ClassifierMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.ClassifierMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.ClassifierMixin.html)

Collapse Sidebar Expand Sidebar

ClassifierMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#classifiermixin "Link to this heading")

===============================================================================================================================================

class sklearn.base.ClassifierMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L561)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "Link to this definition")

Mixin class for all classifiers in scikit-learn.

This mixin defines the following functionality:

*   set estimator type to `"classifier"` through the `estimator_type` tag;
    
*   `score` method that default to [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    .
    
*   enforce that `fit` requires `y` to be passed through the `requires_y` tag, which is done by setting the classifier type tag.
    

Read more in the [User Guide](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)
.

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, ClassifierMixin
\>>> \# Mixin classes should always be on the left-hand side for a correct MRO
\>>> class MyEstimator(ClassifierMixin, BaseEstimator):
...     def \_\_init\_\_(self, \*, param\=1):
...         self.param \= param
...     def fit(self, X, y\=None):
...         self.is\_fitted\_ \= True
...         return self
...     def predict(self, X):
...         return np.full(shape\=X.shape\[0\], fill\_value\=self.param)
\>>> estimator \= MyEstimator(param\=1)
\>>> X \= np.array(\[\[1, 2\], \[2, 3\], \[3, 4\]\])
\>>> y \= np.array(\[1, 0, 1\])
\>>> estimator.fit(X, y).predict(X)
array(\[1, 1, 1\])
\>>> estimator.score(X, y)
0.66...

Copy to clipboard

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin.score "Link to this definition")

Return [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
 on provided data and labels.

In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True labels for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

Mean accuracy of `self.predict(X)` w.r.t. `y`.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_sklearn_is_fitted_thumb.png)

[\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)

\_\_sklearn\_is\_fitted\_\_ as Developer API

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