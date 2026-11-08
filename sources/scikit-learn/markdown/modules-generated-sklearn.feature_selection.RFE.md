[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.RFE.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.RFE.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.RFE.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.RFE.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.RFE.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.RFE.html)

Collapse Sidebar Expand Sidebar

RFE[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#rfe "Link to this heading")

========================================================================================================================

class sklearn.feature\_selection.RFE(_estimator_, _\*_, _n\_features\_to\_select\=None_, _step\=1_, _verbose\=0_, _importance\_getter\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L74)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "Link to this definition")

Feature ranking with recursive feature elimination.

Given an external estimator that assigns weights to features (e.g., the coefficients of a linear model), the goal of recursive feature elimination (RFE) is to select features by recursively considering smaller and smaller sets of features. First, the estimator is trained on the initial set of features and the importance of each feature is obtained either through any specific attribute or callable. Then, the least important features are pruned from current set of features. That procedure is recursively repeated on the pruned set until the desired number of features to select is eventually reached.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#rfe)
.

Parameters:

**estimator**`Estimator` instance

A supervised learning estimator with a `fit` method that provides information about feature importance (e.g. `coef_`, `feature_importances_`).

**n\_features\_to\_select**int or float, default=None

The number of features to select. If `None`, half of the features are selected. If integer, the parameter is the absolute number of features to select. If float between 0 and 1, it is the fraction of features to select.

Changed in version 0.24: Added float values for fractions.

**step**int or float, default=1

If greater than or equal to 1, then `step` corresponds to the (integer) number of features to remove at each iteration. If within (0.0, 1.0), then `step` corresponds to the percentage (rounded down) of features to remove at each iteration.

**verbose**int, default=0

Controls verbosity of output.

**importance\_getter**str or callable, default=’auto’

If ‘auto’, uses the feature importance either through a `coef_` or `feature_importances_` attributes of estimator.

Also accepts a string that specifies an attribute name/path for extracting feature importance (implemented with `attrgetter`). For example, give `regressor_.coef_` in case of [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 or `named_steps.clf.feature_importances_` in case of class:`~sklearn.pipeline.Pipeline` with its last step named `clf`.

If `callable`, overrides the default feature importance getter. The callable is passed with the fitted estimator and it should return importance for each feature.

Added in version 0.24.

Attributes:

`classes_`ndarray of shape (n\_classes,)

Classes labels available when `estimator` is a classifier.

**estimator\_**`Estimator` instance

The fitted estimator used to select features.

**n\_features\_**int

The number of selected features.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**ranking\_**ndarray of shape (n\_features,)

The feature ranking, such that `ranking_[i]` corresponds to the ranking position of the i-th feature. Selected (i.e., estimated best) features are assigned rank 1.

**support\_**ndarray of shape (n\_features,)

The mask of selected features.

See also

[`RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")

Recursive feature elimination with built-in cross-validated selection of the best number of features.

[`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")

Feature selection based on thresholds of importance weights.

[`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")

Sequential cross-validation based feature selection. Does not rely on importance weights.

Notes

Allows NaN/Inf in the input if the underlying estimator does as well.

References

\[1\]

Guyon, I., Weston, J., Barnhill, S., & Vapnik, V., “Gene selection for cancer classification using support vector machines”, Mach. Learn., 46(1-3), 389–422, 2002.

Examples

The following example shows how to retrieve the 5 most informative features in the Friedman #1 dataset.

\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.feature\_selection import RFE
\>>> from sklearn.svm import SVR
\>>> X, y \= make\_friedman1(n\_samples\=50, n\_features\=10, random\_state\=0)
\>>> estimator \= SVR(kernel\="linear")
\>>> selector \= RFE(estimator, n\_features\_to\_select\=5, step\=1)
\>>> selector \= selector.fit(X, y)
\>>> selector.support\_
array(\[ True,  True,  True,  True,  True, False, False, False, False,\
       False\])
\>>> selector.ranking\_
array(\[1, 1, 1, 1, 1, 6, 4, 3, 2, 5\])

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.decision_function "Link to this definition")

Compute the decision function of `X`.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**score**array, shape = \[n\_samples, n\_classes\] or \[n\_samples\]

The decision function of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
. Regression and binary classification produce an array of shape \[n\_samples\].

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L241)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.fit "Link to this definition")

Fit the RFE model and then the underlying estimator on the selected features.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The training input samples.

**y**array-like of shape (n\_samples,)

The target values.

**\*\*fit\_params**dict

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` method of the underlying estimator.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` method of the underlying estimator.
    

Changed in version 1.6: See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.get_feature_names_out "Link to this definition")

Mask feature names according to selected features.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L535)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.6.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_support(_indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.get_support "Link to this definition")

Get a mask, or integer index, of the features selected.

Parameters:

**indices**bool, default=False

If True, the return value will be an array of integers, rather than a boolean mask.

Returns:

**support**array

An index that selects the retained features from a feature vector. If `indices` is False, this is a boolean array of shape \[# input features\], in which an element is True iff its corresponding feature is selected for retention. If `indices` is True, this is an integer array of shape \[# output features\] whose values are indices into the input feature vector.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.inverse_transform "Link to this definition")

Reverse the transformation operation.

Parameters:

**X**array of shape \[n\_samples, n\_selected\_features\]

The input samples.

Returns:

**X\_original**array of shape \[n\_samples, n\_original\_features\]

`X` with columns of zeros inserted where features would have been removed by [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.transform "sklearn.feature_selection.RFE.transform")
.

predict(_X_, _\*\*predict\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L379)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict "Link to this definition")

Reduce X to the selected features and predict using the estimator.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

**\*\*predict\_params**dict

Parameters to route to the `predict` method of the underlying estimator.

Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y**array of shape \[n\_samples\]

The predicted target values.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L502)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict_log_proba "Link to this definition")

Predict class log-probabilities for X.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**p**array of shape (n\_samples, n\_classes)

The class log-probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L482)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.predict_proba "Link to this definition")

Predict class probabilities for X.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**p**array of shape (n\_samples, n\_classes)

The class probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

score(_X_, _y_, _\*\*score\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L415)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.score "Link to this definition")

Reduce X to the selected features and return the score of the estimator.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

**y**array of shape \[n\_samples\]

The target values.

**\*\*score\_params**dict

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `score` method of the underlying estimator.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `score` method of the underlying estimator.
    

Added in version 1.0.

Changed in version 1.6: See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**score**float

Score of the underlying base estimator computed with the selected features returned by `rfe.transform(X)` and `y`.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.set_params "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.transform "Link to this definition")

Reduce X to the selected features.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**X\_r**array of shape \[n\_samples, n\_selected\_features\]

The input samples with only the selected features.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_thumb.png)

[Recursive feature elimination](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)

Recursive feature elimination

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)