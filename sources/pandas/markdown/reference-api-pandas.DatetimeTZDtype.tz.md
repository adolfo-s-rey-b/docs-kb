[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.tz.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeTZDtype.tz[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.tz.html#pandas-datetimetzdtype-tz "Link to this heading")

===========================================================================================================================================================

property DatetimeTZDtype.tz[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L849-L868)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.tz.html#pandas.DatetimeTZDtype.tz "Link to this definition")

The timezone.

Returns the [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.15)")
 object associated with this dtype, representing the timezone used for localization.

See also

[`DatetimeTZDtype.unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html#pandas.DatetimeTZDtype.unit "pandas.DatetimeTZDtype.unit")

Retrieves precision of the datetime data.

Examples

\>>> from zoneinfo import ZoneInfo
\>>> dtype \= pd.DatetimeTZDtype(tz\=ZoneInfo("America/Los\_Angeles"))
\>>> dtype.tz
zoneinfo.ZoneInfo(key='America/Los\_Angeles')

Copy to clipboard

On this page