[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.start\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#pandas-periodindex-start-time "Link to this heading")

========================================================================================================================================================================

property PeriodIndex.start\_time[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L317-L341)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#pandas.PeriodIndex.start_time "Link to this definition")

Get the Timestamp for the start of the period.

Returns a DatetimeIndex with the exact start Timestamp of each period in the index.

Returns:

DatetimeIndex

See also

[`PeriodIndex.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#pandas.PeriodIndex.end_time "pandas.PeriodIndex.end_time")

Return the end Timestamp.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeIndex.

[`Period.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time")

Return the start Timestamp for a single Period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02"\], freq\="M")
\>>> idx.start\_time
DatetimeIndex(\['2023-01-01', '2023-02-01'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page