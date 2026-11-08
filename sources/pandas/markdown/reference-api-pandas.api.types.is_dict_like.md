[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dict_like.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_dict\_like[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dict_like.html#pandas-api-types-is-dict-like "Link to this heading")

=========================================================================================================================================================================

pandas.api.types.is\_dict\_like(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L306-L349)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dict_like.html#pandas.api.types.is_dict_like "Link to this definition")

Check if the object is dict-like.

An object is considered dict-like if it has the `__getitem__`, `keys`, and `__contains__` attributes but is not a type itself.

Parameters:

**obj**object

The object to check. This can be any Python object, and the function will determine whether it behaves like a dictionary.

Returns:

bool

Whether obj has dict-like properties.

See also

`api.types.is_list_like`

Check if the object is list-like.

`api.types.is_file_like`

Check if the object is a file-like.

`api.types.is_named_tuple`

Check if the object is a named tuple.

Examples

\>>> from pandas.api.types import is\_dict\_like
\>>> is\_dict\_like({1: 2})
True
\>>> is\_dict\_like(\[1, 2, 3\])
False
\>>> is\_dict\_like(dict)
False
\>>> is\_dict\_like(dict())
True

Copy to clipboard

On this page