[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.truncate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.truncate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.truncate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.truncate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.truncate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.truncate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.truncate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.truncate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.truncate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.truncate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.truncate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.truncate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.truncate[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html#pandas-multiindex-truncate "Link to this heading")

==============================================================================================================================================================

MultiIndex.truncate(_before\=None_, _after\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L4550-L4601)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html#pandas.MultiIndex.truncate "Link to this definition")

Slice index between two labels / tuples, return new MultiIndex.

This method returns a new MultiIndex containing only the entries that fall within the specified range on the first level.

Parameters:

**before**label or tuple, can be partial. Default None

None defaults to start.

**after**label or tuple, can be partial. Default None

None defaults to end.

Returns:

MultiIndex

The truncated MultiIndex.

See also

[`DataFrame.truncate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html#pandas.DataFrame.truncate "pandas.DataFrame.truncate")

Truncate a DataFrame before and after some index values.

[`Series.truncate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#pandas.Series.truncate "pandas.Series.truncate")

Truncate a Series before and after some index values.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a", "b", "c"\], \["x", "y", "z"\]\])
\>>> mi
MultiIndex(\[('a', 'x'), ('b', 'y'), ('c', 'z')\],
           )
\>>> mi.truncate(before\="a", after\="b")
MultiIndex(\[('a', 'x'), ('b', 'y')\],
           )

Copy to clipboard

On this page