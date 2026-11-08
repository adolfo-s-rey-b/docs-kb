[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.SelectFromModel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.SelectFromModel.html)

Collapse Sidebar Expand Sidebar

SelectFromModel[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#selectfrommodel "Link to this heading")

============================================================================================================================================================

class sklearn.feature\_selection.SelectFromModel(_estimator_, _\*_, _threshold\=None_, _prefit\=False_, _norm\_order\=1_, _max\_features\=None_, _importance\_getter\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_from_model.py#L95)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "Link to this definition")

Meta-transformer for selecting features based on importance weights.

Added in version 0.17.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#select-from-model)
.

Parameters:

**estimator**object

The base estimator from which the transformer is built. This can be both a fitted (if `prefit` is set to True) or a non-fitted estimator. The estimator should have a `feature_importances_` or `coef_` attribute after fitting. Otherwise, the `importance_getter` parameter should be used.

**threshold**str or float, default=None

The threshold value to use for feature selection. Features whose absolute importance value is greater or equal are kept while the others are discarded. If “median” (resp. “mean”), then the `threshold` value is the median (resp. the mean) of the feature importances. A scaling factor (e.g., “1.25\*mean”) may also be used. If None and if the estimator has a parameter penalty set to l1, either explicitly or implicitly (e.g, Lasso), the threshold used is 1e-5. Otherwise, “mean” is used by default.

**prefit**bool, default=False

Whether a prefit model is expected to be passed into the constructor directly or not. If `True`, `estimator` must be a fitted estimator. If `False`, `estimator` is fitted and updated by calling `fit` and `partial_fit`, respectively.

**norm\_order**non-zero int, inf, -inf, default=1

Order of the norm used to filter the vectors of coefficients below `threshold` in the case where the `coef_` attribute of the estimator is of dimension 2.

**max\_features**int, callable, default=None

The maximum number of features to select.

*   If an integer, then it specifies the maximum number of features to allow.
    
*   If a callable, then it specifies how to calculate the maximum number of features allowed. The callable will receive `X` as input: `max_features(X)`.
    
*   If `None`, then all features are kept.
    

To only select based on `max_features`, set `threshold=-np.inf`.

Added in version 0.20.

Changed in version 1.1: `max_features` accepts a callable.

**importance\_getter**str or callable, default=’auto’

If ‘auto’, uses the feature importance either through a `coef_` attribute or `feature_importances_` attribute of estimator.

Also accepts a string that specifies an attribute name/path for extracting feature importance (implemented with `attrgetter`). For example, give `regressor_.coef_` in case of [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 or `named_steps.clf.feature_importances_` in case of [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with its last step named `clf`.

If `callable`, overrides the default feature importance getter. The callable is passed with the fitted estimator and it should return importance for each feature.

Added in version 0.24.

Attributes:

**estimator\_**estimator

The base estimator from which the transformer is built. This attribute exist only when `fit` has been called.

*   If `prefit=True`, it is a deep copy of `estimator`.
    
*   If `prefit=False`, it is a clone of `estimator` and fit on the data passed to `fit` or `partial_fit`.
    

`n_features_in_`int

Number of features seen during `fit`.

**max\_features\_**int

Maximum number of features calculated during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the `max_features` is not `None`.

*   If `max_features` is an `int`, then `max_features_ = max_features`.
    
*   If `max_features` is a callable, then `max_features_ = max_features(X)`.
    

Added in version 1.1.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

`threshold_`float

Threshold value used for feature selection.

See also

[`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")

Recursive feature elimination based on importance weights.

[`RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")

Recursive feature elimination with built-in cross-validated selection of the best number of features.

[`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")

Sequential cross-validation based feature selection. Does not rely on importance weights.

Notes

Allows NaN/Inf in the input if the underlying estimator does as well.

Examples

\>>> from sklearn.feature\_selection import SelectFromModel
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X \= \[\[ 0.87, \-1.34,  0.31 \],\
...      \[\-2.79, \-0.02, \-0.85 \],\
...      \[\-1.34, \-0.48, \-2.55 \],\
...      \[ 1.92,  1.48,  0.65 \]\]
\>>> y \= \[0, 1, 0, 1\]
\>>> selector \= SelectFromModel(estimator\=LogisticRegression()).fit(X, y)
\>>> selector.estimator\_.coef\_
array(\[\[-0.3252,  0.8345,  0.4976\]\])
\>>> selector.threshold\_
np.float64(0.55249)
\>>> selector.get\_support()
array(\[False,  True, False\])
\>>> selector.transform(X)
array(\[\[-1.34\],\
       \[-0.02\],\
       \[-0.48\],\
       \[ 1.48\]\])

Copy to clipboard

Using a callable to create a selector that can use no more than half of the input features.

\>>> def half\_callable(X):
...     return round(len(X\[0\]) / 2)
\>>> half\_selector \= SelectFromModel(estimator\=LogisticRegression(),
...                                 max\_features\=half\_callable)
\>>> \_ \= half\_selector.fit(X, y)
\>>> half\_selector.max\_features\_
2

Copy to clipboard

fit(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_from_model.py#L333)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.fit "Link to this definition")

Fit the SelectFromModel meta-transformer.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The training input samples.

**y**array-like of shape (n\_samples,), default=None

The target values (integers that correspond to classes in classification, real numbers in regression).

**\*\*fit\_params**dict

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` method of the sub-estimator. They are ignored if `prefit=True`.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` method of the sub-estimator. They are ignored if `prefit=True`.
    

Changed in version 1.4: See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.get_feature_names_out "Link to this definition")

Mask feature names according to selected features.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_from_model.py#L493)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_support(_indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.get_support "Link to this definition")

Get a mask, or integer index, of the features selected.

Parameters:

**indices**bool, default=False

If True, the return value will be an array of integers, rather than a boolean mask.

Returns:

**support**array

An index that selects the retained features from a feature vector. If `indices` is False, this is a boolean array of shape \[# input features\], in which an element is True iff its corresponding feature is selected for retention. If `indices` is True, this is an integer array of shape \[# output features\] whose values are indices into the input feature vector.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.inverse_transform "Link to this definition")

Reverse the transformation operation.

Parameters:

**X**array of shape \[n\_samples, n\_selected\_features\]

The input samples.

Returns:

**X\_original**array of shape \[n\_samples, n\_original\_features\]

`X` with columns of zeros inserted where features would have been removed by [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.transform "sklearn.feature_selection.SelectFromModel.transform")
.

partial\_fit(_X_, _y\=None_, _\*\*partial\_fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_from_model.py#L405)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.partial_fit "Link to this definition")

Fit the SelectFromModel meta-transformer only once.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The training input samples.

**y**array-like of shape (n\_samples,), default=None

The target values (integers that correspond to classes in classification, real numbers in regression).

**\*\*partial\_fit\_params**dict

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `partial_fit` method of the sub-estimator.
    
*   If `enable_metadata_routing=True`: Parameters passed to the `partial_fit` method of the sub-estimator. They are ignored if `prefit=True`.
    

Changed in version 1.4: `**partial_fit_params` are routed to the sub-estimator, if `enable_metadata_routing=True` is set via [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
, which allows for aliasing.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.set_params "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.transform "Link to this definition")

Reduce X to the selected features.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**X\_r**array of shape \[n\_samples, n\_selected\_features\]

The input samples with only the selected features.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)