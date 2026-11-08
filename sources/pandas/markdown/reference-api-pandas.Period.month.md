[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.month[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#pandas-period-month "Link to this heading")

=========================================================================================================================================

Period.month[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#pandas.Period.month "Link to this definition")

Return the month this Period falls on.

Months are numbered from 1 (January) through 12 (December).

Returns:

int

See also

`period.week`

Get the week of the year on the given Period.

[`Period.year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas.Period.year "pandas.Period.year")

Return the year this Period falls on.

[`Period.day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day")

Return the day of the month this Period falls on.

Notes

The month is based on the ordinal and base attributes of the Period.

Examples

Create a Period object for January 2022 and get the month:

\>>> period \= pd.Period('2022-01', 'M')
\>>> period.month
1

Copy to clipboard

Period object with no specified frequency, resulting in a default frequency:

\>>> period \= pd.Period('2022', 'Y')
\>>> period.month
12

Copy to clipboard

Create a Period object with a specified frequency but an incomplete date string:

\>>> period \= pd.Period('2022', 'M')
\>>> period.month
1

Copy to clipboard

Handle a case where the Period object is empty, which results in NaN:

\>>> period \= pd.Period('nan', 'M')
\>>> period.month
nan

Copy to clipboard

On this page