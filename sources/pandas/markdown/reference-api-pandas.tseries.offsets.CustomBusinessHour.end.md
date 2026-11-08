[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessHour.end[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#pandas-tseries-offsets-custombusinesshour-end "Link to this heading")

=======================================================================================================================================================================================================================

CustomBusinessHour.end[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#pandas.tseries.offsets.CustomBusinessHour.end "Link to this definition")

Return the end time(s) of the business hour.

This property returns a tuple of datetime.time objects representing the end times of business hours.

See also

[`BusinessHour.start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#pandas.tseries.offsets.BusinessHour.start "pandas.tseries.offsets.BusinessHour.start")

Return the start time(s) of the business hour.

[`CustomBusinessHour.start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.start.html#pandas.tseries.offsets.CustomBusinessHour.start "pandas.tseries.offsets.CustomBusinessHour.start")

Return the start time(s) of the custom business hour.

Examples

\>>> pd.offsets.BusinessHour().end
(datetime.time(17, 0),)

Copy to clipboard

On this page