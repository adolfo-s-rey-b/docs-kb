[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.QuantileTransformer.html)

Collapse Sidebar Expand Sidebar

QuantileTransformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#quantiletransformer "Link to this heading")

====================================================================================================================================================================

class sklearn.preprocessing.QuantileTransformer(_\*_, _n\_quantiles\=1000_, _output\_distribution\='uniform'_, _ignore\_implicit\_zeros\=False_, _subsample\=10000_, _random\_state\=None_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L2670)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "Link to this definition")

Transform features using quantiles information.

This method transforms the features to follow a uniform or a normal distribution. Therefore, for a given feature, this transformation tends to spread out the most frequent values. It also reduces the impact of (marginal) outliers: this is therefore a robust preprocessing scheme.

The transformation is applied on each feature independently. First an estimate of the cumulative distribution function of a feature is used to map the original values to a uniform distribution. The obtained values are then mapped to the desired output distribution using the associated quantile function. Features values of new/unseen data that fall below or above the fitted range will be mapped to the bounds of the output distribution. Note that this transform is non-linear. It may distort linear correlations between variables measured at the same scale but renders variables measured at different scales more directly comparable.

For example visualizations, refer to [Compare QuantileTransformer with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-quantile-transformer-section)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-transformer)
.

Added in version 0.19.

Parameters:

**n\_quantiles**int, default=1000 or n\_samples

Number of quantiles to be computed. It corresponds to the number of landmarks used to discretize the cumulative distribution function. If n\_quantiles is larger than the number of samples, n\_quantiles is set to the number of samples as a larger number of quantiles does not give a better approximation of the cumulative distribution function estimator.

**output\_distribution**{‘uniform’, ‘normal’}, default=’uniform’

Marginal distribution for the transformed data. The choices are ‘uniform’ (default) or ‘normal’.

**ignore\_implicit\_zeros**bool, default=False

Only applies to sparse matrices. If True, the sparse entries of the matrix are discarded to compute the quantile statistics, including when subsampling. If False, these entries are treated as zeros.

**subsample**int or None, default=10\_000

Maximum number of samples used to estimate the quantiles for computational efficiency. Note that the subsampling procedure may differ for value-identical sparse and dense matrices. Disable subsampling by setting `subsample=None`.

Added in version 1.5: The option `None` to disable subsampling was added.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for subsampling and smoothing noise. Please see `subsample` for more details. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**copy**bool, default=True

Set to False to perform inplace transformation and avoid a copy (if the input is already a numpy array).

Attributes:

**n\_quantiles\_**int

The actual number of quantiles used to discretize the cumulative distribution function.

**quantiles\_**ndarray of shape (n\_quantiles, n\_features)

The values corresponding the quantiles of reference.

**references\_**ndarray of shape (n\_quantiles, )

Quantiles of references.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")

Equivalent function without the estimator API.

[`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")

Perform mapping to a normal distribution using a power transform.

[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

Perform standardization that is faster, but less robust to outliers.

[`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")

Perform robust standardization that removes the influence of outliers but does not put outliers and inliers on the same scale.

Notes

NaNs are treated as missing values: disregarded in fit, and maintained in transform.

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import QuantileTransformer
\>>> rng \= np.random.RandomState(0)
\>>> X \= np.sort(rng.normal(loc\=0.5, scale\=0.25, size\=(25, 1)), axis\=0)
\>>> qt \= QuantileTransformer(n\_quantiles\=10, random\_state\=0)
\>>> qt.fit\_transform(X)
array(\[...\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L2881)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.fit "Link to this definition")

Compute the quantiles used for transforming.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data used to scale along the features axis. If a sparse matrix is provided, it will be converted into a sparse CSC matrix. Additionally, the sparse matrix needs to be nonnegative if `ignore_implicit_zeros` is False.

**y**None

Ignored.

Returns:

**self**object

Fitted transformer.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L994)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Same as input features.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3075)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.inverse_transform "Link to this definition")

Back-projection to the original space.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data used to scale along the features axis. If a sparse matrix is provided, it will be converted into a sparse CSC\_matrix. Additionally, the sparse matrix needs to be nonnegative if `ignore_implicit_zeros` is False.

Returns:

**X\_original**{ndarray, sparse matrix} of (n\_samples, n\_features)

The projected data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3054)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer.transform "Link to this definition")

Feature-wise transformation of the data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data used to scale along the features axis. If a sparse matrix is provided, it will be converted into a sparse CSC matrix. Additionally, the sparse matrix needs to be nonnegative if `ignore_implicit_zeros` is False.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The projected data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_thumb.png)

[Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)

Map data to a normal distribution

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)