[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.RidgeCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.RidgeCV.html)

Collapse Sidebar Expand Sidebar

RidgeCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#ridgecv "Link to this heading")

===============================================================================================================================

class sklearn.linear\_model.RidgeCV(_alphas\=(0.1, 1.0, 10.0)_, _\*_, _fit\_intercept\=True_, _scoring\=None_, _cv\=None_, _gcv\_mode\=None_, _store\_cv\_results\=False_, _alpha\_per\_target\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2658)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "Link to this definition")

Ridge regression with built-in cross-validation.

See glossary entry for [cross-validation estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator)
.

By default, it performs efficient Leave-One-Out Cross-Validation.

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
     if cv is None (i.e. when using leave-one-out cross-validation), or [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)
     (R2) otherwise.
    

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the efficient Leave-One-Out cross-validation
    
*   integer, to specify the number of folds,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if `y` is binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used, else, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

**gcv\_mode**{‘auto’, ‘svd’, ‘eigen’}, default=’auto’

Flag indicating which strategy to use when performing Leave-One-Out Cross-Validation. Options are:

'auto' : same as 'eigen'
'svd' : use singular value decomposition of X when X is dense,
    fallback to 'eigen' when X is sparse
'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features
    or X' X when n\_features < n\_samples

Copy to clipboard

The ‘auto’ mode is the default and is intended to pick the cheaper option depending on the shape and sparsity of the training data.

**store\_cv\_results**bool, default=False

Flag indicating if the cross-validation values corresponding to each alpha should be stored in the `cv_results_` attribute (see below). This flag is only compatible with `cv=None` (i.e. using Leave-One-Out Cross-Validation).

Changed in version 1.5: Parameter name changed from `store_cv_values` to `store_cv_results`.

**alpha\_per\_target**bool, default=False

Flag indicating whether to optimize the alpha value (picked from the `alphas` parameter list) for each target separately (for multi-output settings: multiple prediction targets). When set to `True`, after fitting, the `alpha_` attribute will contain a value for each target. When set to `False`, a single alpha is used for all targets. This flag is only compatible with `cv=None` (i.e. using Leave-One-Out Cross-Validation).

Added in version 0.24.

Attributes:

**cv\_results\_**ndarray of shape (n\_samples, n\_alphas) or shape (n\_samples, n\_targets, n\_alphas), optional

Cross-validation values for each alpha (only available if `store_cv_results=True` and `cv=None`). After `fit()` has been called, this attribute will contain the mean squared errors if `scoring is None` otherwise it will contain standardized per point prediction values.

Changed in version 1.5: `cv_values_` changed to `cv_results_`.

**coef\_**ndarray of shape (n\_features) or (n\_targets, n\_features)

Weight vector(s).

**intercept\_**float or ndarray of shape (n\_targets,)

Independent term in decision function. Set to 0.0 if `fit_intercept = False`.

**alpha\_**float or ndarray of shape (n\_targets,)

Estimated regularization parameter, or, if `alpha_per_target=True`, the estimated regularization parameter for each target.

**best\_score\_**float or ndarray of shape (n\_targets,)

Score of base estimator with best alpha, or, if `alpha_per_target=True`, a score for each target.

Added in version 0.23.

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

Classifier based on ridge regression on {-1, 1} labels.

[`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")

Ridge classifier with built-in cross validation.

Examples

\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.linear\_model import RidgeCV
\>>> X, y \= load\_diabetes(return\_X\_y\=True)
\>>> clf \= RidgeCV(alphas\=\[1e-3, 1e-2, 1e-1, 1\]).fit(X, y)
\>>> clf.score(X, y)
0.5166...

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2803)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.fit "Link to this definition")

Fit Ridge regression model with cv.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Training data. If using GCV, will be cast to float64 if necessary.

**y**ndarray of shape (n\_samples,) or (n\_samples, n\_targets)

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

Notes

When sample\_weight is provided, the selected hyperparameter may depend on whether we use leave-one-out cross-validation (cv=None) or another form of cross-validation, because only leave-one-out cross-validation takes the sample weights into account when computing the validation score.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2607)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L2846)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.predict "Link to this definition")

Predict using the linear model.

Parameters:

**X**array-like or sparse matrix of shape (n\_samples, n\_features)

Samples.

Returns:

**C**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)

Predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.score "Link to this definition")

Return [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)
 on test data.

The coefficient of determination, R2, is defined as (1−uv), where u is the residual sum of squares `((y_true - y_pred)** 2).sum()` and v is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of `y`, disregarding the input features, would get a R2 score of 0.0.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples. For some estimators this may be a precomputed kernel matrix or a list of generic objects instead with shape `(n_samples, n_samples_fitted)`, where `n_samples_fitted` is the number of samples used in the fitting for the estimator.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True values for `X`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

R2 of `self.predict(X)` w.r.t. `y`.

Notes

The R2 score used when calling `score` on a regressor uses `multioutput='uniform_average'` from version 0.23 to keep consistent with default value of [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
. This influences the `score` method of all the multioutput regressors (except for [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
).

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model._ridge.RidgeCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model._ridge.RidgeCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_thumb.png)

[Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html)

Face completion with a multi-output estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)