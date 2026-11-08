[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_file_like.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_file_like.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_file_like.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_file_like.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_file_like.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_file_like.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_file_like.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_file_like.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_file_like.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_file_like.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_file_like.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_file_like.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_file_like.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_file_like.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_file\_like[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_file_like.html#pandas-api-types-is-file-like "Link to this heading")

=========================================================================================================================================================================

pandas.api.types.is\_file\_like(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L107-L145)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_file_like.html#pandas.api.types.is_file_like "Link to this definition")

Check if the object is a file-like object.

For objects to be considered file-like, they must have a read and/or write method as an attribute.

Parameters:

**obj**object

The object to check for file-like properties. This can be any Python object, and the function will check if it has attributes typically associated with file-like objects (e.g., read, write).

Returns:

bool

Whether obj has file-like properties.

See also

`api.types.is_dict_like`

Check if the object is dict-like.

`api.types.is_hashable`

Return True if hash(obj) will succeed, False otherwise.

`api.types.is_named_tuple`

Check if the object is a named tuple.

`api.types.is_iterator`

Check if the object is an iterator.

Examples

\>>> import io
\>>> from pandas.api.types import is\_file\_like
\>>> buffer \= io.StringIO("data")
\>>> is\_file\_like(buffer)
True
\>>> is\_file\_like(\[1, 2, 3\])
False

Copy to clipboard

On this page