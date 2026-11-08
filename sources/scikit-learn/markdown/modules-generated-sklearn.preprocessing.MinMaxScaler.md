[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

Collapse Sidebar Expand Sidebar

MinMaxScaler[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#minmaxscaler "Link to this heading")

===============================================================================================================================================

class sklearn.preprocessing.MinMaxScaler(_feature\_range\=(0, 1)_, _\*_, _copy\=True_, _clip\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L305)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "Link to this definition")

Transform features by scaling each feature to a given range.

This estimator scales and translates each feature individually such that it is in the given range on the training set, e.g. between zero and one.

The transformation is given by:

X\_std \= (X \- X.min(axis\=0)) / (X.max(axis\=0) \- X.min(axis\=0))
X\_scaled \= X\_std \* (max \- min) + min

Copy to clipboard

where min, max = feature\_range.

This transformation is often used as an alternative to zero mean, unit variance scaling.

`MinMaxScaler` doesn’t reduce the effect of outliers, but it linearly scales them down into a fixed range, where the largest occurring data point corresponds to the maximum value and the smallest one corresponds to the minimum value. For an example visualization, refer to [Compare MinMaxScaler with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-minmax-scaler-section)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)
.

Parameters:

**feature\_range**tuple (min, max), default=(0, 1)

Desired range of transformed data.

**copy**bool, default=True

Set to False to perform inplace row normalization and avoid a copy (if the input is already a numpy array).

**clip**bool, default=False

Set to True to clip transformed values of held-out data to provided `feature_range`. Since this parameter will clip values, `inverse_transform` may not be able to restore the original data.

Note

Setting `clip=True` does not prevent feature drift (a distribution shift between training and test data). The transformed values are clipped to the `feature_range`, which helps avoid unintended behavior in models sensitive to out-of-range inputs (e.g. linear models). Use with care, as clipping can distort the distribution of test data.

Added in version 0.24.

Attributes:

**min\_**ndarray of shape (n\_features,)

Per feature adjustment for minimum. Equivalent to `min - X.min(axis=0) * self.scale_`

**scale\_**ndarray of shape (n\_features,)

Per feature relative scaling of the data. Equivalent to `(max - min) / (X.max(axis=0) - X.min(axis=0))`

Added in version 0.17: _scale\__ attribute.

**data\_min\_**ndarray of shape (n\_features,)

Per feature minimum seen in the data

Added in version 0.17: _data\_min\__

**data\_max\_**ndarray of shape (n\_features,)

Per feature maximum seen in the data

Added in version 0.17: _data\_max\__

**data\_range\_**ndarray of shape (n\_features,)

Per feature range `(data_max_ - data_min_)` seen in the data

Added in version 0.17: _data\_range\__

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**n\_samples\_seen\_**int

The number of samples processed by the estimator. It will be reset on new calls to fit, but increments across `partial_fit` calls.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")

Equivalent function without the estimator API.

Notes

NaNs are treated as missing values: disregarded in fit, and maintained in transform.

Examples

\>>> from sklearn.preprocessing import MinMaxScaler
\>>> data \= \[\[\-1, 2\], \[\-0.5, 6\], \[0, 10\], \[1, 18\]\]
\>>> scaler \= MinMaxScaler()
\>>> print(scaler.fit(data))
MinMaxScaler()
\>>> print(scaler.data\_max\_)
\[ 1. 18.\]
\>>> print(scaler.transform(data))
\[\[0.   0.  \]\
 \[0.25 0.25\]\
 \[0.5  0.5 \]\
 \[1.   1.  \]\]
\>>> print(scaler.transform(\[\[2, 2\]\]))
\[\[1.5 0. \]\]

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L454)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit "Link to this definition")

Compute the minimum and maximum to be used for later scaling.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data used to compute the per-feature minimum and maximum used for later scaling along the features axis.

**y**None

Ignored.

Returns:

**self**object

Fitted scaler.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L588)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.inverse_transform "Link to this definition")

Undo the scaling of X according to feature\_range.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data that will be transformed. It cannot be sparse.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

Transformed data.

partial\_fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L475)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.partial_fit "Link to this definition")

Online computation of min and max on X for later scaling.

All of X is processed as a single batch. This is intended for cases when [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.fit "sklearn.preprocessing.MinMaxScaler.fit")
 is not feasible due to very large number of `n_samples` or because X is read from a continuous stream.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data used to compute the mean and standard deviation used for later scaling along the features axis.

**y**None

Ignored.

Returns:

**self**object

Fitted scaler.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L547)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler.transform "Link to this definition")

Scale features of X according to feature\_range.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data that will be transformed.

Returns:

**Xt**ndarray of shape (n\_samples, n\_features)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_thumb.png)

[Recursive feature elimination](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)

Recursive feature elimination

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)

[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)

Scalable learning with polynomial kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)

[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)

Compare Stochastic learning strategies for MLPClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)