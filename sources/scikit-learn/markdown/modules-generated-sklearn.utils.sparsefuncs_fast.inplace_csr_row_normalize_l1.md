[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html)

Collapse Sidebar Expand Sidebar

inplace\_csr\_row\_normalize\_l1[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html#inplace-csr-row-normalize-l1 "Link to this heading")

============================================================================================================================================================================================================

sklearn.utils.sparsefuncs\_fast.inplace\_csr\_row\_normalize\_l1(_X_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html#sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1 "Link to this definition")

Normalize inplace the rows of a CSR matrix or array by their L1 norm.

Parameters:

**X**scipy.sparse.csr\_matrix and scipy.sparse.csr\_array, shape=(n\_samples, n\_features)

The input matrix or array to be modified inplace.

Examples

\>>> from scipy.sparse import csr\_array
\>>> from sklearn.utils.sparsefuncs\_fast import inplace\_csr\_row\_normalize\_l1
\>>> import numpy as np
\>>> indptr \= np.array(\[0, 2, 3, 4\])
\>>> indices \= np.array(\[0, 1, 2, 3\])
\>>> data \= np.array(\[1.0, 2.0, 3.0, 4.0\])
\>>> X \= csr\_array((data, indices, indptr), shape\=(3, 4))
\>>> X.toarray()
array(\[\[1., 2., 0., 0.\],\
       \[0., 0., 3., 0.\],\
       \[0., 0., 0., 4.\]\])
\>>> inplace\_csr\_row\_normalize\_l1(X)
\>>> X.toarray()
array(\[\[0.33...   , 0.66...   , 0.        , 0.        \],\
       \[0.        , 0.        , 1.        , 0.        \],\
       \[0.        , 0.        , 0.        , 1.        \]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)