[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html)

Collapse Sidebar Expand Sidebar

inplace\_column\_scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html#inplace-column-scale "Link to this heading")

=============================================================================================================================================================================

sklearn.utils.sparsefuncs.inplace\_column\_scale(_X_, _scale_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/sparsefuncs.py#L294)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html#sklearn.utils.sparsefuncs.inplace_column_scale "Link to this definition")

Inplace column scaling of a CSC/CSR matrix.

Scale each feature of the data matrix by multiplying with specific scale provided by the caller assuming a (n\_samples, n\_features) shape.

Parameters:

**X**sparse matrix of shape (n\_samples, n\_features)

Matrix to normalize using the variance of the features. It should be of CSC or CSR format.

**scale**ndarray of shape (n\_features,), dtype={np.float32, np.float64}

Array of precomputed feature-wise values to use for scaling.

Examples

\>>> from sklearn.utils import sparsefuncs
\>>> from scipy import sparse
\>>> import numpy as np
\>>> indptr \= np.array(\[0, 3, 4, 4, 4\])
\>>> indices \= np.array(\[0, 1, 2, 2\])
\>>> data \= np.array(\[8, 1, 2, 5\])
\>>> scale \= np.array(\[2, 3, 2\])
\>>> csr \= sparse.csr\_array((data, indices, indptr))
\>>> csr.todense()
array(\[\[8, 1, 2\],\
       \[0, 0, 5\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])
\>>> sparsefuncs.inplace\_column\_scale(csr, scale)
\>>> csr.todense()
array(\[\[16,  3,  4\],\
       \[ 0,  0, 10\],\
       \[ 0,  0,  0\],\
       \[ 0,  0,  0\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)