[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.indexable.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.indexable.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.indexable.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.indexable.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.indexable.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.indexable.html)

Collapse Sidebar Expand Sidebar

indexable[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html#indexable "Link to this heading")

==============================================================================================================================

sklearn.utils.indexable(_\*iterables_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L484)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html#sklearn.utils.indexable "Link to this definition")

Make arrays indexable for cross-validation.

Checks consistent length, passes through None, and ensures that everything can be indexed by converting sparse matrices to csr and converting non-iterable objects to arrays.

Parameters:

**\*iterables**{lists, dataframes, ndarrays, sparse matrices}

List of objects to ensure sliceability.

Returns:

**result**list of {ndarray, sparse matrix, dataframe} or None

Returns a list containing indexable arrays (i.e. NumPy array, sparse matrix, or dataframe) or `None`.

Examples

\>>> from sklearn.utils import indexable
\>>> from scipy.sparse import csr\_array
\>>> import numpy as np
\>>> iterables \= \[\
...     \[1, 2, 3\], np.array(\[2, 3, 4\]), None, csr\_array(\[\[5\], \[6\], \[7\]\])\
... \]
\>>> indexable(\*iterables)
\[\[1, 2, 3\], array(\[2, 3, 4\]), None, <...Sparse...dtype 'int64'...shape (3, 1)>\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)