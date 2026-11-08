[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.minmax_scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.minmax_scale.html)

Collapse Sidebar Expand Sidebar

minmax\_scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#minmax-scale "Link to this heading")

================================================================================================================================================

sklearn.preprocessing.minmax\_scale(_X_, _feature\_range\=(0, 1)_, _\*_, _axis\=0_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L624)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "Link to this definition")

Transform features by scaling each feature to a given range.

This estimator scales and translates each feature individually such that it is in the given range on the training set, i.e. between zero and one.

The transformation is given by (when `axis=0`):

X\_std \= (X \- X.min(axis\=0)) / (X.max(axis\=0) \- X.min(axis\=0))
X\_scaled \= X\_std \* (max \- min) + min

Copy to clipboard

where min, max = feature\_range.

The transformation is calculated as (when `axis=0`):

X\_scaled \= scale \* X + min \- X.min(axis\=0) \* scale
where scale \= (max \- min) / (X.max(axis\=0) \- X.min(axis\=0))

Copy to clipboard

This transformation is often used as an alternative to zero mean, unit variance scaling.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)
.

Added in version 0.17: _minmax\_scale_ function interface to [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The data.

**feature\_range**tuple (min, max), default=(0, 1)

Desired range of transformed data.

**axis**{0, 1}, default=0

Axis used to scale along. If 0, independently scale each feature, otherwise (if 1) scale each sample.

**copy**bool, default=True

If False, try to avoid a copy and scale in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

Returns:

**X\_tr**ndarray of shape (n\_samples, n\_features)

The transformed data.

Warning

Risk of data leak Do not use [`minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking: `pipe = make_pipeline(MinMaxScaler(), LogisticRegression())`.

See also

[`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")

Performs scaling to a given range using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Notes

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Examples

\>>> from sklearn.preprocessing import minmax\_scale
\>>> X \= \[\[\-2, 1, 2\], \[\-1, 0, 1\]\]
\>>> minmax\_scale(X, axis\=0)  \# scale each column independently
array(\[\[0., 1., 1.\],\
       \[1., 0., 0.\]\])
\>>> minmax\_scale(X, axis\=1)  \# scale each row independently
array(\[\[0.  , 0.75, 1.  \],\
       \[0.  , 0.5 , 1.  \]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

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