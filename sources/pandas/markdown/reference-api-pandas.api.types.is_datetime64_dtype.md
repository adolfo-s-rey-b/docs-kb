[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_datetime64\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_dtype.html#pandas-api-types-is-datetime64-dtype "Link to this heading")

==============================================================================================================================================================================================

pandas.api.types.is\_datetime64\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L330-L373)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_dtype.html#pandas.api.types.is_datetime64_dtype "Link to this definition")

Check whether an array-like or dtype is of the datetime64 dtype.

This function checks for the base `datetime64` dtype without regard to timezone information. For timezone-aware checks, use `api.types.is_datetime64_any_dtype()` instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the datetime64 dtype.

See also

`api.types.is_datetime64_ns_dtype`

Check whether the provided array or dtype is of the datetime64\[ns\] dtype.

`api.types.is_datetime64_any_dtype`

Check whether the provided array or dtype is of the datetime64 dtype.

Examples

\>>> from pandas.api.types import is\_datetime64\_dtype
\>>> is\_datetime64\_dtype(object)
False
\>>> is\_datetime64\_dtype(np.datetime64)
True
\>>> is\_datetime64\_dtype(np.array(\[\], dtype\=int))
False
\>>> is\_datetime64\_dtype(np.array(\[\], dtype\=np.datetime64))
True
\>>> is\_datetime64\_dtype(\[1, 2, 3\])
False

Copy to clipboard

On this page