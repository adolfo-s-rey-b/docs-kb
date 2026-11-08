[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.svm.OneClassSVM.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.svm.OneClassSVM.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.OneClassSVM.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.svm.OneClassSVM.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.svm.OneClassSVM.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.svm.OneClassSVM.html)

Collapse Sidebar Expand Sidebar

OneClassSVM[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#oneclasssvm "Link to this heading")

==================================================================================================================================

class sklearn.svm.OneClassSVM(_\*_, _kernel\='rbf'_, _degree\=3_, _gamma\='scale'_, _coef0\=0.0_, _tol\=0.001_, _nu\=0.5_, _shrinking\=True_, _cache\_size\=200_, _verbose\=False_, _max\_iter\=\-1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1573)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "Link to this definition")

Unsupervised Outlier Detection.

Estimate the support of a high-dimensional distribution.

The implementation is based on libsvm.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
.

Parameters:

**kernel**{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’

Specifies the kernel type to be used in the algorithm. If none is given, ‘rbf’ will be used. If a callable is given it is used to precompute the kernel matrix.

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

**tol**float, default=1e-3

Tolerance for stopping criterion.

**nu**float, default=0.5

An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1\]. By default 0.5 will be taken.

**shrinking**bool, default=True

Whether to use the shrinking heuristic. See the [User Guide](https://scikit-learn.org/stable/modules/svm.html#shrinking-svm)
.

**cache\_size**float, default=200

Specify the size of the kernel cache (in MB).

**verbose**bool, default=False

Enable verbose output. Note that this setting takes advantage of a per-process runtime setting in libsvm that, if enabled, may not work properly in a multithreaded context.

**max\_iter**int, default=-1

Hard limit on iterations within solver, or -1 for no limit.

Attributes:

`coef_`ndarray or sparse array/matrix of shape (1, n\_features)

Weights assigned to the features when `kernel="linear"`.

**dual\_coef\_**ndarray or sparse array/matrix of shape (1, n\_SV)

Coefficients of the support vectors in the decision function. If `X` is sparse, these will also be sparse.

**fit\_status\_**int

0 if correctly fitted, 1 otherwise (will raise warning)

**intercept\_**ndarray of shape (1,)

Constant in the decision function.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

Number of iterations run by the optimization routine to fit the model.

Added in version 1.1.

`n_support_`ndarray of shape (n\_classes,), dtype=int32

Number of support vectors for each class.

**offset\_**float

Offset used to define the decision function from the raw scores. We have the relation: decision\_function = score\_samples - `offset_`. The offset is the opposite of `intercept_` and is provided for consistency with other outlier detection algorithms.

Added in version 0.20.

**shape\_fit\_**tuple of int of shape (n\_dimensions\_of\_X,)

Array dimensions of training vector `X`.

**support\_**ndarray of shape (n\_SV,)

Indices of support vectors.

**support\_vectors\_**ndarray or sparse array/matrix of shape (n\_SV, n\_features)

Support vectors. If `X` is sparse, these will also be sparse.

See also

[`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")

Solves linear One-Class SVM using Stochastic Gradient Descent.

[`sklearn.neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")

Unsupervised Outlier Detection using Local Outlier Factor (LOF).

[`sklearn.ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")

Isolation Forest Algorithm.

Examples

\>>> from sklearn.svm import OneClassSVM
\>>> X \= \[\[0\], \[0.44\], \[0.45\], \[0.46\], \[1\]\]
\>>> clf \= OneClassSVM(gamma\='auto').fit(X)
\>>> clf.predict(X)
array(\[-1,  1,  1,  1, -1\])
\>>> clf.score\_samples(X)
array(\[1.7798, 2.0547, 2.0556, 2.0561, 1.7332\])

Copy to clipboard

For a more extended example, see [Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#sphx-glr-auto-examples-applications-plot-species-distribution-modeling-py)

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1778)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.decision_function "Link to this definition")

Signed distance to the separating hyperplane.

Signed distance is positive for an inlier and negative for an outlier.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**dec**ndarray of shape (n\_samples,)

Returns the decision function of the samples.

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1749)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.fit "Link to this definition")

Detect the soft boundary of the set of samples X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Set of samples, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

**sample\_weight**array-like of shape (n\_samples,), default=None

Per-sample weights. Rescale C per sample. Higher weights force the classifier to put more emphasis on these points.

Returns:

**self**object

Fitted estimator.

Notes

If X is not a C-ordered contiguous array it is copied.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1141)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.fit_predict "Link to this definition")

Perform fit on X and returns labels for X.

Returns -1 for outliers and 1 for inliers.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The input samples.

**y**Ignored

Not used, present for API consistency by convention.

**\*\*kwargs**dict

Arguments to be passed to `fit`.

Added in version 1.4.

Returns:

**y**ndarray of shape (n\_samples,)

1 for inliers, -1 for outliers.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1811)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.predict "Link to this definition")

Perform classification on samples in X.

For a one-class model, +1 or -1 is returned.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features) or (n\_samples\_test, n\_samples\_train)

For kernel=”precomputed”, the expected shape of X is (n\_samples\_test, n\_samples\_train).

Returns:

**y\_pred**ndarray of shape (n\_samples,)

Class labels for samples in X.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1796)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.score_samples "Link to this definition")

Raw scoring function of the samples.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**score\_samples**ndarray of shape (n\_samples,)

Returns the (unshifted) scoring function of the samples.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm._classes.OneClassSVM")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)

[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_oneclass_thumb.png)

[One-class SVM with non-linear kernel (RBF)](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html)

One-class SVM with non-linear kernel (RBF)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)