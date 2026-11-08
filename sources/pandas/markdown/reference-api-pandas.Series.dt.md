[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html#pandas-series-dt "Link to this heading")

================================================================================================================================

Series.dt()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/accessors.py#L801-L883)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html#pandas.Series.dt "Link to this definition")

Accessor object for Series values’ datetime-like, timedelta and period properties.

This accessor provides access to properties and methods for datetime-like, timedelta, and period data types. It can be used with Series containing datetime64, timedelta64, or period data.

Parameters:

**data**Series

Series with datetime-like, timedelta, or period dtype.

See also

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

Index of datetime64 data.

Examples

\>>> dates \= pd.Series(
...     \["2024-01-01", "2024-01-15", "2024-02-5"\], dtype\="datetime64\[ns\]"
... )
\>>> dates.dt.day
0     1
1    15
2     5
dtype: int32
\>>> dates.dt.month
0    1
1    1
2    2
dtype: int32

Copy to clipboard

\>>> dates \= pd.Series(
...     \["2024-01-01", "2024-01-15", "2024-02-5"\], dtype\="datetime64\[ns, UTC\]"
... )
\>>> dates.dt.day
0     1
1    15
2     5
dtype: int32
\>>> dates.dt.month
0    1
1    1
2    2
dtype: int32

Copy to clipboard

On this page