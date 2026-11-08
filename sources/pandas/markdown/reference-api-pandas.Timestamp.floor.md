[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.floor[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas-timestamp-floor "Link to this heading")

==================================================================================================================================================

Timestamp.floor(_freq_, _ambiguous\='raise'_, _nonexistent\='raise'_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas.Timestamp.floor "Link to this definition")

Return a new Timestamp floored to this resolution.

This method rounds the Timestamp down to the nearest boundary of the given frequency. The result will never be later than the original Timestamp.

Parameters:

**freq**str or timedelta

Frequency string or timedelta value indicating the flooring resolution.

**ambiguous**bool or {‘raise’, ‘NaT’}, default ‘raise’

The behavior is as follows:

*   bool contains flags to determine if time is dst or not (note that this flag is only applicable for ambiguous fall dst dates).
    
*   ‘NaT’ will return NaT for an ambiguous time.
    
*   ‘raise’ will raise a ValueError for an ambiguous time.
    

**nonexistent**{‘raise’, ‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta}, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time.
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time.
    
*   ‘NaT’ will return NaT where there are nonexistent times.
    
*   timedelta objects will shift nonexistent times by the timedelta.
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

Raises:

ValueError if the freq cannot be converted.

See also

[`Timestamp.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html#pandas.Timestamp.ceil "pandas.Timestamp.ceil")

Round up a Timestamp to the specified resolution.

[`Timestamp.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html#pandas.Timestamp.round "pandas.Timestamp.round")

Round a Timestamp to the specified resolution.

[`Series.dt.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html#pandas.Series.dt.floor "pandas.Series.dt.floor")

Round down the datetime values in a Series.

Notes

If the Timestamp has a timezone, flooring will take place relative to the local (“wall”) time and re-localized to the same timezone. When flooring near daylight savings time, use `nonexistent` and `ambiguous` to control the re-localization behavior.

Examples

Create a timestamp object:

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')

Copy to clipboard

A timestamp can be floored using multiple frequency units:

\>>> ts.floor(freq\='h')  \# hour
Timestamp('2020-03-14 15:00:00')

Copy to clipboard

\>>> ts.floor(freq\='min')  \# minute
Timestamp('2020-03-14 15:32:00')

Copy to clipboard

\>>> ts.floor(freq\='s')  \# seconds
Timestamp('2020-03-14 15:32:52')

Copy to clipboard

\>>> ts.floor(freq\='ns')  \# nanoseconds
Timestamp('2020-03-14 15:32:52.192548651')

Copy to clipboard

`freq` can also be a multiple of a single unit, like ‘5min’ (i.e. 5 minutes):

\>>> ts.floor(freq\='5min')
Timestamp('2020-03-14 15:30:00')

Copy to clipboard

or a combination of multiple units, like ‘1h30min’ (i.e. 1 hour and 30 minutes):

\>>> ts.floor(freq\='1h30min')
Timestamp('2020-03-14 15:00:00')

Copy to clipboard

`freq` can also be a timedelta value:

\>>> ts.floor(freq\=pd.Timedelta('1h30min'))
Timestamp('2020-03-14 15:00:00')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.floor()
NaT

Copy to clipboard

When rounding near a daylight savings time transition, use `ambiguous` or `nonexistent` to control how the timestamp should be re-localized.

\>>> ts\_tz \= pd.Timestamp("2021-10-31 03:30:00").tz\_localize("Europe/Amsterdam")

Copy to clipboard

\>>> ts\_tz.floor("2h", ambiguous\=False)
Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')

Copy to clipboard

\>>> ts\_tz.floor("2h", ambiguous\=True)
Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')

Copy to clipboard

On this page