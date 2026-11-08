[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.multioutput.MultiOutputClassifier.html)

Collapse Sidebar Expand Sidebar

MultiOutputClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#multioutputclassifier "Link to this heading")

========================================================================================================================================================================

class sklearn.multioutput.MultiOutputClassifier(_estimator_, _\*_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L442)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "Link to this definition")

Multi target classification.

This strategy consists of fitting one classifier per target. This is a simple strategy for extending classifiers that do not natively support multi-target classification.

Parameters:

**estimator**estimator object

An estimator object implementing [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
. A [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 method will be exposed only if `estimator` implements it.

**n\_jobs**int or None, optional (default=None)

The number of jobs to run in parallel. [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.fit "sklearn.multioutput.MultiOutputClassifier.fit")
, [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.predict "sklearn.multioutput.MultiOutputClassifier.predict")
 and [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.partial_fit "sklearn.multioutput.MultiOutputClassifier.partial_fit")
 (if supported by the passed estimator) will be parallelized for each target.

When individual estimators are fast to train or predict, using `n_jobs > 1` can result in slower performance due to the parallelism overhead.

`None` means `1` unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all available processes / threads. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Changed in version 0.20: `n_jobs` default changed from `1` to `None`.

Attributes:

**classes\_**ndarray of shape (n\_classes,)

Class labels.

**estimators\_**list of `n_output` estimators

Estimators used for predictions.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying `estimator` exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimators expose such an attribute when fit.

Added in version 1.0.

See also

[`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")

A multi-label model that arranges binary classifiers into a chain.

[`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")

Fits one regressor per target variable.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_multilabel\_classification
\>>> from sklearn.multioutput import MultiOutputClassifier
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= make\_multilabel\_classification(n\_classes\=3, random\_state\=0)
\>>> clf \= MultiOutputClassifier(LogisticRegression()).fit(X, y)
\>>> clf.predict(X\[\-2:\])
array(\[\[1, 1, 1\],\
       \[1, 0, 1\]\])

Copy to clipboard

fit(_X_, _Y_, _sample\_weight\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L514)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.fit "Link to this definition")

Fit the model to data matrix X and targets Y.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

**Y**array-like of shape (n\_samples, n\_classes)

The target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If `None`, then samples are equally weighted. Only supported if the underlying classifier supports sample weights.

**\*\*fit\_params**dict of string -> object

Parameters passed to the `estimator.fit` method of each step.

Added in version 0.23.

Returns:

**self**object

Returns a fitted instance.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L316)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.3.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y_, _classes\=None_, _sample\_weight\=None_, _\*\*partial\_fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L111)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.partial_fit "Link to this definition")

Incrementally fit a separate model for each class output.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

**y**{array-like, sparse matrix} of shape (n\_samples, n\_outputs)

Multi-output targets.

**classes**list of ndarray of shape (n\_outputs,), default=None

Each array is unique classes for one output in str/int. Can be obtained via `[np.unique(y[:, i]) for i in range(y.shape[1])]`, where `y` is the target matrix of the entire dataset. This argument is required for the first call to partial\_fit and can be omitted in the subsequent calls. Note that `y` doesn’t need to contain all labels in `classes`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If `None`, then samples are equally weighted. Only supported if the underlying regressor supports sample weights.

**\*\*partial\_fit\_params**dict of str -> object

Parameters passed to the `estimator.partial_fit` method of each sub-estimator.

Only available if `enable_metadata_routing=True`. See the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
.

Added in version 1.3.

Returns:

**self**object

Returns a fitted instance.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L285)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.predict "Link to this definition")

Predict multi-output variable using model for each target variable.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

Returns:

**y**{array-like, sparse matrix} of shape (n\_samples, n\_outputs)

Multi-output targets predicted across multiple predictors. Note: Separate models are generated for each predictor.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L555)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.predict_proba "Link to this definition")

Return prediction probabilities for each class of each output.

This method will raise a `ValueError` if any of the estimators do not have `predict_proba`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input data.

Returns:

**p**array of shape (n\_samples, n\_classes), or a list of n\_outputs such arrays if n\_outputs > 1.

The class probabilities of the input samples. The order of the classes corresponds to that in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

Changed in version 0.19: This function now returns a list of arrays where the length of the list is `n_outputs`, and each array is (`n_samples`, `n_classes`) for that particular output.

score(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L583)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.score "Link to this definition")

Return the mean accuracy on the given test data and labels.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples, n\_outputs)

True values for X.

Returns:

**scores**float

Mean accuracy of predicted target versus true target.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MultiOutputClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [MultiOutputClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.set_partial_fit_request "Link to this definition")

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

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `partial_fit`.

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