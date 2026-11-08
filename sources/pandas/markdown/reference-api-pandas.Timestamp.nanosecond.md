[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.nanosecond.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.nanosecond[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.nanosecond.html#pandas-timestamp-nanosecond "Link to this heading")

=================================================================================================================================================================

Timestamp.nanosecond[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.nanosecond.html#pandas.Timestamp.nanosecond "Link to this definition")

Return the nanosecond of the Timestamp.

This property returns an integer representing the nanosecond component (0-999) of the Timestamp. This is particularly useful when working with high-precision temporal data that requires sub-microsecond resolution.

Returns:

int

The nanosecond of the Timestamp.

See also

[`Timestamp.second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second")

Return the second of the Timestamp.

[`Timestamp.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas.Timestamp.microsecond "pandas.Timestamp.microsecond")

Return the microsecond of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30.230400015")
\>>> ts.nanosecond
15

Copy to clipboard

On this page