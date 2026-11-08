[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.minute[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas-timestamp-minute "Link to this heading")

=====================================================================================================================================================

Timestamp.minute[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "Link to this definition")

Return the minute of the Timestamp.

Minutes range from 0 through 59.

Returns:

int

The minute of the Timestamp.

See also

[`Timestamp.hour`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.hour.html#pandas.Timestamp.hour "pandas.Timestamp.hour")

Return the hour of the Timestamp.

[`Timestamp.second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second")

Return the second of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30")
\>>> ts.minute
16

Copy to clipboard

On this page