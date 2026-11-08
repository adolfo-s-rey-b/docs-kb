[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.tz_localize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.tz_localize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.tz_localize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.tz_localize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.tz_localize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.tz_localize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.tz_localize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.tz_localize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.tz_localize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.tz_localize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.tz_localize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.tz_localize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.tz\_localize[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas-series-tz-localize "Link to this heading")

============================================================================================================================================================

Series.tz\_localize(_tz_, _axis\=0_, _level\=None_, _copy\=<no\_default>_, _ambiguous\='raise'_, _nonexistent\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L11387-L11598)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "Link to this definition")

Localize time zone naive index of a Series or DataFrame to target time zone.

This operation localizes the Index. To localize the values in a time zone naive Series, use [`Series.dt.tz_localize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize "pandas.Series.dt.tz_localize")
.

Parameters:

**tz**str or tzinfo or None

Time zone to attach to the index; the wall time of each index label is preserved. Passing `None` detaches the time zone from a tz-aware index, returning a tz-naive index with the same wall time.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to localize

**level**int, str, default None

If axis is a MultiIndex, localize a specific level. Otherwise must be None.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**ambiguous**‘infer’, bool, bool-ndarray, ‘NaT’, default ‘raise’

When clocks moved backward due to DST, ambiguous times may arise. For example in Central European Time (UTC+01), when going from 03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC and at 01:30:00 UTC. In such a situation, the ambiguous parameter dictates how ambiguous times should be handled.

*   ‘infer’ will attempt to infer fall dst-transition hours based on order. Requires that the timestamps are monotonically increasing.
    
*   bool (or bool-ndarray) where True signifies a DST time, False designates a non-DST time (note that this flag is only applicable for ambiguous times)
    
*   ‘NaT’ will return NaT where there are ambiguous times
    
*   ‘raise’ will raise a ValueError if there are ambiguous times.
    

**nonexistent**str, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST. Valid values are:

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

Returns:

Series/DataFrame

Same type as the input, with time zone naive or aware index, depending on `tz`.

Raises:

TypeError

If the TimeSeries is tz-aware and tz is not None.

See also

[`Series.dt.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize "pandas.Series.dt.tz_localize")

Localize the values in a time zone naive Series.

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a timezone.

Examples

Attach a time zone to tz-naive timestamps:

\>>> s \= pd.Series(
...     \[1\],
...     index\=pd.DatetimeIndex(\["2018-09-15 01:30:00"\]),
... )
\>>> s.tz\_localize("CET")
2018-09-15 01:30:00+02:00    1
dtype: int64

Copy to clipboard

Pass None to detach the time zone from tz-aware timestamps:

\>>> s \= pd.Series(\[1\], index\=pd.DatetimeIndex(\["2018-09-15 01:30:00+02:00"\]))
\>>> s.tz\_localize(None)
2018-09-15 01:30:00    1
dtype: int64

Copy to clipboard

Be careful with DST changes. When there is sequential data, pandas can infer the DST time:

\>>> s \= pd.Series(
...     range(7),
...     index\=pd.DatetimeIndex(
...         \[\
...             "2018-10-28 01:30:00",\
...             "2018-10-28 02:00:00",\
...             "2018-10-28 02:30:00",\
...             "2018-10-28 02:00:00",\
...             "2018-10-28 02:30:00",\
...             "2018-10-28 03:00:00",\
...             "2018-10-28 03:30:00",\
...         \]
...     ),
... )
\>>> s.tz\_localize("CET", ambiguous\="infer")
2018-10-28 01:30:00+02:00    0
2018-10-28 02:00:00+02:00    1
2018-10-28 02:30:00+02:00    2
2018-10-28 02:00:00+01:00    3
2018-10-28 02:30:00+01:00    4
2018-10-28 03:00:00+01:00    5
2018-10-28 03:30:00+01:00    6
dtype: int64

Copy to clipboard

In some cases, inferring the DST is impossible. In such cases, you can pass an ndarray to the ambiguous parameter to set the DST explicitly

\>>> s \= pd.Series(
...     range(3),
...     index\=pd.DatetimeIndex(
...         \[\
...             "2018-10-28 01:20:00",\
...             "2018-10-28 02:36:00",\
...             "2018-10-28 03:46:00",\
...         \]
...     ),
... )
\>>> s.tz\_localize("CET", ambiguous\=np.array(\[True, True, False\]))
2018-10-28 01:20:00+02:00    0
2018-10-28 02:36:00+02:00    1
2018-10-28 03:46:00+01:00    2
dtype: int64

Copy to clipboard

If the DST transition causes nonexistent times, you can shift these dates forward or backward with a timedelta object or ‘shift\_forward’ or ‘shift\_backward’.

\>>> dti \= pd.DatetimeIndex(
...     \["2015-03-29 02:30:00", "2015-03-29 03:30:00"\], dtype\="M8\[ns\]"
... )
\>>> s \= pd.Series(range(2), index\=dti)
\>>> s.tz\_localize("Europe/Warsaw", nonexistent\="shift\_forward")
2015-03-29 03:00:00+02:00    0
2015-03-29 03:30:00+02:00    1
dtype: int64
\>>> s.tz\_localize("Europe/Warsaw", nonexistent\="shift\_backward")
2015-03-29 01:59:59.999999999+01:00    0
2015-03-29 03:30:00.000000000+02:00    1
dtype: int64
\>>> s.tz\_localize("Europe/Warsaw", nonexistent\=pd.Timedelta("1h"))
2015-03-29 03:30:00+02:00    0
2015-03-29 03:30:00+02:00    1
dtype: int64

Copy to clipboard

On this page