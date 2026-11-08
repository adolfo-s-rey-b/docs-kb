[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.SGDOneClassSVM.html)

Collapse Sidebar Expand Sidebar

SGDOneClassSVM[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sgdoneclasssvm "Link to this heading")

====================================================================================================================================================

class sklearn.linear\_model.SGDOneClassSVM(_nu\=0.5_, _fit\_intercept\=True_, _max\_iter\=1000_, _tol\=0.001_, _shuffle\=True_, _verbose\=0_, _random\_state\=None_, _learning\_rate\='optimal'_, _eta0\=0.01_, _power\_t\=0.5_, _warm\_start\=False_, _average\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2125)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "Link to this definition")

Solves linear One-Class SVM using Stochastic Gradient Descent.

This implementation is meant to be used with a kernel approximation technique (e.g. `sklearn.kernel_approximation.Nystroem`) to obtain results similar to `sklearn.svm.OneClassSVM` which uses a Gaussian kernel by default.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/sgd.html#sgd-online-one-class-svm)
.

Added in version 1.0.

Parameters:

**nu**float, default=0.5

The nu parameter of the One Class SVM: an upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1\]. By default 0.5 will be taken.

**fit\_intercept**bool, default=True

Whether the intercept should be estimated or not. Defaults to True.

**max\_iter**int, default=1000

The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the `fit` method, and not the `partial_fit`. Defaults to 1000. Values must be in the range `[1, inf)`.\
\
**tol**float or None, default=1e-3\
\
The stopping criterion. If it is not None, the iterations will stop when (loss > previous\_loss - tol). Defaults to 1e-3. Values must be in the range `[0.0, inf)`.\
\
**shuffle**bool, default=True\
\
Whether or not the training data should be shuffled after each epoch. Defaults to True.\
\
**verbose**int, default=0\
\
The verbosity level.\
\
**random\_state**int, RandomState instance or None, default=None\
\
The seed of the pseudo random number generator to use when shuffling the data. If int, random\_state is the seed used by the random number generator; If RandomState instance, random\_state is the random number generator; If None, the random number generator is the RandomState instance used by `np.random`.\
\
**learning\_rate**{‘constant’, ‘optimal’, ‘invscaling’, ‘adaptive’}, default=’optimal’\
\
The learning rate schedule to use with `fit`. (If using `partial_fit`, learning rate must be controlled directly).\
\
*   ‘constant’: `eta = eta0`\
    \
*   ‘optimal’: `eta = 1.0 / (alpha * (t + t0))` where t0 is chosen by a heuristic proposed by Leon Bottou.\
    \
*   ‘invscaling’: `eta = eta0 / pow(t, power_t)`\
    \
*   ‘adaptive’: eta = eta0, as long as the training keeps decreasing. Each time n\_iter\_no\_change consecutive epochs fail to decrease the training loss by tol or fail to increase validation score by tol if early\_stopping is True, the current learning rate is divided by 5.\
    \
\
**eta0**float, default=0.01\
\
The initial learning rate for the ‘constant’, ‘invscaling’ or ‘adaptive’ schedules. The default value is 0.0, but note that eta0 is not used by the default learning rate ‘optimal’. Values must be in the range `(0.0, inf)`.\
\
**power\_t**float, default=0.5\
\
The exponent for inverse scaling learning rate. Values must be in the range `[0.0, inf)`.\
\
Deprecated since version 1.8: Negative values for `power_t` are deprecated in version 1.8 and will raise an error in 1.10. Use values in the range \[0.0, inf) instead.\
\
**warm\_start**bool, default=False\
\
When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)\
.\
\
Repeatedly calling fit or partial\_fit when warm\_start is True can result in a different solution than when calling fit a single time because of the way the data is shuffled. If a dynamic learning rate is used, the learning rate is adapted depending on the number of samples already seen. Calling `fit` resets this counter, while `partial_fit` will result in increasing the existing counter.\
\
**average**bool or int, default=False\
\
When set to True, computes the averaged SGD weights and stores the result in the `coef_` attribute. If set to an int greater than 1, averaging will begin once the total number of samples seen reaches average. So `average=10` will begin averaging after seeing 10 samples.\
\
Attributes:\
\
**coef\_**ndarray of shape (1, n\_features)\
\
Weights assigned to the features.\
\
**offset\_**ndarray of shape (1,)\
\
Offset used to define the decision function from the raw scores. We have the relation: decision\_function = score\_samples - offset.\
\
**n\_iter\_**int\
\
The actual number of iterations to reach the stopping criterion.\
\
**t\_**int\
\
Number of weight updates performed during training. Same as `(n_iter_ * n_samples + 1)`.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
See also\
\
[`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")\
\
Unsupervised Outlier Detection.\
\
Notes\
\
This estimator has a linear complexity in the number of training samples and is thus better suited than the `sklearn.svm.OneClassSVM` implementation for datasets with a large number of training samples (say > 10,000).\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn import linear\_model\
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[1, 1\], \[2, 1\]\])\
\>>> clf \= linear\_model.SGDOneClassSVM(random\_state\=42, tol\=None)\
\>>> clf.fit(X)\
SGDOneClassSVM(random\_state=42, tol=None)\
\
Copy to clipboard\
\
\>>> print(clf.predict(\[\[4, 4\]\]))\
\[1\]\
\
Copy to clipboard\
\
decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2620)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.decision_function "Link to this definition")\
\
Signed distance to the separating hyperplane.\
\
Signed distance is positive for an inlier and negative for an outlier.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Testing data.\
\
Returns:\
\
**dec**array-like, shape (n\_samples,)\
\
Decision function values of the samples.\
\
densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.densify "Link to this definition")\
\
Convert coefficient matrix to dense array format.\
\
Converts the `coef_` member (back) to a numpy.ndarray. This is the default format of `coef_` and is required for fitting, so calling this method is only required on models that have previously been sparsified; otherwise, it is a no-op.\
\
Returns:\
\
self\
\
Fitted estimator.\
\
fit(_X_, _y\=None_, _coef\_init\=None_, _offset\_init\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2572)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.fit "Link to this definition")\
\
Fit linear One-Class SVM with Stochastic Gradient Descent.\
\
This solves an equivalent optimization problem of the One-Class SVM primal optimization problem and returns a weight vector w and an offset rho such that the decision function is given by <w, x> - rho.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Training data.\
\
**y**Ignored\
\
Not used, present for API consistency by convention.\
\
**coef\_init**array, shape (n\_classes, n\_features)\
\
The initial coefficients to warm-start the optimization.\
\
**offset\_init**array, shape (n\_classes,)\
\
The initial offset to warm-start the optimization.\
\
**sample\_weight**array-like, shape (n\_samples,), optional\
\
Weights applied to individual samples. If not provided, uniform weights are assumed. These weights will be multiplied with class\_weight (passed through the constructor) if class\_weight is specified.\
\
Returns:\
\
**self**object\
\
Returns a fitted instance of self.\
\
fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1141)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.fit_predict "Link to this definition")\
\
Perform fit on X and returns labels for X.\
\
Returns -1 for outliers and 1 for inliers.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input samples.\
\
**y**Ignored\
\
Not used, present for API consistency by convention.\
\
**\*\*kwargs**dict\
\
Arguments to be passed to `fit`.\
\
Added in version 1.4.\
\
Returns:\
\
**y**ndarray of shape (n\_samples,)\
\
1 for inliers, -1 for outliers.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
partial\_fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2480)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.partial_fit "Link to this definition")\
\
Fit linear One-Class SVM with Stochastic Gradient Descent.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Subset of the training data.\
\
**y**Ignored\
\
Not used, present for API consistency by convention.\
\
**sample\_weight**array-like, shape (n\_samples,), optional\
\
Weights applied to individual samples. If not provided, uniform weights are assumed.\
\
Returns:\
\
**self**object\
\
Returns a fitted instance of self.\
\
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2660)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.predict "Link to this definition")\
\
Return labels (1 inlier, -1 outlier) of the samples.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Testing data.\
\
Returns:\
\
**y**array, shape (n\_samples,)\
\
Labels of the samples.\
\
score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L2644)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.score_samples "Link to this definition")\
\
Raw scoring function of the samples.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Testing data.\
\
Returns:\
\
**score\_samples**array-like, shape (n\_samples,)\
\
Unshiffted scoring function values of the samples.\
\
set\_fit\_request(_\*_, _coef\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _offset\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model._stochastic_gradient.SGDOneClassSVM")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.set_fit_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `fit` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**coef\_init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `coef_init` parameter in `fit`.\
\
**offset\_init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `offset_init` parameter in `fit`.\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `fit`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
set\_partial\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [SGDOneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model._stochastic_gradient.SGDOneClassSVM")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.set_partial_fit_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `partial_fit` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `partial_fit` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `partial_fit`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `partial_fit`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.sparsify "Link to this definition")\
\
Convert coefficient matrix to sparse format.\
\
Converts the `coef_` member to a scipy.sparse matrix, which for L1-regularized models can be much more memory- and storage-efficient than the usual numpy.ndarray representation.\
\
The `intercept_` member is not converted.\
\
Warning\
\
This method is not supported for estimators fitted with array API inputs (i.e. when [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")\
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM.predict "sklearn.linear_model.SGDOneClassSVM.predict")\
 and other methods involving passing arrays may raise or return unexpected results.\
\
Returns:\
\
self\
\
Fitted estimator.\
\
Notes\
\
For non-sparse models, i.e. when there are not many zeros in `coef_`, this may actually _increase_ memory usage, so use this method with care. A rule of thumb is that the number of zero elements, which can be computed with `(coef_ == 0).sum()`, must be more than 50% for this to provide significant benefits.\
\
After calling this method, further fitting with the partial\_fit method (if any) will not work until you call densify.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#gallery-examples "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)\
\
[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)\
\
One-Class SVM versus One-Class SVM using Stochastic Gradient Descent\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)\
\
[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)\
\
Comparing anomaly detection algorithms for outlier detection on toy datasets\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)