[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.BaggingRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.BaggingRegressor.html)

Collapse Sidebar Expand Sidebar

BaggingRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#baggingregressor "Link to this heading")

======================================================================================================================================================

class sklearn.ensemble.BaggingRegressor(_estimator\=None_, _n\_estimators\=10_, _\*_, _max\_samples\=None_, _max\_features\=1.0_, _bootstrap\=True_, _bootstrap\_features\=False_, _oob\_score\=False_, _warm\_start\=False_, _n\_jobs\=None_, _random\_state\=None_, _verbose\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_bagging.py#L1192)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "Link to this definition")

A Bagging regressor.

A Bagging regressor is an ensemble meta-estimator that fits base regressors each on random subsets of the original dataset and then aggregate their individual predictions (either by voting or by averaging) to form a final prediction. Such a meta-estimator can typically be used as a way to reduce the variance of a black-box estimator (e.g., a decision tree), by introducing randomization into its construction procedure and then making an ensemble out of it.

This algorithm encompasses several works from the literature. When random subsets of the dataset are drawn as random subsets of the samples, then this algorithm is known as Pasting [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#r4d113ba76fc0-1)
. If samples are drawn with replacement, then the method is known as Bagging [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#r4d113ba76fc0-2)
. When random subsets of the dataset are drawn as random subsets of the features, then the method is known as Random Subspaces [\[3\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#r4d113ba76fc0-3)
. Finally, when base estimators are built on subsets of both samples and features, then the method is known as Random Patches [\[4\]](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#r4d113ba76fc0-4)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#bagging)
.

Added in version 0.15.

Parameters:

**estimator**object, default=None

The base estimator to fit on random subsets of the dataset. If None, then the base estimator is a [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
.

Added in version 1.2: `base_estimator` was renamed to `estimator`.

**n\_estimators**int, default=10

The number of base estimators in the ensemble.

**max\_samples**int or float, default=None

The number of samples to draw from X to train each base estimator (with replacement by default, see `bootstrap` for more details).

*   If None, then draw `X.shape[0]` samples irrespective of `sample_weight`.
    
*   If int, then draw `max_samples` samples.
    
*   If float, then draw `max_samples * X.shape[0]` unweighted samples or `max_samples * sample_weight.sum()` weighted samples.
    

**max\_features**int or float, default=1.0

The number of features to draw from X to train each base estimator ( without replacement by default, see `bootstrap_features` for more details).

*   If int, then draw `max_features` features.
    
*   If float, then draw `max(1, int(max_features * n_features_in_))` features.
    

**bootstrap**bool, default=True

Whether samples are drawn with replacement. If False, sampling without replacement is performed. If fitting with `sample_weight`, it is strongly recommended to choose True, as only drawing with replacement will ensure the expected frequency semantics of `sample_weight`.

**bootstrap\_features**bool, default=False

Whether features are drawn with replacement.

**oob\_score**bool, default=False

Whether to use out-of-bag samples to estimate the generalization error. Only available if bootstrap=True.

**warm\_start**bool, default=False

When set to True, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just fit a whole new ensemble. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**n\_jobs**int, default=None

The number of jobs to run in parallel for both [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.fit "sklearn.ensemble.BaggingRegressor.fit")
 and [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.predict "sklearn.ensemble.BaggingRegressor.predict")
. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance or None, default=None

Controls the random resampling of the original dataset (sample wise and feature wise). If the base estimator accepts a `random_state` attribute, a different seed is generated for each instance in the ensemble. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**int, default=0

Controls the verbosity when fitting and predicting.

Attributes:

**estimator\_**estimator

The base estimator from which the ensemble is grown.

Added in version 1.2: `base_estimator_` was renamed to `estimator_`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**estimators\_**list of estimators

The collection of fitted sub-estimators.

`estimators_samples_`list of arrays

The subset of drawn samples for each base estimator.

**estimators\_features\_**list of arrays

The subset of drawn features for each base estimator.

**oob\_score\_**float

Score of the training dataset obtained using an out-of-bag estimate. This attribute exists only when `oob_score` is True.

**oob\_prediction\_**ndarray of shape (n\_samples,)

Prediction computed with out-of-bag estimate on the training set. If n\_estimators is small it might be possible that a data point was never left out during the bootstrap. In this case, `oob_prediction_` might contain NaN. This attribute exists only when `oob_score` is True.

See also

[`BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")

A Bagging classifier.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#id1)\
\]

L. Breiman, “Pasting small votes for classification in large databases and on-line”, Machine Learning, 36(1), 85-103, 1999.

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#id2)\
\]

L. Breiman, “Bagging predictors”, Machine Learning, 24(2), 123-140, 1996.

\[[3](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#id3)\
\]

T. Ho, “The random subspace method for constructing decision forests”, Pattern Analysis and Machine Intelligence, 20(8), 832-844, 1998.

\[[4](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#id4)\
\]

G. Louppe and P. Geurts, “Ensembles on Random Patches”, Machine Learning and Knowledge Discovery in Databases, 346-361, 2012.

Examples

\>>> from sklearn.svm import SVR
\>>> from sklearn.ensemble import BaggingRegressor
\>>> from sklearn.datasets import make\_regression
\>>> X, y \= make\_regression(n\_samples\=100, n\_features\=4,
...                        n\_informative\=2, n\_targets\=1,
...                        random\_state\=0, shuffle\=False)
\>>> regr \= BaggingRegressor(estimator\=SVR(),
...                         n\_estimators\=10, random\_state\=0).fit(X, y)
\>>> regr.predict(\[\[0, 0, 0, 0\]\])
array(\[-2.8720\])

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_bagging.py#L323)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.fit "Link to this definition")

Build a Bagging ensemble of estimators from the training set (X, y).

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The training input samples. Sparse matrices are accepted only if they are supported by the base estimator.

**y**array-like of shape (n\_samples,)

The target values (class labels in classification, real numbers in regression).

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If None, then samples are equally weighted. Used as probabilities to sample the training set. Note that the expected frequency semantics for the `sample_weight` parameter are only fulfilled when sampling with replacement `bootstrap=True` and using a float or integer `max_samples` (instead of the default `max_samples=None`).

**\*\*fit\_params**dict

Parameters to pass to the underlying estimators.

Added in version 1.5: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_bagging.py#L614)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_bagging.py#L1384)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.predict "Link to this definition")

Predict regression target for X.

The predicted regression target of an input sample is computed as the mean predicted regression targets of the estimators in the ensemble.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The training input samples. Sparse matrices are accepted only if they are supported by the base estimator.

**\*\*params**dict

Parameters routed to the `predict` method of the sub-estimators via the metadata routing API.

Added in version 1.7: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y**ndarray of shape (n\_samples,)

The predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble._bagging.BaggingRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble._bagging.BaggingRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bias_variance_thumb.png)

[Single estimator versus bagging: bias-variance decomposition](https://scikit-learn.org/stable/auto_examples/ensemble/plot_bias_variance.html)

Single estimator versus bagging: bias-variance decomposition

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)