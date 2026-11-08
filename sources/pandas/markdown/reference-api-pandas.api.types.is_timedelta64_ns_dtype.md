[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_timedelta64\_ns\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html#pandas-api-types-is-timedelta64-ns-dtype "Link to this heading")

===========================================================================================================================================================================================================

pandas.api.types.is\_timedelta64\_ns\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1179-L1214)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html#pandas.api.types.is_timedelta64_ns_dtype "Link to this definition")

Check whether the provided array or dtype is of the timedelta64\[ns\] dtype.

This is a very specific dtype, so generic ones like np.timedelta64 will return False if passed into this function.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of the timedelta64\[ns\] dtype.

See also

`api.types.is_timedelta64_dtype`

Check whether an array-like or dtype is of the timedelta64 dtype.

Examples

\>>> from pandas.api.types import is\_timedelta64\_ns\_dtype
\>>> is\_timedelta64\_ns\_dtype(np.dtype("m8\[ns\]"))
True
\>>> is\_timedelta64\_ns\_dtype(np.dtype("m8\[ps\]"))  \# Wrong frequency
False
\>>> is\_timedelta64\_ns\_dtype(np.array(\[1, 2\], dtype\="m8\[ns\]"))
True
\>>> is\_timedelta64\_ns\_dtype(np.array(\[1, 2\], dtype\="m8\[ms\]"))
False

Copy to clipboard

On this page