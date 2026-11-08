[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.SGDRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.SGDRegressor.html)

Collapse Sidebar Expand Sidebar

SGDRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sgdregressor "Link to this heading")

==============================================================================================================================================

class sklearn.linear\_model.SGDRegressor(_loss\='squared\_error'_, _\*_, _penalty\='l2'_, _alpha\=0.0001_, _l1\_ratio\=0.15_, _fit\_intercept\=True_, _max\_iter\=1000_, _tol\=0.001_, _shuffle\=True_, _verbose\=0_, _epsilon\=0.1_, _random\_state\=None_, _learning\_rate\='invscaling'_, _eta0\=0.01_, _power\_t\=0.25_, _early\_stopping\=False_, _validation\_fraction\=0.1_, _n\_iter\_no\_change\=5_, _warm\_start\=False_, _average\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L1802)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "Link to this definition")

Linear model fitted by minimizing a regularized empirical loss with SGD.

SGD stands for Stochastic Gradient Descent: the gradient of the loss is estimated each sample at a time and the model is updated along the way with a decreasing strength schedule (aka learning rate).

The regularizer is a penalty added to the loss function that shrinks model parameters towards the zero vector using either the squared euclidean norm L2 or the absolute norm L1 or a combination of both (Elastic Net). If the parameter update crosses the 0.0 value because of the regularizer, the update is truncated to 0.0 to allow for learning sparse models and achieve online feature selection.

This implementation works with data represented as dense numpy arrays of floating point values for the features.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/sgd.html#sgd)
.

Parameters:

**loss**str, default=’squared\_error’

The loss function to be used. The possible values are ‘squared\_error’, ‘huber’, ‘epsilon\_insensitive’, or ‘squared\_epsilon\_insensitive’

The ‘squared\_error’ refers to the ordinary least squares fit. ‘huber’ modifies ‘squared\_error’ to focus less on getting outliers correct by switching from squared to linear loss past a distance of epsilon. ‘epsilon\_insensitive’ ignores errors less than epsilon and is linear past that; this is the loss function used in SVR. ‘squared\_epsilon\_insensitive’ is the same but becomes squared loss past a tolerance of epsilon.

More details about the losses formulas can be found in the [User Guide](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
.

**penalty**{‘l2’, ‘l1’, ‘elasticnet’, None}, default=’l2’

The penalty (aka regularization term) to be used. Defaults to ‘l2’ which is the standard regularizer for linear SVM models. ‘l1’ and ‘elasticnet’ might bring sparsity to the model (feature selection) not achievable with ‘l2’. No penalty is added when set to `None`.

You can see a visualisation of the penalties in [SGD: Penalties](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html#sphx-glr-auto-examples-linear-model-plot-sgd-penalties-py)
.

**alpha**float, default=0.0001

Constant that multiplies the regularization term. The higher the value, the stronger the regularization. Also used to compute the learning rate when `learning_rate` is set to ‘optimal’. Values must be in the range `[0.0, inf)`.\
\
**l1\_ratio**float, default=0.15\
\
The Elastic Net mixing parameter, with 0 <= l1\_ratio <= 1. l1\_ratio=0 corresponds to L2 penalty, l1\_ratio=1 to L1. Only used if `penalty` is ‘elasticnet’. Values must be in the range `[0.0, 1.0]` or can be `None` if `penalty` is not `elasticnet`.\
\
Changed in version 1.7: `l1_ratio` can be `None` when `penalty` is not “elasticnet”.\
\
**fit\_intercept**bool, default=True\
\
Whether the intercept should be estimated or not. If False, the data is assumed to be already centered.\
\
**max\_iter**int, default=1000\
\
The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the `fit` method, and not the [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.partial_fit "sklearn.linear_model.SGDRegressor.partial_fit")\
 method. Values must be in the range `[1, inf)`.\
\
Added in version 0.19.\
\
**tol**float or None, default=1e-3\
\
The stopping criterion. If it is not None, training will stop when (loss > best\_loss - tol) for `n_iter_no_change` consecutive epochs. Convergence is checked against the training loss or the validation loss depending on the `early_stopping` parameter. Values must be in the range `[0.0, inf)`.\
\
Added in version 0.19.\
\
**shuffle**bool, default=True\
\
Whether or not the training data should be shuffled after each epoch.\
\
**verbose**int, default=0\
\
The verbosity level. Values must be in the range `[0, inf)`.\
\
**epsilon**float, default=0.1\
\
Epsilon in the epsilon-insensitive loss functions; only if `loss` is ‘huber’, ‘epsilon\_insensitive’, or ‘squared\_epsilon\_insensitive’. For ‘huber’, determines the threshold at which it becomes less important to get the prediction exactly right. For epsilon-insensitive, any differences between the current prediction and the correct label are ignored if they are less than this threshold. Values must be in the range `[0.0, inf)`.\
\
**random\_state**int, RandomState instance, default=None\
\
Used for shuffling the data, when `shuffle` is set to `True`. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
.\
\
**learning\_rate**str, default=’invscaling’\
\
The learning rate schedule:\
\
*   ‘constant’: `eta = eta0`\
    \
*   ‘optimal’: `eta = 1.0 / (alpha * (t + t0))` where t0 is chosen by a heuristic proposed by Leon Bottou.\
    \
*   ‘invscaling’: `eta = eta0 / pow(t, power_t)`\
    \
*   ‘adaptive’: eta = eta0, as long as the training keeps decreasing. Each time n\_iter\_no\_change consecutive epochs fail to decrease the training loss by tol or fail to increase validation score by tol if early\_stopping is True, the current learning rate is divided by 5.\
    \
*   ‘pa1’: passive-aggressive algorithm 1, see [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#r4f447a970fb6-1)\
    . Only with `loss='epsilon_insensitive'`. Update is `w += eta y x` with `eta = min(eta0, loss/||x||**2)`.\
    \
*   ‘pa2’: passive-aggressive algorithm 2, see [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#r4f447a970fb6-1)\
    . Only with `loss='epsilon_insensitive'`. Update is `w += eta y x` with `eta = hinge_loss / (||x||**2 + 1/(2 eta0))`.\
    \
\
Added in version 0.20: Added ‘adaptive’ option.\
\
Added in version 1.8: Added options ‘pa1’ and ‘pa2’\
\
**eta0**float, default=0.01\
\
The initial learning rate for the ‘constant’, ‘invscaling’ or ‘adaptive’ schedules. The default value is 0.01. Values must be in the range `(0.0, inf)`.\
\
For PA-1 (`learning_rate=pa1`) and PA-II (`pa2`), it specifies the aggressiveness parameter for the passive-aggressive algorithm, see \[1\] where it is called C:\
\
*   For PA-I it is the maximum step size.\
    \
*   For PA-II it regularizes the step size (the smaller `eta0` the more it regularizes).\
    \
\
As a general rule-of-thumb for PA, `eta0` should be small when the data is noisy.\
\
**power\_t**float, default=0.25\
\
The exponent for inverse scaling learning rate. Values must be in the range `[0.0, inf)`.\
\
Deprecated since version 1.8: Negative values for `power_t` are deprecated in version 1.8 and will raise an error in 1.10. Use values in the range \[0.0, inf) instead.\
\
**early\_stopping**bool, default=False\
\
Whether to use early stopping to terminate training when validation score is not improving. If set to True, it will automatically set aside a fraction of training data as validation and terminate training when validation score returned by the `score` method is not improving by at least `tol` for `n_iter_no_change` consecutive epochs.\
\
See [Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html#sphx-glr-auto-examples-linear-model-plot-sgd-early-stopping-py)\
 for an example of the effects of early stopping.\
\
Added in version 0.20: Added ‘early\_stopping’ option\
\
**validation\_fraction**float, default=0.1\
\
The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1. Only used if `early_stopping` is True. Values must be in the range `(0.0, 1.0)`.\
\
Added in version 0.20: Added ‘validation\_fraction’ option\
\
**n\_iter\_no\_change**int, default=5\
\
Number of iterations with no improvement to wait before stopping fitting. Convergence is checked against the training loss or the validation loss depending on the `early_stopping` parameter. Integer values must be in the range `[1, max_iter)`.\
\
Added in version 0.20: Added ‘n\_iter\_no\_change’ option\
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
When set to True, computes the averaged SGD weights across all updates and stores the result in the `coef_` attribute. If set to an int greater than 1, averaging will begin once the total number of samples seen reaches `average`. So `average=10` will begin averaging after seeing 10 samples.\
\
Attributes:\
\
**coef\_**ndarray of shape (n\_features,)\
\
Weights assigned to the features.\
\
**intercept\_**ndarray of shape (1,)\
\
The intercept term.\
\
**n\_iter\_**int\
\
The actual number of iterations before reaching the stopping criterion.\
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
[`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")\
\
Linear regression model that is robust to outliers.\
\
[`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")\
\
Least Angle Regression model.\
\
[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")\
\
Linear Model trained with L1 prior as regularizer.\
\
[`RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")\
\
RANSAC (RANdom SAmple Consensus) algorithm.\
\
[`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")\
\
Linear least squares with l2 regularization.\
\
[`sklearn.svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")\
\
Epsilon-Support Vector Regression.\
\
[`TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")\
\
Theil-Sen Estimator robust multivariate regression model.\
\
References\
\
\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#id1)\
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#id2)\
)\
\
Online Passive-Aggressive Algorithms <[http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf](http://jmlr.csail.mit.edu/papers/volume7/crammer06a/crammer06a.pdf)\
\> K. Crammer, O. Dekel, J. Keshat, S. Shalev-Shwartz, Y. Singer - JMLR (2006)\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn.linear\_model import SGDRegressor\
\>>> from sklearn.pipeline import make\_pipeline\
\>>> from sklearn.preprocessing import StandardScaler\
\>>> n\_samples, n\_features \= 10, 5\
\>>> rng \= np.random.RandomState(0)\
\>>> y \= rng.randn(n\_samples)\
\>>> X \= rng.randn(n\_samples, n\_features)\
\>>> \# Always scale the input. The most convenient way is to use a pipeline.\
\>>> reg \= make\_pipeline(StandardScaler(),\
...                     SGDRegressor(max\_iter\=1000, tol\=1e-3))\
\>>> reg.fit(X, y)\
Pipeline(steps=\[('standardscaler', StandardScaler()),\
                ('sgdregressor', SGDRegressor())\])\
\
Copy to clipboard\
\
densify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L460)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.densify "Link to this definition")\
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
fit(_X_, _y_, _coef\_init\=None_, _intercept\_init\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L1639)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.fit "Link to this definition")\
\
Fit linear model with Stochastic Gradient Descent.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Training data.\
\
**y**ndarray of shape (n\_samples,)\
\
Target values.\
\
**coef\_init**ndarray of shape (n\_features,), default=None\
\
The initial coefficients to warm-start the optimization.\
\
**intercept\_init**ndarray of shape (1,), default=None\
\
The initial intercept to warm-start the optimization.\
\
**sample\_weight**array-like, shape (n\_samples,), default=None\
\
Weights applied to individual samples (1. for unweighted).\
\
Returns:\
\
**self**object\
\
Fitted `SGDRegressor` estimator.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.get_metadata_routing "Link to this definition")\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.get_params "Link to this definition")\
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
partial\_fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L1539)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.partial_fit "Link to this definition")\
\
Perform one epoch of stochastic gradient descent on given samples.\
\
Internally, this method uses `max_iter = 1`. Therefore, it is not guaranteed that a minimum of the cost function is reached after calling it once. Matters such as objective convergence and early stopping should be handled by the user.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Subset of training data.\
\
**y**numpy array of shape (n\_samples,)\
\
Subset of target values.\
\
**sample\_weight**array-like, shape (n\_samples,), default=None\
\
Weights applied to individual samples. If not provided, uniform weights are assumed.\
\
Returns:\
\
**self**object\
\
Returns an instance of self.\
\
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_stochastic_gradient.py#L1697)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.predict "Link to this definition")\
\
Predict using the linear model.\
\
Parameters:\
\
**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)\
\
Input data.\
\
Returns:\
\
ndarray of shape (n\_samples,)\
\
Predicted target values per element in X.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.score "Link to this definition")\
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
set\_fit\_request(_\*_, _coef\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _intercept\_init: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model._stochastic_gradient.SGDRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.set_fit_request "Link to this definition")\
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
**intercept\_init**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `intercept_init` parameter in `fit`.\
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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.set_params "Link to this definition")\
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
 \= '$UNCHANGED$'_) → [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model._stochastic_gradient.SGDRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.set_partial_fit_request "Link to this definition")\
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
set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model._stochastic_gradient.SGDRegressor")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.set_score_request "Link to this definition")\
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
sparsify()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_base.py#L480)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.sparsify "Link to this definition")\
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
 is used with `array_api_dispatch=True`). The call may succeed but subsequent calls to [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor.predict "sklearn.linear_model.SGDRegressor.predict")\
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
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#gallery-examples "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_thumb.png)\
\
[Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)\
\
Prediction Latency\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_penalties_thumb.png)\
\
[SGD: Penalties](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html)\
\
SGD: Penalties\
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