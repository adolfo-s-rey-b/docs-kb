[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.power_transform.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.power_transform.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.power_transform.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.power_transform.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.power_transform.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.power_transform.html)

Collapse Sidebar Expand Sidebar

power\_transform[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#power-transform "Link to this heading")

=========================================================================================================================================================

sklearn.preprocessing.power\_transform(_X_, _method\='yeo-johnson'_, _\*_, _standardize\=True_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L3662)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "Link to this definition")

Parametric, monotonic transformation to make data more Gaussian-like.

Power transforms are a family of parametric, monotonic transformations that are applied to make data more Gaussian-like. This is useful for modeling issues related to heteroscedasticity (non-constant variance), or other situations where normality is desired.

Currently, power\_transform supports the Box-Cox transform and the Yeo-Johnson transform. The optimal parameter for stabilizing variance and minimizing skewness is estimated through maximum likelihood.

Box-Cox requires input data to be strictly positive, while Yeo-Johnson supports both positive or negative data.

By default, zero-mean, unit-variance normalization is applied to the transformed data.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-transformer)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data to be transformed using a power transformation.

**method**{‘yeo-johnson’, ‘box-cox’}, default=’yeo-johnson’

The power transform method. Available methods are:

*   ‘yeo-johnson’ [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#r742a88cfa144-1)
    , works with positive and negative values
    
*   ‘box-cox’ [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#r742a88cfa144-2)
    , only works with strictly positive values
    

Changed in version 0.23: The default value of the `method` parameter changed from ‘box-cox’ to ‘yeo-johnson’ in 0.23.

**standardize**bool, default=True

Set to True to apply zero-mean, unit-variance normalization to the transformed output.

**copy**bool, default=True

If False, try to avoid a copy and transform in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

Returns:

**X\_trans**ndarray of shape (n\_samples, n\_features)

The transformed data.

See also

[`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")

Equivalent transformation with the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

[`quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")

Maps data to a standard normal distribution with the parameter `output_distribution='normal'`.

Notes

NaNs are treated as missing values: disregarded in `fit`, and maintained in `transform`.

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#id1)\
\]

I.K. Yeo and R.A. Johnson, “A new family of power transformations to improve normality or symmetry.” Biometrika, 87(4), pp.954-959, (2000).

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#id2)\
\]

G.E.P. Box and D.R. Cox, “An Analysis of Transformations”, Journal of the Royal Statistical Society B, 26, 211-252 (1964).

Examples

\>>> import numpy as np
\>>> from sklearn.preprocessing import power\_transform
\>>> data \= \[\[1, 2\], \[3, 2\], \[4, 5\]\]
\>>> print(power\_transform(data, method\='box-cox'))
\[\[-1.332 -0.707\]\
 \[ 0.256 -0.707\]\
 \[ 1.076  1.414\]\]

Copy to clipboard

Warning

Risk of data leak. Do not use [`power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking, e.g.: `pipe = make_pipeline(PowerTransformer(), LogisticRegression())`.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)