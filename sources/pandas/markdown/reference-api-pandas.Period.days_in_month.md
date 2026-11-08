[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas-period-days-in-month "Link to this heading")

===================================================================================================================================================================

Period.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas.Period.days_in_month "Link to this definition")

Get the total number of days in the month that this period falls on.

This value depends on the month and whether the year is a leap year (e.g., February has 28 or 29 days).

Returns:

int

See also

[`Period.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "pandas.Period.daysinmonth")

Gets the number of days in the month.

`DatetimeIndex.daysinmonth`

Gets the number of days in the month.

[`calendar.monthrange`](https://docs.python.org/3/library/calendar.html#calendar.monthrange "(in Python v3.15)")

Returns a tuple containing weekday (0-6 ~ Mon-Sun) and number of days (28-31).

Examples

\>>> p \= pd.Period('2018-2-17')
\>>> p.days\_in\_month
28

Copy to clipboard

\>>> pd.Period('2018-03-01').days\_in\_month
31

Copy to clipboard

Handles the leap year case as well:

\>>> p \= pd.Period('2016-2-17')
\>>> p.days\_in\_month
29

Copy to clipboard

On this page