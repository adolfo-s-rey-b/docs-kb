[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.is\_quarter\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#pandas-timestamp-is-quarter-end "Link to this heading")

===============================================================================================================================================================================

Timestamp.is\_quarter\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#pandas.Timestamp.is_quarter_end "Link to this definition")

Check if date is last day of the quarter.

Quarters end on the last day of March, June, September, and December in the standard calendar.

Returns:

bool

True if date is last day of the quarter.

See also

[`Timestamp.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#pandas.Timestamp.is_quarter_start "pandas.Timestamp.is_quarter_start")

Similar property indicating the quarter start.

[`Timestamp.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter")

Return the quarter of the date.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.is\_quarter\_end
False

Copy to clipboard

\>>> ts \= pd.Timestamp(2020, 3, 31)
\>>> ts.is\_quarter\_end
True

Copy to clipboard

On this page