[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_ns_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_datetime64\_ns\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_ns_dtype.html#pandas-api-types-is-datetime64-ns-dtype "Link to this heading")

========================================================================================================================================================================================================

pandas.api.types.is\_datetime64\_ns\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1119-L1176)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_ns_dtype.html#pandas.api.types.is_datetime64_ns_dtype "Link to this definition")

Check whether the provided array or dtype is of the datetime64\[ns\] dtype.

This function is more restrictive than `api.types.is_datetime64_dtype()` because it requires the dtype to have nanosecond resolution specifically, including timezone-aware `DatetimeTZDtype` with nanosecond units.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

bool

Whether or not the array or dtype is of the datetime64\[ns\] dtype.

See also

`api.types.is_datetime64_dtype`

Check whether an array-like or dtype is of the datetime64 dtype.

`api.types.is_datetime64_any_dtype`

Check whether the provided array or dtype is of the datetime64 dtype.

Examples

\>>> from pandas.api.types import is\_datetime64\_ns\_dtype
\>>> from pandas.api.types import DatetimeTZDtype
\>>> is\_datetime64\_ns\_dtype(str)
False
\>>> is\_datetime64\_ns\_dtype(int)
False
\>>> is\_datetime64\_ns\_dtype(np.datetime64)  \# no unit
False
\>>> is\_datetime64\_ns\_dtype(DatetimeTZDtype("ns", "US/Eastern"))
True
\>>> is\_datetime64\_ns\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_datetime64\_ns\_dtype(np.array(\[1, 2\]))
False
\>>> is\_datetime64\_ns\_dtype(np.array(\[\], dtype\="datetime64"))  \# no unit
False
\>>> is\_datetime64\_ns\_dtype(np.array(\[\], dtype\="datetime64\[ps\]"))  \# wrong unit
False
\>>> is\_datetime64\_ns\_dtype(pd.DatetimeIndex(\[1, 2, 3\], dtype\="datetime64\[ns\]"))
True

Copy to clipboard

On this page