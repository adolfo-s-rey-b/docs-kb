[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.as_unit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.as_unit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.as_unit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.as_unit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.as_unit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.as_unit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.as_unit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.as_unit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.as_unit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.as_unit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.as_unit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.as_unit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.as\_unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas-series-dt-as-unit "Link to this heading")

=========================================================================================================================================================

Series.dt.as\_unit(_unit_, _round\_ok\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimelike.py#L1936-L1993)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit "Link to this definition")

Convert to a dtype with the given unit resolution.

The limits of timestamp representation depend on the chosen resolution. Different resolutions can be converted to each other through as\_unit.

Parameters:

**unit**{‘s’, ‘ms’, ‘us’, ‘ns’}

**round\_ok**bool, default True

If False and the conversion requires rounding, raise ValueError.

Returns:

same type as self

Converted to the specified unit.

See also

[`Timestamp.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "pandas.Timestamp.as_unit")

Convert to the given unit.

Examples

For [`pandas.DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
:

\>>> idx \= pd.DatetimeIndex(\["2020-01-02 01:02:03.004005006"\])
\>>> idx
DatetimeIndex(\['2020-01-02 01:02:03.004005006'\],
              dtype='datetime64\[ns\]', freq=None)
\>>> idx.as\_unit("s")
DatetimeIndex(\['2020-01-02 01:02:03'\], dtype='datetime64\[s\]', freq=None)

Copy to clipboard

For [`pandas.TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
:

\>>> tdelta\_idx \= pd.to\_timedelta(\["1 day 3 min 2 us 42 ns"\])
\>>> tdelta\_idx
TimedeltaIndex(\['1 days 00:03:00.000002042'\],
                dtype='timedelta64\[ns\]', freq=None)
\>>> tdelta\_idx.as\_unit("s")
TimedeltaIndex(\['1 days 00:03:00'\], dtype='timedelta64\[s\]', freq=None)

Copy to clipboard

On this page