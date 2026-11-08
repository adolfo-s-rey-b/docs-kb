[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.asfreq.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.asfreq.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.asfreq.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.asfreq.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.asfreq.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.asfreq.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.asfreq.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.asfreq.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.asfreq.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.asfreq.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.asfreq.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.asfreq.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.asfreq[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas-period-asfreq "Link to this heading")

============================================================================================================================================

Period.asfreq(_freq_, _how\='E'_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "Link to this definition")

Convert Period to desired frequency, at the start or end of the interval.

This method converts the Period to a different frequency, aligning the result to either the start or end of the original interval.

Parameters:

**freq**str, DateOffset

The target frequency to convert the Period object to. If a string is provided, it must be a valid [period alias](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-aliases)
.

**how**{‘end’, ‘start’, ‘e’, ‘s’}, default ‘end’

Whether to align the period to the end or start of the interval. Case-insensitive.

Returns:

**Period**Period object with the specified frequency, aligned to the parameter.

See also

[`Period.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "pandas.Period.end_time")

Return the end Timestamp.

[`Period.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time")

Return the start Timestamp.

[`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear")

Return the day of the year.

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Return the day of the week.

Examples

Convert a daily period to an hourly period, aligning to the end of the day:

\>>> period \= pd.Period('2023-01-01', freq\='D')
\>>> period.asfreq('h')
Period('2023-01-01 23:00', 'h')

Copy to clipboard

Convert a monthly period to a daily period, aligning to the start of the month:

\>>> period \= pd.Period('2023-01', freq\='M')
\>>> period.asfreq('D', how\='start')
Period('2023-01-01', 'D')

Copy to clipboard

Convert a yearly period to a monthly period, aligning to the last month:

\>>> period \= pd.Period('2023', freq\='Y')
\>>> period.asfreq('M', how\='end')
Period('2023-12', 'M')

Copy to clipboard

Convert a monthly period to an hourly period, aligning to the first day of the month:

\>>> period \= pd.Period('2023-01', freq\='M')
\>>> period.asfreq('h', how\='start')
Period('2023-01-01 00:00', 'h')

Copy to clipboard

Convert a weekly period to a daily period, aligning to the last day of the week:

\>>> period \= pd.Period('2023-08-01', freq\='W')
\>>> period.asfreq('D', how\='end')
Period('2023-08-06', 'D')

Copy to clipboard

On this page