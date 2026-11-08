[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.TransformerMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.TransformerMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.TransformerMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.TransformerMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.TransformerMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.TransformerMixin.html)

Collapse Sidebar Expand Sidebar

TransformerMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#transformermixin "Link to this heading")

==================================================================================================================================================

class sklearn.base.TransformerMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L875)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "Link to this definition")

Mixin class for all transformers in scikit-learn.

This mixin defines the following functionality:

*   a `fit_transform` method that delegates to `fit` and `transform`;
    
*   a `set_output` method to output `X` as a specific container type.
    

If [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
 is defined, then [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
 will automatically wrap `transform` and `fit_transform` to follow the `set_output` API. See the [Developer API for set\_output](https://scikit-learn.org/stable/developers/develop.html#developer-api-set-output)
 for details.

[`OneToOneFeatureMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#sklearn.base.OneToOneFeatureMixin "sklearn.base.OneToOneFeatureMixin")
 and [`ClassNamePrefixFeaturesOutMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "sklearn.base.ClassNamePrefixFeaturesOutMixin")
 are helpful mixins for defining [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
.

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, TransformerMixin
\>>> class MyTransformer(TransformerMixin, BaseEstimator):
...     def \_\_init\_\_(self, \*, param\=1):
...         self.param \= param
...     def fit(self, X, y\=None):
...         return self
...     def transform(self, X):
...         return np.full(shape\=len(X), fill\_value\=self.param)
\>>> transformer \= MyTransformer()
\>>> X \= \[\[1, 2\], \[2, 3\], \[3, 4\]\]
\>>> transformer.fit\_transform(X)
array(\[1, 1, 1\])

Copy to clipboard

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

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