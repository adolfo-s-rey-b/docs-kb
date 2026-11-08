[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.days_in_month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.days_in_month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.days_in_month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.days_in_month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.days_in_month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.days_in_month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.days_in_month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.days_in_month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.days_in_month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.days_in_month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.days_in_month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.days_in_month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html#pandas-timestamp-days-in-month "Link to this heading")

============================================================================================================================================================================

Timestamp.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html#pandas.Timestamp.days_in_month "Link to this definition")

Return the number of days in the month.

This value depends on the month and whether the year is a leap year.

Returns:

int

See also

[`Timestamp.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#pandas.Timestamp.month_name "pandas.Timestamp.month_name")

Return the month name of the Timestamp with specified locale.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.days\_in\_month
31

Copy to clipboard

On this page