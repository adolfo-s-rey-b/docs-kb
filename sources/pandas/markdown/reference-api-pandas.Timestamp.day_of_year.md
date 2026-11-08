[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.day_of_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.day_of_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.day_of_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.day_of_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.day_of_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.day_of_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.day_of_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.day_of_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.day_of_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.day_of_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.day_of_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.day_of_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas-timestamp-day-of-year "Link to this heading")

======================================================================================================================================================================

Timestamp.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas.Timestamp.day_of_year "Link to this definition")

Return the day of the year.

Days are numbered from 1 through 365 (or 366 in leap years).

Returns:

int

See also

[`Timestamp.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas.Timestamp.day_of_week "pandas.Timestamp.day_of_week")

Return day of the week.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.day\_of\_year
74

Copy to clipboard

On this page