[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.normalize.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.normalize.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.normalize.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.normalize.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.normalize.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.normalize.html)

Collapse Sidebar Expand Sidebar

normalize[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#normalize "Link to this heading")

======================================================================================================================================

sklearn.preprocessing.normalize(_X_, _norm\='l2'_, _\*_, _axis\=1_, _copy\=True_, _return\_norm\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L1968)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "Link to this definition")

Scale input vectors individually to unit norm (vector length).

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-normalization)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to normalize, element by element. scipy.sparse matrices should be in CSR format to avoid an un-necessary copy.

**norm**{‘l1’, ‘l2’, ‘max’}, default=’l2’

The norm to use to normalize each non zero sample (or each non-zero feature if axis is 0).

**axis**{0, 1}, default=1

Define axis used to normalize the data along. If 1, independently normalize each sample, otherwise (if 0) normalize each feature.

**copy**bool, default=True

If False, try to avoid a copy and normalize in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an int dtype, a copy will be returned even with copy=False.

**return\_norm**bool, default=False

Whether to return the computed norms.

Returns:

**X**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Normalized input X.

**norms**ndarray of shape (n\_samples, ) if axis=1 else (n\_features, )

An array of norms along given axis for X. When X is sparse, a NotImplementedError will be raised for norm ‘l1’ or ‘l2’.

See also

[`Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")

Performs normalization using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Notes

For a comparison of the different scalers, transformers, and normalizers, see: [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
.

Examples

\>>> from sklearn.preprocessing import normalize
\>>> X \= \[\[\-2, 1, 2\], \[\-1, 0, 1\]\]
\>>> normalize(X, norm\="l1")  \# L1 normalization each row independently
array(\[\[-0.4,  0.2,  0.4\],\
       \[-0.5,  0. ,  0.5\]\])
\>>> normalize(X, norm\="l2")  \# L2 normalization each row independently
array(\[\[-0.67, 0.33, 0.67\],\
       \[-0.71, 0.  , 0.71\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)