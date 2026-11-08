[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.first.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.first.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.first.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.first[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.first.html#pandas-api-typing-seriesgroupby-first "Link to this heading")

===============================================================================================================================================================================================

SeriesGroupBy.first(_numeric\_only\=False_, _min\_count\=\-1_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3200-L3285)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.first.html#pandas.api.typing.SeriesGroupBy.first "Link to this definition")

Compute the first entry of each column within each group.

NA values are skipped by default, so the result is the first non-NA value per column — which may differ from the first row of the group. Pass `skipna=False` to keep NAs.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**min\_count**int, default -1

The required number of valid values to perform the operation. If fewer than `min_count` valid values are present the result will be NA.

**skipna**bool, default True

Exclude NA values. If an entire group is NA, the result will be NA.

Added in version 2.2.1.

Returns:

Series or DataFrame

First values within each group.

See also

`DataFrame.groupby`

Apply a function groupby to each row or column of a DataFrame.

`api.typing.DataFrameGroupBy.last`

Compute the last entry of each column within each group.

`api.typing.DataFrameGroupBy.nth`

Take the nth row from each group.

Examples

\>>> df \= pd.DataFrame(
...     dict(
...         A\=\[1, 1, 3\],
...         B\=\[None, 5, 6\],
...         C\=\[1, 2, 3\],
...         D\=\["3/11/2000", "3/12/2000", "3/13/2000"\],
...     )
... )
\>>> df\["D"\] \= pd.to\_datetime(df\["D"\])
\>>> df.groupby("A").first()
     B  C          D
A
1  5.0  1 2000-03-11
3  6.0  3 2000-03-13
\>>> df.groupby("A").first(min\_count\=2)
    B    C          D
A
1 NaN  1.0 2000-03-11
3 NaN  NaN        NaT
\>>> df.groupby("A").first(numeric\_only\=True)
     B  C
A
1  5.0  1
3  6.0  3

Copy to clipboard

On this page