[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.day_of_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.day_of_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.day_of_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.day_of_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.day_of_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.day_of_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.day_of_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html#pandas-datetimeindex-day-of-year "Link to this heading")

==================================================================================================================================================================================

property DatetimeIndex.day\_of\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L540-L560)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html#pandas.DatetimeIndex.day_of_year "Link to this definition")

The ordinal day of the year.

This attribute returns the day of the year for each datetime value in the DatetimeIndex. Values range from 1 to 365 (or 366 for leap years).

See also

[`DatetimeIndex.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_week.html#pandas.DatetimeIndex.day_of_week "pandas.DatetimeIndex.day_of_week")

The day of the week with Monday=0, Sunday=6.

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

Examples

\>>> idx \= pd.DatetimeIndex(\["2020-01-01", "2020-02-01"\])
\>>> idx.day\_of\_year
Index(\[1, 32\], dtype='int32')

Copy to clipboard

On this page