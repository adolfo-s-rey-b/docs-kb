[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.NearestCentroid.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.NearestCentroid.html)

Collapse Sidebar Expand Sidebar

NearestCentroid[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#nearestcentroid "Link to this heading")

====================================================================================================================================================

class sklearn.neighbors.NearestCentroid(_metric\='euclidean'_, _\*_, _shrink\_threshold\=None_, _priors\='uniform'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nearest_centroid.py#L26)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "Link to this definition")

Nearest centroid classifier.

Each class is represented by its centroid, with test samples classified to the class with the nearest centroid.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#nearest-centroid-classifier)
.

Parameters:

**metric**{“euclidean”, “manhattan”}, default=”euclidean”

Metric to use for distance computation.

If `metric="euclidean"`, the centroid for the samples corresponding to each class is the arithmetic mean, which minimizes the sum of squared L1 distances. If `metric="manhattan"`, the centroid is the feature-wise median, which minimizes the sum of L1 distances.

Changed in version 1.5: All metrics but `"euclidean"` and `"manhattan"` were deprecated and now raise an error.

Changed in version 0.19: `metric='precomputed'` was deprecated and now raises an error

**shrink\_threshold**float, default=None

Threshold for shrinking centroids to remove features.

**priors**{“uniform”, “empirical”} or array-like of shape (n\_classes,), default=”uniform”

The class prior probabilities. By default, the class proportions are inferred from the training data.

Added in version 1.6.

Attributes:

**centroids\_**array-like of shape (n\_classes, n\_features)

Centroid of each class.

**classes\_**array of shape (n\_classes,)

The unique classes labels.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**deviations\_**ndarray of shape (n\_classes, n\_features)

Deviations (or shrinkages) of the centroids of each class from the overall centroid. Equal to eq. (18.4) if `shrink_threshold=None`, else (18.5) p. 653 of \[2\]. Can be used to identify features used for classification.

Added in version 1.6.

**within\_class\_std\_dev\_**ndarray of shape (n\_features,)

Pooled or within-class standard deviation of input data.

Added in version 1.6.

**class\_prior\_**ndarray of shape (n\_classes,)

The class prior probabilities.

Added in version 1.6.

See also

[`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")

Nearest neighbors classifier.

Notes

When used for text classification with tf-idf vectors, this classifier is also known as the Rocchio classifier.

References

\[1\] Tibshirani, R., Hastie, T., Narasimhan, B., & Chu, G. (2002). Diagnosis of multiple cancer types by shrunken centroids of gene expression. Proceedings of the National Academy of Sciences of the United States of America, 99(10), 6567-6572. The National Academy of Sciences.

\[2\] Hastie, T., Tibshirani, R., Friedman, J. (2009). The Elements of Statistical Learning Data Mining, Inference, and Prediction. 2nd Edition. New York, Springer.

Examples

\>>> from sklearn.neighbors import NearestCentroid
\>>> import numpy as np
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[\-3, \-2\], \[1, 1\], \[2, 1\], \[3, 2\]\])
\>>> y \= np.array(\[1, 1, 1, 2, 2, 2\])
\>>> clf \= NearestCentroid()
\>>> clf.fit(X, y)
NearestCentroid()
\>>> print(clf.predict(\[\[\-0.8, \-1\]\]))
\[1\]

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/discriminant_analysis.py#L180)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.decision_function "Link to this definition")

Apply decision function to an array of samples.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Array of samples (test vectors).

Returns:

**y\_scores**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Decision function values related to each class, per sample. In the two-class case, the shape is `(n_samples,)`, giving the log likelihood ratio of the positive class.

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nearest_centroid.py#L149)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.fit "Link to this definition")

Fit the NearestCentroid model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features. Note that centroid shrinking cannot be used with sparse matrices.

**y**array-like of shape (n\_samples,)

Target values.

Returns:

**self**object

Fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nearest_centroid.py#L275)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.predict "Link to this definition")

Perform classification on an array of test vectors `X`.

The predicted class `C` for each sample in `X` is returned.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

The predicted classes.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/discriminant_analysis.py#L235)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.predict_log_proba "Link to this definition")

Estimate log class probabilities.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**y\_log\_proba**ndarray of shape (n\_samples, n\_classes)

Estimated log probabilities.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/discriminant_analysis.py#L219)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.predict_proba "Link to this definition")

Estimate class probabilities.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input data.

Returns:

**y\_proba**ndarray of shape (n\_samples, n\_classes)

Probability estimate of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors._nearest_centroid.NearestCentroid")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)