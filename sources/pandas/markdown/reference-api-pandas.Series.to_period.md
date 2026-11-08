[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_period.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_period.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_period.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_period.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_period.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_period.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_period.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_period.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_period.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_period.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_period.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_period.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_period[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas-series-to-period "Link to this heading")

======================================================================================================================================================

Series.to\_period(_freq\=None_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L7226-L7288)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period "Link to this definition")

Convert Series from DatetimeIndex to PeriodIndex.

This method converts the DatetimeIndex of the Series into a PeriodIndex with a specified frequency, which is useful when period-based indexing is preferred over exact timestamps.

Parameters:

**freq**str, default None

Frequency associated with the PeriodIndex.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

Series

Series with index converted to PeriodIndex.

See also

[`DataFrame.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas.DataFrame.to_period "pandas.DataFrame.to_period")

Equivalent method for DataFrame.

[`Series.dt.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas.Series.dt.to_period "pandas.Series.dt.to_period")

Convert DateTime column values.

Examples

\>>> idx \= pd.DatetimeIndex(\["2023", "2024", "2025"\])
\>>> s \= pd.Series(\[1, 2, 3\], index\=idx)
\>>> s \= s.to\_period()
\>>> s
2023    1
2024    2
2025    3
Freq: Y-DEC, dtype: int64

Copy to clipboard

Viewing the index

\>>> s.index
PeriodIndex(\['2023', '2024', '2025'\], dtype='period\[Y-DEC\]')

Copy to clipboard

On this page