[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.SelectorMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.SelectorMixin.html)

Collapse Sidebar Expand Sidebar

SelectorMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#selectormixin "Link to this heading")

======================================================================================================================================================

class sklearn.feature\_selection.SelectorMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L27)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin "Link to this definition")

Transformer mixin that performs feature selection given a support mask.

This mixin provides a feature selector implementation with `transform` and `inverse_transform` functionality given an implementation of `_get_support_mask`.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.base import BaseEstimator
\>>> from sklearn.feature\_selection import SelectorMixin
\>>> class FeatureSelector(SelectorMixin, BaseEstimator):
...    def fit(self, X, y\=None):
...        self.n\_features\_in\_ \= X.shape\[1\]
...        return self
...    def \_get\_support\_mask(self):
...        mask \= np.zeros(self.n\_features\_in\_, dtype\=bool)
...        mask\[:2\] \= True  \# select the first two features
...        return mask
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> FeatureSelector().fit\_transform(X, y).shape
(150, 2)

Copy to clipboard

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L176)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.get_feature_names_out "Link to this definition")

Mask feature names according to selected features.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_support(_indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.get_support "Link to this definition")

Get a mask, or integer index, of the features selected.

Parameters:

**indices**bool, default=False

If True, the return value will be an array of integers, rather than a boolean mask.

Returns:

**support**array

An index that selects the retained features from a feature vector. If `indices` is False, this is a boolean array of shape \[# input features\], in which an element is True iff its corresponding feature is selected for retention. If `indices` is True, this is an integer array of shape \[# output features\] whose values are indices into the input feature vector.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.inverse_transform "Link to this definition")

Reverse the transformation operation.

Parameters:

**X**array of shape \[n\_samples, n\_selected\_features\]

The input samples.

Returns:

**X\_original**array of shape \[n\_samples, n\_original\_features\]

`X` with columns of zeros inserted where features would have been removed by [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.transform "sklearn.feature_selection.SelectorMixin.transform")
.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.set_output "Link to this definition")

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

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L89)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin.transform "Link to this definition")

Reduce X to the selected features.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**X\_r**array of shape \[n\_samples, n\_selected\_features\]

The input samples with only the selected features.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)