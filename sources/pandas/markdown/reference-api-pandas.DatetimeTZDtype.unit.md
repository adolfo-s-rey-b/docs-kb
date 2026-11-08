[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeTZDtype.unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeTZDtype.unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeTZDtype.unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeTZDtype.unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeTZDtype.unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeTZDtype.unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeTZDtype.unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeTZDtype.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html#pandas-datetimetzdtype-unit "Link to this heading")

=================================================================================================================================================================

property DatetimeTZDtype.unit[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L828-L847)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.unit.html#pandas.DatetimeTZDtype.unit "Link to this definition")

The precision of the datetime data.

Returns the time resolution as one of `'s'`, `'ms'`, `'us'`, or `'ns'`.

See also

[`DatetimeTZDtype.tz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.tz.html#pandas.DatetimeTZDtype.tz "pandas.DatetimeTZDtype.tz")

Retrieves the timezone.

Examples

\>>> from zoneinfo import ZoneInfo
\>>> dtype \= pd.DatetimeTZDtype(tz\=ZoneInfo("America/Los\_Angeles"))
\>>> dtype.unit
'ns'

Copy to clipboard

On this page