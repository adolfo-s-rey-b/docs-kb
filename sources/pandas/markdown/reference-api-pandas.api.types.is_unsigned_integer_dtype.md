[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_unsigned_integer_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_unsigned_integer_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_unsigned\_integer\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_unsigned_integer_dtype.html#pandas-api-types-is-unsigned-integer-dtype "Link to this heading")

=================================================================================================================================================================================================================

pandas.api.types.is\_unsigned\_integer\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L918-L975)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_unsigned_integer_dtype.html#pandas.api.types.is_unsigned_integer_dtype "Link to this definition")

Check whether the provided array or dtype is of an unsigned integer dtype.

The nullable Integer dtypes (e.g. pandas.UInt64Dtype) are also considered as integer by this function.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of an unsigned integer dtype.

See also

`api.types.is_signed_integer_dtype`

Check whether the provided array or dtype is of a signed integer dtype.

`api.types.is_integer_dtype`

Check whether the provided array or dtype is of an integer dtype.

`api.types.is_numeric_dtype`

Check whether the provided array or dtype is of a numeric dtype.

Examples

\>>> from pandas.api.types import is\_unsigned\_integer\_dtype
\>>> is\_unsigned\_integer\_dtype(str)
False
\>>> is\_unsigned\_integer\_dtype(int)  \# signed
False
\>>> is\_unsigned\_integer\_dtype(float)
False
\>>> is\_unsigned\_integer\_dtype(np.uint64)
True
\>>> is\_unsigned\_integer\_dtype("uint8")
True
\>>> is\_unsigned\_integer\_dtype("UInt8")
True
\>>> is\_unsigned\_integer\_dtype(pd.UInt8Dtype)
True
\>>> is\_unsigned\_integer\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_unsigned\_integer\_dtype(pd.Series(\[1, 2\]))  \# signed
False
\>>> is\_unsigned\_integer\_dtype(pd.Index(\[1, 2.0\]))  \# float
False
\>>> is\_unsigned\_integer\_dtype(np.array(\[1, 2\], dtype\=np.uint32))
True

Copy to clipboard

On this page