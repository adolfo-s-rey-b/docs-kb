[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.day_of_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.day_of_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.day_of_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.day_of_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.day_of_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.day_of_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.day_of_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.day_of_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.day_of_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.day_of_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.day_of_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.day_of_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_year.html#pandas-series-dt-day-of-year "Link to this heading")

======================================================================================================================================================================

Series.dt.day\_of\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_year.html#pandas.Series.dt.day_of_year "Link to this definition")

The ordinal day of the year.

This attribute returns the day of the year for each datetime value in the Series/Index. Values range from 1 to 365 (or 366 for leap years).

See also

[`DatetimeIndex.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.dayofweek.html#pandas.DatetimeIndex.dayofweek "pandas.DatetimeIndex.dayofweek")

The day of the week with Monday=0, Sunday=6.

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

Examples

For Series:

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-02-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.day\_of\_year
0    1
1   32
dtype: int32

Copy to clipboard

For DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(\["1/1/2020 10:00:00+00:00",\
...                         "2/1/2020 11:00:00+00:00"\])
\>>> idx.day\_of\_year
Index(\[1, 32\], dtype='int32')

Copy to clipboard

On this page