[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils._safe_indexing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils._safe_indexing.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils._safe_indexing.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils._safe_indexing.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils._safe_indexing.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils._safe_indexing.html)

Collapse Sidebar Expand Sidebar

\_safe\_indexing[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#safe-indexing "Link to this heading")

==============================================================================================================================================

sklearn.utils.\_safe\_indexing(_X_, _indices_, _\*_, _axis\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_indexing.py#L205)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "Link to this definition")

Return rows, items or columns of X using indices.

Warning

This utility is documented, but **private**. This means that backward compatibility might be broken without any deprecation cycle.

Parameters:

**X**array-like, sparse-matrix, list, pandas.DataFrame, pandas.Series

Data from which to sample rows, items or columns. `list` are only supported when `axis=0`.

**indices**bool, int, str, slice, array-like

*   If `axis=0`, boolean and integer array-like, integer slice, and scalar integer are supported.
    
*   If `axis=1`:
    
    *   to select a single column, `indices` can be of `int` type for all `X` types and `str` only for dataframe. The selected subset will be 1D, unless `X` is a sparse matrix in which case it will be 2D.
        
    *   to select multiples columns, `indices` can be one of the following: `list`, `array`, `slice`. The type used in these containers can be one of the following: `int`, ‘bool’ and `str`. However, `str` is only supported when `X` is a dataframe. The selected subset will be 2D.
        
    

**axis**int, default=0

The axis along which `X` will be subsampled. `axis=0` will select rows while `axis=1` will select columns.

Returns:

subset

Subset of X on axis 0 or 1.

Notes

CSR, CSC, and LIL sparse matrices are supported. COO sparse matrices are not supported.

Examples

\>>> import numpy as np
\>>> from sklearn.utils import \_safe\_indexing
\>>> data \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> \_safe\_indexing(data, 0, axis\=0)  \# select the first row
array(\[1, 2\])
\>>> \_safe\_indexing(data, 0, axis\=1)  \# select the first column
array(\[1, 3, 5\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)