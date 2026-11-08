[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.mixture.BayesianGaussianMixture.html)

Collapse Sidebar Expand Sidebar

BayesianGaussianMixture[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#bayesiangaussianmixture "Link to this heading")

==========================================================================================================================================================================

class sklearn.mixture.BayesianGaussianMixture(_\*_, _n\_components\=1_, _covariance\_type\='full'_, _tol\=0.001_, _reg\_covar\=1e-06_, _max\_iter\=100_, _n\_init\=1_, _init\_params\='kmeans'_, _weight\_concentration\_prior\_type\='dirichlet\_process'_, _weight\_concentration\_prior\=None_, _mean\_precision\_prior\=None_, _mean\_prior\=None_, _degrees\_of\_freedom\_prior\=None_, _covariance\_prior\=None_, _random\_state\=None_, _warm\_start\=False_, _verbose\=0_, _verbose\_interval\=10_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_bayesian_mixture.py#L74)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "Link to this definition")

Variational Bayesian estimation of a Gaussian mixture.

This class allows to infer an approximate posterior distribution over the parameters of a Gaussian mixture distribution. The effective number of components can be inferred from the data.

This class implements two types of prior for the weights distribution: a finite mixture model with Dirichlet distribution and an infinite mixture model with the Dirichlet Process. In practice Dirichlet Process inference algorithm is approximated and uses a truncated distribution with a fixed maximum number of components (called the Stick-breaking representation). The number of components actually used almost always depends on the data.

Added in version 0.18.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/mixture.html#bgmm)
.

Parameters:

**n\_components**int, default=1

The number of mixture components. Depending on the data and the value of the `weight_concentration_prior` the model can decide to not use all the components by setting some component `weights_` to values very close to zero. The number of effective components is therefore smaller than n\_components.

**covariance\_type**{‘full’, ‘tied’, ‘diag’, ‘spherical’}, default=’full’

String describing the type of covariance parameters to use. Must be one of:

*   ‘full’ (each component has its own general covariance matrix),
    
*   ‘tied’ (all components share the same general covariance matrix),
    
*   ‘diag’ (each component has its own diagonal covariance matrix),
    
*   ‘spherical’ (each component has its own single variance).
    

**tol**float, default=1e-3

The convergence threshold. EM iterations will stop when the lower bound average gain on the likelihood (of the training data with respect to the model) is below this threshold.

**reg\_covar**float, default=1e-6

Non-negative regularization added to the diagonal of covariance. Allows to assure that the covariance matrices are all positive.

**max\_iter**int, default=100

The number of EM iterations to perform.

**n\_init**int, default=1

The number of initializations to perform. The result with the highest lower bound value on the likelihood is kept.

**init\_params**{‘kmeans’, ‘k-means++’, ‘random’, ‘random\_from\_data’}, default=’kmeans’

The method used to initialize the weights, the means and the covariances. String must be one of:

*   ‘kmeans’: responsibilities are initialized using kmeans.
    
*   ‘k-means++’: use the k-means++ method to initialize.
    
*   ‘random’: responsibilities are initialized randomly.
    
*   ‘random\_from\_data’: initial means are randomly selected data points.
    

Changed in version v1.1: `init_params` now accepts ‘random\_from\_data’ and ‘k-means++’ as initialization methods.

**weight\_concentration\_prior\_type**{‘dirichlet\_process’, ‘dirichlet\_distribution’}, default=’dirichlet\_process’

String describing the type of the weight concentration prior.

**weight\_concentration\_prior**float or None, default=None

The dirichlet concentration of each component on the weight distribution (Dirichlet). This is commonly called gamma in the literature. The higher concentration puts more mass in the center and will lead to more components being active, while a lower concentration parameter will lead to more mass at the edge of the mixture weights simplex. The value of the parameter must be greater than 0. If it is None, it’s set to `1. / n_components`.

**mean\_precision\_prior**float or None, default=None

The precision prior on the mean distribution (Gaussian). Controls the extent of where means can be placed. Larger values concentrate the cluster means around `mean_prior`. The value of the parameter must be greater than 0. If it is None, it is set to 1.

**mean\_prior**array-like, shape (n\_features,), default=None

The prior on the mean distribution (Gaussian). If it is None, it is set to the mean of X.

**degrees\_of\_freedom\_prior**float or None, default=None

The prior of the number of degrees of freedom on the covariance distributions (Wishart). If it is None, it’s set to `n_features`.

**covariance\_prior**float or array-like, default=None

The prior on the covariance distribution (Wishart). If it is None, the emiprical covariance prior is initialized using the covariance of X. The shape depends on `covariance_type`:

(n\_features, n\_features) if 'full',
(n\_features, n\_features) if 'tied',
(n\_features)             if 'diag',
float                    if 'spherical'

Copy to clipboard

**random\_state**int, RandomState instance or None, default=None

Controls the random seed given to the method chosen to initialize the parameters (see `init_params`). In addition, it controls the generation of random samples from the fitted distribution (see the method `sample`). Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**warm\_start**bool, default=False

If ‘warm\_start’ is True, the solution of the last fitting is used as initialization for the next call of fit(). This can speed up convergence when fit is called several times on similar problems. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**verbose**int, default=0

Enable verbose output. If 1 then it prints the current initialization and each iteration step. If greater than 1 then it prints also the log probability and the time needed for each step.

**verbose\_interval**int, default=10

Number of iteration done before the next print.

Attributes:

**weights\_**array-like of shape (n\_components,)

The weights of each mixture components.

**means\_**array-like of shape (n\_components, n\_features)

The mean of each mixture component.

**covariances\_**array-like

The covariance of each mixture component. The shape depends on `covariance_type`:

(n\_components,)                        if 'spherical',
(n\_features, n\_features)               if 'tied',
(n\_components, n\_features)             if 'diag',
(n\_components, n\_features, n\_features) if 'full'

Copy to clipboard

**precisions\_**array-like

The precision matrices for each component in the mixture. A precision matrix is the inverse of a covariance matrix. A covariance matrix is symmetric positive definite so the mixture of Gaussian can be equivalently parameterized by the precision matrices. Storing the precision matrices instead of the covariance matrices makes it more efficient to compute the log-likelihood of new samples at test time. The shape depends on `covariance_type`:

(n\_components,)                        if 'spherical',
(n\_features, n\_features)               if 'tied',
(n\_components, n\_features)             if 'diag',
(n\_components, n\_features, n\_features) if 'full'

Copy to clipboard

**precisions\_cholesky\_**array-like

The Cholesky decomposition of the precision matrices of each mixture component. A precision matrix is the inverse of a covariance matrix. A covariance matrix is symmetric positive definite so the mixture of Gaussian can be equivalently parameterized by the precision matrices. Storing the precision matrices instead of the covariance matrices makes it more efficient to compute the log-likelihood of new samples at test time. The shape depends on `covariance_type`:

(n\_components,)                        if 'spherical',
(n\_features, n\_features)               if 'tied',
(n\_components, n\_features)             if 'diag',
(n\_components, n\_features, n\_features) if 'full'

Copy to clipboard

**converged\_**bool

True when convergence of the best fit of inference was reached, False otherwise.

**n\_iter\_**int

Number of step used by the best fit of inference to reach the convergence.

**lower\_bound\_**float

Lower bound value on the model evidence (of the training data) of the best fit of inference.

**lower\_bounds\_**array-like of shape (`n_iter_`,)

The list of lower bound values on the model evidence from each iteration of the best fit of inference.

**weight\_concentration\_prior\_**tuple or float

The dirichlet concentration of each component on the weight distribution (Dirichlet). The type depends on `weight_concentration_prior_type`:

(float, float) if 'dirichlet\_process' (Beta parameters),
float          if 'dirichlet\_distribution' (Dirichlet parameters).

Copy to clipboard

The higher concentration puts more mass in the center and will lead to more components being active, while a lower concentration parameter will lead to more mass at the edge of the simplex.

**weight\_concentration\_**array-like of shape (n\_components,)

The dirichlet concentration of each component on the weight distribution (Dirichlet).

**mean\_precision\_prior\_**float

The precision prior on the mean distribution (Gaussian). Controls the extent of where means can be placed. Larger values concentrate the cluster means around `mean_prior`. If mean\_precision\_prior is set to None, `mean_precision_prior_` is set to 1.

**mean\_precision\_**array-like of shape (n\_components,)

The precision of each components on the mean distribution (Gaussian).

**mean\_prior\_**array-like of shape (n\_features,)

The prior on the mean distribution (Gaussian).

**degrees\_of\_freedom\_prior\_**float

The prior of the number of degrees of freedom on the covariance distributions (Wishart).

**degrees\_of\_freedom\_**array-like of shape (n\_components,)

The number of degrees of freedom of each components in the model.

**covariance\_prior\_**float or array-like

The prior on the covariance distribution (Wishart). The shape depends on `covariance_type`:

(n\_features, n\_features) if 'full',
(n\_features, n\_features) if 'tied',
(n\_features)             if 'diag',
float                    if 'spherical'

Copy to clipboard

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")

Finite Gaussian mixture fit with EM.

References

\[1\]

[Bishop, Christopher M. (2006). “Pattern recognition and machine learning”. Vol. 4 No. 4. New York: Springer.](https://www.springer.com/kr/book/9780387310732)

\[2\]

[Hagai Attias. (2000). “A Variational Bayesian Framework for Graphical Models”. In Advances in Neural Information Processing Systems 12.](https://proceedings.neurips.cc/paper_files/paper/1999/file/74563ba21a90da13dacf2a73e3ddefa7-Paper.pdf)

\[3\]

[Blei, David M. and Michael I. Jordan. (2006). “Variational inference for Dirichlet process mixtures”. Bayesian analysis 1.1](https://www.cs.princeton.edu/courses/archive/fall11/cos597C/reading/BleiJordan2005.pdf)

Examples

\>>> import numpy as np
\>>> from sklearn.mixture import BayesianGaussianMixture
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\], \[4, 2\], \[12, 4\], \[10, 7\]\])
\>>> bgm \= BayesianGaussianMixture(n\_components\=2, random\_state\=42).fit(X)
\>>> bgm.means\_
array(\[\[2.49 , 2.29\],\
       \[8.45, 4.52 \]\])
\>>> bgm.predict(\[\[0, 0\], \[9, 3\]\])
array(\[0, 1\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L172)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.fit "Link to this definition")

Estimate model parameters with the EM algorithm.

The method fits the model `n_init` times and sets the parameters with which the model has the largest likelihood or lower bound. Within each trial, the method iterates between E-step and M-step for `max_iter` times until the change of likelihood or lower bound is less than `tol`, otherwise, a `ConvergenceWarning` is raised. If `warm_start` is `True`, then `n_init` is ignored and a single initialization is performed upon the first call. Upon consecutive calls, training starts where it left off.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

The fitted mixture.

fit\_predict(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L202)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.fit_predict "Link to this definition")

Estimate model parameters using X and predict the labels for X.

The method fits the model `n_init` times and sets the parameters with which the model has the largest likelihood or lower bound. Within each trial, the method iterates between E-step and M-step for `max_iter` times until the change of likelihood or lower bound is less than `tol`, otherwise, a [`ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
 is raised. After fitting, it predicts the most probable label for the input data points.

Added in version 0.20.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**labels**array, shape (n\_samples,)

Component labels.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L395)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.predict "Link to this definition")

Predict the labels for the data samples in X using trained model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**labels**array, shape (n\_samples,)

Component labels.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L414)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.predict_proba "Link to this definition")

Evaluate the components’ density for each sample.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**resp**array, shape (n\_samples, n\_components)

Density of each Gaussian component for each sample in X.

sample(_n\_samples\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L434)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.sample "Link to this definition")

Generate random samples from the fitted Gaussian distribution.

Parameters:

**n\_samples**int, default=1

Number of samples to generate.

Returns:

**X**array, shape (n\_samples, n\_features)

Randomly generated sample.

**y**array, shape (nsamples,)

Component labels.

score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L375)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.score "Link to this definition")

Compute the per-sample average log-likelihood of the given data X.

Parameters:

**X**array-like of shape (n\_samples, n\_dimensions)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**log\_likelihood**float

Log-likelihood of `X` under the Gaussian mixture model.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L356)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.score_samples "Link to this definition")

Compute the log-likelihood of each sample.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**log\_prob**array, shape (n\_samples,)

Log-likelihood of each sample in `X` under the current model.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)