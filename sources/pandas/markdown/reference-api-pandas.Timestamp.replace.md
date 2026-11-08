[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.replace.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.replace.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.replace.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.replace.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.replace.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.replace.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.replace.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.replace.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.replace.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.replace.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.replace.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.replace.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.replace[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html#pandas-timestamp-replace "Link to this heading")

========================================================================================================================================================

Timestamp.replace(_year\=None_, _month\=None_, _day\=None_, _hour\=None_, _minute\=None_, _second\=None_, _microsecond\=None_, _nanosecond\=None_, _tzinfo\=<class 'object'>_, _fold\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html#pandas.Timestamp.replace "Link to this definition")

Implements datetime.replace, handles nanoseconds.

This method creates a new Timestamp object by replacing the specified fields with new values. The new Timestamp retains the original fields that are not explicitly replaced. This method handles nanoseconds, and the tzinfo parameter allows for timezone replacement without conversion.

Parameters:

**year**int, optional

The year to replace. If None, the year is not changed.

**month**int, optional

The month to replace. If None, the month is not changed.

**day**int, optional

The day to replace. If None, the day is not changed.

**hour**int, optional

The hour to replace. If None, the hour is not changed.

**minute**int, optional

The minute to replace. If None, the minute is not changed.

**second**int, optional

The second to replace. If None, the second is not changed.

**microsecond**int, optional

The microsecond to replace. If None, the microsecond is not changed.

**nanosecond**int, optional

The nanosecond to replace. If None, the nanosecond is not changed.

**tzinfo**tz-convertible, optional

The timezone information to replace. If None, the timezone is not changed.

**fold**int, optional

The fold information to replace. If None, the fold is not changed.

Returns:

Timestamp

A new Timestamp object with the specified fields replaced.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Converts various types of data to datetime.

Notes

The replace method does not perform timezone conversions. If you need to convert the timezone, use the tz\_convert method instead.

Examples

Create a timestamp object:

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651', tz\='UTC')
\>>> ts
Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')

Copy to clipboard

Replace year and the hour:

\>>> ts.replace(year\=1999, hour\=10)
Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')

Copy to clipboard

Replace timezone (not a conversion):

\>>> import zoneinfo
\>>> ts.replace(tzinfo\=zoneinfo.ZoneInfo('US/Pacific'))
Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.replace(tzinfo\=zoneinfo.ZoneInfo('US/Pacific'))
NaT

Copy to clipboard

On this page