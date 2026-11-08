[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_sparse.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_sparse.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_sparse.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_sparse.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_sparse.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_sparse.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_sparse.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_sparse.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_sparse.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_sparse.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_sparse.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_sparse.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_sparse.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_sparse.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_sparse[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_sparse.html#pandas-api-types-is-sparse "Link to this heading")

===============================================================================================================================================================

pandas.api.types.is\_sparse(_arr_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L230-L289)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_sparse.html#pandas.api.types.is_sparse "Link to this definition")

Check whether an array-like is a 1-D pandas sparse array.

Deprecated since version 2.1.0: Use isinstance(dtype, pd.SparseDtype) instead.

Check that the one-dimensional array-like is a pandas sparse array. Returns True if it is a pandas sparse array, not another type of sparse array.

Parameters:

**arr**array-like

Array-like to check.

Returns:

bool

Whether or not the array-like is a pandas sparse array.

See also

`api.types.SparseDtype`

The dtype object for pandas sparse arrays.

Examples

Returns True if the parameter is a 1-D pandas sparse array.

\>>> from pandas.api.types import is\_sparse
\>>> is\_sparse(pd.arrays.SparseArray(\[0, 0, 1, 0\]))
True
\>>> is\_sparse(pd.Series(pd.arrays.SparseArray(\[0, 0, 1, 0\])))
True

Copy to clipboard

Returns False if the parameter is not sparse.

\>>> is\_sparse(np.array(\[0, 0, 1, 0\]))
False
\>>> is\_sparse(pd.Series(\[0, 1, 0, 0\]))
False

Copy to clipboard

Returns False if the parameter is not a pandas sparse array.

\>>> from scipy.sparse import bsr\_matrix
\>>> is\_sparse(bsr\_matrix(\[0, 1, 0, 0\]))
False

Copy to clipboard

Returns False if the parameter has more than one dimension.

On this page