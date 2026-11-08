[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.multiclass.OneVsRestClassifier.html)

Collapse Sidebar Expand Sidebar

OneVsRestClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#onevsrestclassifier "Link to this heading")

=================================================================================================================================================================

class sklearn.multiclass.OneVsRestClassifier(_estimator_, _\*_, _n\_jobs\=None_, _verbose\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L202)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "Link to this definition")

One-vs-the-rest (OvR) multiclass strategy.

Also known as one-vs-all, this strategy consists in fitting one classifier per class. For each classifier, the class is fitted against all the other classes. In addition to its computational efficiency (only `n_classes` classifiers are needed), one advantage of this approach is its interpretability. Since each class is represented by one and one classifier only, it is possible to gain knowledge about the class by inspecting its corresponding classifier. This is the most commonly used strategy for multiclass classification and is a fair default choice.

OneVsRestClassifier can also be used for multilabel classification. To use this feature, provide an indicator matrix for the target `y` when calling `.fit`. In other words, the target labels should be formatted as a 2D binary (0/1) matrix, where \[i, j\] == 1 indicates the presence of label j in sample i. This estimator uses the binary relevance method to perform multilabel classification, which involves training one binary classifier independently for each label.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/multiclass.html#ovr-classification)
.

Parameters:

**estimator**estimator object

A regressor or a classifier that implements [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. When a classifier is passed, [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 will be used in priority and it will fallback to [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 if it is not available. When a regressor is passed, [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 is used.

**n\_jobs**int, default=None

The number of jobs to use for the computation: the `n_classes` one-vs-rest problems are computed in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Changed in version 0.20: `n_jobs` default changed from 1 to None

**verbose**int, default=0

The verbosity level, if non zero, progress messages are printed. Below 50, the output is sent to stderr. Otherwise, the output is sent to stdout. The frequency of the messages increases with the verbosity level, reporting all iterations at 10. See [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 for more details.

Added in version 1.1.

Attributes:

**estimators\_**list of `n_classes` estimators

Estimators used for predictions.

**classes\_**array, shape = \[`n_classes`\]

Class labels.

`n_classes_`int

Number of classes.

**label\_binarizer\_**LabelBinarizer object

Object used to transform multiclass labels to binary labels and vice-versa.

`multilabel_`boolean

Whether this is a multilabel classifier.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 1.0.

See also

[`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")

One-vs-one multiclass strategy.

[`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")

(Error-Correcting) Output-Code multiclass strategy.

[`sklearn.multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")

Alternate way of extending an estimator for multilabel classification.

[`sklearn.preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")

Transform iterable of iterables to binary indicator matrix.

Examples

\>>> import numpy as np
\>>> from sklearn.multiclass import OneVsRestClassifier
\>>> from sklearn.svm import SVC
\>>> X \= np.array(\[\
...     \[10, 10\],\
...     \[8, 10\],\
...     \[\-5, 5.5\],\
...     \[\-5.4, 5.5\],\
...     \[\-20, \-20\],\
...     \[\-15, \-20\]\
... \])
\>>> y \= np.array(\[0, 0, 1, 1, 2, 2\])
\>>> clf \= OneVsRestClassifier(SVC()).fit(X, y)
\>>> clf.predict(\[\[\-19, \-20\], \[9, 9\], \[\-5, 5\]\])
array(\[2, 0, 1\])

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L564)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.decision_function "Link to this definition")

Decision function for the OneVsRestClassifier.

Return the distance of each sample from the decision boundary for each class. This can only be used with estimators which implement the `decision_function` method.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

Returns:

**T**array-like of shape (n\_samples, n\_classes) or (n\_samples,) for binary classification.

Result of calling `decision_function` on the final estimator.

Changed in version 0.19: output shape changed to `(n_samples,)` to conform to scikit-learn conventions for binary classification.

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L327)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.fit "Link to this definition")

Fit underlying estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_classes)

Multi-class targets. An indicator matrix turns on multilabel classification.

**\*\*fit\_params**dict

Parameters passed to the `estimator.fit` method of each sub-estimator.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Instance of fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L611)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y_, _classes\=None_, _\*\*partial\_fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L397)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.partial_fit "Link to this definition")

Partially fit underlying estimators.

Should be used when memory is inefficient to train all data. Chunks of data can be passed in several iterations.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_classes)

Multi-class targets. An indicator matrix turns on multilabel classification.

**classes**array, shape (n\_classes, )

Classes across all calls to partial\_fit. Can be obtained via `np.unique(y_all)`, where y\_all is the target vector of the entire dataset. This argument is only required in the first call of partial\_fit and can be omitted in the subsequent calls.

**\*\*partial\_fit\_params**dict

Parameters passed to the `estimator.partial_fit` method of each sub-estimator.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Instance of partially fitted estimator.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L482)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.predict "Link to this definition")

Predict multi-class targets using underlying estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

Returns:

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted multi-class targets.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L522)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.predict_proba "Link to this definition")

Probability estimates.

The returned estimates for all classes are ordered by label of classes.

Note that in the multilabel case, each sample can have any number of labels. This returns the marginal probability that the given sample has the label in question. For example, it is entirely consistent that two labels both have a 90% probability of applying to a given sample.

In the single label multiclass case, the rows of the returned matrix sum to 1.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**T**array-like of shape (n\_samples, n\_classes)

Returns the probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_partial\_fit\_request(_\*_, _classes: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.set_partial_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `partial_fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `partial_fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `partial_fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**classes**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `classes` parameter in `partial_fit`.

Returns:

**self**object

The updated object.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_thumb.png)

[Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)

Multilabel classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_thumb.png)

[Multilabel classification using a classifier chain](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Multilabel classification using a classifier chain

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)