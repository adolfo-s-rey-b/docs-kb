[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.BaseEstimator.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.BaseEstimator.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.BaseEstimator.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.BaseEstimator.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.BaseEstimator.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.BaseEstimator.html)

Collapse Sidebar Expand Sidebar

BaseEstimator[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#baseestimator "Link to this heading")

=========================================================================================================================================

class sklearn.base.BaseEstimator[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L165)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "Link to this definition")

Base class for all estimators in scikit-learn.

Inheriting from this class provides default implementations of:

*   setting and getting parameters used by `GridSearchCV` and friends;
    
*   textual and HTML representation displayed in terminals and IDEs;
    
*   estimator serialization;
    
*   parameters validation;
    
*   data validation;
    
*   feature names validation.
    

Read more in the [User Guide](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)
.

Notes

All estimators should specify all the parameters that can be set at the class level in their `__init__` as explicit keyword arguments (no `*args` or `**kwargs`).

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator
\>>> class MyEstimator(BaseEstimator):
...     def \_\_init\_\_(self, \*, param\=1):
...         self.param \= param
...     def fit(self, X, y\=None):
...         self.is\_fitted\_ \= True
...         return self
...     def predict(self, X):
...         return np.full(shape\=X.shape\[0\], fill\_value\=self.param)
\>>> estimator \= MyEstimator(param\=2)
\>>> estimator.get\_params()
{'param': 2}
\>>> X \= np.array(\[\[1, 2\], \[2, 3\], \[3, 4\]\])
\>>> y \= np.array(\[1, 0, 1\])
\>>> estimator.fit(X, y).predict(X)
array(\[2, 2, 2\])
\>>> estimator.set\_params(param\=3).fit(X, y).predict(X)
array(\[3, 3, 3\])

Copy to clipboard

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_sklearn_is_fitted_thumb.png)

[\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)

\_\_sklearn\_is\_fitted\_\_ as Developer API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

![](https://scikit-learn.org/stable/_images/sphx_glr_approximate_nearest_neighbors_thumb.png)

[Approximate nearest neighbors in TSNE](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)

Approximate nearest neighbors in TSNE

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)