[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.start_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.start_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.start_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.start_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.start_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.start_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.start_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.start_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.start_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.start_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.start_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.start_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.start\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas-period-start-time "Link to this heading")

=========================================================================================================================================================

Period.start\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "Link to this definition")

Get the Timestamp for the start of the period.

This property returns the exact start time of the period as a Timestamp. For example, a monthly period starting in January 2020 would return a Timestamp of ‘2020-01-01 00:00:00’.

Returns:

Timestamp

See also

[`Period.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "pandas.Period.end_time")

Return the end Timestamp.

[`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear")

Return the day of year.

[`Period.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "pandas.Period.daysinmonth")

Return the days in that month.

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Return the day of the week.

Examples

\>>> period \= pd.Period('2012-1-1', freq\='D')
\>>> period
Period('2012-01-01', 'D')

Copy to clipboard

\>>> period.start\_time
Timestamp('2012-01-01 00:00:00')

Copy to clipboard

\>>> period.end\_time
Timestamp('2012-01-01 23:59:59.999999')

Copy to clipboard

On this page