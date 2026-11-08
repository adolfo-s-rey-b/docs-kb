[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.date[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#pandas-timestamp-date "Link to this heading")

===============================================================================================================================================

Timestamp.date()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#pandas.Timestamp.date "Link to this definition")

Returns datetime.date with the same year, month, and day.

This method extracts the date component from the Timestamp and returns it as a datetime.date object, discarding the time information.

Returns:

datetime.date

The date part of the Timestamp.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`datetime.datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.datetime.date "(in Python v3.15)")

Extract the date component from a datetime object.

Examples

Extract the date from a Timestamp:

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00.00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.date()
datetime.date(2023, 1, 1)

Copy to clipboard

On this page