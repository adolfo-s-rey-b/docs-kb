[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.is\_month\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#pandas-timestamp-is-month-start "Link to this heading")

===============================================================================================================================================================================

Timestamp.is\_month\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#pandas.Timestamp.is_month_start "Link to this definition")

Check if the date is the first day of the month.

This is determined by checking whether the `day` component of the Timestamp is equal to 1.

Returns:

bool

True if the date is the first day of the month.

See also

[`Timestamp.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#pandas.Timestamp.is_month_end "pandas.Timestamp.is_month_end")

Similar property indicating the last day of the month.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.is\_month\_start
False

Copy to clipboard

\>>> ts \= pd.Timestamp(2020, 1, 1)
\>>> ts.is\_month\_start
True

Copy to clipboard

On this page