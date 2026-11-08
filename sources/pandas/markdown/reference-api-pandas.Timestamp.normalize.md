[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.normalize[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html#pandas-timestamp-normalize "Link to this heading")

==============================================================================================================================================================

Timestamp.normalize()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html#pandas.Timestamp.normalize "Link to this definition")

Normalize Timestamp to midnight, preserving tz information.

This method sets the time component of the Timestamp to midnight (00:00:00), while preserving the date and time zone information. It is useful when you need to standardize the time across different Timestamp objects without altering the time zone or the date.

Returns:

Timestamp

See also

[`Timestamp.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas.Timestamp.floor "pandas.Timestamp.floor")

Rounds Timestamp down to the nearest frequency.

[`Timestamp.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html#pandas.Timestamp.ceil "pandas.Timestamp.ceil")

Rounds Timestamp up to the nearest frequency.

[`Timestamp.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html#pandas.Timestamp.round "pandas.Timestamp.round")

Rounds Timestamp to the nearest frequency.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14, 15, 30)
\>>> ts.normalize()
Timestamp('2020-03-14 00:00:00')

Copy to clipboard

On this page