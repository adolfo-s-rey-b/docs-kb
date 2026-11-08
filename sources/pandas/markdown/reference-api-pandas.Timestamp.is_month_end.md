[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.is_month_end.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.is_month_end.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.is_month_end.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.is_month_end.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.is_month_end.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.is_month_end.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.is_month_end.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.is_month_end.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.is_month_end.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.is_month_end.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.is_month_end.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.is_month_end.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.is\_month\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#pandas-timestamp-is-month-end "Link to this heading")

=========================================================================================================================================================================

Timestamp.is\_month\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#pandas.Timestamp.is_month_end "Link to this definition")

Check if the date is the last day of the month.

This is determined by comparing the `day` component with the total number of days in the month of the Timestamp.

Returns:

bool

True if the date is the last day of the month.

See also

[`Timestamp.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#pandas.Timestamp.is_month_start "pandas.Timestamp.is_month_start")

Similar property indicating month start.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.is\_month\_end
False

Copy to clipboard

\>>> ts \= pd.Timestamp(2020, 12, 31)
\>>> ts.is\_month\_end
True

Copy to clipboard

On this page