[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.svm.NuSVC.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.svm.NuSVC.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.NuSVC.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.svm.NuSVC.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.svm.NuSVC.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.svm.NuSVC.html)

Collapse Sidebar Expand Sidebar

NuSVC[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#nusvc "Link to this heading")

================================================================================================================

class sklearn.svm.NuSVC(_\*_, _nu\=0.5_, _kernel\='rbf'_, _degree\=3_, _gamma\='scale'_, _coef0\=0.0_, _shrinking\=True_, _probability\='deprecated'_, _tol\=0.001_, _cache\_size\=200_, _class\_weight\=None_, _verbose\=False_, _max\_iter\=\-1_, _decision\_function\_shape\='ovr'_, _break\_ties\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L915)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "Link to this definition")

Nu-Support Vector Classification.

Similar to SVC but uses a parameter to control the number of support vectors.

The implementation is based on libsvm.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
.

Parameters:

**nu**float, default=0.5

An upper bound on the fraction of margin errors (see [User Guide](https://scikit-learn.org/stable/modules/svm.html#nu-svc)
) and a lower bound of the fraction of support vectors. Should be in the interval (0, 1\].

**kernel**{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’

Specifies the kernel type to be used in the algorithm. If none is given, ‘rbf’ will be used. If a callable is given it is used to precompute the kernel matrix. For an intuitive visualization of different kernel types see [Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#sphx-glr-auto-examples-svm-plot-svm-kernels-py)
.

**degree**int, default=3

Degree of the polynomial kernel function (‘poly’). Must be non-negative. Ignored by all other kernels.

**gamma**{‘scale’, ‘auto’} or float, default=’scale’

Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.

*   if `gamma='scale'` (default) is passed then it uses 1 / (n\_features \* X.var()) as value of gamma,
    
*   if ‘auto’, uses 1 / n\_features
    
*   if float, must be non-negative.
    

Changed in version 0.22: The default value of `gamma` changed from ‘auto’ to ‘scale’.

**coef0**float, default=0.0

Independent term in kernel function. It is only significant in ‘poly’ and ‘sigmoid’.

**shrinking**bool, default=True

Whether to use the shrinking heuristic. See the [User Guide](https://scikit-learn.org/stable/modules/svm.html#shrinking-svm)
.

**probability**bool, default=False

Whether to enable probability estimates. This must be enabled prior to calling `fit`, will slow down that method as it internally uses 5-fold cross-validation, and `predict_proba` may be inconsistent with `predict`. Read more in the [User Guide](https://scikit-learn.org/stable/modules/svm.html#scores-probabilities)
.

..deprecated:: 1.9

The `probability` parameter is deprecated and will be removed in version 1.11. Use `CalibratedClassifierCV(NuSVC(), ensemble=False)` instead of `NuSVC(probability=True)`.

**tol**float, default=1e-3

Tolerance for stopping criterion.

**cache\_size**float, default=200

Specify the size of the kernel cache (in MB).

**class\_weight**{dict, ‘balanced’}, default=None

Set the parameter C of class i to class\_weight\[i\]\*C for SVC. If not given, all classes are supposed to have weight one. The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies as `n_samples / (n_classes * np.bincount(y))`.

**verbose**bool, default=False

Enable verbose output. Note that this setting takes advantage of a per-process runtime setting in libsvm that, if enabled, may not work properly in a multithreaded context.

**max\_iter**int, default=-1

Hard limit on iterations within solver, or -1 for no limit.

**decision\_function\_shape**{‘ovo’, ‘ovr’}, default=’ovr’

Whether to return a one-vs-rest (‘ovr’) decision function of shape (n\_samples, n\_classes) as all other classifiers, or the original one-vs-one (‘ovo’) decision function of libsvm which has shape (n\_samples, n\_classes \* (n\_classes - 1) / 2). However, one-vs-one (‘ovo’) is always used as multi-class strategy. The parameter is ignored for binary classification.

Changed in version 0.19: decision\_function\_shape is ‘ovr’ by default.

Added in version 0.17: _decision\_function\_shape=’ovr’_ is recommended.

Changed in version 0.17: Deprecated _decision\_function\_shape=’ovo’ and None_.

**break\_ties**bool, default=False

If true, `decision_function_shape='ovr'`, and number of classes > 2, [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 will break ties according to the confidence values of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
; otherwise the first class among the tied classes is returned. Please note that breaking ties comes at a relatively high computational cost compared to a simple predict. See [SVM Tie Breaking Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html#sphx-glr-auto-examples-svm-plot-svm-tie-breaking-py)
 for an example of its usage with `decision_function_shape='ovr'`.

Added in version 0.22.

**random\_state**int, RandomState instance or None, default=None

Controls the pseudo random number generation for shuffling the data for probability estimates. Ignored when `probability` is False. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**class\_weight\_**ndarray of shape (n\_classes,)

Multipliers of parameter C of each class. Computed based on the `class_weight` parameter.

**classes\_**ndarray of shape (n\_classes,)

The unique classes labels.

`coef_`ndarray or sparse array/matrix of shape (n\_classes \* (n\_classes -1) / 2, n\_features)

Weights assigned to the features when `kernel="linear"`.

**dual\_coef\_**ndarray or sparse array/matrix of shape (n\_classes - 1, n\_SV)

Dual coefficients of the support vector in the decision function (see [Mathematical formulation](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
), multiplied by their targets. For multiclass, coefficient for all 1-vs-1 classifiers. The layout of the coefficients in the multiclass case is somewhat non-trivial. See the [multi-class section of the User Guide](https://scikit-learn.org/stable/modules/svm.html#svm-multi-class)
 for details. If `X` is sparse, these will also be sparse.

**fit\_status\_**int

0 if correctly fitted, 1 if the algorithm did not converge.

**intercept\_**ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)

Constants in decision function.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**ndarray of shape (n\_classes \* (n\_classes - 1) // 2,)

Number of iterations run by the optimization routine to fit the model. The shape of this attribute depends on the number of models optimized which in turn depends on the number of classes.

Added in version 1.1.

**support\_**ndarray of shape (n\_SV,)

Indices of support vectors.

**support\_vectors\_**ndarray or sparse array/matrix of shape (n\_SV, n\_features)

Support vectors. If `X` is sparse, these will also be sparse.

`n_support_`ndarray of shape (n\_classes,), dtype=int32

Number of support vectors for each class.

**fit\_status\_**int

0 if correctly fitted, 1 if the algorithm did not converge.

`probA_`ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)

Parameter learned in Platt scaling when `probability=True`.

`probB_`ndarray of shape (n\_classes \* (n\_classes - 1) / 2,)

Parameter learned in Platt scaling when `probability=True`.

**shape\_fit\_**tuple of int of shape (n\_dimensions\_of\_X,)

Array dimensions of training vector `X`.

See also

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

Support Vector Machine for classification using libsvm.

[`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

Scalable linear Support Vector Machine for classification using liblinear.

References

\[1\]

[LIBSVM: A Library for Support Vector Machines](http://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf)

\[2\]

[Platt, John (1999). “Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods”](https://citeseerx.ist.psu.edu/doc_view/pid/42e5ed832d4310ce4378c44d05570439df28a393)

Examples

\>>> import numpy as np
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[1, 1\], \[2, 1\]\])
\>>> y \= np.array(\[1, 1, 2, 2\])
\>>> from sklearn.pipeline import make\_pipeline
\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.svm import NuSVC
\>>> clf \= make\_pipeline(StandardScaler(), NuSVC())
\>>> clf.fit(X, y)
Pipeline(steps=\[('standardscaler', StandardScaler()), ('nusvc', NuSVC())\])
\>>> print(clf.predict(\[\[\-0.8, \-1\]\]))
\[1\]

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L795)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.decision_function "Link to this definition")

Evaluate the decision function for the samples in X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The input samples.

Returns:

**X**ndarray of shape (n\_samples, n\_classes \* (n\_classes-1) / 2)

Returns the decision function of the sample for each class in the model. If decision\_function\_shape=’ovr’, the shape is (n\_samples, n\_classes).

Notes

If decision\_function\_shape=’ovo’, the function values are proportional to the distance of the samples X to the separating hyperplane. If the exact distances are required, divide the function values by the norm of the weight vector (`coef_`). See also [this question](https://stats.stackexchange.com/questions/14876/interpreting-distance-from-hyperplane-in-svm)
 for further details. If decision\_function\_shape=’ovr’, the decision function is a monotonic transformation of ovo decision function.

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L167)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.fit "Link to this definition")

Fit the SVM model according to the given training data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features. For kernel=”precomputed”, the expected shape of X is (n\_samples, n\_samples).

**y**array-like of shape (n\_samples,)

Target values (class labels in classification, real numbers in regression).

**sample\_weight**array-like of shape (n\_samples,), default=None

Per-sample weights. Rescale C per sample. Higher weights force the classifier to put more emphasis on these points.

Returns:

**self**object

Fitted estimator.

Notes

If X and y are not C-ordered and contiguous arrays of np.float64 and X is not a sparse CSR format, X and/or y may be copied.

If X is a dense array, then the other methods will not support sparse matrices as input.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L827)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.predict "Link to this definition")

Perform classification on samples in X.

For a one-class model, +1 or -1 is returned.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples\_test, n\_samples\_train)

For kernel=”precomputed”, the expected shape of X is (n\_samples\_test, n\_samples\_train).

Returns:

**y\_pred**ndarray of shape (n\_samples,)

Class labels for samples in X.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L910)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.predict_log_proba "Link to this definition")

Compute log probabilities of possible outcomes for samples in X.

The model need to have probability information computed at training time: fit with attribute `probability` set to True.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples\_test, n\_samples\_train)

For kernel=”precomputed”, the expected shape of X is (n\_samples\_test, n\_samples\_train).

Returns:

**T**ndarray of shape (n\_samples, n\_classes)

Returns the log-probabilities of the sample for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

Notes

The probability model is created using cross validation, so the results can be slightly different than those obtained by predict. Also, it will produce meaningless results on very small datasets.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L873)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.predict_proba "Link to this definition")

Compute probabilities of possible outcomes for samples in X.

The model needs to have probability information computed at training time: fit with attribute `probability` set to True.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

For kernel=”precomputed”, the expected shape of X is (n\_samples\_test, n\_samples\_train).

Returns:

**T**ndarray of shape (n\_samples, n\_classes)

Returns the probability of the sample for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

Notes

The probability model is created using cross validation, so the results can be slightly different than those obtained by predict. Also, it will produce meaningless results on very small datasets.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [NuSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm._classes.NuSVC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [NuSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm._classes.NuSVC")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC.set_score_request "Link to this definition")

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