[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.multioutput.ClassifierChain.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.multioutput.ClassifierChain.html)

Collapse Sidebar Expand Sidebar

ClassifierChain[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#classifierchain "Link to this heading")

======================================================================================================================================================

class sklearn.multioutput.ClassifierChain(_estimator_, _\*_, _order\=None_, _cv\=None_, _chain\_method\='predict'_, _random\_state\=None_, _verbose\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L842)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "Link to this definition")

A multi-label model that arranges binary classifiers into a chain.

Each model makes a prediction in the order specified by the chain using all of the available features provided to the model plus the predictions of models that are earlier in the chain.

For an example of how to use `ClassifierChain` and benefit from its ensemble, see [ClassifierChain on a yeast dataset](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#sphx-glr-auto-examples-multioutput-plot-classifier-chain-yeast-py)
 example.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/multiclass.html#classifierchain)
.

Added in version 0.19.

Parameters:

**estimator**estimator

The base estimator from which the classifier chain is built.

**order**array-like of shape (n\_outputs,) or ‘random’, default=None

If `None`, the order will be determined by the order of columns in the label matrix Y.:

order \= \[0, 1, 2, ..., Y.shape\[1\] \- 1\]

Copy to clipboard

The order of the chain can be explicitly set by providing a list of integers. For example, for a chain of length 5.:

order \= \[1, 3, 2, 4, 0\]

Copy to clipboard

means that the first model in the chain will make predictions for column 1 in the Y matrix, the second model will make predictions for column 3, etc.

If order is `random` a random ordering will be used.

**cv**int, cross-validation generator or an iterable, default=None

Determines whether to use cross validated predictions or true labels for the results of previous estimators in the chain. Possible inputs for cv are:

*   None, to use true labels when fitting,
    
*   integer, to specify the number of folds in a (Stratified)KFold,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

**chain\_method**{‘predict’, ‘predict\_proba’, ‘predict\_log\_proba’, ‘decision\_function’} or list of such str’s, default=’predict’

Prediction method to be used by estimators in the chain for the ‘prediction’ features of previous estimators in the chain.

*   if `str`, name of the method;
    
*   if a list of `str`, provides the method names in order of preference. The method used corresponds to the first method in the list that is implemented by `base_estimator`.
    

Added in version 1.5.

**random\_state**int, RandomState instance or None, optional (default=None)

If `order='random'`, determines random number generation for the chain order. In addition, it controls the random seed given at each `base_estimator` at each chaining iteration. Thus, it is only used when `base_estimator` exposes a `random_state`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**verbose**bool, default=False

If True, chain progress is output as each model is completed.

Added in version 1.2.

Attributes:

**classes\_**list

A list of arrays of length `len(estimators_)` containing the class labels for each estimator in the chain.

**estimators\_**list

A list of clones of base\_estimator.

**order\_**list

The order of labels in the classifier chain.

**chain\_method\_**str

Prediction method used by estimators in the chain for the prediction features.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if the underlying `base_estimator` exposes such an attribute when fit.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")

Equivalent for regression.

[`MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")

Classifies each output independently rather than chaining.

References

Jesse Read, Bernhard Pfahringer, Geoff Holmes, Eibe Frank, “Classifier Chains for Multi-label Classification”, 2009.

Examples

\>>> from sklearn.datasets import make\_multilabel\_classification
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.multioutput import ClassifierChain
\>>> X, Y \= make\_multilabel\_classification(
...    n\_samples\=12, n\_classes\=3, random\_state\=0
... )
\>>> X\_train, X\_test, Y\_train, Y\_test \= train\_test\_split(
...    X, Y, random\_state\=0
... )
\>>> base\_lr \= LogisticRegression(solver\='lbfgs', random\_state\=0)
\>>> chain \= ClassifierChain(base\_lr, order\='random', random\_state\=0)
\>>> chain.fit(X\_train, Y\_train).predict(X\_test)
array(\[\[1., 1., 0.\],\
       \[1., 0., 0.\],\
       \[0., 1., 0.\]\])
\>>> chain.predict\_proba(X\_test)
array(\[\[0.8387, 0.9431, 0.4576\],\
       \[0.8878, 0.3684, 0.2640\],\
       \[0.0321, 0.9935, 0.0626\]\])

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L1075)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.decision_function "Link to this definition")

Evaluate the decision\_function of the models in the chain.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input data.

Returns:

**Y\_decision**array-like of shape (n\_samples, n\_classes)

Returns the decision function of the sample for each model in the chain.

fit(_X_, _Y_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L1010)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.fit "Link to this definition")

Fit the model to data matrix X and targets Y.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

**Y**array-like of shape (n\_samples, n\_classes)

The target values.

**\*\*fit\_params**dict of string -> object

Parameters passed to the `fit` method of each step.

Only available if `enable_metadata_routing=True`. See the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
.

Added in version 1.3.

Returns:

**self**object

Class instance.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L1092)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.3.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L821)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.predict "Link to this definition")

Predict on the data matrix X using the ClassifierChain model.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

Returns:

**Y\_pred**array-like of shape (n\_samples, n\_classes)

The predicted values.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L1060)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.predict_log_proba "Link to this definition")

Predict logarithm of probability estimates.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

Returns:

**Y\_log\_prob**array-like of shape (n\_samples, n\_classes)

The predicted logarithm of the probabilities.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/multioutput.py#L1044)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.predict_proba "Link to this definition")

Predict probability estimates.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input data.

Returns:

**Y\_prob**array-like of shape (n\_samples, n\_classes)

The predicted probabilities.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [ClassifierChain](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

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