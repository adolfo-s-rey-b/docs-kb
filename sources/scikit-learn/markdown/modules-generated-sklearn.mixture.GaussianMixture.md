[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.mixture.GaussianMixture.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.mixture.GaussianMixture.html)

Collapse Sidebar Expand Sidebar

GaussianMixture[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#gaussianmixture "Link to this heading")

==================================================================================================================================================

class sklearn.mixture.GaussianMixture(_n\_components\=1_, _\*_, _covariance\_type\='full'_, _tol\=0.001_, _reg\_covar\=1e-06_, _max\_iter\=100_, _n\_init\=1_, _init\_params\='kmeans'_, _weights\_init\=None_, _means\_init\=None_, _precisions\_init\=None_, _random\_state\=None_, _warm\_start\=False_, _verbose\=0_, _verbose\_interval\=10_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_gaussian_mixture.py#L556)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "Link to this definition")

Gaussian Mixture.

Representation of a Gaussian mixture model probability distribution. This class allows to estimate the parameters of a Gaussian mixture distribution.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/mixture.html#gmm)
.

Added in version 0.18.

Parameters:

**n\_components**int, default=1

The number of mixture components.

**covariance\_type**{‘full’, ‘tied’, ‘diag’, ‘spherical’}, default=’full’

String describing the type of covariance parameters to use. Must be one of:

*   ‘full’: each component has its own general covariance matrix.
    
*   ‘tied’: all components share the same general covariance matrix.
    
*   ‘diag’: each component has its own diagonal covariance matrix.
    
*   ‘spherical’: each component has its own single variance.
    

For an example of using `covariance_type`, refer to [Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#sphx-glr-auto-examples-mixture-plot-gmm-selection-py)
.

**tol**float, default=1e-3

The convergence threshold. EM iterations will stop when the lower bound average gain is below this threshold.

**reg\_covar**float, default=1e-6

Non-negative regularization added to the diagonal of covariance. Allows to assure that the covariance matrices are all positive.

**max\_iter**int, default=100

The number of EM iterations to perform.

**n\_init**int, default=1

The number of initializations to perform. The best results are kept.

**init\_params**{‘kmeans’, ‘k-means++’, ‘random’, ‘random\_from\_data’}, default=’kmeans’

The method used to initialize the weights, the means and the precisions. String must be one of:

*   ‘kmeans’ : responsibilities are initialized using kmeans.
    
*   ‘k-means++’ : use the k-means++ method to initialize.
    
*   ‘random’ : responsibilities are initialized randomly.
    
*   ‘random\_from\_data’ : initial means are randomly selected data points.
    

Changed in version v1.1: `init_params` now accepts ‘random\_from\_data’ and ‘k-means++’ as initialization methods.

**weights\_init**array-like of shape (n\_components, ), default=None

The user-provided initial weights. If it is None, weights are initialized using the `init_params` method.

**means\_init**array-like of shape (n\_components, n\_features), default=None

The user-provided initial means, If it is None, means are initialized using the `init_params` method.

**precisions\_init**array-like, default=None

The user-provided initial precisions (inverse of the covariance matrices). If it is None, precisions are initialized using the ‘init\_params’ method. The shape depends on ‘covariance\_type’:

(n\_components,)                        if 'spherical',
(n\_features, n\_features)               if 'tied',
(n\_components, n\_features)             if 'diag',
(n\_components, n\_features, n\_features) if 'full'

Copy to clipboard

**random\_state**int, RandomState instance or None, default=None

Controls the random seed given to the method chosen to initialize the parameters (see `init_params`). In addition, it controls the generation of random samples from the fitted distribution (see the method `sample`). Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**warm\_start**bool, default=False

If ‘warm\_start’ is True, the solution of the last fitting is used as initialization for the next call of fit(). This can speed up convergence when fit is called several times on similar problems. In that case, ‘n\_init’ is ignored and only a single initialization occurs upon the first call. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
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

For an example of using covariances, refer to [GMM covariances](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html#sphx-glr-auto-examples-mixture-plot-gmm-covariances-py)
.

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

True when convergence of the best fit of EM was reached, False otherwise.

**n\_iter\_**int

Number of step used by the best fit of EM to reach the convergence.

**lower\_bound\_**float

Lower bound value on the log-likelihood (of the training data with respect to the model) of the best fit of EM.

**lower\_bounds\_**array-like of shape (`n_iter_`,)

The list of lower bound values on the log-likelihood from each iteration of the best fit of EM.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")

Gaussian mixture model fit with a variational inference.

Examples

\>>> import numpy as np
\>>> from sklearn.mixture import GaussianMixture
\>>> X \= np.array(\[\[1, 2\], \[1, 4\], \[1, 0\], \[10, 2\], \[10, 4\], \[10, 0\]\])
\>>> gm \= GaussianMixture(n\_components\=2, random\_state\=0).fit(X)
\>>> gm.means\_
array(\[\[10.,  2.\],\
       \[ 1.,  2.\]\])
\>>> gm.predict(\[\[0, 0\], \[12, 3\]\])
array(\[1, 0\])

Copy to clipboard

For a comparison of Gaussian Mixture with other clustering algorithms, see [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)
.

For an illustration of the negative log-likelihood surface of a [`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
 Model, see [Density Estimation for a Gaussian mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html#sphx-glr-auto-examples-mixture-plot-gmm-pdf-py)
.

aic(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_gaussian_mixture.py#L982)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.aic "Link to this definition")

Akaike information criterion for the current model on the input X.

You can refer to this [mathematical section](https://scikit-learn.org/stable/modules/linear_model.html#aic-bic)
 for more details regarding the formulation of the AIC used.

Parameters:

**X**array of shape (n\_samples, n\_dimensions)

The input samples.

Returns:

**aic**float

The lower the better.

bic(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_gaussian_mixture.py#L959)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.bic "Link to this definition")

Bayesian information criterion for the current model on the input X.

You can refer to this [mathematical section](https://scikit-learn.org/stable/modules/linear_model.html#aic-bic)
 for more details regarding the formulation of the BIC used.

For an example of GMM selection using `bic` information criterion, refer to [Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#sphx-glr-auto-examples-mixture-plot-gmm-selection-py)
.

Parameters:

**X**array of shape (n\_samples, n\_dimensions)

The input samples.

Returns:

**bic**float

The lower the better.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L172)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.fit "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.fit_predict "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L395)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.predict "Link to this definition")

Predict the labels for the data samples in X using trained model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**labels**array, shape (n\_samples,)

Component labels.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L414)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.predict_proba "Link to this definition")

Evaluate the components’ density for each sample.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**resp**array, shape (n\_samples, n\_components)

Density of each Gaussian component for each sample in X.

sample(_n\_samples\=1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/mixture/_base.py#L434)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.sample "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.score_samples "Link to this definition")

Compute the log-likelihood of each sample.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

List of n\_features-dimensional data points. Each row corresponds to a single data point.

Returns:

**log\_prob**array, shape (n\_samples,)

Log-likelihood of each sample in `X` under the current model.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_thumb.png)

[Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)

Demonstration of k-means assumptions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_thumb.png)

[GMM covariances](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html)

GMM covariances

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_init_thumb.png)

[GMM Initialization Methods](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_init.html)

GMM Initialization Methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_pdf_thumb.png)

[Density Estimation for a Gaussian mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html)

Density Estimation for a Gaussian mixture

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

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