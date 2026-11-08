[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ngroup.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.ngroup[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ngroup.html#pandas-api-typing-seriesgroupby-ngroup "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.ngroup(_ascending\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4550-L4631)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ngroup.html#pandas.api.typing.SeriesGroupBy.ngroup "Link to this definition")

Number each group from 0 to the number of groups - 1.

This is the enumerative complement of cumcount. Note that the numbers given to the groups match the order in which the groups would be seen when iterating over the groupby object, not the order they are first observed.

Groups with missing keys (where pd.isna() is True) will be labeled with NaN and will be skipped from the count.

Parameters:

**ascending**bool, default True

If False, number in reverse, from number of group - 1 to 0.

Returns:

Series

Unique numbers for each group.

See also

[`cumcount`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumcount.html#pandas.api.typing.SeriesGroupBy.cumcount "pandas.api.typing.SeriesGroupBy.cumcount")

Number the rows in each group.

Examples

\>>> df \= pd.DataFrame({"color": \["red", None, "red", "blue", "blue", "red"\]})
\>>> df
  color
0   red
1   NaN
2   red
3  blue
4  blue
5   red
\>>> df.groupby("color").ngroup()
0    1.0
1    NaN
2    1.0
3    0.0
4    0.0
5    1.0
dtype: float64
\>>> df.groupby("color", dropna\=False).ngroup()
0    1
1    2
2    1
3    0
4    0
5    1
dtype: int64
\>>> df.groupby("color", dropna\=False).ngroup(ascending\=False)
0    1
1    0
2    1
3    2
4    2
5    1
dtype: int64

Copy to clipboard

On this page