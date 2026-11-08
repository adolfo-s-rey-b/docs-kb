[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html)

Collapse Sidebar Expand Sidebar

GaussianProcessRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#gaussianprocessregressor "Link to this heading")

======================================================================================================================================================================================

class sklearn.gaussian\_process.GaussianProcessRegressor(_kernel\=None_, _\*_, _alpha\=1e-10_, _optimizer\='fmin\_l\_bfgs\_b'_, _n\_restarts\_optimizer\=0_, _normalize\_y\=False_, _copy\_X\_train\=True_, _n\_targets\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpr.py#L32)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "Link to this definition")

Gaussian process regression (GPR).

The implementation is based on Algorithm 2.1 of [\[RW2006\]](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#rf75674b0f418-rw2006)
.

In addition to standard scikit-learn estimator API, [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
:

*   allows prediction without prior fitting (based on the GP prior)
    
*   provides an additional method `sample_y(X)`, which evaluates samples drawn from the GPR (prior or posterior) at given inputs
    
*   exposes a method `log_marginal_likelihood(theta)`, which can be used externally for other ways of selecting hyperparameters, e.g., via Markov chain Monte Carlo.
    

To learn the difference between a point-estimate approach vs. a more Bayesian modelling approach, refer to the example entitled [Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html#sphx-glr-auto-examples-gaussian-process-plot-compare-gpr-krr-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process)
.

Added in version 0.18.

Parameters:

**kernel**kernel instance, default=None

The kernel specifying the covariance function of the GP. If `None` is passed, the kernel `ConstantKernel() * RBF()` is used as default. Note that the kernel hyperparameters are optimized during fitting unless the bounds are marked as `"fixed"` or the argument `optimizer` is set to `None`.

**alpha**float or ndarray of shape (n\_samples,), default=1e-10

Value added to the diagonal of the kernel matrix during fitting. This can prevent a potential numerical issue during fitting, by ensuring that the calculated values form a positive definite matrix. It can also be interpreted as the variance of additional Gaussian measurement noise on the training observations. Note that this is different from using a `WhiteKernel`. If an array is passed, it must have the same number of entries as the data used for fitting and is used as datapoint-dependent noise level. Allowing to specify the noise level directly as a parameter is mainly for convenience and for consistency with [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
. For an example illustrating how the alpha parameter controls the noise variance in Gaussian Process Regression, see [Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#sphx-glr-auto-examples-gaussian-process-plot-gpr-noisy-targets-py)
.

**optimizer**“fmin\_l\_bfgs\_b”, callable or None, default=”fmin\_l\_bfgs\_b”

Can either be one of the internally supported optimizers for optimizing the kernel’s parameters, specified by a string, or an externally defined optimizer passed as a callable. If a callable is passed, it must have the signature:

def optimizer(obj\_func, initial\_theta, bounds):
    \# \* 'obj\_func': the objective function to be minimized, which
    \#   takes the hyperparameters theta as a parameter and an
    \#   optional flag eval\_gradient, which determines if the
    \#   gradient is returned additionally to the function value
    \# \* 'initial\_theta': the initial value for theta, which can be
    \#   used by local optimizers
    \# \* 'bounds': the bounds on the values of theta
    ....
    \# Returned are the best found hyperparameters theta and
    \# the corresponding value of the target function.
    return theta\_opt, func\_min

Copy to clipboard

Per default, the L-BFGS-B algorithm from `scipy.optimize.minimize` is used. If None is passed, the kernel’s parameters are kept fixed. Available internal optimizers are: `{'fmin_l_bfgs_b'}`.

**n\_restarts\_optimizer**int, default=0

The number of restarts of the optimizer for finding the kernel’s parameters which maximize the log-marginal likelihood. The first run of the optimizer is performed from the kernel’s initial parameters, the remaining ones (if any) from thetas sampled log-uniform randomly from the space of allowed theta-values. If greater than 0, all bounds must be finite. Note that `n_restarts_optimizer == 0` implies that one run is performed.

**normalize\_y**bool, default=False

Whether or not to normalize the target values `y` by removing the mean and scaling to unit-variance. This is recommended for cases where zero-mean, unit-variance priors are used. Note that, in this implementation, the normalisation is reversed before the GP predictions are reported.

Changed in version 0.23.

**copy\_X\_train**bool, default=True

If True, a persistent copy of the training data is stored in the object. Otherwise, just a reference to the training data is stored, which might cause predictions to change if the data is modified externally.

**n\_targets**int, default=None

The number of dimensions of the target values. Used to decide the number of outputs when sampling from the prior distributions (i.e. calling [`sample_y`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.sample_y "sklearn.gaussian_process.GaussianProcessRegressor.sample_y")
 before [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.fit "sklearn.gaussian_process.GaussianProcessRegressor.fit")
). This parameter is ignored once [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.fit "sklearn.gaussian_process.GaussianProcessRegressor.fit")
 has been called.

Added in version 1.3.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation used to initialize the centers. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**X\_train\_**array-like of shape (n\_samples, n\_features) or list of object

Feature vectors or other representations of training data (also required for prediction).

**y\_train\_**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values in training data (also required for prediction).

**kernel\_**kernel instance

The kernel used for prediction. The structure of the kernel is the same as the one passed as parameter but with optimized hyperparameters.

**L\_**array-like of shape (n\_samples, n\_samples)

Lower-triangular Cholesky decomposition of the kernel in `X_train_`.

**alpha\_**array-like of shape (n\_samples,)

Dual coefficients of training data points in kernel space.

**log\_marginal\_likelihood\_value\_**float

The log-marginal-likelihood of `self.kernel_.theta`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")

Gaussian process classification (GPC) based on Laplace approximation.

References

\[[RW2006](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#id1)\
\]

[Carl E. Rasmussen and Christopher K.I. Williams, “Gaussian Processes for Machine Learning”, MIT Press 2006](https://www.gaussianprocess.org/gpml/chapters/RW.pdf)

Examples

\>>> from sklearn.datasets import make\_friedman2
\>>> from sklearn.gaussian\_process import GaussianProcessRegressor
\>>> from sklearn.gaussian\_process.kernels import DotProduct, WhiteKernel
\>>> X, y \= make\_friedman2(n\_samples\=500, noise\=0, random\_state\=0)
\>>> kernel \= DotProduct() + WhiteKernel()
\>>> gpr \= GaussianProcessRegressor(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpr.score(X, y)
0.3680...
\>>> gpr.predict(X\[:2,:\], return\_std\=True)
(array(\[653.0, 592.1\]), array(\[316.6, 316.6\]))

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpr.py#L232)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.fit "Link to this definition")

Fit Gaussian process regression model.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Feature vectors or other representations of training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

Returns:

**self**object

GaussianProcessRegressor class instance.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

log\_marginal\_likelihood(_theta\=None_, _eval\_gradient\=False_, _clone\_kernel\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpr.py#L541)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.log_marginal_likelihood "Link to this definition")

Return log-marginal likelihood of theta for training data.

Parameters:

**theta**array-like of shape (n\_kernel\_params,) default=None

Kernel hyperparameters for which the log-marginal likelihood is evaluated. If None, the precomputed log\_marginal\_likelihood of `self.kernel_.theta` is returned.

**eval\_gradient**bool, default=False

If True, the gradient of the log-marginal likelihood with respect to the kernel hyperparameters at position theta is returned additionally. If True, theta must not be None.

**clone\_kernel**bool, default=True

If True, the kernel attribute is copied. If False, the kernel attribute is modified, but may result in a performance improvement.

Returns:

**log\_likelihood**float

Log-marginal likelihood of theta for training data.

**log\_likelihood\_gradient**ndarray of shape (n\_kernel\_params,), optional

Gradient of the log-marginal likelihood with respect to the kernel hyperparameters at position theta. Only returned when eval\_gradient is True.

predict(_X_, _return\_std\=False_, _return\_cov\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpr.py#L370)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.predict "Link to this definition")

Predict using the Gaussian process regression model.

We can also predict based on an unfitted model by using the GP prior. In addition to the mean of the predictive distribution, optionally also returns its standard deviation (`return_std=True`) or covariance (`return_cov=True`). Note that at most one of the two can be requested.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Query points where the GP is evaluated.

**return\_std**bool, default=False

If True, the standard-deviation of the predictive distribution at the query points is returned along with the mean.

**return\_cov**bool, default=False

If True, the covariance of the joint predictive distribution at the query points is returned along with the mean.

Returns:

**y\_mean**ndarray of shape (n\_samples,) or (n\_samples, n\_targets)

Mean of predictive distribution at query points.

**y\_std**ndarray of shape (n\_samples,) or (n\_samples, n\_targets), optional

Standard deviation of predictive distribution at query points. Only returned when `return_std` is True.

**y\_cov**ndarray of shape (n\_samples, n\_samples) or (n\_samples, n\_samples, n\_targets), optional

Covariance of joint predictive distribution at query points. Only returned when `return_cov` is True.

sample\_y(_X_, _n\_samples\=1_, _random\_state\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpr.py#L502)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.sample_y "Link to this definition")

Draw samples from Gaussian process and evaluate at X.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features) or list of object

Query points where the GP is evaluated.

**n\_samples**int, default=1

Number of samples drawn from the Gaussian process per query point.

**random\_state**int, RandomState instance or None, default=0

Determines random number generation to randomly draw samples. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**y\_samples**ndarray of shape (n\_samples\_X, n\_samples), or (n\_samples\_X, n\_targets, n\_samples)

Values of n\_samples samples drawn from Gaussian process and evaluated at query points.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L672)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.score "Link to this definition")

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

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_predict\_request(_\*_, _return\_cov: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_, _return\_std: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process._gpr.GaussianProcessRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.set_predict_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `predict` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `predict` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `predict`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**return\_cov**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `return_cov` parameter in `predict`.

**return\_std**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `return_std` parameter in `predict`.

Returns:

**self**object

The updated object.

set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process._gpr.GaussianProcessRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_thumb.png)

[Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_thumb.png)

[Gaussian processes on discrete data structures](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)

Gaussian processes on discrete data structures

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_thumb.png)

[Illustration of prior and posterior Gaussian process for different kernels](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)

Illustration of prior and posterior Gaussian process for different kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)