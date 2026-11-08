[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.naive_bayes.BernoulliNB.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.naive_bayes.BernoulliNB.html)

Collapse Sidebar Expand Sidebar

BernoulliNB[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#bernoullinb "Link to this heading")

==========================================================================================================================================

class sklearn.naive\_bayes.BernoulliNB(_\*_, _alpha\=1.0_, _force\_alpha\=True_, _binarize\=0.0_, _fit\_prior\=True_, _class\_prior\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L1094)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "Link to this definition")

Naive Bayes classifier for multivariate Bernoulli models.

Like MultinomialNB, this classifier is suitable for discrete data. The difference is that while MultinomialNB works with occurrence counts, BernoulliNB is designed for binary/boolean features.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes)
.

Parameters:

**alpha**float or array-like of shape (n\_features,), default=1.0

Additive (Laplace/Lidstone) smoothing parameter (set alpha=0 and force\_alpha=True, for no smoothing).

**force\_alpha**bool, default=True

If False and alpha is less than 1e-10, it will set alpha to 1e-10. If True, alpha will remain unchanged. This may cause numerical errors if alpha is too close to 0.

Added in version 1.2.

Changed in version 1.4: The default value of `force_alpha` changed to `True`.

**binarize**float or None, default=0.0

Threshold for binarizing (mapping to booleans) of sample features. If None, input is presumed to already consist of binary vectors.

**fit\_prior**bool, default=True

Whether to learn class prior probabilities or not. If false, a uniform prior will be used.

**class\_prior**array-like of shape (n\_classes,), default=None

Prior probabilities of the classes. If specified, the priors are not adjusted according to the data.

Attributes:

**class\_count\_**ndarray of shape (n\_classes,)

Number of samples encountered for each class during fitting. This value is weighted by the sample weight when provided.

**class\_log\_prior\_**ndarray of shape (n\_classes,)

Log probability of each class (smoothed).

**classes\_**ndarray of shape (n\_classes,)

Class labels known to the classifier

**feature\_count\_**ndarray of shape (n\_classes, n\_features)

Number of samples encountered for each (class, feature) during fitting. This value is weighted by the sample weight when provided.

**feature\_log\_prob\_**ndarray of shape (n\_classes, n\_features)

Empirical log probability of features given a class, P(x\_i|y).

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")

Naive Bayes classifier for categorical features.

[`ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")

The Complement Naive Bayes classifier described in Rennie et al. (2003).

[`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")

Gaussian Naive Bayes (GaussianNB).

[`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")

Naive Bayes classifier for multinomial models.

References

C.D. Manning, P. Raghavan and H. Schuetze (2008). Introduction to Information Retrieval. Cambridge University Press, pp. 234-265. [https://nlp.stanford.edu/IR-book/html/htmledition/the-bernoulli-model-1.html](https://nlp.stanford.edu/IR-book/html/htmledition/the-bernoulli-model-1.html)

A. McCallum and K. Nigam (1998). A comparison of event models for naive Bayes text classification. Proc. AAAI/ICML-98 Workshop on Learning for Text Categorization, pp. 41-48.

V. Metsis, I. Androutsopoulos and G. Paliouras (2006). Spam filtering with naive Bayes – Which naive Bayes? 3rd Conf. on Email and Anti-Spam (CEAS).

Examples

\>>> import numpy as np
\>>> rng \= np.random.RandomState(1)
\>>> X \= rng.randint(5, size\=(6, 100))
\>>> Y \= np.array(\[1, 2, 3, 4, 4, 5\])
\>>> from sklearn.naive\_bayes import BernoulliNB
\>>> clf \= BernoulliNB()
\>>> clf.fit(X, Y)
BernoulliNB()
\>>> print(clf.predict(X\[2:3\]))
\[3\]

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L746)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.fit "Link to this definition")

Fit Naive Bayes classifier according to X, y.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weights applied to individual samples (1. for unweighted).

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y_, _classes\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L663)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.partial_fit "Link to this definition")

Incremental fit on a batch of samples.

This method is expected to be called several times consecutively on different chunks of a dataset so as to implement out-of-core or online learning.

This is especially useful when the whole dataset is too big to fit in memory at once.

This method has some performance overhead hence it is better to call partial\_fit on chunks of data that are as large as possible (as long as fitting in the memory budget) to hide the overhead.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target values.

**classes**array-like of shape (n\_classes,), default=None

List of all the classes that can possibly appear in the y vector.

Must be provided at the first call to partial\_fit, can be omitted in subsequent calls.

**sample\_weight**array-like of shape (n\_samples,), default=None

Weights applied to individual samples (1. for unweighted).

Returns:

**self**object

Returns the instance itself.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L96)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.predict "Link to this definition")

Perform classification on an array of test vectors X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Returns:

**C**ndarray of shape (n\_samples,)

Predicted target values for X.

predict\_joint\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L72)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.predict_joint_log_proba "Link to this definition")

Return joint log probability estimates for the test vector X.

For each row x of X and class y, the joint log probability is given by `log P(x, y) = log P(y) + log P(x|y),` where `log P(y)` is the class prior probability and `log P(x|y)` is the class-conditional probability.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Returns:

**C**ndarray of shape (n\_samples, n\_classes)

Returns the joint log-probability of the samples for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L119)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.predict_log_proba "Link to this definition")

Return log-probability estimates for the test vector X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Returns:

**C**array-like of shape (n\_samples, n\_classes)

Returns the log-probability of the samples for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/naive_bayes.py#L143)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.predict_proba "Link to this definition")

Return probability estimates for the test vector X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Returns:

**C**array-like of shape (n\_samples, n\_classes)

Returns the probability of the samples for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.score "Link to this definition")

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

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.set_partial_fit_request "Link to this definition")

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

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_thumb.png)

[Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)

Hashing feature transformation using Totally Random Trees

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)