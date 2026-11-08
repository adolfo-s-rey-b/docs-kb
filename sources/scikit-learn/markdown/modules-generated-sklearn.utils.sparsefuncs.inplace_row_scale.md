[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html)

Collapse Sidebar Expand Sidebar

inplace\_row\_scale[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html#inplace-row-scale "Link to this heading")

====================================================================================================================================================================

sklearn.utils.sparsefuncs.inplace\_row\_scale(_X_, _scale_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/sparsefuncs.py#L339)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html#sklearn.utils.sparsefuncs.inplace_row_scale "Link to this definition")

Inplace row scaling of a CSR or CSC matrix.

Scale each row of the data matrix by multiplying with specific scale provided by the caller assuming a (n\_samples, n\_features) shape.

Parameters:

**X**sparse matrix of shape (n\_samples, n\_features)

Matrix to be scaled. It should be of CSR or CSC format.

**scale**ndarray of shape (n\_features,), dtype={np.float32, np.float64}

Array of precomputed sample-wise values to use for scaling.

Examples

\>>> from sklearn.utils import sparsefuncs
\>>> from scipy import sparse
\>>> import numpy as np
\>>> indptr \= np.array(\[0, 2, 3, 4, 5\])
\>>> indices \= np.array(\[0, 1, 2, 3, 3\])
\>>> data \= np.array(\[8, 1, 2, 5, 6\])
\>>> scale \= np.array(\[2, 3, 4, 5\])
\>>> csr \= sparse.csr\_array((data, indices, indptr))
\>>> csr.todense()
array(\[\[8, 1, 0, 0\],\
       \[0, 0, 2, 0\],\
       \[0, 0, 0, 5\],\
       \[0, 0, 0, 6\]\])
\>>> sparsefuncs.inplace\_row\_scale(csr, scale)
\>>> csr.todense()
 array(\[\[16,  2,  0,  0\],\
        \[ 0,  0,  6,  0\],\
        \[ 0,  0,  0, 20\],\
        \[ 0,  0,  0, 30\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)