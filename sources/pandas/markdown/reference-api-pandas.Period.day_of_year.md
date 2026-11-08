[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.day_of_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.day_of_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.day_of_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.day_of_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.day_of_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.day_of_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.day_of_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.day_of_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.day_of_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.day_of_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.day_of_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.day_of_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas-period-day-of-year "Link to this heading")

=============================================================================================================================================================

Period.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas.Period.day_of_year "Link to this definition")

Return the day of the year.

This attribute returns the day of the year on which the particular date occurs. The return value ranges between 1 to 365 for regular years and 1 to 366 for leap years.

Returns:

int

The day of year.

See also

[`Period.day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day")

Return the day of the month.

[`Period.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas.Period.day_of_week "pandas.Period.day_of_week")

Return the day of week.

[`PeriodIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year")

Return the day of year of all indexes.

Examples

\>>> period \= pd.Period("2015-10-23", freq\='h')
\>>> period.day\_of\_year
296
\>>> period \= pd.Period("2012-12-31", freq\='D')
\>>> period.day\_of\_year
366
\>>> period \= pd.Period("2013-01-01", freq\='D')
\>>> period.day\_of\_year
1

Copy to clipboard

On this page