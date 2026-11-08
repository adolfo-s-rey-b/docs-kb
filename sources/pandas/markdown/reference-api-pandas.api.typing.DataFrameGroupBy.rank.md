[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rank.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.rank[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rank.html#pandas-api-typing-dataframegroupby-rank "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.rank(_method\='average'_, _ascending\=True_, _na\_option\='keep'_, _pct\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4690-L4781)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rank.html#pandas.api.typing.DataFrameGroupBy.rank "Link to this definition")

Provide the rank of values within each group.

This method assigns ranks to values within each group, with options for handling duplicate values, NaN values, and computing percentage ranks.

Parameters:

**method**{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}, default ‘average’

*   average: average rank of group.
    
*   min: lowest rank in group.
    
*   max: highest rank in group.
    
*   first: ranks assigned in order they appear in the array.
    
*   dense: like ‘min’, but rank always increases by 1 between groups.
    

**ascending**bool, default True

False for ranks by high (1) to low (N).

**na\_option**{‘keep’, ‘top’, ‘bottom’}, default ‘keep’

*   keep: leave NA values where they are.
    
*   top: smallest rank if ascending.
    
*   bottom: smallest rank if descending.
    

**pct**bool, default False

Compute percentage rank of data within each group.

Returns:

DataFrame

The ranking of values within each group.

See also

`Series.rank`

Apply function rank to a Series.

`DataFrame.rank`

Apply function rank to each row or column of a DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "group": \["a", "a", "a", "a", "a", "b", "b", "b", "b", "b"\],
...         "value": \[2, 4, 2, 3, 5, 1, 2, 4, 1, 5\],
...     }
... )
\>>> df
  group  value
0     a      2
1     a      4
2     a      2
3     a      3
4     a      5
5     b      1
6     b      2
7     b      4
8     b      1
9     b      5
\>>> for method in \["average", "min", "max", "dense", "first"\]:
...     df\[f"{method}\_rank"\] \= df.groupby("group")\["value"\].rank(method)
\>>> df
  group  value  average\_rank  min\_rank  max\_rank  dense\_rank  first\_rank
0     a      2           1.5       1.0       2.0         1.0         1.0
1     a      4           4.0       4.0       4.0         3.0         4.0
2     a      2           1.5       1.0       2.0         1.0         2.0
3     a      3           3.0       3.0       3.0         2.0         3.0
4     a      5           5.0       5.0       5.0         4.0         5.0
5     b      1           1.5       1.0       2.0         1.0         1.0
6     b      2           3.0       3.0       3.0         2.0         3.0
7     b      4           4.0       4.0       4.0         3.0         4.0
8     b      1           1.5       1.0       2.0         1.0         2.0
9     b      5           5.0       5.0       5.0         4.0         5.0

Copy to clipboard

On this page