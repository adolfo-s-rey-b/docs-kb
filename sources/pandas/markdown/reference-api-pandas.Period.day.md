[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.day.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.day.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.day.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.day.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.day.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.day.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.day.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.day.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.day.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.day.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.day.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.day.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.day[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas-period-day "Link to this heading")

===================================================================================================================================

Period.day[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "Link to this definition")

Get day of the month that a Period falls on.

The day property provides a simple way to access the day component of a Period object, which represents time spans in various frequencies (e.g., daily, hourly, monthly). If the period’s frequency does not include a day component (e.g., yearly or quarterly periods), the returned day corresponds to the first day of that period.

Returns:

int

See also

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Get the day of the week.

[`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear")

Get the day of the year.

Examples

\>>> p \= pd.Period("2018-03-11", freq\='h')
\>>> p.day
11

Copy to clipboard

On this page