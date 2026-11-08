[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.multiclass.OneVsOneClassifier.html)

Collapse Sidebar Expand Sidebar

OneVsOneClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#onevsoneclassifier "Link to this heading")

==============================================================================================================================================================

class sklearn.multiclass.OneVsOneClassifier(_estimator_, _\*_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L678)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "Link to this definition")

One-vs-one multiclass strategy.

This strategy consists in fitting one classifier per class pair. At prediction time, the class which received the most votes is selected. Since it requires to fit `n_classes * (n_classes - 1) / 2` classifiers, this method is usually slower than one-vs-the-rest, due to its O(n\_classes^2) complexity. However, this method may be advantageous for algorithms such as kernel algorithms which don’t scale well with `n_samples`. This is because each individual learning problem only involves a small subset of the data whereas, with one-vs-the-rest, the complete dataset is used `n_classes` times.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/multiclass.html#ovo-classification)
.

Parameters:

**estimator**estimator object

A regressor or a classifier that implements [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. When a classifier is passed, [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 will be used in priority and it will fallback to [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 if it is not available. When a regressor is passed, [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 is used.

**n\_jobs**int, default=None

The number of jobs to use for the computation: the `n_classes * ( n_classes - 1) / 2` OVO problems are computed in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**estimators\_**list of `n_classes * (n_classes - 1) / 2` estimators

Estimators used for predictions.

**classes\_**numpy array of shape \[n\_classes\]

Array containing labels.

`n_classes_`int

Number of classes.

**pairwise\_indices\_**list, length = `len(estimators_)`, or `None`

Indices of samples used when training the estimators. `None` when `estimator`’s `pairwise` tag is False.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

One-vs-all multiclass strategy.

[`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")

(Error-Correcting) Output-Code multiclass strategy.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.multiclass import OneVsOneClassifier
\>>> from sklearn.svm import LinearSVC
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(
...     X, y, test\_size\=0.33, shuffle\=True, random\_state\=0)
\>>> clf \= OneVsOneClassifier(
...     LinearSVC(random\_state\=0)).fit(X\_train, y\_train)
\>>> clf.predict(X\_test\[:10\])
array(\[2, 1, 0, 2, 0, 2, 0, 1, 1, 1\])

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L955)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.decision_function "Link to this definition")

Decision function for the OneVsOneClassifier.

The decision values for the samples are computed by adding the normalized sum of pair-wise classification confidence levels to the votes in order to disambiguate between the decision values when the votes for all the classes are equal leading to a tie.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data.

Returns:

**Y**array-like of shape (n\_samples, n\_classes) or (n\_samples,)

Result of calling `decision_function` on the final estimator.

Changed in version 0.19: output shape changed to `(n_samples,)` to conform to scikit-learn conventions for binary classification.

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L765)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.fit "Link to this definition")

Fit underlying estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

**y**array-like of shape (n\_samples,)

Multi-class targets.

**\*\*fit\_params**dict

Parameters passed to the `estimator.fit` method of each sub-estimator.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

The fitted underlying estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L1015)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y_, _classes\=None_, _\*\*partial\_fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L840)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.partial_fit "Link to this definition")

Partially fit underlying estimators.

Should be used when memory is inefficient to train all data. Chunks of data can be passed in several iteration, where the first call should have an array of all target variables.

Parameters:

**X**{array-like, sparse matrix) of shape (n\_samples, n\_features)

Data.

**y**array-like of shape (n\_samples,)

Multi-class targets.

**classes**array, shape (n\_classes, )

Classes across all calls to partial\_fit. Can be obtained via `np.unique(y_all)`, where y\_all is the target vector of the entire dataset. This argument is only required in the first call of partial\_fit and can be omitted in the subsequent calls.

**\*\*partial\_fit\_params**dict

Parameters passed to the `estimator.partial_fit` method of each sub-estimator.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

The partially fitted underlying estimator.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L932)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.predict "Link to this definition")

Estimate the best class label for each sample in X.

This is implemented as `argmax(decision_function(X), axis=1)` which will return the label of the class with most votes by estimators predicting the outcome of a decision for each possible class pair.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

Returns:

**y**numpy array of shape \[n\_samples\]

Predicted multi-class targets.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [OneVsOneClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.set_partial_fit_request "Link to this definition")

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
 \= '$UNCHANGED$'_) → [OneVsOneClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)