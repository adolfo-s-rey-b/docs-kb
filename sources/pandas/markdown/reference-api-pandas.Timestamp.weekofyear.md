[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.weekofyear.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.weekofyear.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.weekofyear.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.weekofyear.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.weekofyear.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.weekofyear.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.weekofyear.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.weekofyear.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.weekofyear.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.weekofyear.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.weekofyear.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.weekofyear.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.weekofyear[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html#pandas-timestamp-weekofyear "Link to this heading")

=================================================================================================================================================================

Timestamp.weekofyear[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html#pandas.Timestamp.weekofyear "Link to this definition")

Return the week number of the year.

Weeks are numbered according to the ISO 8601 standard, where weeks start on Monday and the first week of the year contains the year’s first Thursday.

Returns:

int

See also

[`Timestamp.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")

Return the day of the week.

[`Timestamp.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter")

Return the quarter of the year.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.week
11

Copy to clipboard

On this page