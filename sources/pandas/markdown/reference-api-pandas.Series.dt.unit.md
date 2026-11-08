[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#pandas-series-dt-unit "Link to this heading")

===============================================================================================================================================

Series.dt.unit[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#pandas.Series.dt.unit "Link to this definition")

The precision unit of the datetime data.

Returns the precision unit for the dtype. It means the smallest time frame that can be stored within this dtype.

Returns:

str

Unit string representation (e.g. “ns”).

See also

`TimelikeOps.as_unit`

Converts to a specific unit.

Examples

\>>> idx \= pd.DatetimeIndex(\["2020-01-02 01:02:03.004005006"\])
\>>> idx.unit
'ns'
\>>> idx.as\_unit("s").unit
's'

Copy to clipboard

On this page