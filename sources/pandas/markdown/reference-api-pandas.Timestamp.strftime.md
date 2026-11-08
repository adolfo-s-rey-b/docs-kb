[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.strftime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.strftime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.strftime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.strftime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.strftime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.strftime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.strftime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.strftime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.strftime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.strftime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.strftime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.strftime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.strftime[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas-timestamp-strftime "Link to this heading")

===========================================================================================================================================================

Timestamp.strftime(_format_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "Link to this definition")

Return a formatted string of the Timestamp.

This method converts a Timestamp to a string according to the given format string, using the same directives as the standard library’s [`datetime.datetime.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.15)")
.

In addition to the standard directives, `%N` is supported to format the nanoseconds as a 9-digit zero-padded number.

Parameters:

**format**str

Format string to convert Timestamp to string. See strftime documentation for more information on the format string: [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
.

See also

[`Timestamp.isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "pandas.Timestamp.isoformat")

Return the time formatted according to ISO 8601.

`pd.to_datetime`

Convert argument to datetime.

[`Period.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")

Format a single Period.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts.strftime('%Y-%m-%d %X')
'2020-03-14 15:32:52'

Copy to clipboard

Use `%N` to format nanoseconds:

\>>> ts.strftime('%Y-%m-%dT%H:%M:%S.%N')
'2020-03-14T15:32:52.192548651'

Copy to clipboard

On this page