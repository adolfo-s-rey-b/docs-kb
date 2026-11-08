[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.EllipticEnvelope.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.EllipticEnvelope.html)

Collapse Sidebar Expand Sidebar

EllipticEnvelope[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#ellipticenvelope "Link to this heading")

========================================================================================================================================================

class sklearn.covariance.EllipticEnvelope(_\*_, _store\_precision\=True_, _assume\_centered\=False_, _support\_fraction\=None_, _contamination\=0.1_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L15)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "Link to this definition")

An object for detecting outliers in a Gaussian distributed dataset.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
.

Parameters:

**store\_precision**bool, default=True

Specify if the estimated precision is stored.

**assume\_centered**bool, default=False

If True, the support of robust location and covariance estimates is computed, and a covariance estimate is recomputed from it, without centering the data. Useful to work with data whose mean is significantly equal to zero but is not exactly zero. If False, the robust location and covariance are directly computed with the FastMCD algorithm without additional treatment.

**support\_fraction**float, default=None

The proportion of points to be included in the support of the raw MCD estimate. If None, the minimum value of support\_fraction will be used within the algorithm: `(n_samples + n_features + 1) / 2 * n_samples`. Range is (0, 1).

**contamination**float, default=0.1

The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Range is (0, 0.5\].

**random\_state**int, RandomState instance or None, default=None

Determines the pseudo random number generator for shuffling the data. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**location\_**ndarray of shape (n\_features,)

Estimated robust location.

**covariance\_**ndarray of shape (n\_features, n\_features)

Estimated robust covariance matrix.

**precision\_**ndarray of shape (n\_features, n\_features)

Estimated pseudo inverse matrix. (stored only if store\_precision is True)

**support\_**ndarray of shape (n\_samples,)

A mask of the observations that have been used to compute the robust estimates of location and shape.

**offset\_**float

Offset used to define the decision function from the raw scores. We have the relation: `decision_function = score_samples - offset_`. The offset depends on the contamination parameter and is defined in such a way we obtain the expected number of outliers (samples with decision function < 0) in training.

Added in version 0.20.

**raw\_location\_**ndarray of shape (n\_features,)

The raw robust estimated location before correction and re-weighting.

**raw\_covariance\_**ndarray of shape (n\_features, n\_features)

The raw robust estimated covariance before correction and re-weighting.

**raw\_support\_**ndarray of shape (n\_samples,)

A mask of the observations that have been used to compute the raw robust estimates of location and shape, before correction and re-weighting.

**dist\_**ndarray of shape (n\_samples,)

Mahalanobis distances of the training set (on which [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.fit "sklearn.covariance.EllipticEnvelope.fit")
 is called) observations.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`EmpiricalCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")

Maximum likelihood covariance estimator.

[`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")

Sparse inverse covariance estimation with an l1-penalized estimator.

[`LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")

LedoitWolf Estimator.

[`MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")

Minimum Covariance Determinant (robust estimator of covariance).

[`OAS`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")

Oracle Approximating Shrinkage Estimator.

[`ShrunkCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")

Covariance estimator with shrinkage.

Notes

Outlier detection from covariance estimation may break or not perform well in high-dimensional settings. In particular, one will always take care to work with `n_samples > n_features ** 2`.

References

\[1\]

Rousseeuw, P.J., Van Driessen, K. “A fast algorithm for the minimum covariance determinant estimator” Technometrics 41(3), 212 (1999)

Examples

\>>> import numpy as np
\>>> from sklearn.covariance import EllipticEnvelope
\>>> true\_cov \= np.array(\[\[.8, .3\],\
...                      \[.3, .4\]\])
\>>> X \= np.random.RandomState(0).multivariate\_normal(mean\=\[0, 0\],
...                                                  cov\=true\_cov,
...                                                  size\=500)
\>>> cov \= EllipticEnvelope(random\_state\=0).fit(X)
\>>> \# predict returns 1 for an inlier and -1 for an outlier
\>>> cov.predict(\[\[0, 0\],\
...              \[3, 3\]\])
array(\[ 1, -1\])
\>>> cov.covariance\_
array(\[\[0.8102, 0.2736\],\
       \[0.2736, 0.3330\]\])
\>>> cov.location\_
array(\[0.0769 , 0.0397\])

Copy to clipboard

correct\_covariance(_data_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_robust_covariance.py#L824)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.correct_covariance "Link to this definition")

Apply a correction to raw Minimum Covariance Determinant estimates.

Correction using the asymptotic correction factor derived by [\[Croux1999\]](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#rbb2ba44703ed-croux1999)
.

Parameters:

**data**array-like of shape (n\_samples, n\_features)

The data matrix, with p features and n samples. The data set must be the one which was used to compute the raw estimates.

Returns:

**covariance\_corrected**ndarray of shape (n\_features, n\_features)

Corrected robust covariance estimate.

References

\[[Croux1999](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#id2)\
\]

Influence Function and Efficiency of the Minimum Covariance Determinant Scatter Matrix Estimator, 1999, Journal of Multivariate Analysis, Volume 71, Issue 2, Pages 161-190

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L187)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.decision_function "Link to this definition")

Compute the decision function of the given observations.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**decision**ndarray of shape (n\_samples,)

Decision function of the samples. It is equal to the shifted Mahalanobis distances. The threshold for being an outlier is 0, which ensures a compatibility with other outlier detection algorithms.

error\_norm(_comp\_cov_, _norm\='frobenius'_, _scaling\=True_, _squared\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L290)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.error_norm "Link to this definition")

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

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L166)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.fit "Link to this definition")

Fit the EllipticEnvelope model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_predict(_X_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1141)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.fit_predict "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_precision()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L217)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.get_precision "Link to this definition")

Getter for the precision matrix.

Returns:

**precision\_**array-like of shape (n\_features, n\_features)

The precision matrix associated to the current covariance object.

mahalanobis(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L341)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.mahalanobis "Link to this definition")

Compute the squared Mahalanobis distances of given observations.

For a detailed example of how outliers affects the Mahalanobis distance, see [Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#sphx-glr-auto-examples-covariance-plot-mahalanobis-distances-py)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The observations, the Mahalanobis distances of the which we compute. Observations are assumed to be drawn from the same distribution than the data used in fit.

Returns:

**dist**ndarray of shape (n\_samples,)

Squared Mahalanobis distances of the observations.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.predict "Link to this definition")

Predict labels (1 inlier, -1 outlier) of X according to fitted model.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**is\_inlier**ndarray of shape (n\_samples,)

Returns -1 for anomalies/outliers and +1 for inliers.

reweight\_covariance(_data_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_robust_covariance.py#L863)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.reweight_covariance "Link to this definition")

Re-weight raw Minimum Covariance Determinant estimates.

Re-weight observations using Rousseeuw’s method (equivalent to deleting outlying observations from the data set before computing location and covariance estimates) described in [\[RVDriessen\]](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#rd2c89e63f1c9-rvdriessen)
.

Corrects the re-weighted covariance to be consistent at the normal distribution, following [\[Croux1999\]](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#rd2c89e63f1c9-croux1999)
.

Parameters:

**data**array-like of shape (n\_samples, n\_features)

The data matrix, with p features and n samples. The data set must be the one which was used to compute the raw estimates.

Returns:

**location\_reweighted**ndarray of shape (n\_features,)

Re-weighted robust location estimate.

**covariance\_reweighted**ndarray of shape (n\_features, n\_features)

Re-weighted robust covariance estimate.

**support\_reweighted**ndarray of shape (n\_samples,), dtype=bool

A mask of the observations that have been used to compute the re-weighted robust location and covariance estimates.

References

\[[RVDriessen](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#id4)\
\]

A Fast Algorithm for the Minimum Covariance Determinant Estimator, 1999, American Statistical Association and the American Society for Quality, TECHNOMETRICS

\[[Croux1999](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#id5)\
\]

Influence Function and Efficiency of the Minimum Covariance Determinant Scatter Matrix Estimator, 1999, Journal of Multivariate Analysis, Volume 71, Issue 2, Pages 161-190

score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L243)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.score "Link to this definition")

Return the mean accuracy on the given test data and labels.

In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Test samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

True labels for X.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

Mean accuracy of self.predict(X) w.r.t. y.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_elliptic_envelope.py#L207)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.score_samples "Link to this definition")

Compute the negative Mahalanobis distances.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data matrix.

Returns:

**negative\_mahal\_distances**array-like of shape (n\_samples,)

Opposite of the Mahalanobis distances.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)