[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.quarter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.quarter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.quarter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.quarter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.quarter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.quarter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.quarter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.quarter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.quarter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.quarter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.quarter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.quarter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#pandas-series-dt-quarter "Link to this heading")

========================================================================================================================================================

Series.dt.quarter[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#pandas.Series.dt.quarter "Link to this definition")

The quarter of the date.

This attribute returns the quarter of the year for each datetime value in the Series/Index. Quarter 1 includes January through March, quarter 2 includes April through June, quarter 3 includes July through September, and quarter 4 includes October through December.

See also

[`DatetimeIndex.snap`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#pandas.DatetimeIndex.snap "pandas.DatetimeIndex.snap")

Snap time stamps to nearest occurring frequency.

[`DatetimeIndex.time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#pandas.DatetimeIndex.time "pandas.DatetimeIndex.time")

Returns numpy array of datetime.time objects. The time part of the Timestamps.

Examples

For Series:

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "4/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-04-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.quarter
0    1
1    2
dtype: int32

Copy to clipboard

For DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(\["1/1/2020 10:00:00+00:00",\
...                         "2/1/2020 11:00:00+00:00"\])
\>>> idx.quarter
Index(\[1, 1\], dtype='int32')

Copy to clipboard

On this page