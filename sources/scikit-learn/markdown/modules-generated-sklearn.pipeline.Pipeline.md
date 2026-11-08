[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.pipeline.Pipeline.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.pipeline.Pipeline.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.pipeline.Pipeline.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.pipeline.Pipeline.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.pipeline.Pipeline.html)

Collapse Sidebar Expand Sidebar

Pipeline[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#pipeline "Link to this heading")

==============================================================================================================================

class sklearn.pipeline.Pipeline(_steps_, _\*_, _transform\_input\=None_, _memory\=None_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L93)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "Link to this definition")

A sequence of data transformers with an optional final predictor.

`Pipeline` allows you to sequentially apply a list of transformers to preprocess the data and, if desired, conclude the sequence with a final [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
 for predictive modeling.

Intermediate steps of the pipeline must be transformers, that is, they must implement `fit` and `transform` methods. The final [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 only needs to implement `fit`. The transformers in the pipeline can be cached using `memory` argument.

The purpose of the pipeline is to assemble several steps that can be cross-validated together while setting different parameters. For this, it enables setting parameters of the various steps using their names and the parameter name separated by a `'__'`, as in the example below. A step’s estimator may be replaced entirely by setting the parameter with its name to another estimator, or a transformer removed by setting it to `'passthrough'` or `None`.

For an example use case of `Pipeline` combined with [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, refer to [Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#sphx-glr-auto-examples-compose-plot-compare-reduction-py)
. The example [Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html#sphx-glr-auto-examples-compose-plot-digits-pipe-py)
 shows how to grid search on a pipeline using `'__'` as a separator in the parameter names.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/compose.html#pipeline)
.

Added in version 0.5.

Parameters:

**steps**list of tuples

List of (name of step, estimator) tuples that are to be chained in sequential order. To be compatible with the scikit-learn API, all steps must define `fit`. All non-last steps must also define `transform`. See [Combining Estimators](https://scikit-learn.org/stable/modules/compose.html#combining-estimators)
 for more details.

**transform\_input**list of str, default=None

The names of the [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata)
 parameters that should be transformed by the pipeline before passing it to the step consuming it.

This enables transforming some input arguments to `fit` (other than `X`) to be transformed by the steps of the pipeline up to the step which requires them. Requirement is defined via [metadata routing](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
. For instance, this can be used to pass a validation set through the pipeline.

You can only set this if metadata routing is enabled, which you can enable using `sklearn.set_config(enable_metadata_routing=True)`.

Added in version 1.6.

**memory**str or object with the joblib.Memory interface, default=None

Used to cache the fitted transformers of the pipeline. The last step will never be cached, even if it is a transformer. By default, no caching is performed. If a string is given, it is the path to the caching directory. Enabling caching triggers a clone of the transformers before fitting. Therefore, the transformer instance given to the pipeline cannot be inspected directly. Use the attribute `named_steps` or `steps` to inspect estimators within the pipeline. Caching the transformers is advantageous when fitting is time consuming. See [Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html#sphx-glr-auto-examples-neighbors-plot-caching-nearest-neighbors-py)
 for an example on how to enable caching.

**verbose**bool, default=False

If True, the time elapsed while fitting each step will be printed as it is completed.

Attributes:

[`named_steps`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.named_steps "sklearn.pipeline.Pipeline.named_steps")
[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Access the steps by name.

`classes_`ndarray of shape (n\_classes,)

The classes labels.

`n_features_in_`int

Number of features seen during first step `fit` method.

`feature_names_in_`ndarray of shape (`n_features_in_`,)

Names of features seen during first step `fit` method.

See also

[`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

Convenience function for simplified pipeline construction.

Examples

\>>> from sklearn.svm import SVC
\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.pipeline import Pipeline
\>>> X, y \= make\_classification(random\_state\=0)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y,
...                                                     random\_state\=0)
\>>> pipe \= Pipeline(\[('scaler', StandardScaler()), ('svc', SVC())\])
\>>> \# The pipeline can be used as any other estimator
\>>> \# and avoids leaking the test set into the train set
\>>> pipe.fit(X\_train, y\_train).score(X\_test, y\_test)
0.88
\>>> \# An estimator's parameter can be set using '\_\_' syntax
\>>> pipe.set\_params(svc\_\_C\=10).fit(X\_train, y\_train).score(X\_test, y\_test)
0.76

Copy to clipboard

decision\_function(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L936)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.decision_function "Link to this definition")

Transform the data, and apply `decision_function` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `decision_function` method. Only valid if the final estimator implements `decision_function`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

**\*\*params**dict of string -> object

Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y\_score**ndarray of shape (n\_samples, n\_classes)

Result of calling `decision_function` on the final estimator.

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L578)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit "Link to this definition")

Fit the model.

Fit all the transformers one after the other and sequentially transform the data. Finally, fit the transformed data using the final estimator.

Parameters:

**X**iterable

Training data. Must fulfill input requirements of first step of the pipeline.

**y**iterable, default=None

Training targets. Must fulfill label requirements for all steps of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters passed to the `fit` method of each step, where each parameter name is prefixed such that parameter `p` for step `s` has key `s__p`.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True` is set via [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Pipeline with fitted steps.

fit\_predict(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L803)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_predict "Link to this definition")

Transform the data, and apply `fit_predict` with the final estimator.

Call `fit_transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `fit_predict` method. Only valid if the final estimator implements `fit_predict`.

Parameters:

**X**iterable

Training data. Must fulfill input requirements of first step of the pipeline.

**y**iterable, default=None

Training targets. Must fulfill label requirements for all steps of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters to the `predict` called at the end of all transformations in the pipeline.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Added in version 0.20.

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True`.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Note that while this may be used to return uncertainties from some models with `return_std` or `return_cov`, uncertainties that are generated by the transformations in the pipeline are not propagated to the final estimator.

Returns:

**y\_pred**ndarray

Result of calling `fit_predict` on the final estimator.

fit\_transform(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L662)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_transform "Link to this definition")

Fit the model and transform with the final estimator.

Fit all the transformers one after the other and sequentially transform the data. Only valid if the final estimator either implements `fit_transform` or `fit` and `transform`.

Parameters:

**X**iterable

Training data. Must fulfill input requirements of first step of the pipeline.

**y**iterable, default=None

Training targets. Must fulfill label requirements for all steps of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters passed to the `fit` method of each step, where each parameter name is prefixed such that parameter `p` for step `s` has key `s__p`.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True`.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**Xt**ndarray of shape (n\_samples, n\_transformed\_features)

Transformed samples.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1264)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Transform input features using the pipeline.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1360)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.get_params "Link to this definition")

Get parameters for this estimator.

Returns the parameters given in the constructor as well as the estimators contained within the `steps` of the `Pipeline`.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**mapping of string to any

Parameter names mapped to their values.

inverse\_transform(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1116)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.inverse_transform "Link to this definition")

Apply `inverse_transform` for each step in a reverse order.

All estimators in the pipeline must support `inverse_transform`.

Parameters:

**X**array-like of shape (n\_samples, n\_transformed\_features)

Data samples, where `n_samples` is the number of samples and `n_features` is the number of features. Must fulfill input requirements of last step of pipeline’s `inverse_transform` method.

**\*\*params**dict of str -> object

Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Inverse transformed data, that is, data in the original feature space.

property named\_steps[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.named_steps "Link to this definition")

Access the steps by name.

Read-only attribute to access any step by given name. Keys are steps names and values are the steps objects.

predict(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L746)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict "Link to this definition")

Transform the data, and apply `predict` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `predict` method. Only valid if the final estimator implements `predict`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters to the `predict` called at the end of all transformations in the pipeline.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Added in version 0.20.

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True` is set via [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Note that while this may be used to return uncertainties from some models with `return_std` or `return_cov`, uncertainties that are generated by the transformations in the pipeline are not propagated to the final estimator.

Returns:

**y\_pred**ndarray

Result of calling `predict` on the final estimator.

predict\_log\_proba(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1009)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict_log_proba "Link to this definition")

Transform the data, and apply `predict_log_proba` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `predict_log_proba` method. Only valid if the final estimator implements `predict_log_proba`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters to the `predict_log_proba` called at the end of all transformations in the pipeline.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Added in version 0.20.

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True`.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y\_log\_proba**ndarray of shape (n\_samples, n\_classes)

Result of calling `predict_log_proba` on the final estimator.

predict\_proba(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L882)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.predict_proba "Link to this definition")

Transform the data, and apply `predict_proba` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `predict_proba` method. Only valid if the final estimator implements `predict_proba`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

**\*\*params**dict of str -> object

*   If `enable_metadata_routing=False` (default): Parameters to the `predict_proba` called at the end of all transformations in the pipeline.
    
*   If `enable_metadata_routing=True`: Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.
    

Added in version 0.20.

Changed in version 1.4: Parameters are now passed to the `transform` method of the intermediate steps as well, if requested, and if `enable_metadata_routing=True`.

See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y\_proba**ndarray of shape (n\_samples, n\_classes)

Result of calling `predict_proba` on the final estimator.

score(_X_, _y\=None_, _sample\_weight\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1157)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.score "Link to this definition")

Transform the data, and apply `score` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `score` method. Only valid if the final estimator implements `score`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

**y**iterable, default=None

Targets used for scoring. Must fulfill label requirements for all steps of the pipeline.

**sample\_weight**array-like, default=None

If not None, this argument is passed as `sample_weight` keyword argument to the `score` method of the final estimator.

**\*\*params**dict of str -> object

Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**score**float

Result of calling `score` on the final estimator.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L983)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.score_samples "Link to this definition")

Transform the data, and apply `score_samples` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `score_samples` method. Only valid if the final estimator implements `score_samples`.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of first step of the pipeline.

Returns:

**y\_score**ndarray of shape (n\_samples,)

Result of calling `score_samples` on the final estimator.

set\_callbacks(_\*callbacks_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L18)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.set_callbacks "Link to this definition")

Set callbacks for the estimator.

Parameters:

**\*callbacks**callback instances

The callbacks to set.

Returns:

**self**estimator instance

The estimator instance itself.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L224)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.set_output "Link to this definition")

Set the output container when `"transform"` and `"fit_transform"` are called.

Calling `set_output` will set the output of all estimators in `steps`.

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

set\_params(_\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L270)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.set_params "Link to this definition")

Set the parameters of this estimator.

Valid parameter keys can be listed with `get_params()`. Note that you can directly set the parameters of the estimators contained in `steps`.

Parameters:

**\*\*kwargs**dict

Parameters of this estimator or parameters of estimators contained in `steps`. Parameters of the steps may be set using its name and the parameter name separated by a ‘\_\_’.

Returns:

**self**object

Pipeline class instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.set_score_request "Link to this definition")

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

transform(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/pipeline.py#L1069)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.transform "Link to this definition")

Transform the data, and apply `transform` with the final estimator.

Call `transform` of each transformer in the pipeline. The transformed data are finally passed to the final estimator that calls `transform` method. Only valid if the final estimator implements `transform`.

This also works where final estimator is `None` in which case all prior transformations are applied.

Parameters:

**X**iterable

Data to transform. Must fulfill input requirements of first step of the pipeline.

**\*\*params**dict of str -> object

Parameters requested and accepted by steps. Each step must have requested certain metadata for these parameters to be forwarded to them.

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**Xt**ndarray of shape (n\_samples, n\_transformed\_features)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_thumb.png)

[Recursive feature elimination](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)

Recursive feature elimination

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_thumb.png)

[Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)

Explicit feature map approximation for RBF kernels

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_thumb.png)

[Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)

Underfitting vs. Overfitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_cross_val_thumb.png)

[Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html)

Target Encoder's Internal Cross fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_thumb.png)

[Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Semi-supervised Classification on a Text Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)