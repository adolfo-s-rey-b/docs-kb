[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BusinessHour.start.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BusinessHour.start.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessHour.start[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#pandas-tseries-offsets-businesshour-start "Link to this heading")

===========================================================================================================================================================================================================

BusinessHour.start[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#pandas.tseries.offsets.BusinessHour.start "Link to this definition")

Return the start time(s) of the business hour.

This property returns a tuple of datetime.time objects representing the start times of business hours.

See also

[`BusinessHour.end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.end.html#pandas.tseries.offsets.BusinessHour.end "pandas.tseries.offsets.BusinessHour.end")

Return the end time(s) of the business hour.

[`CustomBusinessHour.end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#pandas.tseries.offsets.CustomBusinessHour.end "pandas.tseries.offsets.CustomBusinessHour.end")

Return the end time(s) of the custom business hour.

Examples

\>>> pd.offsets.BusinessHour().start
(datetime.time(9, 0),)

Copy to clipboard

On this page