[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.is\_quarter\_start[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html#pandas-tseries-offsets-baseoffset-is-quarter-start "Link to this heading")

========================================================================================================================================================================================================================================

BaseOffset.is\_quarter\_start(_ts_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html#pandas.tseries.offsets.BaseOffset.is_quarter_start "Link to this definition")

Return boolean whether a timestamp occurs on the quarter start.

This method checks if the given timestamp falls on the first day of a calendar quarter (January 1, April 1, July 1, or October 1).

Parameters:

**ts**Timestamp

The timestamp to check.

See also

[`is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_end.html#pandas.tseries.offsets.BaseOffset.is_quarter_end "pandas.tseries.offsets.BaseOffset.is_quarter_end")

Return boolean whether a timestamp occurs on the quarter end.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> freq \= pd.offsets.Hour(5)
\>>> freq.is\_quarter\_start(ts)
True

Copy to clipboard

On this page