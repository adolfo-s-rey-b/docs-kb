[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.normalize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.normalize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.normalize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.normalize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.normalize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.normalize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.normalize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.normalize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.normalize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.normalize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.normalize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.normalize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.normalize[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#pandas-series-dt-normalize "Link to this heading")

==============================================================================================================================================================

Series.dt.normalize()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimes.py#L1158-L1200)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#pandas.Series.dt.normalize "Link to this definition")

Convert times to midnight.

The time component of the date-time is converted to midnight i.e. 00:00:00. This is useful in cases, when the time does not matter. Length is unaltered. The timezones are unaffected.

This method is available on Series with datetime values under the `.dt` accessor, and directly on Datetime Array/Index.

Returns:

DatetimeArray, DatetimeIndex or Series

The same type as the original data. Series will have the same name and index. DatetimeIndex will have the same name.

See also

[`floor`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html#pandas.Series.dt.floor "pandas.Series.dt.floor")

Floor the datetimes to the specified freq.

[`ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.ceil.html#pandas.Series.dt.ceil "pandas.Series.dt.ceil")

Ceil the datetimes to the specified freq.

[`round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.round.html#pandas.Series.dt.round "pandas.Series.dt.round")

Round the datetimes to the specified freq.

Examples

\>>> idx \= pd.date\_range(
...     start\="2014-08-01 10:00", freq\="h", periods\=3, tz\="Asia/Calcutta"
... )
\>>> idx
DatetimeIndex(\['2014-08-01 10:00:00+05:30',\
               '2014-08-01 11:00:00+05:30',\
               '2014-08-01 12:00:00+05:30'\],
                dtype='datetime64\[us, Asia/Calcutta\]', freq='h')
\>>> idx.normalize()
DatetimeIndex(\['2014-08-01 00:00:00+05:30',\
               '2014-08-01 00:00:00+05:30',\
               '2014-08-01 00:00:00+05:30'\],
               dtype='datetime64\[us, Asia/Calcutta\]', freq=None)

Copy to clipboard

On this page