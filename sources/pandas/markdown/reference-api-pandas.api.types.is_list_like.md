[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_list_like.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_list_like.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_list_like.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_list_like.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_list_like.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_list_like.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_list_like.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_list_like.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_list_like.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_list_like.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_list_like.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_list_like.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_list_like.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_list_like.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_list\_like[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_list_like.html#pandas-api-types-is-list-like "Link to this heading")

=========================================================================================================================================================================

pandas.api.types.is\_list\_like(_obj_, _allow\_sets\=True_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_list_like.html#pandas.api.types.is_list_like "Link to this definition")

Check if the object is list-like.

Objects that are considered list-like are for example Python lists, tuples, sets, NumPy arrays, and Pandas Series.

Strings and datetime objects, however, are not considered list-like.

Parameters:

**obj**object

Object to check.

**allow\_sets**bool, default True

If this parameter is False, sets will not be considered list-like.

Returns:

bool

Whether obj has list-like properties.

See also

`Series`

One-dimensional ndarray with axis labels (including time series).

`Index`

Immutable sequence used for indexing and alignment.

[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

Array object from NumPy, which is considered list-like.

Examples

\>>> import datetime
\>>> from pandas.api.types import is\_list\_like
\>>> is\_list\_like(\[1, 2, 3\])
True
\>>> is\_list\_like({1, 2, 3})
True
\>>> is\_list\_like(datetime.datetime(2017, 1, 1))
False
\>>> is\_list\_like("foo")
False
\>>> is\_list\_like(1)
False
\>>> is\_list\_like(np.array(\[2\]))
True
\>>> is\_list\_like(np.array(2))
False

Copy to clipboard

On this page