[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html)

Collapse Sidebar Expand Sidebar

FixedThresholdClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#fixedthresholdclassifier "Link to this heading")

=====================================================================================================================================================================================

class sklearn.model\_selection.FixedThresholdClassifier(_estimator_, _\*_, _threshold\='auto'_, _pos\_label\=None_, _response\_method\='auto'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L208)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "Link to this definition")

Binary classifier that manually sets the decision threshold.

This classifier allows to change the default decision threshold used for converting posterior probability estimates (i.e. output of `predict_proba`) or decision scores (i.e. output of `decision_function`) into a class label.

Here, the threshold is not optimized and is set to a constant value.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/classification_threshold.html#fixedthresholdclassifier)
.

Added in version 1.5.

Parameters:

**estimator**estimator instance

The binary classifier, fitted or not, for which we want to optimize the decision threshold used during `predict`.

**threshold**{“auto”} or float, default=”auto”

The decision threshold to use when converting posterior probability estimates (i.e. output of `predict_proba`) or decision scores (i.e. output of `decision_function`) into a class label. When `"auto"`, the threshold is set to 0.5 if `predict_proba` is used as `response_method`, otherwise it is set to 0 (i.e. the default threshold for `decision_function`).

**pos\_label**int, float, bool or str, default=None

The label of the positive class. Used to process the output of the `response_method` method. When `pos_label=None`, if `y_true` is in `{-1, 1}` or `{0, 1}`, `pos_label` is set to 1, otherwise an error will be raised.

**response\_method**{“auto”, “decision\_function”, “predict\_proba”}, default=”auto”

Methods by the classifier `estimator` corresponding to the decision function for which we want to find a threshold. It can be:

*   if `"auto"`, it will try to invoke `"predict_proba"` or `"decision_function"` in that order.
    
*   otherwise, one of `"predict_proba"` or `"decision_function"`. If the method is not implemented by the classifier, it will raise an error.
    

Attributes:

**estimator\_**estimator instance

The fitted classifier used when predicting.

`classes_`ndarray of shape (n\_classes,)

Classes labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

See also

[`sklearn.model_selection.TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")

Classifier that post-tunes the decision threshold based on some metrics and using cross-validation.

[`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")

Estimator that calibrates probabilities.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.metrics import confusion\_matrix
\>>> from sklearn.model\_selection import FixedThresholdClassifier, train\_test\_split
\>>> X, y \= make\_classification(
...     n\_samples\=1\_000, weights\=\[0.9, 0.1\], class\_sep\=0.8, random\_state\=42
... )
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, stratify\=y, random\_state\=42
... )
\>>> classifier \= LogisticRegression(random\_state\=0).fit(X\_train, y\_train)
\>>> print(confusion\_matrix(y\_test, classifier.predict(X\_test)))
\[\[217   7\]\
 \[ 19   7\]\]
\>>> classifier\_other\_threshold \= FixedThresholdClassifier(
...     classifier, threshold\=0.1, response\_method\="predict\_proba"
... ).fit(X\_train, y\_train)
\>>> print(confusion\_matrix(y\_test, classifier\_other\_threshold.predict(X\_test)))
\[\[184  40\]\
 \[  6  20\]\]

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L182)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.decision_function "Link to this definition")

Decision function for samples in `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**decisions**ndarray of shape (n\_samples,)

The decision function computed the fitted estimator.

fit(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L96)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.fit "Link to this definition")

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

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L384)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L350)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.predict "Link to this definition")

Predict the target of new samples.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The samples, as accepted by `estimator.predict`.

Returns:

**class\_labels**ndarray of shape (n\_samples,)

The predicted class.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L163)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.predict_log_proba "Link to this definition")

Predict logarithm class probabilities for `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**log\_probabilities**ndarray of shape (n\_samples, n\_classes)

The logarithm class probabilities of the input samples.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_classification_threshold.py#L144)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.predict_proba "Link to this definition")

Predict class probabilities for `X` using the fitted estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**probabilities**ndarray of shape (n\_samples, n\_classes)

The class probabilities of the input samples.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection._classification_threshold.FixedThresholdClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)