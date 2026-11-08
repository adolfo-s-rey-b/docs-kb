[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.month[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#pandas-timestamp-month "Link to this heading")

==================================================================================================================================================

Timestamp.month[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#pandas.Timestamp.month "Link to this definition")

Return the month of the Timestamp.

Months are numbered from 1 (January) through 12 (December).

Returns:

int

The month of the Timestamp.

See also

[`Timestamp.day`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#pandas.Timestamp.day "pandas.Timestamp.day")

Return the day of the Timestamp.

[`Timestamp.year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.year.html#pandas.Timestamp.year "pandas.Timestamp.year")

Return the year of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30")
\>>> ts.month
8

Copy to clipboard

On this page