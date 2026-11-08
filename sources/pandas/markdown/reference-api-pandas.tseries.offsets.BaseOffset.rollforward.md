[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollforward.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.rollforward[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollforward.html#pandas-tseries-offsets-baseoffset-rollforward "Link to this heading")

=======================================================================================================================================================================================================================

BaseOffset.rollforward(_dt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollforward.html#pandas.tseries.offsets.BaseOffset.rollforward "Link to this definition")

Roll provided date forward to next offset only if not on offset.

If the provided date is already on an offset, it is returned unchanged. Otherwise, the date is rolled forward to the next offset boundary.

Parameters:

**dt**datetime or Timestamp

Timestamp to roll forward.

Returns:

Timestamp

Rolled timestamp if not on offset, otherwise unchanged timestamp.

See also

[`rollback`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollback.html#pandas.tseries.offsets.BaseOffset.rollback "pandas.tseries.offsets.BaseOffset.rollback")

Roll provided date backward to previous offset only if not on offset.

[`is_on_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#pandas.tseries.offsets.BaseOffset.is_on_offset "pandas.tseries.offsets.BaseOffset.is_on_offset")

Return boolean whether a timestamp intersects with this frequency.

Examples

\>>> ts \= pd.Timestamp("2025-01-15 09:00:00")
\>>> offset \= pd.tseries.offsets.MonthEnd()

Copy to clipboard

Timestamp is not on the offset (not a month end), so it rolls forward:

\>>> offset.rollforward(ts)
Timestamp('2025-01-31 09:00:00')

Copy to clipboard

If the timestamp is already on the offset, it remains unchanged:

\>>> ts\_on\_offset \= pd.Timestamp("2025-01-31")
\>>> offset.rollforward(ts\_on\_offset)
Timestamp('2025-01-31 00:00:00')

Copy to clipboard

On this page