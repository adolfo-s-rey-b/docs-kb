[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.HuberRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.HuberRegressor.html)

Collapse Sidebar Expand Sidebar

HuberRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#huberregressor "Link to this heading")

====================================================================================================================================================

class sklearn.linear\_model.HuberRegressor(_\*_, _epsilon\=1.35_, _max\_iter\=100_, _alpha\=0.0001_, _warm\_start\=False_, _fit\_intercept\=True_, _tol\=1e-05_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_huber.py#L129)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "Link to this definition")

L2-regularized linear regression model that is robust to outliers.

The Huber Regressor optimizes the squared loss for the samples where `|(y - Xw - c) / sigma| < epsilon` and the absolute loss for the samples where `|(y - Xw - c) / sigma| > epsilon`, where the model coefficients `w`, the intercept `c` and the scale `sigma` are parameters to be optimized. The parameter `sigma` makes sure that if `y` is scaled up or down by a certain factor, one does not need to rescale `epsilon` to achieve the same robustness. Note that this does not take into account the fact that the different features of `X` may be of different scales.

The Huber loss function has the advantage of not being heavily influenced by the outliers while not completely ignoring their effect.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#huber-regression)

Added in version 0.18.

Parameters:

**epsilon**float, default=1.35

The parameter epsilon controls the number of samples that should be classified as outliers. The smaller the epsilon, the more robust it is to outliers. Epsilon must be in the range `[1, inf)`.\
\
**max\_iter**int, default=100\
\
Maximum number of iterations that `scipy.optimize.minimize(method="L-BFGS-B")` should run for.\
\
**alpha**float, default=0.0001\
\
Strength of the squared L2 regularization. Note that the penalty is equal to `alpha * ||w||^2`. Must be in the range `[0, inf)`.\
\
**warm\_start**bool, default=False\
\
This is useful if the stored attributes of a previously used model has to be reused. If set to False, then the coefficients will be rewritten for every call to fit. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)\
.\
\
**fit\_intercept**bool, default=True\
\
Whether or not to fit the intercept. This can be set to False if the data is already centered around the origin.\
\
**tol**float, default=1e-05\
\
The iteration will stop when `max{|proj g_i | i = 1, ..., n}` <= `tol` where pg\_i is the i-th component of the projected gradient.\
\
Attributes:\
\
**coef\_**array, shape (n\_features,)\
\
Features got by optimizing the L2-regularized Huber loss.\
\
**intercept\_**float\
\
Bias.\
\
**scale\_**float\
\
The value by which `|y - Xw - c|` is scaled down.\
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
**n\_iter\_**int\
\
Number of iterations that `scipy.optimize.minimize(method="L-BFGS-B")` has run for.\
\
Changed in version 0.20: In SciPy <= 1.0.0 the number of lbfgs iterations may exceed `max_iter`. `n_iter_` will now report at most `max_iter`.\
\
**outliers\_**array, shape (n\_samples,)\
\
A boolean mask which is set to True where the samples are identified as outliers.\
\
See also\
\
[`RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")\
\
RANSAC (RANdom SAmple Consensus) algorithm.\
\
[`TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")\
\
Theil-Sen Estimator robust multivariate regression model.\
\
[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")\
\
Fitted by minimizing a regularized empirical loss with SGD.\
\
References\
\
\[1\]\
\
Peter J. Huber, Elvezio M. Ronchetti, Robust Statistics Concomitant scale estimates, p. 172\
\
\[2\]\
\
Art B. Owen (2006), [A robust hybrid of lasso and ridge regression.](https://artowen.su.domains/reports/hhu.pdf)\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn.linear\_model import HuberRegressor, LinearRegression\
\>>> from sklearn.datasets import make\_regression\
\>>> rng \= np.random.RandomState(0)\
\>>> X, y, coef \= make\_regression(\
...     n\_samples\=200, n\_features\=2, noise\=4.0, coef\=True, random\_state\=0)\
\>>> X\[:4\] \= rng.uniform(10, 20, (4, 2))\
\>>> y\[:4\] \= rng.uniform(10, 20, 4)\
\>>> huber \= HuberRegressor().fit(X, y)\
\>>> huber.score(X, y)\
\-7.284\
\>>> huber.predict(X\[:1,\])\
array(\[806.7200\])\
\>>> linear \= LinearRegression().fit(X, y)\
\>>> print("True coefficients:", coef)\
True coefficients: \[20.4923...  34.1698...\]\
\>>> print("Huber coefficients:", huber.coef\_)\
Huber coefficients: \[17.7906... 31.0106...\]\
\>>> print("Linear Regression coefficients:", linear.coef\_)\
Linear Regression coefficients: \[-1.9221...  7.0226...\]\
\
Copy to clipboard\
\
fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_huber.py#L277)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.fit "Link to this definition")\
\
Fit the model according to the given training data.\
\
Parameters:\
\
**X**array-like, shape (n\_samples, n\_features)\
\
Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
**y**array-like, shape (n\_samples,)\
\
Target vector relative to X.\
\
**sample\_weight**array-like, shape (n\_samples,)\
\
Weight given to each sample.\
\
Returns:\
\
**self**object\
\
Fitted `HuberRegressor` estimator.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.get_metadata_routing "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.get_params "Link to this definition")\
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
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L301)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.predict "Link to this definition")\
\
Predict using the linear model.\
\
Parameters:\
\
**X**array-like or sparse matrix of shape (n\_samples, n\_features)\
\
Samples.\
\
Returns:\
\
**C**ndarray of shape (n\_samples,)\
\
Predicted values.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.score "Link to this definition")\
\
Return [coefficient of determination](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)\
 on test data.\
\
The coefficient of determination, R2, is defined as (1−uv), where u is the residual sum of squares `((y_true - y_pred)** 2).sum()` and v is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`. The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of `y`, disregarding the input features, would get a R2 score of 0.0.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
Test samples. For some estimators this may be a precomputed kernel matrix or a list of generic objects instead with shape `(n_samples, n_samples_fitted)`, where `n_samples_fitted` is the number of samples used in the fitting for the estimator.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
True values for `X`.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Returns:\
\
**score**float\
\
R2 of `self.predict(X)` w.r.t. `y`.\
\
Notes\
\
The R2 score used when calling `score` on a regressor uses `multioutput='uniform_average'` from version 0.23 to keep consistent with default value of [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")\
. This influences the `score` method of all the multioutput regressors (except for [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")\
).\
\
set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model._huber.HuberRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.set_fit_request "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.set_params "Link to this definition")\
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
set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model._huber.HuberRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor.set_score_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `score` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.\
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
Metadata routing for `sample_weight` parameter in `score`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#gallery-examples "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)\
\
[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)\
\
HuberRegressor vs Ridge on dataset with strong outliers\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)\
\
[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)\
\
Ridge coefficients as a function of the L2 Regularization\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)\
\
[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)\
\
Robust linear estimator fitting\
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