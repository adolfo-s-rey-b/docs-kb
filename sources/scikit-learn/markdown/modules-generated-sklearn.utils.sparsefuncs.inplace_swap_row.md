[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html)

Collapse Sidebar Expand Sidebar

inplace\_swap\_row[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html#inplace-swap-row "Link to this heading")

=================================================================================================================================================================

sklearn.utils.sparsefuncs.inplace\_swap\_row(_X_, _m_, _n_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/sparsefuncs.py#L475)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html#sklearn.utils.sparsefuncs.inplace_swap_row "Link to this definition")

Swap two rows of a CSC/CSR matrix in-place.

Parameters:

**X**sparse matrix of shape (n\_samples, n\_features)

Matrix whose two rows are to be swapped. It should be of CSR or CSC format.

**m**int

Index of the row of X to be swapped.

**n**int

Index of the row of X to be swapped.

Examples

\>>> from sklearn.utils import sparsefuncs
\>>> from scipy import sparse
\>>> import numpy as np
\>>> indptr \= np.array(\[0, 2, 3, 3, 3\])
\>>> indices \= np.array(\[0, 2, 2\])
\>>> data \= np.array(\[8, 2, 5\])
\>>> csr \= sparse.csr\_array((data, indices, indptr))
\>>> csr.todense()
array(\[\[8, 0, 2\],\
       \[0, 0, 5\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])
\>>> sparsefuncs.inplace\_swap\_row(csr, 0, 1)
\>>> csr.todense()
array(\[\[0, 0, 5\],\
       \[8, 0, 2\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)