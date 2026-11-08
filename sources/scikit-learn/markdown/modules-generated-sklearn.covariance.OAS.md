[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.OAS.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.OAS.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.OAS.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.OAS.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.OAS.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.OAS.html)

Collapse Sidebar Expand Sidebar

OAS[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#oas "Link to this heading")

=================================================================================================================

class sklearn.covariance.OAS(_\*_, _store\_precision\=True_, _assume\_centered\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_shrunk_covariance.py#L688)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "Link to this definition")

Oracle Approximating Shrinkage Estimator.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance)
.

Parameters:

**store\_precision**bool, default=True

Specify if the estimated precision is stored.

**assume\_centered**bool, default=False

If True, data will not be centered before computation. Useful when working with data whose mean is almost, but not exactly zero. If False (default), data will be centered before computation.

Attributes:

**covariance\_**ndarray of shape (n\_features, n\_features)

Estimated covariance matrix.

**location\_**ndarray of shape (n\_features,)

Estimated location, i.e. the estimated mean.

**precision\_**ndarray of shape (n\_features, n\_features)

Estimated pseudo inverse matrix. (stored only if store\_precision is True)

**shrinkage\_**float

coefficient in the convex combination used for the computation of the shrunk estimate. Range is \[0, 1\].

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")

An object for detecting outliers in a Gaussian distributed dataset.

[`EmpiricalCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")

Maximum likelihood covariance estimator.

[`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")

Sparse inverse covariance estimation with an l1-penalized estimator.

[`GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")

Sparse inverse covariance with cross-validated choice of the l1 penalty.

[`LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")

LedoitWolf Estimator.

[`MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")

Minimum Covariance Determinant (robust estimator of covariance).

[`ShrunkCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")

Covariance estimator with shrinkage.

Notes

The regularised covariance is:

(1 - shrinkage) \* cov + shrinkage \* mu \* np.identity(n\_features),

where mu = trace(cov) / n\_features and shrinkage is given by the OAS formula (see [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#r69773891e6a6-1)
).

The shrinkage formulation implemented here differs from Eq. 23 in [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#r69773891e6a6-1)
. In the original article, formula (23) states that 2/p (p being the number of features) is multiplied by Trace(cov\*cov) in both the numerator and denominator, but this operation is omitted because for a large p, the value of 2/p is so small that it doesn’t affect the value of the estimator.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#id2)
)

[“Shrinkage algorithms for MMSE covariance estimation.”, Chen, Y., Wiesel, A., Eldar, Y. C., & Hero, A. O. IEEE Transactions on Signal Processing, 58(10), 5016-5029, 2010.](https://arxiv.org/abs/0907.4698)

Examples

\>>> import numpy as np
\>>> from sklearn.covariance import OAS
\>>> from sklearn.datasets import make\_gaussian\_quantiles
\>>> real\_cov \= np.array(\[\[.8, .3\],\
...                      \[.3, .4\]\])
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.multivariate\_normal(mean\=\[0, 0\],
...                             cov\=real\_cov,
...                             size\=500)
\>>> oas \= OAS().fit(X)
\>>> oas.covariance\_
array(\[\[0.7533, 0.2763\],\
       \[0.2763, 0.3964\]\])
\>>> oas.precision\_
array(\[\[ 1.7833, -1.2431 \],\
       \[-1.2431,  3.3889\]\])
\>>> oas.shrinkage\_
np.float64(0.0195)

Copy to clipboard

See also [Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html#sphx-glr-auto-examples-covariance-plot-covariance-estimation-py)
 and [Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html#sphx-glr-auto-examples-covariance-plot-lw-vs-oas-py)
 for more detailed examples.

error\_norm(_comp\_cov_, _norm\='frobenius'_, _scaling\=True_, _squared\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L290)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.error_norm "Link to this definition")

Compute the Mean Squared Error between two covariance estimators.

Parameters:

**comp\_cov**array-like of shape (n\_features, n\_features)

The covariance to compare with.

**norm**{“frobenius”, “spectral”}, default=”frobenius”

The type of norm used to compute the error. Available error types: - ‘frobenius’ (default): sqrt(tr(A^t.A)) - ‘spectral’: sqrt(max(eigenvalues(A^t.A)) where A is the error `(comp_cov - self.covariance_)`.

**scaling**bool, default=True

If True (default), the squared error norm is divided by n\_features. If False, the squared error norm is not rescaled.

**squared**bool, default=True

Whether to compute the squared error norm or the error norm. If True (default), the squared error norm is returned. If False, the error norm is returned.

Returns:

**result**float

The Mean Squared Error (in the sense of the Frobenius norm) between `self` and `comp_cov` covariance estimators.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_shrunk_covariance.py#L793)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.fit "Link to this definition")

Fit the Oracle Approximating Shrinkage covariance model to X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L217)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.get_precision "Link to this definition")

Getter for the precision matrix.

Returns:

**precision\_**array-like of shape (n\_features, n\_features)

The precision matrix associated to the current covariance object.

mahalanobis(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.mahalanobis "Link to this definition")

Compute the squared Mahalanobis distances of given observations.

For a detailed example of how outliers affects the Mahalanobis distance, see [Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#sphx-glr-auto-examples-covariance-plot-mahalanobis-distances-py)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The observations, the Mahalanobis distances of the which we compute. Observations are assumed to be drawn from the same distribution than the data used in fit.

Returns:

**dist**ndarray of shape (n\_samples,)

Squared Mahalanobis distances of the observations.

score(_X\_test_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L259)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.score "Link to this definition")

Compute the log-likelihood of `X_test` under the estimated Gaussian model.

The Gaussian model is defined by its mean and covariance matrix which are represented respectively by `self.location_` and `self.covariance_`.

Parameters:

**X\_test**array-like of shape (n\_samples, n\_features)

Test data of which we compute the likelihood, where `n_samples` is the number of samples and `n_features` is the number of features. `X_test` is assumed to be drawn from the same distribution than the data used in fit (including centering).

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**res**float

The log-likelihood of `X_test` with `self.location_` and `self.covariance_` as estimators of the Gaussian model mean and covariance matrix respectively.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)