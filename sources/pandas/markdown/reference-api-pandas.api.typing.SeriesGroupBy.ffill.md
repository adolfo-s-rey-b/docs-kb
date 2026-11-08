[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.ffill[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html#pandas-api-typing-seriesgroupby-ffill "Link to this heading")

===============================================================================================================================================================================================

SeriesGroupBy.ffill(_limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4093-L4186)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html#pandas.api.typing.SeriesGroupBy.ffill "Link to this definition")

Forward fill the values.

Propagates the last valid observation forward within each group to fill missing values.

Parameters:

**limit**int, optional

Limit of how many values to fill.

Returns:

Series or DataFrame

Object with missing values filled.

See also

`Series.ffill`

Forward fill missing values in a Series.

`DataFrame.ffill`

Forward fill missing values in a DataFrame.

`Series.fillna`

Fill NaN values of a Series.

`DataFrame.fillna`

Fill NaN values of a DataFrame.

Examples

For SeriesGroupBy:

\>>> key \= \[0, 0, 1, 1\]
\>>> ser \= pd.Series(\[np.nan, 2, 3, np.nan\], index\=key)
\>>> ser
0    NaN
0    2.0
1    3.0
1    NaN
dtype: float64
\>>> ser.groupby(level\=0).ffill()
0    NaN
0    2.0
1    3.0
1    3.0
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> df \= pd.DataFrame(
...     {
...         "key": \[0, 0, 1, 1, 1\],
...         "A": \[np.nan, 2, np.nan, 3, np.nan\],
...         "B": \[2, 3, np.nan, np.nan, np.nan\],
...         "C": \[np.nan, np.nan, 2, np.nan, np.nan\],
...     }
... )
\>>> df
   key    A    B   C
0    0  NaN  2.0 NaN
1    0  2.0  3.0 NaN
2    1  NaN  NaN 2.0
3    1  3.0  NaN NaN
4    1  NaN  NaN NaN

Copy to clipboard

Propagate non-null values forward or backward within each group along columns.

\>>> df.groupby("key").ffill()
     A    B   C
0  NaN  2.0 NaN
1  2.0  3.0 NaN
2  NaN  NaN 2.0
3  3.0  NaN 2.0
4  3.0  NaN 2.0

Copy to clipboard

Propagate non-null values forward or backward within each group along rows.

\>>> df.T.groupby(np.array(\[0, 0, 1, 1\])).ffill().T
   key    A    B    C
0  0.0  0.0  2.0  2.0
1  0.0  2.0  3.0  3.0
2  1.0  1.0  NaN  2.0
3  1.0  3.0  NaN  NaN
4  1.0  1.0  NaN  NaN

Copy to clipboard

Only replace the first NaN element within a group along columns.

\>>> df.groupby("key").ffill(limit\=1)
     A    B    C
0  NaN  2.0  NaN
1  2.0  3.0  NaN
2  NaN  NaN  2.0
3  3.0  NaN  2.0
4  3.0  NaN  NaN

Copy to clipboard

On this page