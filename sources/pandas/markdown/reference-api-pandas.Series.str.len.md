[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.len[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas-series-str-len "Link to this heading")

===============================================================================================================================================

Series.str.len()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3876-L3920)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "Link to this definition")

Compute the length of each element in the Series/Index.

The element may be a sequence (such as a string, tuple or list) or a collection (such as a dictionary).

Returns:

Series or Index of int

A Series or Index of integer values indicating the length of each element in the Series or Index.

See also

`str.len`

Python built-in function returning the length of an object.

[`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size")

Returns the length of the Series.

Examples

Returns the length (number of characters) in a string. Returns the number of entries for dictionaries, lists or tuples.

\>>> s \= pd.Series(
...     \["dog", "", 5, {"foo": "bar"}, \[2, 3, 5, 7\], ("one", "two", "three")\]
... )
\>>> s
0                  dog
1
2                    5
3       {'foo': 'bar'}
4         \[2, 3, 5, 7\]
5    (one, two, three)
dtype: object
\>>> s.str.len()
0    3.0
1    0.0
2    NaN
3    1.0
4    4.0
5    3.0
dtype: float64

Copy to clipboard

On this page