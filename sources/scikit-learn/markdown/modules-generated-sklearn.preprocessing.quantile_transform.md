[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

quantile\_transform[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#quantile-transform "Link to this heading")

==================================================================================================================================================================

sklearn.preprocessing.quantile\_transform(_X_, _\*_, _axis\=0_, _n\_quantiles\=1000_, _output\_distribution\='uniform'_, _ignore\_implicit\_zeros\=False_, _subsample\=100000_, _random\_state\=None_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3116)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "Link to this definition")

Transform features using quantiles information.

This method transforms the features to follow a uniform or a normal distribution. Therefore, for a given feature, this transformation tends to spread out the most frequent values. It also reduces the impact of (marginal) outliers: this is therefore a robust preprocessing scheme.

The transformation is applied on each feature independently. First an estimate of the cumulative distribution function of a feature is used to map the original values to a uniform distribution. The obtained values are then mapped to the desired output distribution using the associated quantile function. Features values of new/unseen data that fall below or above the fitted range will be mapped to the bounds of the output distribution. Note that this transform is non-linear. It may distort linear correlations between variables measured at the same scale but renders variables measured at different scales more directly comparable.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-transformer)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to transform.

**axis**int, default=0

Axis used to compute the means and standard deviations along. If 0, transform each feature, otherwise (if 1) transform each sample.

**n\_quantiles**int, default=1000 or n\_samples

Number of quantiles to be computed. It corresponds to the number of landmarks used to discretize the cumulative distribution function. If n\_quantiles is larger than the number of samples, n\_quantiles is set to the number of samples as a larger number of quantiles does not give a better approximation of the cumulative distribution function estimator.

**output\_distribution**{‘uniform’, ‘normal’}, default=’uniform’

Marginal distribution for the transformed data. The choices are ‘uniform’ (default) or ‘normal’.

**ignore\_implicit\_zeros**bool, default=False

Only applies to sparse matrices. If True, the sparse entries of the matrix are discarded to compute the quantile statistics, including when subsampling. If False, these entries are treated as zeros.

**subsample**int or None, default=1e5

Maximum number of samples used to estimate the quantiles for computational efficiency. Note that the subsampling procedure may differ for value-identical sparse and dense matrices. Disable subsampling by setting `subsample=None`.

Added in version 1.5: The option `None` to disable subsampling was added.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for subsampling and smoothing noise. Please see `subsample` for more details. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**copy**bool, default=True

If False, try to avoid a copy and transform in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

Changed in version 0.23: The default value of `copy` changed from False to True in 0.23.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The transformed data.

See also

[`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")

Performs quantile-based scaling using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

[`power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")

Maps data to a normal distribution using a power transformation.

[`scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")

Performs standardization that is faster, but less robust to outliers.

[`robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale")

Performs robust standardization that removes the influence of outliers but does not put outliers and inliers on the same scale.

Notes

NaNs are treated as missing values: disregarded in fit, and maintained in transform.

Warning

Risk of data leak

Do not use [`quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking:`pipe = make_pipeline(QuantileTransformer(), LogisticRegression())`.

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import quantile\_transform
\>>> rng \= np.random.RandomState(0)
\>>> X \= np.sort(rng.normal(loc\=0.5, scale\=0.25, size\=(25, 1)), axis\=0)
\>>> quantile\_transform(X, n\_quantiles\=10, random\_state\=0, copy\=True)
array(\[...\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)