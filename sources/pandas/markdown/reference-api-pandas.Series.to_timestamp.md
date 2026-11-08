[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas-series-to-timestamp "Link to this heading")

===============================================================================================================================================================

Series.to\_timestamp(_freq\=None_, _how\='start'_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L7147-L7224)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp "Link to this definition")

Cast to DatetimeIndex of Timestamps, at _beginning_ of period.

This can be changed to the _end_ of the period, by specifying how=”e”.

Parameters:

**freq**str, default frequency of PeriodIndex

Desired frequency.

**how**{‘start’, ‘end’, ‘s’, ‘e’}, default ‘start’

Convention for converting period to timestamp; start of period vs. end. Case-insensitive.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

Series with DatetimeIndex

Series with the PeriodIndex cast to DatetimeIndex.

See also

[`Series.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period "pandas.Series.to_period")

Inverse method to cast DatetimeIndex to PeriodIndex.

[`DataFrame.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#pandas.DataFrame.to_timestamp "pandas.DataFrame.to_timestamp")

Equivalent method for DataFrame.

Examples

\>>> idx \= pd.PeriodIndex(\["2023", "2024", "2025"\], freq\="Y")
\>>> s1 \= pd.Series(\[1, 2, 3\], index\=idx)
\>>> s1
2023    1
2024    2
2025    3
Freq: Y-DEC, dtype: int64

Copy to clipboard

The resulting frequency of the Timestamps is YearBegin

\>>> s1 \= s1.to\_timestamp()
\>>> s1
2023-01-01    1
2024-01-01    2
2025-01-01    3
Freq: YS-JAN, dtype: int64

Copy to clipboard

Using freq which is the offset that the Timestamps will have

\>>> s2 \= pd.Series(\[1, 2, 3\], index\=idx)
\>>> s2 \= s2.to\_timestamp(freq\="M")
\>>> s2
2023-01-31    1
2024-01-31    2
2025-01-31    3
Freq: YE-JAN, dtype: int64

Copy to clipboard

On this page