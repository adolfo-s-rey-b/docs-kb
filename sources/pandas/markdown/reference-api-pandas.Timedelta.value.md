[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.value.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.value.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.value.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.value.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.value.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.value.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.value.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.value.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.value.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.value.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.value.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.value.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.value[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#pandas-timedelta-value "Link to this heading")

==================================================================================================================================================

Timedelta.value[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#pandas.Timedelta.value "Link to this definition")

Return the value of Timedelta object in nanoseconds.

Return the total seconds, milliseconds and microseconds of the timedelta as nanoseconds.

Returns:

int

See also

[`Timedelta.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#pandas.Timedelta.unit "pandas.Timedelta.unit")

Return the unit of Timedelta object.

Examples

\>>> pd.Timedelta(1, "us").value
1000

Copy to clipboard

On this page