[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#pandas-dataframe-to-timestamp "Link to this heading")

========================================================================================================================================================================

DataFrame.to\_timestamp(_freq\=None_, _how\='start'_, _axis\=0_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19806-L19892)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#pandas.DataFrame.to_timestamp "Link to this definition")

Cast PeriodIndex to DatetimeIndex of timestamps, at _beginning_ of period.

This can be changed to the _end_ of the period, by specifying how=”e”.

Parameters:

**freq**str, default frequency of PeriodIndex

Desired frequency.

**how**{‘start’, ‘end’, ‘s’, ‘e’}, default ‘start’

Convention for converting period to timestamp; start of period vs. end. Case-insensitive.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to convert (the index by default).

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

DataFrame with DatetimeIndex

DataFrame with the PeriodIndex cast to DatetimeIndex.

See also

[`DataFrame.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas.DataFrame.to_period "pandas.DataFrame.to_period")

Inverse method to cast DatetimeIndex to PeriodIndex.

[`Series.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp "pandas.Series.to_timestamp")

Equivalent method for Series.

Examples

\>>> idx \= pd.PeriodIndex(\["2023", "2024"\], freq\="Y")
\>>> d \= {"col1": \[1, 2\], "col2": \[3, 4\]}
\>>> df1 \= pd.DataFrame(data\=d, index\=idx)
\>>> df1
      col1   col2
2023     1      3
2024     2      4

Copy to clipboard

The resulting timestamps will be at the beginning of the year in this case

\>>> df1 \= df1.to\_timestamp()
\>>> df1
            col1   col2
2023-01-01     1      3
2024-01-01     2      4
\>>> df1.index
DatetimeIndex(\['2023-01-01', '2024-01-01'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Using freq which is the offset that the Timestamps will have

\>>> df2 \= pd.DataFrame(data\=d, index\=idx)
\>>> df2 \= df2.to\_timestamp(freq\="M")
\>>> df2
            col1   col2
2023-01-31     1      3
2024-01-31     2      4
\>>> df2.index
DatetimeIndex(\['2023-01-31', '2024-01-31'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page