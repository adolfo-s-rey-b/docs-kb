[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.svm.NuSVR.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.svm.NuSVR.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.NuSVR.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.svm.NuSVR.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.svm.NuSVR.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.svm.NuSVR.html)

Collapse Sidebar Expand Sidebar

NuSVR[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#nusvr "Link to this heading")

================================================================================================================

class sklearn.svm.NuSVR(_\*_, _nu\=0.5_, _C\=1.0_, _kernel\='rbf'_, _degree\=3_, _gamma\='scale'_, _coef0\=0.0_, _shrinking\=True_, _tol\=0.001_, _cache\_size\=200_, _verbose\=False_, _max\_iter\=\-1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_classes.py#L1385)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "Link to this definition")

Nu Support Vector Regression.

Similar to NuSVC, for regression, uses a parameter nu to control the number of support vectors. However, unlike NuSVC, where nu replaces C, here nu replaces the parameter epsilon of epsilon-SVR.

The implementation is based on libsvm.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/svm.html#svm-regression)
.

Parameters:

**nu**float, default=0.5

An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1\]. By default 0.5 will be taken.

**C**float, default=1.0

Penalty parameter C of the error term. For an intuitive visualization of the effects of scaling the regularization parameter C, see [Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#sphx-glr-auto-examples-svm-plot-svm-scale-c-py)
.

**kernel**{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’

Specifies the kernel type to be used in the algorithm. If none is given, ‘rbf’ will be used. If a callable is given it is used to precompute the kernel matrix. For an intuitive visualization of different kernel types see See [Support Vector Regression (SVR) using linear and non-linear kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#sphx-glr-auto-examples-svm-plot-svm-regression-py)

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

**tol**float, default=1e-3

Tolerance for stopping criterion.

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

Coefficients of the support vector in the decision function. If `X` is sparse, these will also be sparse.

**fit\_status\_**int

0 if correctly fitted, 1 otherwise (will raise warning)

**intercept\_**ndarray of shape (1,)

Constants in decision function.

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

`n_support_`ndarray of shape (1,), dtype=int32

Number of support vectors for each class.

**shape\_fit\_**tuple of int of shape (n\_dimensions\_of\_X,)

Array dimensions of training vector `X`.

**support\_**ndarray of shape (n\_SV,)

Indices of support vectors.

**support\_vectors\_**ndarray or sparse array/matrix of shape (n\_SV, n\_features)

Support vectors. If `X` is sparse, these will also be sparse.

See also

[`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")

Support Vector Machine for classification implemented with libsvm with a parameter to control the number of support vectors.

[`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")

Epsilon Support Vector Machine for regression implemented with libsvm.

References

\[1\]

[LIBSVM: A Library for Support Vector Machines](http://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf)

\[2\]

[Platt, John (1999). “Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods”](https://citeseerx.ist.psu.edu/doc_view/pid/42e5ed832d4310ce4378c44d05570439df28a393)

Examples

\>>> from sklearn.svm import NuSVR
\>>> from sklearn.pipeline import make\_pipeline
\>>> from sklearn.preprocessing import StandardScaler
\>>> import numpy as np
\>>> n\_samples, n\_features \= 10, 5
\>>> np.random.seed(0)
\>>> y \= np.random.randn(n\_samples)
\>>> X \= np.random.randn(n\_samples, n\_features)
\>>> regr \= make\_pipeline(StandardScaler(), NuSVR(C\=1.0, nu\=0.1))
\>>> regr.fit(X, y)
Pipeline(steps=\[('standardscaler', StandardScaler()),\
                ('nusvr', NuSVR(nu=0.1))\])

Copy to clipboard

fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L167)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.fit "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/svm/_base.py#L455)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.predict "Link to this definition")

Perform regression on samples in X.

For a one-class model, +1 (inlier) or -1 (outlier) is returned.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

For kernel=”precomputed”, the expected shape of X is (n\_samples\_test, n\_samples\_train).

Returns:

**y\_pred**ndarray of shape (n\_samples,)

The predicted values.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.score "Link to this definition")

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
 \= '$UNCHANGED$'_) → [NuSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm._classes.NuSVR")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.set_fit_request "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [NuSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm._classes.NuSVR")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_model_complexity_influence_thumb.png)

[Model Complexity Influence](https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html)

Model Complexity Influence

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)