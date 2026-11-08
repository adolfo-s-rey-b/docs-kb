[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.RidgeClassifierCV.html)

Collapse Sidebar Expand Sidebar

RidgeClassifierCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#ridgeclassifiercv "Link to this heading")

=============================================================================================================================================================

class sklearn.linear\_model.RidgeClassifierCV(_alphas\=(0.1, 1.0, 10.0)_, _\*_, _fit\_intercept\=True_, _scoring\=None_, _cv\=None_, _class\_weight\=None_, _store\_cv\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2869)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "Link to this definition")

Ridge classifier with built-in cross-validation.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

By default, it performs Leave-One-Out Cross-Validation. Currently, only the n\_features > n\_samples case is handled efficiently.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)
.

Parameters:

**alphas**array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)

Array of alpha values to try. Regularization strength; must be a positive float. Regularization improves the conditioning of the problem and reduces the variance of the estimates. Larger values specify stronger regularization. Alpha corresponds to `1 / (2C)` in other linear models such as [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 or [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
. If using Leave-One-Out cross-validation, alphas must be strictly positive.

For an example on how regularization strength affects the model coefficients, see [Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#sphx-glr-auto-examples-linear-model-plot-ridge-coeffs-py)
.

**fit\_intercept**bool, default=True

Whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (i.e. data is expected to be centered).

**scoring**str, callable, default=None

The scoring method to use for cross-validation. Options:

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: negative [mean squared error](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error)
     if cv is None (i.e. when using leave-one-out cross-validation), or [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
     otherwise.
    

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the efficient Leave-One-Out cross-validation
    
*   integer, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

**class\_weight**dict or ‘balanced’, default=None

Weights associated with classes in the form `{class_label: weight}`. If not given, all classes are supposed to have weight one.

The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as `n_samples / (n_classes * np.bincount(y))`.

**store\_cv\_results**bool, default=False

Flag indicating if the cross-validation results corresponding to each alpha should be stored in the `cv_results_` attribute (see below). This flag is only compatible with `cv=None` (i.e. using Leave-One-Out Cross-Validation).

Changed in version 1.5: Parameter name changed from `store_cv_values` to `store_cv_results`.

Attributes:

**cv\_results\_**ndarray of shape (n\_samples, n\_targets, n\_alphas), optional

Cross-validation results for each alpha (only if `store_cv_results=True` and `cv=None`). After `fit()` has been called, this attribute will contain the mean squared errors if `scoring is None` otherwise it will contain standardized per point prediction values.

Changed in version 1.5: `cv_values_` changed to `cv_results_`.

**coef\_**ndarray of shape (n\_features,) or (n\_targets, n\_features)

Coefficient of the features in the decision function.

`coef_` is of shape `(n_features,)` when the given problem is binary.

**intercept\_**float or ndarray of shape (n\_targets,)

Independent term in decision function. Set to 0.0 if `fit_intercept = False`.

**alpha\_**float

Estimated regularization parameter.

**best\_score\_**float

Score of base estimator with best alpha.

Added in version 0.23.

**classes\_**ndarray of shape (n\_classes,)

The classes labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")

Ridge regression.

[`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")

Ridge classifier.

[`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")

Ridge regression with built-in cross validation.

Notes

For multi-class classification, n\_class classifiers are trained in a one-versus-all approach. Concretely, this is implemented by taking advantage of the multi-variate response support in Ridge.

Examples

\>>> from sklearn.datasets import load\_breast\_cancer
\>>> from sklearn.linear\_model import RidgeClassifierCV
\>>> X, y \= load\_breast\_cancer(return\_X\_y\=True)
\>>> clf \= RidgeClassifierCV(alphas\=\[1e-3, 1e-2, 1e-1, 1\]).fit(X, y)
\>>> clf.score(X, y)
0.9630...

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L366)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.decision_function "Link to this definition")

Predict confidence scores for samples.

The confidence score for a sample is proportional to the signed distance of that sample to the hyperplane.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to get the confidence scores.

Returns:

**scores**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Confidence scores per `(n_samples, n_classes)` combination. In the binary case, confidence score for `self.classes_[1]` where >0 means this class would be predicted.

fit(_X_, _y_, _sample\_weight\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L3028)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.fit "Link to this definition")

Fit Ridge classifier with cv.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features. When using GCV, will be cast to float64 if necessary.

**y**ndarray of shape (n\_samples,)

Target values. Will be cast to X’s dtype if necessary.

**sample\_weight**float or ndarray of shape (n\_samples,), default=None

Individual weights for each sample. If given a float, every sample will have the same weight.

**\*\*params**dict, default=None

Parameters to be passed to the underlying scorer.

Added in version 1.5: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2607)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L1350)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.predict "Link to this definition")

Predict class labels for samples in `X`.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix for which we want to predict the targets.

Returns:

**y\_pred**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Vector or matrix containing the predictions. In binary and multiclass problems, this is a vector containing `n_samples`. In a multilabel problem, it returns a matrix of shape `(n_samples, n_outputs)`.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.score "Link to this definition")

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

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [RidgeClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model._ridge.RidgeClassifierCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [RidgeClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model._ridge.RidgeClassifierCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV.set_score_request "Link to this definition")

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)