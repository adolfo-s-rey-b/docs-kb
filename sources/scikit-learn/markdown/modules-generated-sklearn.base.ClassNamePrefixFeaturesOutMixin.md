[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html)

Collapse Sidebar Expand Sidebar

ClassNamePrefixFeaturesOutMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#classnameprefixfeaturesoutmixin "Link to this heading")

===============================================================================================================================================================================================

class sklearn.base.ClassNamePrefixFeaturesOutMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1021)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "Link to this definition")

Mixin class for transformers that generate their own names by prefixing.

This mixin is useful when the transformer needs to generate its own feature names out, such as [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
. For example, if [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 outputs 3 features, then the generated feature names out are: `["pca0", "pca1", "pca2"]`.

This mixin assumes that a `_n_features_out` attribute is defined when the transformer is fitted. `_n_features_out` is the number of output features that the transformer will return in `transform` of `fit_transform`.

Examples

\>>> import numpy as np
\>>> from sklearn.base import ClassNamePrefixFeaturesOutMixin, BaseEstimator
\>>> class MyEstimator(ClassNamePrefixFeaturesOutMixin, BaseEstimator):
...     def fit(self, X, y\=None):
...         self.\_n\_features\_out \= X.shape\[1\]
...         return self
\>>> X \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> MyEstimator().fit(X).get\_feature\_names\_out()
array(\['myestimator0', 'myestimator1'\], dtype=object)

Copy to clipboard

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)