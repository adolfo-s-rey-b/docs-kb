[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.RFECV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.RFECV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.RFECV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.RFECV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.RFECV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.RFECV.html)

Collapse Sidebar Expand Sidebar

RFECV[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#rfecv "Link to this heading")

==============================================================================================================================

class sklearn.feature\_selection.RFECV(_estimator_, _\*_, _step\=1_, _min\_features\_to\_select\=1_, _cv\=None_, _scoring\=None_, _verbose\=0_, _n\_jobs\=None_, _importance\_getter\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L559)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "Link to this definition")

Recursive feature elimination with cross-validation to select features.

The number of features selected is tuned automatically by fitting an [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
 selector on the different cross-validation splits (provided by the `cv` parameter). The performance of each [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
 selector is evaluated using `scoring` for different numbers of selected features and aggregated together. Finally, the scores are averaged across folds and the number of features selected is set to the number of features that maximize the cross-validation score.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#rfe)
.

Parameters:

**estimator**`Estimator` instance

A supervised learning estimator with a `fit` method that provides information about feature importance either through a `coef_` attribute or through a `feature_importances_` attribute.

**step**int or float, default=1

If greater than or equal to 1, then `step` corresponds to the (integer) number of features to remove at each iteration. If within (0.0, 1.0), then `step` corresponds to the percentage (rounded down) of features to remove at each iteration. Note that the last iteration may remove fewer than `step` features in order to reach `min_features_to_select`.

**min\_features\_to\_select**int, default=1

The minimum number of features to be selected. This number of features will always be scored, even if the difference between the original feature count and `min_features_to_select` isn’t divisible by `step`.

Added in version 0.20.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross-validation,
    
*   integer, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if `y` is binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. If the estimator is not a classifier or if `y` is neither binary nor multiclass, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value of None changed from 3-fold to 5-fold.

**scoring**str or callable, default=None

Scoring method to evaluate the [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
 selectors’ performance. Options:

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

**verbose**int, default=0

Controls verbosity of output.

**n\_jobs**int or None, default=None

Number of cores to run in parallel while fitting across folds. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 0.18.

**importance\_getter**str or callable, default=’auto’

If ‘auto’, uses the feature importance either through a `coef_` or `feature_importances_` attributes of estimator.

Also accepts a string that specifies an attribute name/path for extracting feature importance. For example, give `regressor_.coef_` in case of [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 or `named_steps.clf.feature_importances_` in case of [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with its last step named `clf`.

If `callable`, overrides the default feature importance getter. The callable is passed with the fitted estimator and it should return importance for each feature.

Added in version 0.24.

Attributes:

`classes_`ndarray of shape (n\_classes,)

Classes labels available when `estimator` is a classifier.

**estimator\_**`Estimator` instance

The fitted estimator used to select features.

**cv\_results\_**dict of ndarrays

All arrays (values of the dictionary) are sorted in ascending order by the number of features used (i.e., the first element of the array represents the models that used the least number of features, while the last element represents the models that used all available features).

Added in version 1.0.

This dictionary contains the following keys:

split(k)\_test\_scorendarray of shape (n\_subsets\_of\_features,)

The cross-validation scores across (k)th fold.

mean\_test\_scorendarray of shape (n\_subsets\_of\_features,)

Mean of scores over the folds.

std\_test\_scorendarray of shape (n\_subsets\_of\_features,)

Standard deviation of scores over the folds.

n\_featuresndarray of shape (n\_subsets\_of\_features,)

Number of features used at each step.

Added in version 1.5.

split(k)\_rankingndarray of shape (n\_subsets\_of\_features,)

The cross-validation rankings across (k)th fold. Selected (i.e., estimated best) features are assigned rank 1. Illustration in [Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#sphx-glr-auto-examples-feature-selection-plot-rfe-with-cross-validation-py)

Added in version 1.7.

split(k)\_supportndarray of shape (n\_subsets\_of\_features,)

The cross-validation supports across (k)th fold. The support is the mask of selected features.

Added in version 1.7.

**n\_features\_**int

The number of selected features with cross-validation.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**ranking\_**narray of shape (n\_features,)

The feature ranking, such that `ranking_[i]` corresponds to the ranking position of the i-th feature. Selected (i.e., estimated best) features are assigned rank 1.

**support\_**ndarray of shape (n\_features,)

The mask of selected features.

See also

[`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")

Recursive feature elimination.

Notes

The size of all values in `cv_results_` is equal to `ceil((n_features - min_features_to_select) / step) + 1`, where step is the number of features removed at each iteration.

Allows NaN/Inf in the input if the underlying estimator does as well.

References

\[1\]

Guyon, I., Weston, J., Barnhill, S., & Vapnik, V., “Gene selection for cancer classification using support vector machines”, Mach. Learn., 46(1-3), 389–422, 2002.

Examples

The following example shows how to retrieve the a-priori not known 5 informative features in the Friedman #1 dataset.

\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.feature\_selection import RFECV
\>>> from sklearn.svm import SVR
\>>> X, y \= make\_friedman1(n\_samples\=50, n\_features\=10, random\_state\=0)
\>>> estimator \= SVR(kernel\="linear")
\>>> selector \= RFECV(estimator, step\=1, cv\=5)
\>>> selector \= selector.fit(X, y)
\>>> selector.support\_
array(\[ True,  True,  True,  True,  True, False, False, False, False,\
       False\])
\>>> selector.ranking\_
array(\[1, 1, 1, 1, 1, 6, 4, 3, 2, 5\])

Copy to clipboard

For a detailed example of using RFECV to select features when training a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, see [Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#sphx-glr-auto-examples-feature-selection-plot-rfe-with-cross-validation-py)
.

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.decision_function "Link to this definition")

Compute the decision function of `X`.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**score**array, shape = \[n\_samples, n\_classes\] or \[n\_samples\]

The decision function of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
. Regression and binary classification produce an array of shape \[n\_samples\].

fit(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L797)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.fit "Link to this definition")

Fit the RFE model and automatically tune the number of selected features.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the total number of features.

**y**array-like of shape (n\_samples,)

Target values (integers for classification, real numbers for regression).

**\*\*params**dict of str -> object

Parameters passed to the `fit` method of the estimator, the scorer, and the CV splitter.

Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.get_feature_names_out "Link to this definition")

Mask feature names according to selected features.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L976)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.6.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_support(_indices\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L54)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.get_support "Link to this definition")

Get a mask, or integer index, of the features selected.

Parameters:

**indices**bool, default=False

If True, the return value will be an array of integers, rather than a boolean mask.

Returns:

**support**array

An index that selects the retained features from a feature vector. If `indices` is False, this is a boolean array of shape \[# input features\], in which an element is True iff its corresponding feature is selected for retention. If `indices` is True, this is an integer array of shape \[# output features\] whose values are indices into the input feature vector.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_base.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.inverse_transform "Link to this definition")

Reverse the transformation operation.

Parameters:

**X**array of shape \[n\_samples, n\_selected\_features\]

The input samples.

Returns:

**X\_original**array of shape \[n\_samples, n\_original\_features\]

`X` with columns of zeros inserted where features would have been removed by [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.transform "sklearn.feature_selection.RFECV.transform")
.

predict(_X_, _\*\*predict\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L379)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.predict "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.predict_log_proba "Link to this definition")

Predict class log-probabilities for X.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**p**array of shape (n\_samples, n\_classes)

The class log-probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L482)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.predict_proba "Link to this definition")

Predict class probabilities for X.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

The input samples. Internally, it will be converted to `dtype=np.float32` and if a sparse matrix is provided to a sparse `csr_matrix`.

Returns:

**p**array of shape (n\_samples, n\_classes)

The class probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

score(_X_, _y_, _\*\*score\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_rfe.py#L941)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.score "Link to this definition")

Score using the `scoring` option on the given test data and labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,)

True labels for X.

**\*\*score\_params**dict

Parameters to pass to the `score` method of the underlying scorer.

Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**score**float

Score of self.predict(X) w.r.t. y defined by `scoring`.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.set_params "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV.transform "Link to this definition")

Reduce X to the selected features.

Parameters:

**X**array of shape \[n\_samples, n\_features\]

The input samples.

Returns:

**X\_r**array of shape \[n\_samples, n\_selected\_features\]

The input samples with only the selected features.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)