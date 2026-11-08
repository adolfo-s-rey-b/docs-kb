[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.microsecond.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.microsecond.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.microsecond.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.microsecond.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.microsecond.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.microsecond.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.microsecond.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.microsecond.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.microsecond.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.microsecond.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.microsecond.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.microsecond.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.microsecond[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas-timestamp-microsecond "Link to this heading")

====================================================================================================================================================================

Timestamp.microsecond[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas.Timestamp.microsecond "Link to this definition")

Return the microsecond of the Timestamp.

Microseconds range from 0 through 999999 and represent the sub-second component of the Timestamp at microsecond resolution.

Returns:

int

The microsecond of the Timestamp.

See also

[`Timestamp.second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second")

Return the second of the Timestamp.

[`Timestamp.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "pandas.Timestamp.minute")

Return the minute of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30.2304")
\>>> ts.microsecond
230400

Copy to clipboard

On this page