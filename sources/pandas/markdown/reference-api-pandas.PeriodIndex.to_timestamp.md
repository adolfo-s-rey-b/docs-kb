[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.to_timestamp.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.to_timestamp.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.to_timestamp.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.to_timestamp.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.to_timestamp.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.to_timestamp.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.to_timestamp.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.to\_timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas-periodindex-to-timestamp "Link to this heading")

==============================================================================================================================================================================

PeriodIndex.to\_timestamp(_freq\=None_, _how\='start'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L218-L276)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "Link to this definition")

Cast to DatetimeIndex.

If possible, gives microsecond-unit DatetimeIndex. Otherwise gives nanosecond unit.

Parameters:

**freq**str or DateOffset, optional

Target frequency. The default is ‘D’ for week or longer, ‘s’ otherwise.

**how**{‘start’, ‘end’, ‘s’, ‘e’}, default ‘start’

Whether to use the start or end of the time period being converted. Case-insensitive.

Returns:

DatetimeIndex

Timestamp representation of given Period-like object.

See also

[`PeriodIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day")

The days of the period.

[`PeriodIndex.from_fields`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas.PeriodIndex.from_fields "pandas.PeriodIndex.from_fields")

Construct a PeriodIndex from fields (year, month, day, etc.).

[`PeriodIndex.from_ordinals`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas.PeriodIndex.from_ordinals "pandas.PeriodIndex.from_ordinals")

Construct a PeriodIndex from ordinals.

[`PeriodIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.hour.html#pandas.PeriodIndex.hour "pandas.PeriodIndex.hour")

The hour of the period.

[`PeriodIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas.PeriodIndex.minute "pandas.PeriodIndex.minute")

The minute of the period.

[`PeriodIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas.PeriodIndex.month "pandas.PeriodIndex.month")

The month as January=1, December=12.

[`PeriodIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas.PeriodIndex.second "pandas.PeriodIndex.second")

The second of the period.

[`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year")

The year of the period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.to\_timestamp()
DatetimeIndex(\['2023-01-01', '2023-02-01', '2023-03-01'\],
dtype='datetime64\[us\]', freq='MS')

Copy to clipboard

The frequency will not be inferred if the index contains less than three elements, or if the values of index are not strictly monotonic:

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02"\], freq\="M")
\>>> idx.to\_timestamp()
DatetimeIndex(\['2023-01-01', '2023-02-01'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

\>>> idx \= pd.PeriodIndex(
...     \["2023-01", "2023-02", "2023-02", "2023-03"\], freq\="2M"
... )
\>>> idx.to\_timestamp()
DatetimeIndex(\['2023-01-01', '2023-02-01', '2023-02-01', '2023-03-01'\],
dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page