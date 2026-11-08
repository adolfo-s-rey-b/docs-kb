[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_int64_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_int64_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_int64_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_int64_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_int64_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_int64_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_int64_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_int64_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_int64_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_int64_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_int64_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_int64_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_int64_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_int64_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_int64\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_int64_dtype.html#pandas-api-types-is-int64-dtype "Link to this heading")

===============================================================================================================================================================================

pandas.api.types.is\_int64\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L978-L1049)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_int64_dtype.html#pandas.api.types.is_int64_dtype "Link to this definition")

Check whether the provided array or dtype is of the int64 dtype.

Deprecated since version 2.1.0: is\_int64\_dtype is deprecated and will be removed in a future version. Use dtype == np.int64 instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of the int64 dtype.

See also

`api.types.is_float_dtype`

Check whether the provided array or dtype is of a float dtype.

`api.types.is_bool_dtype`

Check whether the provided array or dtype is of a boolean dtype.

`api.types.is_object_dtype`

Check whether an array-like or dtype is of the object dtype.

[`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "(in NumPy v2.5)")

Numpy’s 64-bit integer type.

Notes

Depending on system architecture, the return value of is\_int64\_dtype( int) will be True if the OS uses 64-bit integers and False if the OS uses 32-bit integers.

Examples

\>>> from pandas.api.types import is\_int64\_dtype
\>>> is\_int64\_dtype(str)
False
\>>> is\_int64\_dtype(np.int32)
False
\>>> is\_int64\_dtype(np.int64)
True
\>>> is\_int64\_dtype("int8")
False
\>>> is\_int64\_dtype("Int8")
False
\>>> is\_int64\_dtype(pd.Int64Dtype)
True
\>>> is\_int64\_dtype(float)
False
\>>> is\_int64\_dtype(np.uint64)  \# unsigned
False
\>>> is\_int64\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_int64\_dtype(np.array(\[1, 2\], dtype\=np.int64))
True
\>>> is\_int64\_dtype(pd.Index(\[1, 2.0\]))  \# float
False
\>>> is\_int64\_dtype(np.array(\[1, 2\], dtype\=np.uint32))  \# unsigned
False

Copy to clipboard

On this page