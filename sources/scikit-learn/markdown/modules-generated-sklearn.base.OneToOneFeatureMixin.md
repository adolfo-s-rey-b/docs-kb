[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.OneToOneFeatureMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.OneToOneFeatureMixin.html)

Collapse Sidebar Expand Sidebar

OneToOneFeatureMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#onetoonefeaturemixin "Link to this heading")

==============================================================================================================================================================

class sklearn.base.OneToOneFeatureMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L975)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#sklearn.base.OneToOneFeatureMixin "Link to this definition")

Provides `get_feature_names_out` for simple transformers.

This mixin assumes there’s a 1-to-1 correspondence between input features and output features, such as [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
.

Examples

\>>> import numpy as np
\>>> from sklearn.base import OneToOneFeatureMixin, BaseEstimator
\>>> class MyEstimator(OneToOneFeatureMixin, BaseEstimator):
...     def fit(self, X, y\=None):
...         self.n\_features\_in\_ \= X.shape\[1\]
...         return self
\>>> X \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> MyEstimator().fit(X).get\_feature\_names\_out()
array(\['x0', 'x1'\], dtype=object)

Copy to clipboard

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L994)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#sklearn.base.OneToOneFeatureMixin.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Same as input features.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)