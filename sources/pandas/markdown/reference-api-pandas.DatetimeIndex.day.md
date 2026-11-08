[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.day.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.day.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.day.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.day.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.day.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.day.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.day.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.day.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.day.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.day.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.day.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.day.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.day[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas-datetimeindex-day "Link to this heading")

========================================================================================================================================================

property DatetimeIndex.day[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L382-L402)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "Link to this definition")

The day of the datetime.

This attribute returns the day of the month component of each datetime value in the DatetimeIndex.

See also

[`DatetimeIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "pandas.DatetimeIndex.year")

The year of the datetime.

[`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month")

The month as January=1, December=12.

[`DatetimeIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas.DatetimeIndex.hour "pandas.DatetimeIndex.hour")

The hours of the datetime.

Examples

\>>> idx \= pd.DatetimeIndex(\["2000-01-01", "2000-01-02", "2000-01-03"\])
\>>> idx.day
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page