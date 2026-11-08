[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strptime.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.strptime[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strptime.html#pandas-timestamp-strptime "Link to this heading")

===========================================================================================================================================================

classmethod Timestamp.strptime(_date\_string_, _format_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strptime.html#pandas.Timestamp.strptime "Link to this definition")

Convert string argument to datetime.

This method is not implemented; calling it will raise NotImplementedError. Use pd.to\_datetime() instead.

Parameters:

**date\_string**str

String to convert to a datetime.

**format**str, default None

The format string to parse time, e.g. “%d/%m/%Y”.

See also

`pd.to_datetime`

Convert argument to datetime.

[`datetime.datetime.strptime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "(in Python v3.15)")

Return a datetime corresponding to a string representing a date and time, parsed according to a separate format string.

[`datetime.datetime.strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.15)")

Return a string representing the date and time, controlled by an explicit format string.

[`Timestamp.isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "pandas.Timestamp.isoformat")

Return the time formatted according to ISO 8601.

Examples

\>>> pd.Timestamp.strptime("2023-01-01", "%d/%m/%y")
Traceback (most recent call last):
NotImplementedError

Copy to clipboard

On this page