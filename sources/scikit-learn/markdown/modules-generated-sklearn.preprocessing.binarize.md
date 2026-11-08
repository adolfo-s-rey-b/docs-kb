[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

binarize[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html#binarize "Link to this heading")

===================================================================================================================================

sklearn.preprocessing.binarize(_X_, _\*_, _threshold\=0.0_, _copy\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_data.py#L2228)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html#sklearn.preprocessing.binarize "Link to this definition")

Boolean thresholding of array-like or scipy.sparse matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-binarization)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to binarize, element by element. scipy.sparse matrices should be in CSR or CSC format to avoid an un-necessary copy.

**threshold**float, default=0.0

Feature values below or equal to this are replaced by 0, above it by 1. Threshold may not be less than 0 for operations on sparse matrices.

**copy**bool, default=True

If False, try to avoid a copy and binarize in place. This is not guaranteed to always work in place; e.g. if the data is a numpy array with an object dtype, a copy will be returned even with copy=False.

Returns:

**X\_tr**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

The transformed data.

See also

[`Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")

Performs binarization using the Transformer API (e.g. as part of a preprocessing [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
).

Examples

\>>> from sklearn.preprocessing import binarize
\>>> X \= \[\[0.4, 0.6, 0.5\], \[0.6, 0.1, 0.2\]\]
\>>> binarize(X, threshold\=0.5)
array(\[\[0., 1., 0.\],\
       \[1., 0., 0.\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)