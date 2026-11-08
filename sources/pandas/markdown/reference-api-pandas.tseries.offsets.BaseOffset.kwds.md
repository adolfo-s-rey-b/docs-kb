[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.kwds.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.kwds[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.kwds.html#pandas-tseries-offsets-baseoffset-kwds "Link to this heading")

==================================================================================================================================================================================================

BaseOffset.kwds[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.kwds.html#pandas.tseries.offsets.BaseOffset.kwds "Link to this definition")

Return a dict of extra parameters for the offset.

These parameters exclude `n` and `normalize`, which are common to all offsets. The returned dictionary can be passed to the offset constructor to recreate the offset with the same settings.

See also

`tseries.offsets.DateOffset`

The base class for all pandas date offsets.

`tseries.offsets.WeekOfMonth`

Represents the week of the month.

`tseries.offsets.LastWeekOfMonth`

Represents the last week of the month.

Examples

\>>> pd.DateOffset(5).kwds
{}

Copy to clipboard

\>>> pd.offsets.FY5253Quarter().kwds
{'weekday': 0,
 'startingMonth': 1,
 'qtr\_with\_extra\_week': 1,
 'variation': 'nearest'}

Copy to clipboard

On this page