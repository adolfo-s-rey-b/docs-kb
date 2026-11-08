[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.is\_year\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html#pandas-tseries-offsets-baseoffset-is-year-end "Link to this heading")

=========================================================================================================================================================================================================================

BaseOffset.is\_year\_end(_ts_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html#pandas.tseries.offsets.BaseOffset.is_year_end "Link to this definition")

Return boolean whether a timestamp occurs on the year end.

This method checks if the given timestamp falls on December 31st, which marks the end of a calendar year.

Parameters:

**ts**Timestamp

The timestamp to check.

See also

[`is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_start.html#pandas.tseries.offsets.BaseOffset.is_year_start "pandas.tseries.offsets.BaseOffset.is_year_start")

Return boolean whether a timestamp occurs on the year start.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> freq \= pd.offsets.Hour(5)
\>>> freq.is\_year\_end(ts)
False

Copy to clipboard

On this page