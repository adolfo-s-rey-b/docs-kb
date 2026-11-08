[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_numeric_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_numeric_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_numeric_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_numeric_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_numeric_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_numeric_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_numeric_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_numeric\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html#pandas-api-types-is-numeric-dtype "Link to this heading")

=====================================================================================================================================================================================

pandas.api.types.is\_numeric\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1338-L1393)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html#pandas.api.types.is_numeric_dtype "Link to this definition")

Check whether the provided array or dtype is of a numeric dtype.

Numeric dtypes include integer, float, complex, and boolean types. Datetime and timedelta dtypes are not considered numeric.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of a numeric dtype.

See also

`api.types.is_integer_dtype`

Check whether the provided array or dtype is of an integer dtype.

`api.types.is_unsigned_integer_dtype`

Check whether the provided array or dtype is of an unsigned integer dtype.

`api.types.is_signed_integer_dtype`

Check whether the provided array or dtype is of a signed integer dtype.

Examples

\>>> from pandas.api.types import is\_numeric\_dtype
\>>> is\_numeric\_dtype(str)
False
\>>> is\_numeric\_dtype(int)
True
\>>> is\_numeric\_dtype(float)
True
\>>> is\_numeric\_dtype(np.uint64)
True
\>>> is\_numeric\_dtype(np.datetime64)
False
\>>> is\_numeric\_dtype(np.timedelta64)
False
\>>> is\_numeric\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_numeric\_dtype(pd.Series(\[1, 2\]))
True
\>>> is\_numeric\_dtype(pd.Index(\[1, 2.0\]))
True
\>>> is\_numeric\_dtype(np.array(\[\], dtype\="m8\[ns\]"))
False

Copy to clipboard

On this page