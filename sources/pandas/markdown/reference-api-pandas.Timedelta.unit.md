[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#pandas-timedelta-unit "Link to this heading")

===============================================================================================================================================

Timedelta.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#pandas.Timedelta.unit "Link to this definition")

Return the unit of Timedelta object.

The unit of Timedelta object is nanosecond, i.e., ‘ns’ by default.

Returns:

str

See also

[`Timedelta.value`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#pandas.Timedelta.value "pandas.Timedelta.value")

Return the value of Timedelta object in nanoseconds.

[`Timedelta.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas.Timedelta.as_unit "pandas.Timedelta.as_unit")

Convert the underlying int64 representation to the given unit.

Examples

\>>> td \= pd.Timedelta(42, unit\='us')
\>>> td.unit
'us'

Copy to clipboard

On this page