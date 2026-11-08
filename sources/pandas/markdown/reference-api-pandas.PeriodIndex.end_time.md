[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.end_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.end_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.end_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.end_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.end_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.end_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.end_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.end_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.end_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.end_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.end_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.end_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.end\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#pandas-periodindex-end-time "Link to this heading")

==================================================================================================================================================================

property PeriodIndex.end\_time[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L343-L368)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#pandas.PeriodIndex.end_time "Link to this definition")

Get the Timestamp for the end of the period.

Returns a DatetimeIndex with the last possible moment within each period in the index (e.g. 23:59:59.999999 for a daily period).

Returns:

DatetimeIndex

See also

[`PeriodIndex.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#pandas.PeriodIndex.start_time "pandas.PeriodIndex.start_time")

Return the start Timestamp.

[`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")

Cast to DatetimeIndex.

[`Period.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "pandas.Period.end_time")

Return the end Timestamp for a single Period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02"\], freq\="M")
\>>> idx.end\_time
DatetimeIndex(\['2023-01-31 23:59:59.999999', '2023-02-28 23:59:59.999999'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page