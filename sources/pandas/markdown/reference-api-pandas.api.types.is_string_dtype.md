[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_string_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_string_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_string_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_string_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_string_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_string_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_string_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_string_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_string_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_string_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_string_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_string_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_string_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_string_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_string\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_string_dtype.html#pandas-api-types-is-string-dtype "Link to this heading")

==================================================================================================================================================================================

pandas.api.types.is\_string\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L660-L710)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_string_dtype.html#pandas.api.types.is_string_dtype "Link to this definition")

Check whether the provided array or dtype is of the string dtype.

If an array is passed with an object dtype, the elements must be inferred as strings.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of the string dtype.

See also

`api.types.is_object_dtype`

Check whether an array-like or dtype is of the object dtype.

Examples

\>>> from pandas.api.types import is\_string\_dtype
\>>> is\_string\_dtype(str)
True
\>>> is\_string\_dtype(object)
True
\>>> is\_string\_dtype(int)
False
\>>> is\_string\_dtype(np.array(\["a", "b"\]))
True
\>>> is\_string\_dtype(pd.Series(\[1, 2\]))
False
\>>> is\_string\_dtype(pd.Series(\[1, 2\], dtype\=object))
False

Copy to clipboard

On this page