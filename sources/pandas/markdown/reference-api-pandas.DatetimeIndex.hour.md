[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.hour.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.hour.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.hour.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.hour.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.hour.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.hour.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.hour.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.hour.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.hour.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.hour.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.hour.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.hour.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.hour[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas-datetimeindex-hour "Link to this heading")

===========================================================================================================================================================

property DatetimeIndex.hour[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L404-L424)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas.DatetimeIndex.hour "Link to this definition")

The hours of the datetime.

This attribute returns the hour component of each datetime value in the DatetimeIndex.

See also

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

[`DatetimeIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.minute.html#pandas.DatetimeIndex.minute "pandas.DatetimeIndex.minute")

The minutes of the datetime.

[`DatetimeIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas.DatetimeIndex.second "pandas.DatetimeIndex.second")

The seconds of the datetime.

Examples

\>>> idx \= pd.date\_range("2000-01-01", periods\=3, freq\="h")
\>>> idx.hour
Index(\[0, 1, 2\], dtype='int32')

Copy to clipboard

On this page