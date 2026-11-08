[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.weekday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.weekday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.weekday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.weekday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.weekday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.weekday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.weekday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.weekday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.weekday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.weekday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.weekday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.weekday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas-period-weekday "Link to this heading")

===============================================================================================================================================

Period.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "Link to this definition")

Day of the week the period lies in, with Monday=0 and Sunday=6.

If the period frequency is lower than daily (e.g. hourly), and the period spans over multiple days, the day at the start of the period is used.

If the frequency is higher than daily (e.g. monthly), the last day of the period is used.

Returns:

int

Day of the week.

See also

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Day of the week the period lies in.

[`Period.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "pandas.Period.weekday")

Alias of Period.day\_of\_week.

[`Period.day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day")

Day of the month.

[`Period.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas.Period.day_of_year "pandas.Period.day_of_year")

Day of the year.

Examples

\>>> per \= pd.Period('2017-12-31 22:00', 'h')
\>>> per.day\_of\_week
6

Copy to clipboard

For periods that span over multiple days, the day at the beginning of the period is returned.

\>>> per \= pd.Period('2017-12-31 22:00', '4h')
\>>> per.day\_of\_week
6
\>>> per.start\_time.day\_of\_week
6

Copy to clipboard

For periods with a frequency higher than days, the last day of the period is returned.

\>>> per \= pd.Period('2018-01', 'M')
\>>> per.day\_of\_week
2
\>>> per.end\_time.day\_of\_week
2

Copy to clipboard

On this page