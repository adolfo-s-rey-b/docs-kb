[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.quarter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.quarter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.quarter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.quarter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.quarter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.quarter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.quarter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.quarter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.quarter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.quarter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.quarter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.quarter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#pandas-datetimeindex-quarter "Link to this heading")

====================================================================================================================================================================

property DatetimeIndex.quarter[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L562-L587)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#pandas.DatetimeIndex.quarter "Link to this definition")

The quarter of the date.

This attribute returns the quarter of the year for each datetime value in the DatetimeIndex. Quarter 1 includes January through March, quarter 2 includes April through June, quarter 3 includes July through September, and quarter 4 includes October through December.

See also

[`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month")

The month as January=1, December=12.

[`DatetimeIndex.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#pandas.DatetimeIndex.is_quarter_start "pandas.DatetimeIndex.is_quarter_start")

Indicator for whether the date is the first day of a quarter.

[`DatetimeIndex.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#pandas.DatetimeIndex.is_quarter_end "pandas.DatetimeIndex.is_quarter_end")

Indicator for whether the date is the last day of a quarter.

Examples

\>>> idx \= pd.DatetimeIndex(\["2020-01-01", "2020-04-01"\])
\>>> idx.quarter
Index(\[1, 2\], dtype='int32')

Copy to clipboard

On this page