[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.value.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.value[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.value.html#pandas-timestamp-value "Link to this heading")

==================================================================================================================================================

Timestamp.value[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.value.html#pandas.Timestamp.value "Link to this definition")

Return the value of the Timestamp.

This represents the Timestamp as the number of nanoseconds since the Unix epoch (1970-01-01 00:00:00 UTC). It may overflow for Timestamps far from the epoch.

Returns:

int

The integer representation of the Timestamp object in nanoseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

See also

[`Timestamp.second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second")

Return the second of the Timestamp.

[`Timestamp.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "pandas.Timestamp.minute")

Return the minute of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30")
\>>> ts.value
1725120990000000000

Copy to clipboard

On this page