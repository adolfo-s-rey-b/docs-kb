[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html)

Collapse Sidebar Expand Sidebar

KBinsDiscretizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#kbinsdiscretizer "Link to this heading")

===========================================================================================================================================================

class sklearn.preprocessing.KBinsDiscretizer(_n\_bins\=5_, _\*_, _encode\='onehot'_, _strategy\='quantile'_, _quantile\_method\='averaged\_inverted\_cdf'_, _dtype\=None_, _subsample\=200000_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_discretization.py#L24)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "Link to this definition")

Bin continuous data into intervals.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-discretization)
.

Added in version 0.20.

Parameters:

**n\_bins**int or array-like of shape (n\_features,), default=5

The number of bins to produce. Raises ValueError if `n_bins < 2`.

**encode**{‘onehot’, ‘onehot-dense’, ‘ordinal’}, default=’onehot’

Method used to encode the transformed result.

*   ‘onehot’: Encode the transformed result with one-hot encoding and return a sparse matrix. Ignored features are always stacked to the right.
    
*   ‘onehot-dense’: Encode the transformed result with one-hot encoding and return a dense array. Ignored features are always stacked to the right.
    
*   ‘ordinal’: Return the bin identifier encoded as an integer value.
    

**strategy**{‘uniform’, ‘quantile’, ‘kmeans’}, default=’quantile’

Strategy used to define the widths of the bins.

*   ‘uniform’: All bins in each feature have identical widths.
    
*   ‘quantile’: All bins in each feature have the same number of points.
    
*   ‘kmeans’: Values in each bin have the same nearest center of a 1D k-means cluster.
    

For an example of the different strategies see: [Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html#sphx-glr-auto-examples-preprocessing-plot-discretization-strategies-py)
.

**quantile\_method**{“inverted\_cdf”, “averaged\_inverted\_cdf”,

“closest\_observation”, “interpolated\_inverted\_cdf”, “hazen”, “weibull”, “linear”, “median\_unbiased”, “normal\_unbiased”}, default=”averaged\_inverted\_cdf” Method to pass on to np.percentile calculation when using strategy=”quantile”. Only `averaged_inverted_cdf` and `inverted_cdf` support the use of `sample_weight != None` when subsampling is not active.

Added in version 1.7.

Changed in version 1.9: The default value changed from `"linear"` to `"averaged_inverted_cdf"`.

**dtype**{np.float32, np.float64}, default=None

The desired data-type for the output. If None, output dtype is consistent with input dtype. Only np.float32 and np.float64 are supported.

Added in version 0.24.

**subsample**int or None, default=200\_000

Maximum number of samples, used to fit the model, for computational efficiency. `subsample=None` means that all the training samples are used when computing the quantiles that determine the binning thresholds. Since quantile computation relies on sorting each column of `X` and that sorting has an `n log(n)` time complexity, it is recommended to use subsampling on datasets with a very large number of samples.

Changed in version 1.3: The default value of `subsample` changed from `None` to `200_000` when `strategy="quantile"`.

Changed in version 1.5: The default value of `subsample` changed from `None` to `200_000` when `strategy="uniform"` or `strategy="kmeans"`.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for subsampling. Pass an int for reproducible results across multiple function calls. See the `subsample` parameter for more details. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Added in version 1.1.

Attributes:

**bin\_edges\_**ndarray of ndarray of shape (n\_features,)

The edges of each bin. Contain arrays of varying shapes `(n_bins_, )` Ignored features will have empty arrays.

**n\_bins\_**ndarray of shape (n\_features,), dtype=np.int64

Number of bins per feature. Bins whose width are too small (i.e., <= 1e-8) are removed with a warning.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")

Class used to bin values as `0` or `1` based on a parameter `threshold`.

Notes

For a visualization of discretization on different datasets refer to [Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html#sphx-glr-auto-examples-preprocessing-plot-discretization-classification-py)
. On the effect of discretization on linear models see: [Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html#sphx-glr-auto-examples-preprocessing-plot-discretization-py)
.

In bin edges for feature `i`, the first and last values are used only for `inverse_transform`. During transform, bin edges are extended to:

np.concatenate(\[\-np.inf, bin\_edges\_\[i\]\[1:\-1\], np.inf\])

Copy to clipboard

You can combine `KBinsDiscretizer` with [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 if you only want to preprocess part of the features.

`KBinsDiscretizer` might produce constant features (e.g., when `encode = 'onehot'` and certain bins do not contain any data). These features can be removed with feature selection algorithms (e.g., [`VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
).

Examples

\>>> from sklearn.preprocessing import KBinsDiscretizer
\>>> X \= \[\[\-2, 1, \-4,   \-1\],\
...      \[\-1, 2, \-3, \-0.5\],\
...      \[ 0, 3, \-2,  0.5\],\
...      \[ 1, 4, \-1,    2\]\]
\>>> est \= KBinsDiscretizer(
...     n\_bins\=3, encode\='ordinal', strategy\='uniform'
... )
\>>> est.fit(X)
KBinsDiscretizer(...)
\>>> Xt \= est.transform(X)
\>>> Xt
array(\[\[ 0., 0., 0., 0.\],\
       \[ 1., 1., 1., 0.\],\
       \[ 2., 2., 2., 1.\],\
       \[ 2., 2., 2., 2.\]\])

Copy to clipboard

Sometimes it may be useful to convert the data back into the original feature space. The `inverse_transform` function converts the binned data into the original feature space. Each value will be equal to the mean of the two bin edges.

\>>> est.bin\_edges\_\[0\]
array(\[-2., -1.,  0.,  1.\])
\>>> est.inverse\_transform(Xt)
array(\[\[-1.5,  1.5, -3.5, -0.5\],\
       \[-0.5,  2.5, -2.5, -0.5\],\
       \[ 0.5,  3.5, -1.5,  0.5\],\
       \[ 0.5,  3.5, -1.5,  1.5\]\])

Copy to clipboard

While this preprocessing step can be an optimization, it is important to note the array returned by `inverse_transform` will have an internal type of `np.float64` or `np.float32`, denoted by the `dtype` input argument. This can drastically increase the memory usage of the array. See the [Vector Quantization Example](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#sphx-glr-auto-examples-cluster-plot-face-compress-py)
 where `KBinsDescretizer` is used to cluster the image into bins and increases the size of the image by 8x.

fit(_X_, _y\=None_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_discretization.py#L238)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.fit "Link to this definition")

Fit the estimator.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data to be discretized.

**y**None

Ignored. This parameter exists only for compatibility with [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
.

**sample\_weight**ndarray of shape (n\_samples,)

Contains weight values to be associated with each sample.

Added in version 1.3.

Changed in version 1.7: Added support for strategy=”uniform”.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.fit_transform "Link to this definition")

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

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_discretization.py#L510)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.get_feature_names_out "Link to this definition")

Get output feature names.

Parameters:

**input\_features**array-like of str or None, default=None

Input features.

*   If `input_features` is `None`, then `feature_names_in_` is used as feature names in. If `feature_names_in_` is not defined, then the following input feature names are generated: `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
    
*   If `input_features` is an array-like, then `input_features` must match `feature_names_in_` if `feature_names_in_` is defined.
    

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_discretization.py#L471)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.inverse_transform "Link to this definition")

Transform discretized data back to original feature space.

Note that this function does not regenerate the original data due to discretization rounding.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Transformed data in the binned space.

Returns:

**X\_original**ndarray, dtype={np.float32, np.float64}

Data in the original feature space.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing._discretization.KBinsDiscretizer")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_discretization.py#L432)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.transform "Link to this definition")

Discretize the data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data to be discretized.

Returns:

**Xt**{ndarray, sparse matrix}, dtype={np.float32, np.float64}

Data in the binned space. Will be a sparse matrix if `self.encode='onehot'` and ndarray otherwise.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_thumb.png)

[Vector Quantization Example](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html)

Vector Quantization Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)

[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)

Using KBinsDiscretizer to discretize continuous features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_cross_val_thumb.png)

[Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html)

Target Encoder's Internal Cross fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)