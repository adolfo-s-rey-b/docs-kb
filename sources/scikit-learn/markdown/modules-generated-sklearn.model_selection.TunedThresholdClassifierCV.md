[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)

Collapse Sidebar Expand Sidebar

TunedThresholdClassifierCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#tunedthresholdclassifiercv "Link to this heading")

===========================================================================================================================================================================================

class sklearn.model\_selection.TunedThresholdClassifierCV(_estimator_, _\*_, _scoring\='balanced\_accuracy'_, _response\_method\='auto'_, _thresholds\=100_, _cv\=None_, _refit\=True_, _n\_jobs\=None_, _random\_state\=None_, _store\_cv\_results\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L499)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "Link to this definition")

Classifier that post-tunes the decision threshold using cross-validation.

This estimator post-tunes the decision threshold (cut-off point) that is used for converting posterior probability estimates (i.e. output of `predict_proba`) or decision scores (i.e. output of `decision_function`) into a class label. The tuning is done by optimizing a binary metric, potentially constrained by another metric.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/classification_threshold.html#threshold-tuning)
.

Added in version 1.5.

Parameters:

**estimator**estimator instance

The classifier, fitted or not, for which we want to optimize the decision threshold used during `predict`.

**scoring**str or callable, default=”balanced\_accuracy”

The objective metric to be optimized. Can be one of:

*   str: string associated to a scoring function for binary classification, see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    

**response\_method**{“auto”, “decision\_function”, “predict\_proba”}, default=”auto”

Methods by the classifier `estimator` corresponding to the decision function for which we want to find a threshold. It can be:

*   if `"auto"`, it will try to invoke, for each classifier, `"predict_proba"` or `"decision_function"` in that order.
    
*   otherwise, one of `"predict_proba"` or `"decision_function"`. If the method is not implemented by the classifier, it will raise an error.
    

**thresholds**int or array-like, default=100

The number of decision threshold to use when discretizing the output of the classifier `method`. Pass an array-like to manually specify the thresholds to use.

**cv**int, float, cross-validation generator, iterable or “prefit”, default=None

Determines the cross-validation splitting strategy to train classifier. Possible inputs for cv are:

*   `None`, to use the default 5-fold stratified K-fold cross validation;
    
*   An integer number, to specify the number of folds in a stratified k-fold;
    
*   A float number, to specify a single shuffle split. The floating number should be in (0, 1) and represent the size of the validation set;
    
*   An object to be used as a cross-validation generator;
    
*   An iterable yielding train, test splits;
    
*   `"prefit"`, to bypass the cross-validation.
    

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Warning

Using `cv="prefit"` and passing the same dataset for fitting `estimator` and tuning the cut-off point is subject to undesired overfitting. You can refer to [Consideration regarding model refitting and cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#tunedthresholdclassifiercv-no-cv)
 for an example.

This option should only be used when the set used to fit `estimator` is different from the one used to tune the cut-off point (by calling [`TunedThresholdClassifierCV.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.fit "sklearn.model_selection.TunedThresholdClassifierCV.fit")
).

**refit**bool, default=True

Whether or not to refit the classifier on the entire training set once the decision threshold has been found. Note that forcing `refit=False` on cross-validation having more than a single split will raise an error. Similarly, `refit=True` in conjunction with `cv="prefit"` will raise an error.

**n\_jobs**int, default=None

The number of jobs to run in parallel. When `cv` represents a cross-validation strategy, the fitting and scoring on each data split is done in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of cross-validation when `cv` is a float. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**store\_cv\_results**bool, default=False

Whether to store all scores and thresholds computed during the cross-validation process.

Attributes:

**estimator\_**estimator instance

The fitted classifier used when predicting.

**best\_threshold\_**float

The new decision threshold.

**best\_score\_**float or None

The optimal score of the objective metric, evaluated at `best_threshold_`.

**cv\_results\_**dict or None

A dictionary containing the scores and thresholds computed during the cross-validation process. Only exist if `store_cv_results=True`. The keys are `"thresholds"` and `"scores"`.

`classes_`ndarray of shape (n\_classes,)

Classes labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

See also

[`sklearn.model_selection.FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")

Classifier that uses a constant threshold.

[`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")

Estimator that calibrates probabilities.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.ensemble import RandomForestClassifier
\>>> from sklearn.metrics import classification\_report
\>>> from sklearn.model\_selection import TunedThresholdClassifierCV, train\_test\_split
\>>> X, y \= make\_classification(
...     n\_samples\=1\_000, weights\=\[0.9, 0.1\], class\_sep\=0.8, random\_state\=42
... )
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, stratify\=y, random\_state\=42
... )
\>>> classifier \= RandomForestClassifier(random\_state\=0).fit(X\_train, y\_train)
\>>> print(classification\_report(y\_test, classifier.predict(X\_test)))
              precision    recall  f1-score   support

           0       0.94      0.99      0.96       224
           1       0.80      0.46      0.59        26

    accuracy                           0.93       250
   macro avg       0.87      0.72      0.77       250
weighted avg       0.93      0.93      0.92       250

\>>> classifier\_tuned \= TunedThresholdClassifierCV(
...     classifier, scoring\="balanced\_accuracy"
... ).fit(X\_train, y\_train)
\>>> print(
...     f"Cut-off point found at {classifier\_tuned.best\_threshold\_:.3f}"
... )
Cut-off point found at 0.342
\>>> print(classification\_report(y\_test, classifier\_tuned.predict(X\_test)))
              precision    recall  f1-score   support

           0       0.96      0.95      0.96       224
           1       0.61      0.65      0.63        26

    accuracy                           0.92       250
   macro avg       0.78      0.80      0.79       250
weighted avg       0.92      0.92      0.92       250

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L182)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.decision_function "Link to this definition")

Decision function for samples in `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**decisions**ndarray of shape (n\_samples,)

The decision function computed the fitted estimator.

fit(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L96)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.fit "Link to this definition")

Fit the classifier.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,)

Target values.

**\*\*params**dict

Parameters to pass to the `fit` method of the underlying classifier.

Returns:

**self**object

Returns an instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L849)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L823)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.predict "Link to this definition")

Predict the target of new samples.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The samples, as accepted by `estimator.predict`.

Returns:

**class\_labels**ndarray of shape (n\_samples,)

The predicted class.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L163)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.predict_log_proba "Link to this definition")

Predict logarithm class probabilities for `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**log\_probabilities**ndarray of shape (n\_samples, n\_classes)

The logarithm class probabilities of the input samples.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L144)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.predict_proba "Link to this definition")

Predict class probabilities for `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**probabilities**ndarray of shape (n\_samples, n\_classes)

The class probabilities of the input samples.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.score "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection._classification_threshold.TunedThresholdClassifierCV")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)