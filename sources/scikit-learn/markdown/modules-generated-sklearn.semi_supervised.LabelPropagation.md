[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.semi_supervised.LabelPropagation.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.semi_supervised.LabelPropagation.html)

Collapse Sidebar Expand Sidebar

LabelPropagation[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#labelpropagation "Link to this heading")

=============================================================================================================================================================

class sklearn.semi\_supervised.LabelPropagation(_kernel\='rbf'_, _\*_, _gamma\=20_, _n\_neighbors\=7_, _max\_iter\=1000_, _tol\=0.001_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_label_propagation.py#L346)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "Link to this definition")

Label Propagation classifier.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/semi_supervised.html#label-propagation)
.

Parameters:

**kernel**{‘knn’, ‘rbf’} or callable, default=’rbf’

String identifier for kernel function to use or the kernel function itself. Only ‘rbf’ and ‘knn’ strings are valid inputs. The function passed should take two inputs, each of shape (n\_samples, n\_features), and return a (n\_samples, n\_samples) shaped weight matrix.

**gamma**float, default=20

Parameter for rbf kernel.

**n\_neighbors**int, default=7

Parameter for knn kernel which need to be strictly positive.

**max\_iter**int, default=1000

Change maximum number of iterations allowed.

**tol**float, default=1e-3

Convergence tolerance: threshold to consider the system at steady state.

**n\_jobs**int, default=None

The number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**X\_**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Input array.

**classes\_**ndarray of shape (n\_classes,)

The distinct labels used in classifying instances.

**label\_distributions\_**ndarray of shape (n\_samples, n\_classes)

Categorical distribution for each item.

**transduction\_**ndarray of shape (n\_samples)

Label assigned to each item during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

Number of iterations run.

See also

[`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")

Alternate label propagation strategy more robust to noise.

References

Xiaojin Zhu and Zoubin Ghahramani. Learning from labeled and unlabeled data with label propagation. Technical Report CMU-CALD-02-107, Carnegie Mellon University, 2002 [http://pages.cs.wisc.edu/~jerryzhu/pub/CMU-CALD-02-107.pdf](http://pages.cs.wisc.edu/~jerryzhu/pub/CMU-CALD-02-107.pdf)

Examples

\>>> import numpy as np
\>>> from sklearn import datasets
\>>> from sklearn.semi\_supervised import LabelPropagation
\>>> label\_prop\_model \= LabelPropagation()
\>>> iris \= datasets.load\_iris()
\>>> rng \= np.random.RandomState(42)
\>>> random\_unlabeled\_points \= rng.rand(len(iris.target)) < 0.3
\>>> labels \= np.copy(iris.target)
\>>> labels\[random\_unlabeled\_points\] \= \-1
\>>> label\_prop\_model.fit(iris.data, labels)
LabelPropagation(...)

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_label_propagation.py#L478)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.fit "Link to this definition")

Fit a semi-supervised label propagation model to X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,)

Target class values with unlabeled points marked as -1. All unlabeled samples will be transductively assigned labels internally, which are stored in `transduction_`.

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_label_propagation.py#L174)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.predict "Link to this definition")

Perform inductive inference across the model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**y**ndarray of shape (n\_samples,)

Predictions for input data.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/semi_supervised/_label_propagation.py#L194)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.predict_proba "Link to this definition")

Predict probability for each possible outcome.

Compute the probability estimates for each single sample in X and each possible outcome seen during training (categorical distribution).

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**probabilities**ndarray of shape (n\_samples, n\_classes)

Normalized probability distributions across class labels.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [LabelPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised._label_propagation.LabelPropagation")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.set_score_request "Link to this definition")

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

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)