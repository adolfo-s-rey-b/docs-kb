[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.robust_scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.robust_scale.html)

Collapse Sidebar Expand Sidebar

robust\_scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#robust-scale "Link to this heading")

================================================================================================================================================

sklearn.preprocessing.robust\_scale(_X_, _\*_, _axis\=0_, _with\_centering\=True_, _with\_scaling\=True_, _quantile\_range\=(25.0, 75.0)_, _copy\=True_, _unit\_variance\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1827)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "Link to this definition")

Standardize a dataset along any axis.

Center to the median and component wise scale according to the interquartile range.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_sample, n\_features)

The data to center and scale.

**axis**int, default=0

Axis used to compute the medians and IQR along. If 0, independently scale each feature, otherwise (if 1) scale each sample.

**with\_centering**bool, default=True

If `True`, center the data before scaling.

**with\_scaling**bool, default=True

If `True`, scale the data to unit variance (or equivalently, unit standard deviation).

**quantile\_range**tuple (q\_min, q\_max), 0.0 < q\_min < q\_max < 100.0, default=(25.0, 75.0)

Quantile range used to calculate `scale_`. By default this is equal to the IQR, i.e., `q_min` is the first quantile and `q_max` is the third quantile.

Added in version 0.18.

**copy**bool, default=True

If False, try to avoid a copy and scale in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

**unit\_variance**bool, default=False

If `True`, scale data so that normally distributed features have a variance of 1. In general, if the difference between the x-values of `q_max` and `q_min` for a standard normal distribution is greater than 1, the dataset will be scaled down. If less than 1, the dataset will be scaled up.

Added in version 0.24.

Returns:

**X\_tr**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The transformed data.

See also

[`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")

Performs centering and scaling using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Notes

This implementation will refuse to center scipy.sparse matrices since it would make them non-sparse and would potentially crash the program with memory exhaustion problems.

Instead the caller is expected to either set explicitly `with_centering=False` (in that case, only variance scaling will be performed on the features of the CSR matrix) or to call `X.toarray()` if he/she expects the materialized dense array to fit in memory.

To avoid memory copy the caller should pass a CSR matrix.

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Warning

Risk of data leak

Do not use [`robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking: `pipe = make_pipeline(RobustScaler(), LogisticRegression())`.

Examples

\>>> from sklearn.preprocessing import robust\_scale
\>>> X \= \[\[\-2, 1, 2\], \[\-1, 0, 1\]\]
\>>> robust\_scale(X, axis\=0)  \# scale each column independently
array(\[\[-1.,  1.,  1.\],\
       \[ 1., -1., -1.\]\])
\>>> robust\_scale(X, axis\=1)  \# scale each row independently
array(\[\[-1.5,  0. ,  0.5\],\
       \[-1. ,  0. ,  1. \]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)