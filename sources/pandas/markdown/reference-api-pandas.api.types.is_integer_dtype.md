[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_integer\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer_dtype.html#pandas-api-types-is-integer-dtype "Link to this heading")

=====================================================================================================================================================================================

pandas.api.types.is\_integer\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L782-L846)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer_dtype.html#pandas.api.types.is_integer_dtype "Link to this definition")

Check whether the provided array or dtype is of an integer dtype.

Unlike in is\_any\_int\_dtype, timedelta64 instances will return False.

The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered as integer by this function.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of an integer dtype and not an instance of timedelta64.

See also

`api.types.is_integer`

Return True if given object is integer.

`api.types.is_numeric_dtype`

Check whether the provided array or dtype is of a numeric dtype.

`api.types.is_float_dtype`

Check whether the provided array or dtype is of a float dtype.

`Int64Dtype`

An ExtensionDtype for Int64Dtype integer data.

Examples

\>>> from pandas.api.types import is\_integer\_dtype
\>>> is\_integer\_dtype(str)
False
\>>> is\_integer\_dtype(int)
True
\>>> is\_integer\_dtype(float)
False
\>>> is\_integer\_dtype(np.uint64)
True
\>>> is\_integer\_dtype("int8")
True
\>>> is\_integer\_dtype("Int8")
True
\>>> is\_integer\_dtype(pd.Int8Dtype)
True
\>>> is\_integer\_dtype(np.datetime64)
False
\>>> is\_integer\_dtype(np.timedelta64)
False
\>>> is\_integer\_dtype(np.array(\["a", "b"\]))
False
\>>> is\_integer\_dtype(pd.Series(\[1, 2\]))
True
\>>> is\_integer\_dtype(np.array(\[\], dtype\="m8\[ns\]"))
False
\>>> is\_integer\_dtype(pd.Index(\[1, 2.0\]))  \# float
False

Copy to clipboard

On this page