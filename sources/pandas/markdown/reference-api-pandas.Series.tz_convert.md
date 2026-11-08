[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.tz_convert.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.tz_convert.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.tz_convert.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.tz_convert.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.tz_convert.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.tz_convert.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.tz_convert.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.tz_convert.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.tz_convert.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.tz_convert.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.tz_convert.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.tz_convert.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.tz\_convert[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#pandas-series-tz-convert "Link to this heading")

=========================================================================================================================================================

Series.tz\_convert(_tz_, _axis\=0_, _level\=None_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L11285-L11385)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert "Link to this definition")

Convert tz-aware axis to target time zone.

This method converts the timezone of a datetime-based index from one timezone to another.

Parameters:

**tz**str or tzinfo object or None

Target time zone. Passing `None` will convert to UTC and remove the timezone information.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to convert

**level**int, str, default None

If axis is a MultiIndex, convert a specific level. Otherwise must be None.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

Series/DataFrame

Object with time zone converted axis.

Raises:

TypeError

If the axis is tz-naive.

See also

[`DataFrame.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html#pandas.DataFrame.tz_localize "pandas.DataFrame.tz_localize")

Localize tz-naive index of DataFrame to target time zone.

[`Series.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "pandas.Series.tz_localize")

Localize tz-naive index of Series to target time zone.

Examples

Change to another time zone:

\>>> s \= pd.Series(
...     \[1\],
...     index\=pd.DatetimeIndex(\["2018-09-15 01:30:00+02:00"\]),
... )
\>>> s.tz\_convert("Asia/Shanghai")
2018-09-15 07:30:00+08:00    1
dtype: int64

Copy to clipboard

Pass None to convert to UTC and get a tz-naive index:

\>>> s \= pd.Series(\[1\], index\=pd.DatetimeIndex(\["2018-09-15 01:30:00+02:00"\]))
\>>> s.tz\_convert(None)
2018-09-14 23:30:00    1
dtype: int64

Copy to clipboard

On this page