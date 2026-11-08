[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas-period-year "Link to this heading")

======================================================================================================================================

Period.year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas.Period.year "Link to this definition")

Return the year this Period falls on.

The year is derived from the internal representation of the Period based on its ordinal value and frequency.

Returns:

int

See also

`period.month`

Get the month of the year for the given Period.

`period.day`

Return the day of the month the Period falls on.

Notes

The year is based on the ordinal and base attributes of the Period.

Examples

Create a Period object for January 2023 and get the year:

\>>> period \= pd.Period('2023-01', 'M')
\>>> period.year
2023

Copy to clipboard

Create a Period object for 01 January 2023 and get the year:

\>>> period \= pd.Period('2023', 'D')
\>>> period.year
2023

Copy to clipboard

Get the year for a period representing a quarter:

\>>> period \= pd.Period('2023Q2', 'Q')
\>>> period.year
2023

Copy to clipboard

Handle a case where the Period object is empty, which results in NaN:

\>>> period \= pd.Period('nan', 'M')
\>>> period.year
nan

Copy to clipboard

On this page