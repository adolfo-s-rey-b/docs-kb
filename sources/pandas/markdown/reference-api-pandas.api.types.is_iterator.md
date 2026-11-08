[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_iterator.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_iterator.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_iterator.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_iterator.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_iterator.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_iterator.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_iterator.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_iterator.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_iterator.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_iterator.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_iterator.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_iterator.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_iterator.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_iterator.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_iterator[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_iterator.html#pandas-api-types-is-iterator "Link to this heading")

=====================================================================================================================================================================

pandas.api.types.is\_iterator(_obj_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_iterator.html#pandas.api.types.is_iterator "Link to this definition")

Check if the object is an iterator.

This is intended for generators, not list-like objects. This method checks whether the passed object is an iterator. It returns True if the object is an iterator, and False otherwise.

Parameters:

**obj**The object to check

The object to check for iterator type.

Returns:

**is\_iter**bool

Whether obj is an iterator. True if the object is of iterator type, otherwise False.

See also

`api.types.is_list_like`

Check if the input is list-like.

Examples

\>>> import datetime
\>>> from pandas.api.types import is\_iterator
\>>> is\_iterator((x for x in \[\]))
True
\>>> is\_iterator(\[1, 2, 3\])
False
\>>> is\_iterator(datetime.datetime(2017, 1, 1))
False
\>>> is\_iterator("foo")
False
\>>> is\_iterator(1)
False

Copy to clipboard

On this page