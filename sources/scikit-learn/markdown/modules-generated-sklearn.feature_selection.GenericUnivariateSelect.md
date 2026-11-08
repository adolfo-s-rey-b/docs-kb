[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html)

Collapse Sidebar Expand Sidebar

GenericUnivariateSelect[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#genericunivariateselect "Link to this heading")

====================================================================================================================================================================================

class sklearn.feature\_selection.GenericUnivariateSelect(_score\_func\=<function f\_classif>_, _\*_, _mode\='percentile'_, _param\=1e-05_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L1062)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "Link to this definition")

Univariate feature selector with configurable strategy.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Parameters:

**score\_func**callable, default=f\_classif

Function taking two arrays X and y, and returning a pair of arrays (scores, pvalues). For modes ‘percentile’ or ‘kbest’ it can return a single array scores.

**mode**{‘percentile’, ‘k\_best’, ‘fpr’, ‘fdr’, ‘fwe’}, default=’percentile’

Feature selection mode. Note that the `'percentile'` and `'kbest'` modes are supporting unsupervised feature selection (when `y` is `None`).

**param**“all”, float or int, default=1e-5

Parameter of the corresponding mode.

Attributes:

**scores\_**array-like of shape (n\_features,)

Scores of features.

**pvalues\_**array-like of shape (n\_features,)

p-values of feature scores, None if `score_func` returned scores only.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")

ANOVA F-value between label/feature for classification tasks.

[`mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")

Mutual information for a discrete target.

[`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")

Chi-squared stats of non-negative features for classification tasks.

[`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")

F-value between label/feature for regression tasks.

[`mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")

Mutual information for a continuous target.

[`SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")

Select features based on percentile of the highest scores.

[`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")

Select features based on the k highest scores.

[`SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr "sklearn.feature_selection.SelectFpr")

Select features based on a false positive rate test.

[`SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")

Select features based on an estimated false discovery rate.

[`SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe "sklearn.feature_selection.SelectFwe")

Select features based on family-wise error rate.

Examples

\>>> from sklearn.datasets import load\_breast\_cancer
\>>> from sklearn.feature\_selection import GenericUnivariateSelect, chi2
\>>> X, y \= load\_breast\_cancer(return\_X\_y\=True)
\>>> X.shape
(569, 30)
\>>> transformer \= GenericUnivariateSelect(chi2, mode\='k\_best', param\=20)
\>>> X\_new \= transformer.fit\_transform(X, y)
\>>> X\_new.shape
(569, 20)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L542)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.fit "Link to this definition")

Run score function on (X, y) and get the appropriate features.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The training input samples.

**y**array-like of shape (n\_samples,) or None

The target values (class labels in classification, real numbers in regression). If the selector is unsupervised then `y` can be set to `None`.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.get_feature_names_out "Link to this definition")

Mask feature names according to selected features.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_support(_indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.get_support "Link to this definition")

Get a mask, or integer index, of the features selected.

Parameters:

**indices**bool, default=False

If True, the return value will be an array of integers, rather than a boolean mask.

Returns:

**support**array

An index that selects the retained features from a feature vector. If `indices` is False, this is a boolean array of shape \[# input features\], in which an element is True iff its corresponding feature is selected for retention. If `indices` is True, this is an integer array of shape \[# output features\] whose values are indices into the input feature vector.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.inverse_transform "Link to this definition")

Reverse the transformation operation.

Parameters:

**X**array of shape \[n\_samples, n\_selected\_features\]

The input samples.

Returns:

**X\_original**array of shape \[n\_samples, n\_original\_features\]

`X` with columns of zeros inserted where features would have been removed by [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.transform "sklearn.feature_selection.GenericUnivariateSelect.transform")
.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.set_output "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L89)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect.transform "Link to this definition")

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