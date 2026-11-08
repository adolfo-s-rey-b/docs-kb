[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_period[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas-dataframe-to-period "Link to this heading")

===============================================================================================================================================================

DataFrame.to\_period(_freq\=None_, _axis\=0_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19894-L19969)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas.DataFrame.to_period "Link to this definition")

Convert DataFrame from DatetimeIndex to PeriodIndex.

Convert DataFrame from DatetimeIndex to PeriodIndex with desired frequency (inferred from index if not passed). Either index of columns can be converted, depending on axis argument.

Parameters:

**freq**str, default

Frequency of the PeriodIndex.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to convert (the index by default).

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

DataFrame

The DataFrame with the converted PeriodIndex.

See also

[`Series.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period "pandas.Series.to_period")

Equivalent method for Series.

[`Series.dt.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas.Series.dt.to_period "pandas.Series.dt.to_period")

Convert DateTime column values.

Examples

\>>> idx \= pd.to\_datetime(
...     \[\
...         "2001-03-31 00:00:00",\
...         "2002-05-31 00:00:00",\
...         "2003-08-31 00:00:00",\
...     \]
... )

Copy to clipboard

\>>> idx
DatetimeIndex(\['2001-03-31', '2002-05-31', '2003-08-31'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

\>>> idx.to\_period("M")
PeriodIndex(\['2001-03', '2002-05', '2003-08'\], dtype='period\[M\]')

Copy to clipboard

For the yearly frequency

\>>> idx.to\_period("Y")
PeriodIndex(\['2001', '2002', '2003'\], dtype='period\[Y-DEC\]')

Copy to clipboard

On this page