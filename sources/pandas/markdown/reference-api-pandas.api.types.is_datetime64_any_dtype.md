[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_any_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_datetime64_any_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_datetime64_any_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_datetime64\_any\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_any_dtype.html#pandas-api-types-is-datetime64-any-dtype "Link to this heading")

===========================================================================================================================================================================================================

pandas.api.types.is\_datetime64\_any\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1052-L1116)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_any_dtype.html#pandas.api.types.is_datetime64_any_dtype "Link to this definition")

Check whether the provided array or dtype is of the datetime64 dtype.

Unlike `api.types.is_datetime64_dtype()`, this function also considers timezone-aware dtypes such as `DatetimeTZDtype` to be datetime64 dtypes.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

bool

Whether or not the array or dtype is of the datetime64 dtype.

See also

`api.types.is_datetime64_dtype`

Check whether an array-like or dtype is of the datetime64 dtype.

`api.is_datetime64_ns_dtype`

Check whether the provided array or dtype is of the datetime64\[ns\] dtype.

`api.is_datetime64tz_dtype`

Check whether an array-like or dtype is of a DatetimeTZDtype dtype.

Examples

\>>> from pandas.api.types import is\_datetime64\_any\_dtype
\>>> from pandas.api.types import DatetimeTZDtype
\>>> is\_datetime64\_any\_dtype(str)
False
\>>> is\_datetime64\_any\_dtype(int)
False
\>>> is\_datetime64\_any\_dtype(np.datetime64)  \# can be tz-naive
True
\>>> is\_datetime64\_any\_dtype(DatetimeTZDtype("ns", "US/Eastern"))
True
\>>> is\_datetime64\_any\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_datetime64\_any\_dtype(np.array(\[1, 2\]))
False
\>>> is\_datetime64\_any\_dtype(np.array(\[\], dtype\="datetime64\[ns\]"))
True
\>>> is\_datetime64\_any\_dtype(pd.DatetimeIndex(\[1, 2, 3\], dtype\="datetime64\[ns\]"))
True

Copy to clipboard

On this page