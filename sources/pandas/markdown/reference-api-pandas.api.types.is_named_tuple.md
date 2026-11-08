[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_named_tuple.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_named_tuple.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_named_tuple.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_named_tuple.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_named_tuple.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_named_tuple.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_named_tuple.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_named_tuple.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_named_tuple.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_named_tuple.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_named_tuple.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_named_tuple.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_named_tuple.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_named_tuple.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_named\_tuple[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_named_tuple.html#pandas-api-types-is-named-tuple "Link to this heading")

===============================================================================================================================================================================

pandas.api.types.is\_named\_tuple(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L352-L390)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_named_tuple.html#pandas.api.types.is_named_tuple "Link to this definition")

Check if the object is a named tuple.

A named tuple is a subclass of [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
 that has named fields, as created by [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.15)")
.

Parameters:

**obj**object

The object that will be checked to determine whether it is a named tuple.

Returns:

bool

Whether obj is a named tuple.

See also

`api.types.is_dict_like`

Check if the object is dict-like.

`api.types.is_hashable`

Return True if hash(obj) will succeed, False otherwise.

`api.types.is_categorical_dtype`

Check if the dtype is categorical.

Examples

\>>> from collections import namedtuple
\>>> from pandas.api.types import is\_named\_tuple
\>>> Point \= namedtuple("Point", \["x", "y"\])
\>>> p \= Point(1, 2)
\>>>
\>>> is\_named\_tuple(p)
True
\>>> is\_named\_tuple((1, 2))
False

Copy to clipboard

On this page