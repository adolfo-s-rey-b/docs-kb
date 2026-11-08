[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.tz\_localize[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas-timestamp-tz-localize "Link to this heading")

=====================================================================================================================================================================

Timestamp.tz\_localize(_tz_, _ambiguous\='raise'_, _nonexistent\='raise'_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "Link to this definition")

Attach or detach a time zone on a Timestamp.

This method does not shift the date/time values. It attaches a time zone to a tz-naive Timestamp, or detaches the time zone from a tz-aware Timestamp. In both cases the wall time is preserved.

Parameters:

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None

Time zone to attach to the tz-naive Timestamp; the wall time is preserved. `None` detaches the time zone from a tz-aware Timestamp, returning a tz-naive Timestamp with the same wall time.

**ambiguous**bool, ‘NaT’, default ‘raise’

When clocks moved backward due to DST, ambiguous times may arise. For example in Central European Time (UTC+01), when going from 03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC and at 01:30:00 UTC. In such a situation, the ambiguous parameter dictates how ambiguous times should be handled.

The behavior is as follows:

*   bool contains flags to determine if time is dst or not (note that this flag is only applicable for ambiguous fall dst dates).
    
*   ‘NaT’ will return NaT for an ambiguous time.
    
*   ‘raise’ will raise a ValueError for an ambiguous time.
    

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

The behavior is as follows:

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time.
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time.
    
*   ‘NaT’ will return NaT where there are nonexistent times.
    
*   timedelta objects will shift nonexistent times by the timedelta.
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

Returns:

**localized**Timestamp

Raises:

TypeError

If the Timestamp is tz-aware and tz is not None.

See also

[`Timestamp.tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo")

Returns the timezone information of the Timestamp.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

[`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")

Localize a DatetimeIndex to a specific time zone.

[`datetime.datetime.astimezone`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "(in Python v3.15)")

Convert a datetime object to another time zone.

Examples

Create a naive timestamp object:

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts
Timestamp('2020-03-14 15:32:52.192548651')

Copy to clipboard

Add ‘Europe/Stockholm’ as timezone:

\>>> ts.tz\_localize(tz\='Europe/Stockholm')
Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.tz\_localize()
NaT

Copy to clipboard

On this page