[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.to_julian_date.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.to_julian_date.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.to_julian_date.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.to_julian_date.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.to_julian_date.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.to_julian_date.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.to_julian_date.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.to_julian_date.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.to_julian_date.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.to_julian_date.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.to_julian_date.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.to_julian_date.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.to\_julian\_date[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#pandas-timestamp-to-julian-date "Link to this heading")

===============================================================================================================================================================================

Timestamp.to\_julian\_date()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#pandas.Timestamp.to_julian_date "Link to this definition")

Convert Timestamp to a Julian Date.

This method returns the number of days as a float since 0 Julian date, which is noon January 1, 4713 BC.

See also

[`Timestamp.toordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#pandas.Timestamp.toordinal "pandas.Timestamp.toordinal")

Return proleptic Gregorian ordinal.

[`Timestamp.timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")

Return POSIX timestamp as float.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52')
\>>> ts.to\_julian\_date()
2458923.147824074

Copy to clipboard

On this page