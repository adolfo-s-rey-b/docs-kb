[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_timedelta64\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_dtype.html#pandas-api-types-is-timedelta64-dtype "Link to this heading")

=================================================================================================================================================================================================

pandas.api.types.is\_timedelta64\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L438-L482)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_dtype.html#pandas.api.types.is_timedelta64_dtype "Link to this definition")

Check whether an array-like or dtype is of the timedelta64 dtype.

This function checks if the provided array-like object or dtype corresponds to a timedelta64 dtype, which is used to represent differences between two datetime values.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the timedelta64 dtype.

See also

`api.types.is_timedelta64_ns_dtype`

Check whether the provided array or dtype is of the timedelta64\[ns\] dtype.

`api.types.is_period_dtype`

Check whether an array-like or dtype is of the Period dtype.

Examples

\>>> from pandas.api.types import is\_timedelta64\_dtype
\>>> is\_timedelta64\_dtype(object)
False
\>>> is\_timedelta64\_dtype(np.timedelta64)
True
\>>> is\_timedelta64\_dtype(\[1, 2, 3\])
False
\>>> is\_timedelta64\_dtype(pd.Series(\[\], dtype\="timedelta64\[ns\]"))
True
\>>> is\_timedelta64\_dtype("0 days")
False

Copy to clipboard

On this page