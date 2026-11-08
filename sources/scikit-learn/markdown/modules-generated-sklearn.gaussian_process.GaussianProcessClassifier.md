[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)

Collapse Sidebar Expand Sidebar

GaussianProcessClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#gaussianprocessclassifier "Link to this heading")

=========================================================================================================================================================================================

class sklearn.gaussian\_process.GaussianProcessClassifier(_kernel\=None_, _\*_, _optimizer\='fmin\_l\_bfgs\_b'_, _n\_restarts\_optimizer\=0_, _max\_iter\_predict\=100_, _warm\_start\=False_, _copy\_X\_train\=True_, _random\_state\=None_, _multi\_class\='one\_vs\_rest'_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L516)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "Link to this definition")

Gaussian process classification (GPC) based on Laplace approximation.

The implementation is based on Algorithm 3.1, 3.2, and 5.1 from [\[RW2006\]](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#r2da648a61a73-rw2006)
.

Internally, the Laplace approximation is used for approximating the non-Gaussian posterior by a Gaussian.

Currently, the implementation is restricted to using the logistic link function. For multi-class classification, several binary one-versus rest classifiers are fitted. Note that this class thus does not implement a true multi-class Laplace approximation.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process)
.

Added in version 0.18.

Parameters:

**kernel**kernel instance, default=None

The kernel specifying the covariance function of the GP. If None is passed, the kernel “1.0 \* RBF(1.0)” is used as default. Note that the kernel’s hyperparameters are optimized during fitting. Also kernel cannot be a `CompoundKernel`.

**optimizer**‘fmin\_l\_bfgs\_b’, callable or None, default=’fmin\_l\_bfgs\_b’

Can either be one of the internally supported optimizers for optimizing the kernel’s parameters, specified by a string, or an externally defined optimizer passed as a callable. If a callable is passed, it must have the signature:

def optimizer(obj\_func, initial\_theta, bounds):
    \# \* 'obj\_func' is the objective function to be maximized, which
    \#   takes the hyperparameters theta as parameter and an
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

Per default, the ‘L-BFGS-B’ algorithm from scipy.optimize.minimize is used. If None is passed, the kernel’s parameters are kept fixed. Available internal optimizers are:

'fmin\_l\_bfgs\_b'

Copy to clipboard

**n\_restarts\_optimizer**int, default=0

The number of restarts of the optimizer for finding the kernel’s parameters which maximize the log-marginal likelihood. The first run of the optimizer is performed from the kernel’s initial parameters, the remaining ones (if any) from thetas sampled log-uniform randomly from the space of allowed theta-values. If greater than 0, all bounds must be finite. Note that n\_restarts\_optimizer=0 implies that one run is performed.

**max\_iter\_predict**int, default=100

The maximum number of iterations in Newton’s method for approximating the posterior during predict. Smaller values will reduce computation time at the cost of worse results.

**warm\_start**bool, default=False

If warm-starts are enabled, the solution of the last Newton iteration on the Laplace approximation of the posterior mode is used as initialization for the next call of \_posterior\_mode(). This can speed up convergence when \_posterior\_mode is called several times on similar problems as in hyperparameter optimization. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**copy\_X\_train**bool, default=True

If True, a persistent copy of the training data is stored in the object. Otherwise, just a reference to the training data is stored, which might cause predictions to change if the data is modified externally.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation used to initialize the centers. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**multi\_class**{‘one\_vs\_rest’, ‘one\_vs\_one’}, default=’one\_vs\_rest’

Specifies how multi-class classification problems are handled. Supported are ‘one\_vs\_rest’ and ‘one\_vs\_one’. In ‘one\_vs\_rest’, one binary Gaussian process classifier is fitted for each class, which is trained to separate this class from the rest. In ‘one\_vs\_one’, one binary Gaussian process classifier is fitted for each pair of classes, which is trained to separate these two classes. The predictions of these binary predictors are combined into multi-class predictions. Note that ‘one\_vs\_one’ does not support predicting probability estimates.

**n\_jobs**int, default=None

The number of jobs to use for the computation: the specified multiclass problems are computed in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Attributes:

**base\_estimator\_**`Estimator` instance

The estimator instance that defines the likelihood function using the observed data.

`kernel_`kernel instance

Return the kernel of the base estimator.

**log\_marginal\_likelihood\_value\_**float

The log-marginal-likelihood of `self.kernel_.theta`

**classes\_**array-like of shape (n\_classes,)

Unique class labels.

**n\_classes\_**int

The number of classes in the training data

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")

Gaussian process regression (GPR).

References

\[[RW2006](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#id1)\
\]

[Carl E. Rasmussen and Christopher K.I. Williams, “Gaussian Processes for Machine Learning”, MIT Press 2006](https://www.gaussianprocess.org/gpml/chapters/RW.pdf)

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.gaussian\_process import GaussianProcessClassifier
\>>> from sklearn.gaussian\_process.kernels import RBF
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> kernel \= 1.0 \* RBF(1.0)
\>>> gpc \= GaussianProcessClassifier(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpc.score(X, y)
0.9866...
\>>> gpc.predict\_proba(X\[:2,:\])
array(\[\[0.83548752, 0.03228706, 0.13222543\],\
       \[0.79064206, 0.06525643, 0.14410151\]\])

Copy to clipboard

For a comparison of the GaussianProcessClassifier with other classifiers see: [Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py)
.

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L714)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.fit "Link to this definition")

Fit Gaussian process classification model.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Feature vectors or other representations of training data.

**y**array-like of shape (n\_samples,)

Target values, must be binary.

Returns:

**self**object

Returns an instance of self.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

latent\_mean\_and\_variance(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L936)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.latent_mean_and_variance "Link to this definition")

Compute the mean and variance of the latent function.

Based on algorithm 3.2 of [\[RW2006\]](https://scikit-learn.org/stable/modules/gaussian_process.html#rw2006)
, this function returns the latent mean (Line 4) and variance (Line 6) of the Gaussian process classification model.

Note that this function is only supported for binary classification.

Added in version 1.7.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Query points where the GP is evaluated for classification.

Returns:

**latent\_mean**array-like of shape (n\_samples,)

Mean of the latent function values at the query points.

**latent\_var**array-like of shape (n\_samples,)

Variance of the latent function values at the query points.

log\_marginal\_likelihood(_theta\=None_, _eval\_gradient\=False_, _clone\_kernel\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L851)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.log_marginal_likelihood "Link to this definition")

Return log-marginal likelihood of theta for training data.

In the case of multi-class classification, the mean log-marginal likelihood of the one-versus-rest classifiers are returned.

Parameters:

**theta**array-like of shape (n\_kernel\_params,), default=None

Kernel hyperparameters for which the log-marginal likelihood is evaluated. In the case of multi-class classification, theta may be the hyperparameters of the compound kernel or of an individual kernel. In the latter case, all individual kernel get assigned the same theta values. If None, the precomputed log\_marginal\_likelihood of `self.kernel_.theta` is returned.

**eval\_gradient**bool, default=False

If True, the gradient of the log-marginal likelihood with respect to the kernel hyperparameters at position theta is returned additionally. Note that gradient computation is not supported for non-binary classification. If True, theta must not be None.

**clone\_kernel**bool, default=True

If True, the kernel attribute is copied. If False, the kernel attribute is modified, but may result in a performance improvement.

Returns:

**log\_likelihood**float

Log-marginal likelihood of theta for training data.

**log\_likelihood\_gradient**ndarray of shape (n\_kernel\_params,), optional

Gradient of the log-marginal likelihood with respect to the kernel hyperparameters at position theta. Only returned when `eval_gradient` is True.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L789)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.predict "Link to this definition")

Perform classification on an array of test vectors X.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Query points where the GP is evaluated for classification.

Returns:

**C**ndarray of shape (n\_samples,)

Predicted target values for X, values are from `classes_`.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/_gpc.py#L811)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.predict_proba "Link to this definition")

Return probability estimates for the test vector X.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or list of object

Query points where the GP is evaluated for classification.

Returns:

**C**array-like of shape (n\_samples, n\_classes)

Returns the probability of the samples for each class in the model. The columns correspond to the classes in sorted order, as they appear in the attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.set_params "Link to this definition")

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
 \= '$UNCHANGED$'_) → [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process._gpc.GaussianProcessClassifier")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.set_score_request "Link to this definition")

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

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)

[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Classifier comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_thumb.png)

[Probabilistic predictions with Gaussian process classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)

Probabilistic predictions with Gaussian process classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_isoprobability_thumb.png)

[Iso-probability lines for Gaussian Processes classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html)

Iso-probability lines for Gaussian Processes classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_thumb.png)

[Gaussian processes on discrete data structures](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)

Gaussian processes on discrete data structures

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)