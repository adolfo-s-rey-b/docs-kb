[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.is_quarter_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.is_quarter_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.is_quarter_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.is_quarter_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.is_quarter_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.is_quarter_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.is_quarter_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.is\_quarter\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#pandas-timestamp-is-quarter-start "Link to this heading")

=====================================================================================================================================================================================

Timestamp.is\_quarter\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#pandas.Timestamp.is_quarter_start "Link to this definition")

Check if the date is the first day of the quarter.

Quarters start on the first day of January, April, July, and October in the standard calendar.

Returns:

bool

True if date is first day of the quarter.

See also

[`Timestamp.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#pandas.Timestamp.is_quarter_end "pandas.Timestamp.is_quarter_end")

Similar property indicating the quarter end.

[`Timestamp.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter")

Return the quarter of the date.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14)
\>>> ts.is\_quarter\_start
False

Copy to clipboard

\>>> ts \= pd.Timestamp(2020, 4, 1)
\>>> ts.is\_quarter\_start
True

Copy to clipboard

On this page