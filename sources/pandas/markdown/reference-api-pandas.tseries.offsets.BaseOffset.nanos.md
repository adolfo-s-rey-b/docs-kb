[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.nanos.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.nanos[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.nanos.html#pandas-tseries-offsets-baseoffset-nanos "Link to this heading")

=====================================================================================================================================================================================================

BaseOffset.nanos[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.nanos.html#pandas.tseries.offsets.BaseOffset.nanos "Link to this definition")

Return an integer of the total number of nanoseconds.

This property computes the offset duration in nanoseconds. For fixed frequency offsets (like Hour, Minute, Second), this returns the exact number of nanoseconds. For non-fixed frequencies that depend on calendar context (like Week without a specified weekday), this raises an error.

Raises:

ValueError

If the frequency is non-fixed.

See also

`tseries.offsets.Hour.nanos`

Returns an integer of the total number of nanoseconds.

`tseries.offsets.Day.nanos`

Returns an integer of the total number of nanoseconds.

Examples

\>>> pd.offsets.Week(n\=1).nanos
ValueError: Week: weekday=None is a non-fixed frequency

Copy to clipboard

On this page