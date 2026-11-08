[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.second.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.second.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.second.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.second.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.second.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.second.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.second.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.second.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.second.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.second.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.second.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.second.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.second[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas-timestamp-second "Link to this heading")

=====================================================================================================================================================

Timestamp.second[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "Link to this definition")

Return the second of the Timestamp.

Seconds range from 0 to 59.

Returns:

int

The second of the Timestamp.

See also

[`Timestamp.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas.Timestamp.microsecond "pandas.Timestamp.microsecond")

Return the microsecond of the Timestamp.

[`Timestamp.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "pandas.Timestamp.minute")

Return the minute of the Timestamp.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30")
\>>> ts.second
30

Copy to clipboard

On this page