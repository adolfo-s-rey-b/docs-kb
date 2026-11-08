[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_object_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_object_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_object_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_object_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_object_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_object_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_object_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_object_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_object_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_object_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_object_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_object_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_object_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_object_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_object\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_object_dtype.html#pandas-api-types-is-object-dtype "Link to this heading")

==================================================================================================================================================================================

pandas.api.types.is\_object\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L184-L227)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_object_dtype.html#pandas.api.types.is_object_dtype "Link to this definition")

Check whether an array-like or dtype is of the object dtype.

This method examines the input to determine if it is of the object data type. Object dtype is a generic data type that can hold any Python objects, including strings, lists, and custom objects.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the object dtype.

See also

`api.types.is_numeric_dtype`

Check whether the provided array or dtype is of a numeric dtype.

`api.types.is_string_dtype`

Check whether the provided array or dtype is of the string dtype.

`api.types.is_bool_dtype`

Check whether the provided array or dtype is of a boolean dtype.

Examples

\>>> from pandas.api.types import is\_object\_dtype
\>>> is\_object\_dtype(object)
True
\>>> is\_object\_dtype(int)
False
\>>> is\_object\_dtype(np.array(\[\], dtype\=object))
True
\>>> is\_object\_dtype(np.array(\[\], dtype\=int))
False
\>>> is\_object\_dtype(\[1, 2, 3\])
False

Copy to clipboard

On this page