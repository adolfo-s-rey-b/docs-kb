[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_hashable.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_hashable[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_hashable.html#pandas-api-types-is-hashable "Link to this heading")

=====================================================================================================================================================================

pandas.api.types.is\_hashable(_obj_, _allow\_slice\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L393-L451)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_hashable.html#pandas.api.types.is_hashable "Link to this definition")

Return True if hash(obj) will succeed, False otherwise.

Some types will pass a test against collections.abc.Hashable but fail when they are actually hashed with hash().

Distinguish between these and other types by trying the call to hash() and seeing if they raise TypeError.

Parameters:

**obj**object

The object to check for hashability. Any Python object can be passed here.

**allow\_slice**bool

If True, return True if the object is hashable (including slices). If False, return True if the object is hashable and not a slice.

Returns:

bool

True if object can be hashed (i.e., does not raise TypeError when passed to hash()) and passes the slice check according to ‘allow\_slice’. False otherwise (e.g., if object is mutable like a list or dictionary or if allow\_slice is False and object is a slice or contains a slice).

See also

`api.types.is_float`

Return True if given object is float.

`api.types.is_iterator`

Check if the object is an iterator.

`api.types.is_list_like`

Check if the object is list-like.

`api.types.is_dict_like`

Check if the object is dict-like.

Examples

\>>> import collections
\>>> from pandas.api.types import is\_hashable
\>>> a \= (\[\],)
\>>> isinstance(a, collections.abc.Hashable)
True
\>>> is\_hashable(a)
False

Copy to clipboard

On this page