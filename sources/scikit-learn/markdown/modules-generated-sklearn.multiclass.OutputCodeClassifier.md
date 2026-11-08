[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.multiclass.OutputCodeClassifier.html)

Collapse Sidebar Expand Sidebar

OutputCodeClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#outputcodeclassifier "Link to this heading")

====================================================================================================================================================================

class sklearn.multiclass.OutputCodeClassifier(_estimator_, _\*_, _code\_size\=1.5_, _random\_state\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L1043)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "Link to this definition")

(Error-Correcting) Output-Code multiclass strategy.

Output-code based strategies consist in representing each class with a binary code (an array of 0s and 1s). At fitting time, one binary classifier per bit in the code book is fitted. At prediction time, the classifiers are used to project new points in the class space and the class closest to the points is chosen. The main advantage of these strategies is that the number of classifiers used can be controlled by the user, either for compressing the model (0 < `code_size` < 1) or for making the model more robust to errors (`code_size` > 1). See the documentation for more details.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/multiclass.html#ecoc)
.

Parameters:

**estimator**estimator object

An estimator object implementing [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and one of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 or [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
.

**code\_size**float, default=1.5

Percentage of the number of classes to be used to create the code book. A number between 0 and 1 will require fewer classifiers than one-vs-the-rest. A number greater than 1 will require more classifiers than one-vs-the-rest.

**random\_state**int, RandomState instance, default=None

The generator used to initialize the codebook. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int, default=None

The number of jobs to use for the computation: the multiclass problems are computed in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**estimators\_**list of `int(n_classes * code_size)` estimators

Estimators used for predictions.

**classes\_**ndarray of shape (n\_classes,)

Array containing labels.

**code\_book\_**ndarray of shape (n\_classes, `len(estimators_)`)

Binary array containing the code of each class.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimator exposes such an attribute when fit.

Added in version 1.0.

See also

[`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

One-vs-all multiclass strategy.

[`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")

One-vs-one multiclass strategy.

References

\[1\]

“Solving multiclass learning problems via error-correcting output codes”, Dietterich T., Bakiri G., Journal of Artificial Intelligence Research 2, 1995.

\[2\]

“The error coding method and PICTs”, James G., Hastie T., Journal of Computational and Graphical statistics 7, 1998.

\[3\]

“The Elements of Statistical Learning”, Hastie T., Tibshirani R., Friedman J., page 606 (second-edition) 2008.

Examples

\>>> from sklearn.multiclass import OutputCodeClassifier
\>>> from sklearn.ensemble import RandomForestClassifier
\>>> from sklearn.datasets import make\_classification
\>>> X, y \= make\_classification(n\_samples\=100, n\_features\=4,
...                            n\_informative\=2, n\_redundant\=0,
...                            random\_state\=0, shuffle\=False)
\>>> clf \= OutputCodeClassifier(
...     estimator\=RandomForestClassifier(random\_state\=0),
...     random\_state\=0).fit(X, y)
\>>> clf.predict(\[\[0, 0, 0, 0\]\])
array(\[1\])

Copy to clipboard

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L1159)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.fit "Link to this definition")

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

Returns a fitted instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L1265)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multiclass.py#L1240)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.predict "Link to this definition")

Predict multi-class targets using underlying estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Data.

Returns:

**y**ndarray of shape (n\_samples,)

Predicted multi-class targets.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [OutputCodeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

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