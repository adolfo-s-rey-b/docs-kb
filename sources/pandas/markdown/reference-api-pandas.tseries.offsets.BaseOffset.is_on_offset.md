[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.is\_on\_offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#pandas-tseries-offsets-baseoffset-is-on-offset "Link to this heading")

============================================================================================================================================================================================================================

BaseOffset.is\_on\_offset(_dt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#pandas.tseries.offsets.BaseOffset.is_on_offset "Link to this definition")

Return boolean whether a timestamp intersects with this frequency.

This method determines if a given timestamp aligns with the start of a custom business month, as defined by this offset. It accounts for custom rules, such as skipping weekends or other non-business days, and checks whether the provided datetime falls on a valid business day that marks the beginning of the custom business month.

Parameters:

**dt**datetime.datetime

Timestamp to check intersections with frequency.

See also

`tseries.offsets.CustomBusinessMonthBegin`

Represents the start of a custom business month.

`tseries.offsets.CustomBusinessMonthEnd`

Represents the end of a custom business month.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> freq \= pd.offsets.Day(1)
\>>> freq.is\_on\_offset(ts)
True

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 8, 6)
\>>> ts.day\_name()
'Saturday'
\>>> freq \= pd.offsets.BusinessDay(1)
\>>> freq.is\_on\_offset(ts)
False

Copy to clipboard

On this page