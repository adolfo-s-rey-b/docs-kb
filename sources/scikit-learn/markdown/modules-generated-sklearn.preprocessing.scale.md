[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.scale.html)

Collapse Sidebar Expand Sidebar

scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#scale "Link to this heading")

==========================================================================================================================

sklearn.preprocessing.scale(_X_, _\*_, _axis\=0_, _with\_mean\=True_, _with\_std\=True_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L136)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "Link to this definition")

Standardize a dataset along any axis.

Center to the mean and component wise scale to unit variance.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to center and scale.

**axis**{0, 1}, default=0

Axis used to compute the means and standard deviations along. If 0, independently standardize each feature, otherwise (if 1) standardize each sample.

**with\_mean**bool, default=True

If True, center the data before scaling.

**with\_std**bool, default=True

If True, scale the data to unit variance (or equivalently, unit standard deviation).

**copy**bool, default=True

If False, try to avoid a copy and scale in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

Returns:

**X\_tr**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The transformed data.

See also

[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

Performs scaling to unit variance using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Notes

This implementation will refuse to center scipy.sparse matrices since it would make them non-sparse and would potentially crash the program with memory exhaustion problems.

Instead the caller is expected to either set explicitly `with_mean=False` (in that case, only variance scaling will be performed on the features of the CSC matrix) or to call `X.toarray()` if he/she expects the materialized dense array to fit in memory.

To avoid memory copy the caller should pass a CSC matrix.

NaNs are treated as missing values: disregarded to compute the statistics, and maintained during the data transformation.

We use a biased estimator for the standard deviation, equivalent to `numpy.std(x, ddof=0)`. Note that the choice of `ddof` is unlikely to affect model performance.

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Warning

Risk of data leak

Do not use [`scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking: `pipe = make_pipeline(StandardScaler(), LogisticRegression())`.

Examples

\>>> from sklearn.preprocessing import scale
\>>> X \= \[\[\-2, 1, 2\], \[\-1, 0, 1\]\]
\>>> scale(X, axis\=0)  \# scaling each column independently
array(\[\[-1.,  1.,  1.\],\
       \[ 1., -1., -1.\]\])
\>>> scale(X, axis\=1)  \# scaling each row independently
array(\[\[-1.37,  0.39,  0.98\],\
       \[-1.22,  0.     ,  1.22\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)