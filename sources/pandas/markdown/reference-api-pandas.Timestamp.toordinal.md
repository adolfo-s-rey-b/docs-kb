[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.toordinal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.toordinal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.toordinal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.toordinal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.toordinal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.toordinal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.toordinal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.toordinal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.toordinal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.toordinal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.toordinal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.toordinal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.toordinal[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#pandas-timestamp-toordinal "Link to this heading")

==============================================================================================================================================================

Timestamp.toordinal()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#pandas.Timestamp.toordinal "Link to this definition")

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

The proleptic Gregorian ordinal is a continuous count of days since January 1 of year 1, which is considered day 1. This method converts the Timestamp to its equivalent ordinal number, useful for date arithmetic and comparison operations.

See also

[`datetime.datetime.toordinal`](https://docs.python.org/3/library/datetime.html#datetime.datetime.toordinal "(in Python v3.15)")

Equivalent method in the datetime module.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

The Timestamp that represents a specific point in time.

[`Timestamp.fromordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas.Timestamp.fromordinal "pandas.Timestamp.fromordinal")

Create a Timestamp from an ordinal.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:50')
\>>> ts
Timestamp('2023-01-01 10:00:50')
\>>> ts.toordinal()
738521

Copy to clipboard

On this page