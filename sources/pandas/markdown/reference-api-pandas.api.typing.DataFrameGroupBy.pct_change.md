[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.pct\_change[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html#pandas-api-typing-dataframegroupby-pct-change "Link to this heading")

========================================================================================================================================================================================================================

DataFrameGroupBy.pct\_change(_periods\=1_, _fill\_method\=None_, _freq\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5380-L5478)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html#pandas.api.typing.DataFrameGroupBy.pct_change "Link to this definition")

Calculate pct\_change of each value to previous entry in group.

This method calculates the percentage change between the current and a prior element within each group, useful for computing growth rates.

Parameters:

**periods**int, default 1

Periods to shift for calculating percentage change. Comparing with a period of 1 means adjacent elements are compared, whereas a period of 2 compares every other element.

**fill\_method**None

Must be None. This argument will be removed in a future version of pandas.

**freq**str, pandas offset object, or None, default None

The frequency increment for time series data (e.g., ‘M’ for month-end). If None, the frequency is inferred from the index. Relevant for time series data only.

Returns:

Series or DataFrame

Percentage changes within each group.

See also

`Series.pct_change`

Apply function pct\_change to a Series.

`DataFrame.pct_change`

Apply function pct\_change to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3, 4\], index\=lst)
\>>> ser
a    1
a    2
b    3
b    4
dtype: int64
\>>> ser.groupby(level\=0).pct\_change()
a         NaN
a    1.000000
b         NaN
b    0.333333
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[2, 5, 8\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data,
...     columns\=\["a", "b", "c"\],
...     index\=\["tuna", "salmon", "catfish", "goldfish"\],
... )
\>>> df
           a  b  c
    tuna   1  2  3
  salmon   1  5  6
 catfish   2  5  8
goldfish   2  6  9
\>>> df.groupby("a").pct\_change()
            b  c
    tuna    NaN    NaN
  salmon    1.5  1.000
 catfish    NaN    NaN
goldfish    0.2  0.125

Copy to clipboard

On this page