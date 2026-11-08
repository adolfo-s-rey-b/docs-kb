[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.ctime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.ctime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.ctime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.ctime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.ctime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.ctime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.ctime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.ctime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.ctime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.ctime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.ctime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.ctime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.ctime[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html#pandas-timestamp-ctime "Link to this heading")

==================================================================================================================================================

Timestamp.ctime()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html#pandas.Timestamp.ctime "Link to this definition")

Return a ctime() style string representing the Timestamp.

This method returns a string representing the date and time in the format returned by the standard library’s time.ctime() function, which is typically in the form ‘Day Mon DD HH:MM:SS YYYY’.

If the Timestamp is outside the range supported by Python’s standard library, a NotImplementedError is raised.

Returns:

str

A string representing the Timestamp in ctime format.

See also

[`time.ctime`](https://docs.python.org/3/library/time.html#time.ctime "(in Python v3.15)")

Return a string representing time in ctime format.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`datetime.datetime.ctime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.ctime "(in Python v3.15)")

Return a ctime style string from a datetime object.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00.00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.ctime()
'Sun Jan  1 10:00:00 2023'

Copy to clipboard

On this page