[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.maxabs_scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.maxabs_scale.html)

Collapse Sidebar Expand Sidebar

maxabs\_scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#maxabs-scale "Link to this heading")

================================================================================================================================================

sklearn.preprocessing.maxabs\_scale(_X_, _\*_, _axis\=0_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1451)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "Link to this definition")

Scale each feature to the \[-1, 1\] range without breaking the sparsity.

This estimator scales each feature individually such that the maximal absolute value of each feature in the training set will be 1.0.

This scaler can also be applied to sparse CSR or CSC matrices.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data.

**axis**{0, 1}, default=0

Axis used to scale along. If 0, independently scale each feature, otherwise (if 1) scale each sample.

**copy**bool, default=True

If False, try to avoid a copy and scale in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

Returns:

**X\_tr**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The transformed data.

Warning

Risk of data leak Do not use [`maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale")
 unless you know what you are doing. A common mistake is to apply it to the entire data _before_ splitting into training and test sets. This will bias the model evaluation because information would have leaked from the test set to the training set. In general, we recommend using [`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
 within a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
 in order to prevent most risks of data leaking: `pipe = make_pipeline(MaxAbsScaler(), LogisticRegression())`.

See also

[`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")

Performs scaling to the \[-1, 1\] range using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Notes

NaNs are treated as missing values: disregarded to compute the statistics, and maintained during the data transformation.

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Examples

\>>> from sklearn.preprocessing import maxabs\_scale
\>>> X \= \[\[\-2, 1, 2\], \[\-1, 0, 1\]\]
\>>> maxabs\_scale(X, axis\=0)  \# scale each column independently
array(\[\[-1. ,  1. ,  1. \],\
       \[-0.5,  0. ,  0.5\]\])
\>>> maxabs\_scale(X, axis\=1)  \# scale each row independently
array(\[\[-1. ,  0.5,  1. \],\
       \[-1. ,  0. ,  1. \]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)