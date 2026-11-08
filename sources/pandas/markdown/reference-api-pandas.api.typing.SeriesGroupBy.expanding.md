[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.expanding[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html#pandas-api-typing-seriesgroupby-expanding "Link to this heading")

===========================================================================================================================================================================================================

SeriesGroupBy.expanding(_min\_periods\=1_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3835-L3906)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html#pandas.api.typing.SeriesGroupBy.expanding "Link to this definition")

Return an expanding grouper, providing expanding functionality per group.

Each group’s expanding window includes all prior rows within that group up to and including the current row.

Parameters:

**min\_periods**int, default 1

Minimum number of observations in window required to have a value; otherwise, result is `np.nan`.

**method**str {‘single’, ‘table’}, default ‘single’

Execute the expanding operation per single column or row (`'single'`) or over the entire object (`'table'`).

This argument is only implemented when specifying `engine='numba'` in the method call.

Returns:

pandas.api.typing.ExpandingGroupBy

An object that supports expanding transformations over each group.

See also

`Series.expanding`

Expanding transformations for Series.

`DataFrame.expanding`

Expanding transformations for DataFrames.

`Series.groupby`

Apply a function groupby to a Series.

`DataFrame.groupby`

Apply a function groupby.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "Class": \["A", "A", "A", "B", "B", "B"\],
...         "Value": \[10, 20, 30, 40, 50, 60\],
...     }
... )
\>>> df
Class  Value
0     A     10
1     A     20
2     A     30
3     B     40
4     B     50
5     B     60

Copy to clipboard

\>>> df.groupby("Class").expanding().mean()
        Value
Class
A     0   10.0
      1   15.0
      2   20.0
B     3   40.0
      4   45.0
      5   50.0

Copy to clipboard

On this page