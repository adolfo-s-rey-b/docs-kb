[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.StackingClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.StackingClassifier.html)

Collapse Sidebar Expand Sidebar

StackingClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#stackingclassifier "Link to this heading")

============================================================================================================================================================

class sklearn.ensemble.StackingClassifier(_estimators_, _final\_estimator\=None_, _\*_, _cv\=None_, _stack\_method\='auto'_, _n\_jobs\=None_, _passthrough\=False_, _verbose\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L422)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "Link to this definition")

Stack of estimators with a final classifier.

Stacked generalization consists in stacking the output of individual estimator and use a classifier to compute the final prediction. Stacking allows to use the strength of each individual estimator by using their output as input of a final estimator.

Note that `estimators_` are fitted on the full `X` while `final_estimator_` is trained using cross-validated predictions of the base estimators using `cross_val_predict`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#stacking)
.

Added in version 0.22.

Parameters:

**estimators**list of (str, estimator)

Base estimators which will be stacked together. Each element of the list is defined as a tuple of string (i.e. name) and an estimator instance. An estimator can be set to ‘drop’ using `set_params`.

The type of estimator is generally expected to be a classifier. However, one can pass a regressor for some use case (e.g. ordinal regression).

**final\_estimator**estimator, default=None

A classifier which will be used to combine the base estimators. The default classifier is a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
.

**cv**int, cross-validation generator, iterable, or “prefit”, default=None

Determines the cross-validation splitting strategy used in `cross_val_predict` to train `final_estimator`. Possible inputs for cv are:

*   None, to use the default 5-fold cross validation,
    
*   integer, to specify the number of folds in a (Stratified) KFold,
    
*   An object to be used as a cross-validation generator,
    
*   An iterable yielding train, test splits,
    
*   `"prefit"`, to assume the `estimators` are prefit. In this case, the estimators will not be refitted.
    

For integer/None inputs, if the estimator is a classifier and y is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

If “prefit” is passed, it is assumed that all `estimators` have been fitted already. The `final_estimator_` is trained on the `estimators` predictions on the full training set and are **not** cross validated predictions. Please note that if the models have been trained on the same data to train the stacking model, there is a very high risk of overfitting.

Added in version 1.1: The ‘prefit’ option was added in 1.1

Note

A larger number of split will provide no benefits if the number of training samples is large enough. Indeed, the training time will increase. `cv` is not used for model evaluation but for prediction.

**stack\_method**{‘auto’, ‘predict\_proba’, ‘decision\_function’, ‘predict’}, default=’auto’

Methods called for each base estimator. It can be:

*   if ‘auto’, it will try to invoke, for each estimator, `'predict_proba'`, `'decision_function'` or `'predict'` in that order.
    
*   otherwise, one of `'predict_proba'`, `'decision_function'` or `'predict'`. If the method is not implemented by the estimator, it will raise an error.
    

**n\_jobs**int, default=None

The number of jobs to run in parallel for `fit` of all `estimators`. `None` means 1 unless in a `joblib.parallel_backend` context. -1 means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**passthrough**bool, default=False

When False, only the predictions of estimators will be used as training data for `final_estimator`. When True, the `final_estimator` is trained on the predictions as well as the original training data.

**verbose**int, default=0

Verbosity level.

Attributes:

**classes\_**ndarray of shape (n\_classes,) or list of ndarray if `y` is of type `"multilabel-indicator"`.

Class labels.

**estimators\_**list of estimators

The elements of the `estimators` parameter, having been fitted on the training data. If an estimator has been set to `'drop'`, it will not appear in `estimators_`. When `cv="prefit"`, `estimators_` is set to `estimators` and is not fitted again.

**named\_estimators\_**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Attribute to access any fitted sub-estimators by name.

`n_features_in_`int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimators expose such an attribute when fit.

Added in version 1.0.

**final\_estimator\_**estimator

The classifier fit on the output of `estimators_` and responsible for final predictions.

**stack\_method\_**list of str

The method used by each base estimator.

See also

[`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")

Stack of estimators with a final regressor.

Notes

When `predict_proba` is used by each estimator (i.e. most of the time for `stack_method='auto'` or specifically for `stack_method='predict_proba'`), the first column predicted by each estimator will be dropped in the case of a binary classification problem. Indeed, both feature will be perfectly collinear.

In some cases (e.g. ordinal regression), one can pass regressors as the first layer of the [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
. However, note that `y` will be internally encoded in a numerically increasing order or lexicographic order. If this ordering is not adequate, one should manually numerically encode the classes in the desired order.

References

\[1\]

Wolpert, David H. “Stacked generalization.” Neural networks 5.2 (1992): 241-259.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.ensemble import RandomForestClassifier
\>>> from sklearn.svm import LinearSVC
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.pipeline import make\_pipeline
\>>> from sklearn.ensemble import StackingClassifier
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> estimators \= \[\
...     ('rf', RandomForestClassifier(n\_estimators\=10, random\_state\=42)),\
...     ('svr', make\_pipeline(StandardScaler(),\
...                           LinearSVC(random\_state\=42)))\
... \]
\>>> clf \= StackingClassifier(
...     estimators\=estimators, final\_estimator\=LogisticRegression()
... )
\>>> from sklearn.model\_selection import train\_test\_split
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, stratify\=y, random\_state\=42
... )
\>>> clf.fit(X\_train, y\_train).score(X\_test, y\_test)
0.9...

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L791)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.decision_function "Link to this definition")

Decision function for samples in `X` using the final estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**decisions**ndarray of shape (n\_samples,), (n\_samples, n\_classes), or (n\_samples, n\_classes \* (n\_classes-1) / 2)

The decision function computed the final estimator.

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L659)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.fit "Link to this definition")

Fit the estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target values. Note that `y` will be internally encoded in numerically increasing order or lexicographic order. If the order matter (e.g. for ordinal regression), one should numerically encode the target `y` before calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**\*\*fit\_params**dict

Parameters to pass to the underlying estimators.

Added in version 1.6: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Returns a fitted instance of estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L302)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features. The input feature names are only used when `passthrough` is `True`.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then names are generated: `[x0, x1, ..., x(n_features_in_ - 1)]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

If `passthrough` is `False`, then only the names of `estimators` are used to generate the output feature names.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L386)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.6.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_base.py#L276)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.get_params "Link to this definition")

Get the parameters of an estimator from the ensemble.

Returns the parameters given in the constructor as well as the estimators contained within the `estimators` parameter.

Parameters:

**deep**bool, default=True

Setting it to True gets the various estimators and the parameters of the estimators as well.

Returns:

**params**dict

Parameter and estimator names mapped to their values or parameter names mapped to their values.

property named\_estimators[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.named_estimators "Link to this definition")

Dictionary to access any fitted sub-estimators by name.

Returns:

[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

predict(_X_, _\*\*predict\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L708)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.predict "Link to this definition")

Predict target for X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**\*\*predict\_params**dict of str -> obj

Parameters to the `predict` called by the `final_estimator`. Note that this may be used to return uncertainties from some estimators with `return_std` or `return_cov`. Be aware that it will only account for uncertainty in the final estimator.

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `predict` method of the `final_estimator`.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `predict` method of the `final_estimator`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Changed in version 1.6: `**predict_params` can be routed via metadata routing API.

Returns:

**y\_pred**ndarray of shape (n\_samples,) or (n\_samples, n\_output)

Predicted targets.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L763)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.predict_proba "Link to this definition")

Predict class probabilities for `X` using the final estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**probabilities**ndarray of shape (n\_samples, n\_classes) or list of ndarray of shape (n\_output,)

The class probabilities of the input samples.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.score "Link to this definition")

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

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.set_output "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_base.py#L251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.set_params "Link to this definition")

Set the parameters of an estimator from the ensemble.

Valid parameter keys can be listed with `get_params()`. Note that you can directly set the parameters of the estimators contained in `estimators`.

Parameters:

**\*\*params**keyword arguments

Specific parameters using e.g. `set_params(parameter_name=new_value)`. In addition, to setting the parameters of the estimator, the individual estimator of the estimators can also be set, or can be removed by setting them to ‘drop’.

Returns:

**self**object

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble._stacking.StackingClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.set_score_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `score` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `score`.

Returns:

**self**object

The updated object.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_stacking.py#L814)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier.transform "Link to this definition")

Return class labels or probabilities for X for each estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**y\_preds**ndarray of shape (n\_samples, n\_estimators) or (n\_samples, n\_classes \* n\_estimators)

Prediction outputs for each estimator.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)