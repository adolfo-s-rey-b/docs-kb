[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.VotingClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.VotingClassifier.html)

Collapse Sidebar Expand Sidebar

VotingClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#votingclassifier "Link to this heading")

======================================================================================================================================================

class sklearn.ensemble.VotingClassifier(_estimators_, _\*_, _voting\='hard'_, _weights\=None_, _n\_jobs\=None_, _flatten\_transform\=True_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L194)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "Link to this definition")

Soft Voting/Majority Rule classifier for unfitted estimators.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier)
.

Added in version 0.17.

Parameters:

**estimators**list of (str, estimator) tuples

Invoking the `fit` method on the `VotingClassifier` will fit clones of those original estimators that will be stored in the class attribute `self.estimators_`. An estimator can be set to `'drop'` using [`set_params`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_params "sklearn.ensemble.VotingClassifier.set_params")
.

Changed in version 0.21: `'drop'` is accepted. Using None was deprecated in 0.22 and support was removed in 0.24.

**voting**{‘hard’, ‘soft’}, default=’hard’

If ‘hard’, uses predicted class labels for majority rule voting. Else if ‘soft’, predicts the class label based on the argmax of the sums of the predicted probabilities, which is recommended for an ensemble of well-calibrated classifiers.

**weights**array-like of shape (n\_classifiers,), default=None

Sequence of weights (`float` or `int`) to weight the occurrences of predicted class labels (`hard` voting) or class probabilities before averaging (`soft` voting). Uses uniform weights if `None`.

**n\_jobs**int, default=None

The number of jobs to run in parallel for `fit`. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 0.18.

**flatten\_transform**bool, default=True

Affects shape of transform output only when voting=’soft’ If voting=’soft’ and flatten\_transform=True, transform method returns matrix with shape (n\_samples, n\_classifiers \* n\_classes). If flatten\_transform=False, it returns (n\_classifiers, n\_samples, n\_classes).

**verbose**bool, default=False

If True, the time elapsed while fitting will be printed as it is completed.

Added in version 0.23.

Attributes:

**estimators\_**list of classifiers

The collection of fitted sub-estimators as defined in `estimators` that are not ‘drop’. Note that sub-estimators are always fitted on integer-encoded labels (see `le_` attribute). When `y` contains non-integer class labels (e.g. strings), use `le_.inverse_transform` to map predictions back to the original label space.

**named\_estimators\_**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Attribute to access any fitted sub-estimators by name.

Added in version 0.20.

**le\_**[`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")

Transformer used to encode the labels during fit and decode during prediction. Sub-estimators in `estimators_` are fitted on the integer-encoded labels produced by this encoder.

**classes\_**ndarray of shape (n\_classes,)

The classes labels.

`n_features_in_`int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying estimators expose such an attribute when fit.

Added in version 1.0.

See also

[`VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")

Prediction voting regressor.

Examples

\>>> import numpy as np
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.naive\_bayes import GaussianNB
\>>> from sklearn.ensemble import RandomForestClassifier, VotingClassifier
\>>> clf1 \= LogisticRegression(random\_state\=1)
\>>> clf2 \= RandomForestClassifier(n\_estimators\=50, random\_state\=1)
\>>> clf3 \= GaussianNB()
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[\-3, \-2\], \[1, 1\], \[2, 1\], \[3, 2\]\])
\>>> y \= np.array(\[1, 1, 1, 2, 2, 2\])
\>>> eclf1 \= VotingClassifier(estimators\=\[\
...         ('lr', clf1), ('rf', clf2), ('gnb', clf3)\], voting\='hard')
\>>> eclf1 \= eclf1.fit(X, y)
\>>> print(eclf1.predict(X))
\[1 1 1 2 2 2\]
\>>> np.array\_equal(eclf1.named\_estimators\_.lr.predict(X),
...                eclf1.named\_estimators\_\['lr'\].predict(X))
True
\>>> eclf2 \= VotingClassifier(estimators\=\[\
...         ('lr', clf1), ('rf', clf2), ('gnb', clf3)\],
...         voting\='soft')
\>>> eclf2 \= eclf2.fit(X, y)
\>>> print(eclf2.predict(X))
\[1 1 1 2 2 2\]

Copy to clipboard

To drop an estimator, [`set_params`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_params "sklearn.ensemble.VotingClassifier.set_params")
 can be used to remove it. Here we dropped one of the estimators, resulting in 2 fitted estimators:

\>>> eclf2 \= eclf2.set\_params(lr\='drop')
\>>> eclf2 \= eclf2.fit(X, y)
\>>> len(eclf2.estimators\_)
2

Copy to clipboard

Setting `flatten_transform=True` with `voting='soft'` flattens output shape of `transform`:

\>>> eclf3 \= VotingClassifier(estimators\=\[\
...        ('lr', clf1), ('rf', clf2), ('gnb', clf3)\],
...        voting\='soft', weights\=\[2,1,1\],
...        flatten\_transform\=True)
\>>> eclf3 \= eclf3.fit(X, y)
\>>> print(eclf3.predict(X))
\[1 1 1 2 2 2\]
\>>> print(eclf3.transform(X).shape)
(6, 6)

Copy to clipboard

fit(_X_, _y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L354)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.fit "Link to this definition")

Fit the estimators.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target values.

**\*\*fit\_params**dict

Parameters to pass to the underlying estimators.

Added in version 1.5: Only available if `enable_metadata_routing=True`, which can be set by using `sklearn.set_config(enable_metadata_routing=True)`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L125)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.fit_transform "Link to this definition")

Return class labels or probabilities for each estimator.

Return predictions for X for each estimator.

Parameters:

**X**{array-like, sparse matrix, dataframe} of shape (n\_samples, n\_features)

Input samples.

**y**ndarray of shape (n\_samples,), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L503)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Not used, present here for API consistency by convention.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L169)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_base.py#L276)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.get_params "Link to this definition")

Get the parameters of an estimator from the ensemble.

Returns the parameters given in the constructor as well as the estimators contained within the `estimators` parameter.

Parameters:

**deep**bool, default=True

Setting it to True gets the various estimators and the parameters of the estimators as well.

Returns:

**params**dict

Parameter and estimator names mapped to their values or parameter names mapped to their values.

property named\_estimators[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.named_estimators "Link to this definition")

Dictionary to access any fitted sub-estimators by name.

Returns:

[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L411)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.predict "Link to this definition")

Predict class labels for X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

Returns:

**maj**array-like of shape (n\_samples,)

Predicted class labels.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L451)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.predict_proba "Link to this definition")

Compute probabilities of possible outcomes for samples in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

Returns:

**avg**array-like of shape (n\_samples, n\_classes)

Weighted average probability for each class per sample.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.score "Link to this definition")

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

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_base.py#L251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_params "Link to this definition")

Set the parameters of an estimator from the ensemble.

Valid parameter keys can be listed with `get_params()`. Note that you can directly set the parameters of the estimators contained in `estimators`.

Parameters:

**\*\*params**keyword arguments

Specific parameters using e.g. `set_params(parameter_name=new_value)`. In addition, to setting the parameters of the estimator, the individual estimator of the estimators can also be set, or can be removed by setting them to ‘drop’.

Returns:

**self**object

Estimator instance.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble._voting.VotingClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_score_request "Link to this definition")

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

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/ensemble/_voting.py#L471)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.transform "Link to this definition")

Return class labels or probabilities for X for each estimator.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

probabilities\_or\_labels

If `voting='soft'` and `flatten_transform=True`:

returns ndarray of shape (n\_samples, n\_classifiers \* n\_classes), being class probabilities calculated by each classifier.

If ``voting='soft' and `flatten_transform=False``:

ndarray of shape (n\_classifiers, n\_samples, n\_classes)

If `voting='hard'`:

ndarray of shape (n\_samples, n\_classifiers), being class labels predicted by each classifier.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)