[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.fold.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.fold.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.fold.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.fold.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.fold.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.fold.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.fold.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.fold.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.fold.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.fold.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.fold.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.fold.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.fold[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html#pandas-timestamp-fold "Link to this heading")

===============================================================================================================================================

Timestamp.fold[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html#pandas.Timestamp.fold "Link to this definition")

Return the fold value of the Timestamp.

The fold attribute is used to disambiguate wall times in a repeated interval during daylight saving time transitions.

Returns:

int

The fold value of the Timestamp, where 0 indicates the first occurrence of the ambiguous time, and 1 indicates the second.

See also

[`Timestamp.dst`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas.Timestamp.dst "pandas.Timestamp.dst")

Return the daylight saving time (DST) adjustment.

[`Timestamp.tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo")

Return the timezone information associated.

Examples

\>>> ts \= pd.Timestamp("2024-11-03 01:30:00")
\>>> ts.fold
0

Copy to clipboard

On this page