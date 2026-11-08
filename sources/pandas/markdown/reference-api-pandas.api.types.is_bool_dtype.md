[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_bool_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_bool_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_bool_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_bool_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_bool_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_bool_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_bool_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_bool_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_bool_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_bool_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_bool_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_bool_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_bool\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html#pandas-api-types-is-bool-dtype "Link to this heading")

============================================================================================================================================================================

pandas.api.types.is\_bool\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1492-L1570)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html#pandas.api.types.is_bool_dtype "Link to this definition")

Check whether the provided array or dtype is of a boolean dtype.

This function verifies whether a given object is a boolean data type. The input can be an array or a dtype object. Accepted array types include instances of `np.array`, `pd.Series`, `pd.Index`, and similar array-like structures.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of a boolean dtype.

See also

`api.types.is_bool`

Check if an object is a boolean.

Notes

An ExtensionArray is considered boolean when the `_is_boolean` attribute is set to True.

Examples

\>>> from pandas.api.types import is\_bool\_dtype
\>>> is\_bool\_dtype(str)
False
\>>> is\_bool\_dtype(int)
False
\>>> is\_bool\_dtype(bool)
True
\>>> is\_bool\_dtype(np.bool\_)
True
\>>> is\_bool\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_bool\_dtype(pd.Series(\[1, 2\]))
False
\>>> is\_bool\_dtype(np.array(\[True, False\]))
True
\>>> is\_bool\_dtype(pd.Categorical(\[True, False\]))
True
\>>> is\_bool\_dtype(pd.arrays.SparseArray(\[True, False\]))
True

Copy to clipboard

On this page