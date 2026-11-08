[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.PowerTransformer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.PowerTransformer.html)

Collapse Sidebar Expand Sidebar

PowerTransformer[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#powertransformer "Link to this heading")

===========================================================================================================================================================

class sklearn.preprocessing.PowerTransformer(_method\='yeo-johnson'_, _\*_, _standardize\=True_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3264)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "Link to this definition")

Apply a power transform featurewise to make data more Gaussian-like.

Power transforms are a family of parametric, monotonic transformations that are applied to make data more Gaussian-like. This is useful for modeling issues related to heteroscedasticity (non-constant variance), or other situations where normality is desired.

Currently, PowerTransformer supports the Box-Cox transform and the Yeo-Johnson transform. The optimal parameter for stabilizing variance and minimizing skewness is estimated through maximum likelihood.

Box-Cox requires input data to be strictly positive, while Yeo-Johnson supports both positive or negative data.

By default, zero-mean, unit-variance normalization is applied to the transformed data.

For an example visualization, refer to [Compare PowerTransformer with other scalers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#plot-all-scaling-power-transformer-section)
. To see the effect of Box-Cox and Yeo-Johnson transformations on different distributions, see: [Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html#sphx-glr-auto-examples-preprocessing-plot-map-data-to-normal-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-transformer)
.

Added in version 0.20.

Parameters:

**method**{‘yeo-johnson’, ‘box-cox’}, default=’yeo-johnson’

The power transform method. Available methods are:

*   ‘yeo-johnson’ [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#rf3e1504535de-1)
    , works with positive and negative values
    
*   ‘box-cox’ [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#rf3e1504535de-2)
    , only works with strictly positive values
    

**standardize**bool, default=True

Set to True to apply zero-mean, unit-variance normalization to the transformed output.

**copy**bool, default=True

Set to False to perform inplace computation during transformation.

Attributes:

**lambdas\_**ndarray of float of shape (n\_features,)

The parameters of the power transformation for the selected features.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")

Equivalent function without the estimator API.

[`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")

Maps data to a standard normal distribution with the parameter `output_distribution='normal'`.

Notes

NaNs are treated as missing values: disregarded in `fit`, and maintained in `transform`.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#id1)\
\]

[I.K. Yeo and R.A. Johnson, “A new family of power transformations to improve normality or symmetry.” Biometrika, 87(4), pp.954-959, (2000).](https://doi.org/10.1093/biomet/87.4.954)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#id2)\
\]

[G.E.P. Box and D.R. Cox, “An Analysis of Transformations”, Journal of the Royal Statistical Society B, 26, 211-252 (1964).](https://doi.org/10.1111/j.2517-6161.1964.tb00553.x)

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import PowerTransformer
\>>> pt \= PowerTransformer()
\>>> data \= \[\[1, 2\], \[3, 2\], \[4, 5\]\]
\>>> print(pt.fit(data))
PowerTransformer()
\>>> print(pt.lambdas\_)
\[ 1.386 -3.100\]
\>>> print(pt.transform(data))
\[\[-1.316 -0.707\]\
 \[ 0.209 -0.707\]\
 \[ 1.106  1.414\]\]

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3373)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.fit "Link to this definition")

Estimate the optimal parameter lambda for each feature.

The optimal lambda parameter for minimizing skewness is estimated on each feature independently using maximum likelihood.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data used to estimate the optimal transformation parameters.

**y**None

Ignored.

Returns:

**self**object

Fitted transformer.

fit\_transform(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3396)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.fit_transform "Link to this definition")

Fit `PowerTransformer` to `X`, then transform `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data used to estimate the optimal transformation parameters and to be transformed using a power transformation.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**X\_new**ndarray of shape (n\_samples, n\_features)

Transformed data.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L994)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.get_feature_names_out "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3489)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.inverse_transform "Link to this definition")

Apply the inverse power transformation using the fitted lambdas.

The inverse of the Box-Cox transformation is given by:

if lambda\_ \== 0:
    X\_original \= exp(X\_trans)
else:
    X\_original \= (X \* lambda\_ + 1) \*\* (1 / lambda\_)

Copy to clipboard

The inverse of the Yeo-Johnson transformation is given by:

if X \>= 0 and lambda\_ \== 0:
    X\_original \= exp(X) \- 1
elif X \>= 0 and lambda\_ != 0:
    X\_original \= (X \* lambda\_ + 1) \*\* (1 / lambda\_) \- 1
elif X < 0 and lambda\_ != 2:
    X\_original \= 1 \- (\-(2 \- lambda\_) \* X + 1) \*\* (1 / (2 \- lambda\_))
elif X < 0 and lambda\_ \== 2:
    X\_original \= 1 \- exp(\-X)

Copy to clipboard

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The transformed data.

Returns:

**X\_original**ndarray of shape (n\_samples, n\_features)

The original data.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3460)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer.transform "Link to this definition")

Apply the power transform to each feature using the fitted lambdas.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to be transformed using a power transformation.

Returns:

**X\_trans**ndarray of shape (n\_samples, n\_features)

The transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

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