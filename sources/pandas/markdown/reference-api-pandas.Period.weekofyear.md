[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekofyear.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.weekofyear[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekofyear.html#pandas-period-weekofyear "Link to this heading")

========================================================================================================================================================

Period.weekofyear[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekofyear.html#pandas.Period.weekofyear "Link to this definition")

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
\>>> p.weekofyear
10

Copy to clipboard

\>>> p \= pd.Period("2018-02-01", "D")
\>>> p.weekofyear
5

Copy to clipboard

\>>> p \= pd.Period("2018-01-06", "D")
\>>> p.weekofyear
1

Copy to clipboard

On this page