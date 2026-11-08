[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.nsmallest[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html#pandas-api-typing-seriesgroupby-nsmallest "Link to this heading")

===========================================================================================================================================================================================================

SeriesGroupBy.nsmallest(_n\=5_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1605-L1671)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html#pandas.api.typing.SeriesGroupBy.nsmallest "Link to this definition")

Return the smallest n elements.

Within each group, returns the n smallest values sorted in ascending order. The `keep` parameter controls how ties are handled when there are duplicate values at the boundary.

Parameters:

**n**int, default 5

Return this many ascending sorted values.

**keep**{‘first’, ‘last’, ‘all’}, default ‘first’

When there are duplicate values that cannot all fit in a Series of n elements:

*   `first` : return the first n occurrences in order of appearance.
    
*   `last` : return the last n occurrences in reverse order of appearance.
    
*   `all` : keep all occurrences. This can result in a Series of size larger than n.
    

Returns:

Series

The n smallest values in the Series, sorted in increasing order.

See also

`Series.nlargest`

Get the n largest elements.

`Series.sort_values`

Sort Series by values.

`Series.head`

Return the first n rows.

Notes

Faster than `.sort_values().head(n)` for small n relative to the size of the `Series` object.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

\>>> s
0    1
1    2
2    3
3    4
4    5
5    6
dtype: int64

Copy to clipboard

\>>> s.groupby(\[1, 1, 1, 2, 2, 2\]).nsmallest(n\=2)
1  0    1
   1    2
2  3    4
   4    5
dtype: int64

Copy to clipboard

On this page