[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.daysinmonth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.daysinmonth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.daysinmonth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.daysinmonth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.daysinmonth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.daysinmonth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.daysinmonth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.daysinmonth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.daysinmonth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.daysinmonth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.daysinmonth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.daysinmonth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.daysinmonth[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas-period-daysinmonth "Link to this heading")

===========================================================================================================================================================

Period.daysinmonth[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "Link to this definition")

Get the total number of days of the month that this period falls on.

Deprecated since version 3.1.0: Use [`Period.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas.Period.days_in_month "pandas.Period.days_in_month")
 instead.

Returns:

int

See also

[`Period.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas.Period.days_in_month "pandas.Period.days_in_month")

Return the days of the month.

[`Period.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas.Period.day_of_year "pandas.Period.day_of_year")

Return the day of the year.

Examples

\>>> p \= pd.Period("2018-03-11", freq\='h')
\>>> p.days\_in\_month
31

Copy to clipboard

On this page