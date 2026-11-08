[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)

Collapse Sidebar Expand Sidebar

MaxAbsScaler[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#maxabsscaler "Link to this heading")

===============================================================================================================================================

class sklearn.preprocessing.MaxAbsScaler(_\*_, _copy\=True_, _clip\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1190)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "Link to this definition")

Scale each feature by its maximum absolute value.

This estimator scales and translates each feature individually such that the maximal absolute value of each feature in the training set will be 1.0. It does not shift/center the data, and thus does not destroy any sparsity.

This scaler can also be applied to sparse CSR or CSC matrices.

`MaxAbsScaler` doesn’t reduce the effect of outliers; it only linearly scales them down. For an example visualization, refer to [Compare MaxAbsScaler with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-max-abs-scaler-section)
.

Added in version 0.17.

Parameters:

**copy**bool, default=True

Set to False to perform inplace scaling and avoid a copy (if the input is already a numpy array).

**clip**bool, default=False

Set to True to clip transformed values of held-out data to \[-1, 1\]. Since this parameter will clip values, `inverse_transform` may not be able to restore the original data.

Note

Setting `clip=True` does not prevent feature drift (a distribution shift between training and test data). The transformed values are clipped to the \[-1, 1\] range, which helps avoid unintended behavior in models sensitive to out-of-range inputs (e.g. linear models). Use with care, as clipping can distort the distribution of test data.

Attributes:

**scale\_**ndarray of shape (n\_features,)

Per feature relative scaling of the data.

Added in version 0.17: _scale\__ attribute.

**max\_abs\_**ndarray of shape (n\_features,)

Per feature maximum absolute value.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_samples\_seen\_**int

The number of samples processed by the estimator. Will be reset on new calls to fit, but increments across `partial_fit` calls.

See also

[`maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale")

Equivalent function without the estimator API.

Notes

NaNs are treated as missing values: disregarded in fit, and maintained in transform.

Examples

\>>> from sklearn.preprocessing import MaxAbsScaler
\>>> X \= \[\[ 1., \-1.,  2.\],\
...      \[ 2.,  0.,  0.\],\
...      \[ 0.,  1., \-1.\]\]
\>>> transformer \= MaxAbsScaler().fit(X)
\>>> transformer
MaxAbsScaler()
\>>> transformer.transform(X)
array(\[\[ 0.5, -1. ,  1. \],\
       \[ 1. ,  0. ,  0. \],\
       \[ 0. ,  1. , -0.5\]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1295)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.fit "Link to this definition")

Compute the maximum absolute value to be used for later scaling.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data used to compute the per-feature minimum and maximum used for later scaling along the features axis.

**y**None

Ignored.

Returns:

**self**object

Fitted scaler.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1412)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.inverse_transform "Link to this definition")

Scale back the data to the original representation.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data that should be transformed back.

Returns:

**X\_original**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Transformed array.

partial\_fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1316)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.partial_fit "Link to this definition")

Online computation of max absolute value of X for later scaling.

All of X is processed as a single batch. This is intended for cases when [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.fit "sklearn.preprocessing.MaxAbsScaler.fit")
 is not feasible due to very large number of `n_samples` or because X is read from a continuous stream.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data used to compute the mean and standard deviation used for later scaling along the features axis.

**y**None

Ignored.

Returns:

**self**object

Fitted scaler.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1366)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler.transform "Link to this definition")

Scale the data.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data that should be scaled.

Returns:

**X\_tr**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Transformed array.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)