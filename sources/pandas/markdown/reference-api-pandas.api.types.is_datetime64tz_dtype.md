[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64tz_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_datetime64tz_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_datetime64tz_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_datetime64tz\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64tz_dtype.html#pandas-api-types-is-datetime64tz-dtype "Link to this heading")

====================================================================================================================================================================================================

pandas.api.types.is\_datetime64tz\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L376-L435)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64tz_dtype.html#pandas.api.types.is_datetime64tz_dtype "Link to this definition")

Check whether an array-like or dtype is of a DatetimeTZDtype dtype.

Deprecated since version 2.1.0: Use isinstance(dtype, pd.DatetimeTZDtype) instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of a DatetimeTZDtype dtype.

See also

`api.types.is_datetime64_dtype`

Check whether an array-like or dtype is of the datetime64 dtype.

`api.types.is_datetime64_any_dtype`

Check whether the provided array or dtype is of the datetime64 dtype.

Examples

\>>> from pandas.api.types import is\_datetime64tz\_dtype
\>>> is\_datetime64tz\_dtype(object)
False
\>>> is\_datetime64tz\_dtype(\[1, 2, 3\])
False
\>>> is\_datetime64tz\_dtype(pd.DatetimeIndex(\[1, 2, 3\]))  \# tz-naive
False
\>>> is\_datetime64tz\_dtype(pd.DatetimeIndex(\[1, 2, 3\], tz\="US/Eastern"))
True

Copy to clipboard

\>>> from pandas import DatetimeTZDtype
\>>> dtype \= DatetimeTZDtype("ns", tz\="US/Eastern")
\>>> s \= pd.Series(\[\], dtype\=dtype)
\>>> is\_datetime64tz\_dtype(dtype)
True
\>>> is\_datetime64tz\_dtype(s)
True

Copy to clipboard

On this page