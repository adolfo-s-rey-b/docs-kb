[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.copy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html#pandas-tseries-offsets-baseoffset-copy "Link to this heading")

==================================================================================================================================================================================================

BaseOffset.copy()[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html#pandas.tseries.offsets.BaseOffset.copy "Link to this definition")

Return a copy of the frequency.

This method creates a new instance of the same frequency offset with identical parameters. The returned copy is independent of the original, allowing modifications without affecting the source object.

See also

`tseries.offsets.Week.copy`

Return a copy of Week offset.

`tseries.offsets.DateOffset.copy`

Return a copy of date offset.

`tseries.offsets.MonthEnd.copy`

Return a copy of MonthEnd offset.

`tseries.offsets.YearBegin.copy`

Return a copy of YearBegin offset.

Examples

\>>> freq \= pd.DateOffset(1)
\>>> freq\_copy \= freq.copy()
\>>> freq is freq\_copy
False

Copy to clipboard

On this page