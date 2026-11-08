[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_period_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_period_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_period_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_period_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_period_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_period_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_period_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_period_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_period_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_period_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_period_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_period_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_period_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_period_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_period\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_period_dtype.html#pandas-api-types-is-period-dtype "Link to this heading")

==================================================================================================================================================================================

pandas.api.types.is\_period\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L485-L536)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_period_dtype.html#pandas.api.types.is_period_dtype "Link to this definition")

Check whether an array-like or dtype is of the Period dtype.

Deprecated since version 2.2.0: Use isinstance(dtype, pd.PeriodDtype) instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the Period dtype.

See also

`api.types.is_timedelta64_ns_dtype`

Check whether the provided array or dtype is of the timedelta64\[ns\] dtype.

`api.types.is_timedelta64_dtype`

Check whether an array-like or dtype is of the timedelta64 dtype.

Examples

\>>> from pandas.api.types import is\_period\_dtype
\>>> is\_period\_dtype(object)
False
\>>> is\_period\_dtype(pd.PeriodDtype(freq\="D"))
True
\>>> is\_period\_dtype(\[1, 2, 3\])
False
\>>> is\_period\_dtype(pd.Period("2017-01-01"))
False
\>>> is\_period\_dtype(pd.PeriodIndex(\[\], freq\="Y"))
True

Copy to clipboard

On this page