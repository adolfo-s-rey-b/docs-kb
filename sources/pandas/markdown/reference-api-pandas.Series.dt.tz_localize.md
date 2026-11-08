[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.tz_localize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.tz_localize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.tz_localize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.tz_localize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.tz_localize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.tz_localize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.tz_localize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.tz_localize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.tz_localize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.tz_localize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.tz_localize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.tz_localize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.tz\_localize[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas-series-dt-tz-localize "Link to this heading")

=====================================================================================================================================================================

Series.dt.tz\_localize(_tz_, _ambiguous\='raise'_, _nonexistent\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimes.py#L950-L1125)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize "Link to this definition")

Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index.

This method takes a time zone (tz) naive Datetime Array/Index object and makes this time zone aware. It does not move the time to another time zone.

This method can also be used to do the inverse – to create a time zone unaware object from an aware object. To that end, pass tz=None.

Parameters:

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile, datetime.tzinfo or None

Time zone to attach to the tz-naive timestamps; the wall time is preserved. Passing `None` detaches the time zone from a tz-aware Array/Index, returning a tz-naive result with the same wall time.

**ambiguous**‘infer’, ‘NaT’, bool array, default ‘raise’

When clocks moved backward due to DST, ambiguous times may arise. For example in Central European Time (UTC+01), when going from 03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC and at 01:30:00 UTC. In such a situation, the ambiguous parameter dictates how ambiguous times should be handled.

*   ‘infer’ will attempt to infer fall dst-transition hours based on order. Requires that the timestamps are monotonically increasing.
    
*   bool-ndarray where True signifies a DST time, False signifies a non-DST time (note that this flag is only applicable for ambiguous times)
    
*   ‘NaT’ will return NaT where there are ambiguous times
    
*   ‘raise’ will raise a ValueError if there are ambiguous times.
    

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

Returns:

Same type as self

Array/Index converted to the specified time zone.

Raises:

TypeError

If the Datetime Array/Index is tz-aware and tz is not None.

See also

[`DatetimeIndex.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "pandas.DatetimeIndex.tz_convert")

Convert tz-aware DatetimeIndex from one time zone to another.

Examples

\>>> tz\_naive \= pd.date\_range('2018-03-01 09:00', periods\=3)
\>>> tz\_naive
DatetimeIndex(\['2018-03-01 09:00:00', '2018-03-02 09:00:00',\
               '2018-03-03 09:00:00'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Localize DatetimeIndex in US/Eastern time zone:

\>>> tz\_aware \= tz\_naive.tz\_localize(tz\='US/Eastern')
\>>> tz\_aware
DatetimeIndex(\['2018-03-01 09:00:00-05:00', '2018-03-02 09:00:00-05:00',\
               '2018-03-03 09:00:00-05:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq='D')

Copy to clipboard

With `tz=None` we can remove the time zone information while preserving the wall time (no conversion to UTC):

\>>> tz\_aware.tz\_localize(None)
DatetimeIndex(\['2018-03-01 09:00:00', '2018-03-02 09:00:00',\
               '2018-03-03 09:00:00'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Be careful with DST changes. When there is sequential data, pandas can infer the DST time:

\>>> s \= pd.to\_datetime(pd.Series(\['2018-10-28 01:30:00',\
...                               '2018-10-28 02:00:00',\
...                               '2018-10-28 02:30:00',\
...                               '2018-10-28 02:00:00',\
...                               '2018-10-28 02:30:00',\
...                               '2018-10-28 03:00:00',\
...                               '2018-10-28 03:30:00'\]))
\>>> s.dt.tz\_localize('CET', ambiguous\='infer')
0   2018-10-28 01:30:00+02:00
1   2018-10-28 02:00:00+02:00
2   2018-10-28 02:30:00+02:00
3   2018-10-28 02:00:00+01:00
4   2018-10-28 02:30:00+01:00
5   2018-10-28 03:00:00+01:00
6   2018-10-28 03:30:00+01:00
dtype: datetime64\[us, CET\]

Copy to clipboard

In some cases, inferring the DST is impossible. In such cases, you can pass an ndarray to the ambiguous parameter to set the DST explicitly

\>>> s \= pd.to\_datetime(pd.Series(\['2018-10-28 01:20:00',\
...                               '2018-10-28 02:36:00',\
...                               '2018-10-28 03:46:00'\]))
\>>> s.dt.tz\_localize('CET', ambiguous\=np.array(\[True, True, False\]))
0   2018-10-28 01:20:00+02:00
1   2018-10-28 02:36:00+02:00
2   2018-10-28 03:46:00+01:00
dtype: datetime64\[us, CET\]

Copy to clipboard

If the DST transition causes nonexistent times, you can shift these dates forward or backwards with a timedelta object or ‘shift\_forward’ or ‘shift\_backward’.

\>>> s \= pd.to\_datetime(pd.Series(\['2015-03-29 02:30:00',\
...                               '2015-03-29 03:30:00'\], dtype\="M8\[ns\]"))
\>>> s.dt.tz\_localize('Europe/Warsaw', nonexistent\='shift\_forward')
0   2015-03-29 03:00:00+02:00
1   2015-03-29 03:30:00+02:00
dtype: datetime64\[ns, Europe/Warsaw\]

Copy to clipboard

\>>> s.dt.tz\_localize('Europe/Warsaw', nonexistent\='shift\_backward')
0   2015-03-29 01:59:59.999999999+01:00
1   2015-03-29 03:30:00.000000000+02:00
dtype: datetime64\[ns, Europe/Warsaw\]

Copy to clipboard

\>>> s.dt.tz\_localize('Europe/Warsaw', nonexistent\=pd.Timedelta('1h'))
0   2015-03-29 03:30:00+02:00
1   2015-03-29 03:30:00+02:00
dtype: datetime64\[ns, Europe/Warsaw\]

Copy to clipboard

On this page