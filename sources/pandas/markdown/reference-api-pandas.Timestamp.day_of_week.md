[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.day_of_week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.day_of_week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.day_of_week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.day_of_week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.day_of_week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.day_of_week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.day_of_week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.day_of_week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.day_of_week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.day_of_week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.day_of_week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.day_of_week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas-timestamp-day-of-week "Link to this heading")

======================================================================================================================================================================

Timestamp.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas.Timestamp.day_of_week "Link to this definition")

Return day of the week.

Days are numbered Monday=0 through Sunday=6.

Returns:

int

See also

[`Timestamp.isoweekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#pandas.Timestamp.isoweekday "pandas.Timestamp.isoweekday")

Return the ISO day of the week represented by the date.

[`Timestamp.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")

Return the day of the week represented by the date.

[`Timestamp.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas.Timestamp.day_of_year "pandas.Timestamp.day_of_year")

Return day of the year.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.day\_of\_week
5

Copy to clipboard

On this page