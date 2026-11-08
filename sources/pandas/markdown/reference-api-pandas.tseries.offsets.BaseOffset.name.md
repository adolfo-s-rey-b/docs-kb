[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.name[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html#pandas-tseries-offsets-baseoffset-name "Link to this heading")

==================================================================================================================================================================================================

BaseOffset.name[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html#pandas.tseries.offsets.BaseOffset.name "Link to this definition")

Return a string representing the base frequency.

Deprecated since version 3.1.0: The `.name` property is deprecated. Use `.rule_code` instead.

This is typically a short string alias (e.g., ‘h’ for hourly, ‘D’ for daily) used to identify the offset type, regardless of the n multiplier.

See also

`tseries.offsets.Week`

Represents a weekly offset.

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Base class for all other offset classes.

`tseries.offsets.Day`

Represents a single day offset.

`tseries.offsets.MonthEnd`

Represents a monthly offset that snaps to the end of the month.

Examples

\>>> pd.offsets.Hour().name
'h'

Copy to clipboard

\>>> pd.offsets.Hour(5).name
'h'

Copy to clipboard

On this page