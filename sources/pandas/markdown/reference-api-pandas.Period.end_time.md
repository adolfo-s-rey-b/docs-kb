[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.end_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.end_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.end_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.end_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.end_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.end_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.end_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.end_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.end_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.end_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.end_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.end_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.end\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas-period-end-time "Link to this heading")

===================================================================================================================================================

Period.end\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "Link to this definition")

Get the Timestamp for the end of the period.

This property returns the exact end time of the period as a Timestamp. The returned timestamp represents the last possible moment within the period (e.g., 23:59:59.999999 for a daily period).

Returns:

Timestamp

See also

[`Period.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time")

Return the start Timestamp.

[`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear")

Return the day of year.

[`Period.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "pandas.Period.daysinmonth")

Return the days in that month.

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Return the day of the week.

Examples

For Period:

\>>> pd.Period('2020-01', 'D').end\_time
Timestamp('2020-01-01 23:59:59.999999')

Copy to clipboard

For Series:

\>>> period\_index \= pd.period\_range('2020-1-1 00:00', '2020-3-1 00:00', freq\='M')
\>>> s \= pd.Series(period\_index)
\>>> s
0   2020-01
1   2020-02
2   2020-03
dtype: period\[M\]
\>>> s.dt.end\_time
0   2020-01-31 23:59:59.999999
1   2020-02-29 23:59:59.999999
2   2020-03-31 23:59:59.999999
dtype: datetime64\[us\]

Copy to clipboard

For PeriodIndex:

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.end\_time
DatetimeIndex(\['2023-01-31 23:59:59.999999',\
               '2023-02-28 23:59:59.999999',\
               '2023-03-31 23:59:59.999999'\],
               dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page