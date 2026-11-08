[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.week[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html#pandas-period-week "Link to this heading")

======================================================================================================================================

Period.week[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html#pandas.Period.week "Link to this definition")

Get the week of the year on the given Period.

Weeks are numbered according to ISO 8601, where the first week of the year contains the first Thursday of the year.

Returns:

int

See also

[`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek")

Get the day component of the Period.

[`Period.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "pandas.Period.weekday")

Get the day component of the Period.

Examples

\>>> p \= pd.Period("2018-03-11", "h")
\>>> p.week
10

Copy to clipboard

\>>> p \= pd.Period("2018-02-01", "D")
\>>> p.week
5

Copy to clipboard

\>>> p \= pd.Period("2018-01-06", "D")
\>>> p.week
1

Copy to clipboard

On this page