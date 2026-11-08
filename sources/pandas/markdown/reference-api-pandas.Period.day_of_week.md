[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas-period-day-of-week "Link to this heading")

=============================================================================================================================================================

Period.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas.Period.day_of_week "Link to this definition")

Day of the week the period lies in, with Monday=0 and Sunday=6.

If the period frequency is lower than daily (e.g. hourly), and the period spans over multiple days, the day at the start of the period is used.

If the frequency is higher than daily (e.g. monthly), the last day of the period is used.

Returns:

int

Day of the week.

See also

[`Period.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas.Period.day_of_week "pandas.Period.day_of_week")

Day of the week the period lies in.

[`Period.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "pandas.Period.weekday")

Alias of Period.day\_of\_week.

[`Period.day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day")

Day of the month.

[`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear")

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