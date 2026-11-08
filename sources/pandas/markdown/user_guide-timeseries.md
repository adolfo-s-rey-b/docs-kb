[Skip to main content](https://pandas.pydata.org/docs/user_guide/timeseries.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/timeseries.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/timeseries.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/timeseries.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/timeseries.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/timeseries.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/timeseries.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/timeseries.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/timeseries.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/timeseries.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/timeseries.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/timeseries.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/timeseries.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/timeseries.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Time series / date functionality[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-series-date-functionality "Link to this heading")

=====================================================================================================================================================

pandas contains extensive capabilities and features for working with time series data for all domains. Using the NumPy `datetime64` and `timedelta64` dtypes, pandas has consolidated a large number of features from other Python libraries like `scikits.timeseries` as well as created a tremendous amount of new functionality for manipulating time series data.

For example, pandas supports:

Parsing time series information from various sources and formats

In \[1\]: import datetime

In \[2\]: dti \= pd.to\_datetime(
   ...:    \["1/1/2018", np.datetime64("2018-01-01"), datetime.datetime(2018, 1, 1)\]
   ...: )
   ...: 

In \[3\]: dti
Out\[3\]: 
DatetimeIndex(\['2018-01-01', '2018-01-01', '2018-01-01'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Generate sequences of fixed-frequency dates and time spans

In \[4\]: dti \= pd.date\_range("2018-01-01", periods\=3, freq\="h")

In \[5\]: dti
Out\[5\]: 
DatetimeIndex(\['2018-01-01 00:00:00', '2018-01-01 01:00:00',\
               '2018-01-01 02:00:00'\],
              dtype='datetime64\[us\]', freq='h')

Copy to clipboard

Manipulating and converting date times with timezone information

In \[6\]: dti \= dti.tz\_localize("UTC")

In \[7\]: dti
Out\[7\]: 
DatetimeIndex(\['2018-01-01 00:00:00+00:00', '2018-01-01 01:00:00+00:00',\
               '2018-01-01 02:00:00+00:00'\],
              dtype='datetime64\[us, UTC\]', freq='h')

In \[8\]: dti.tz\_convert("US/Pacific")
Out\[8\]: 
DatetimeIndex(\['2017-12-31 16:00:00-08:00', '2017-12-31 17:00:00-08:00',\
               '2017-12-31 18:00:00-08:00'\],
              dtype='datetime64\[us, US/Pacific\]', freq='h')

Copy to clipboard

Resampling or converting a time series to a particular frequency

In \[9\]: idx \= pd.date\_range("2018-01-01", periods\=5, freq\="h")

In \[10\]: ts \= pd.Series(range(len(idx)), index\=idx)

In \[11\]: ts
Out\[11\]: 
2018-01-01 00:00:00    0
2018-01-01 01:00:00    1
2018-01-01 02:00:00    2
2018-01-01 03:00:00    3
2018-01-01 04:00:00    4
Freq: h, dtype: int64

In \[12\]: ts.resample("2h").mean()
Out\[12\]: 
2018-01-01 00:00:00    0.5
2018-01-01 02:00:00    2.5
2018-01-01 04:00:00    4.0
Freq: 2h, dtype: float64

Copy to clipboard

Performing date and time arithmetic with absolute or relative time increments

In \[13\]: friday \= pd.Timestamp("2018-01-05")

In \[14\]: friday.day\_name()
Out\[14\]: 'Friday'

\# Add 1 day
In \[15\]: saturday \= friday + pd.Timedelta("1 day")

In \[16\]: saturday.day\_name()
Out\[16\]: 'Saturday'

\# Add 1 business day (Friday --> Monday)
In \[17\]: monday \= friday + pd.offsets.BDay()

In \[18\]: monday.day\_name()
Out\[18\]: 'Monday'

Copy to clipboard

pandas provides a relatively compact and self-contained set of tools for performing the above tasks and more.

Overview[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#overview "Link to this heading")

-------------------------------------------------------------------------------------------------------

pandas captures 4 general time related concepts:

1.  Date times: A specific date and time with timezone support. Similar to `datetime.datetime` from the standard library.
    
2.  Time deltas: An absolute time duration. Similar to `datetime.timedelta` from the standard library.
    
3.  Time spans: A span of time defined by a point in time and its associated frequency.
    
4.  Date offsets: A relative time duration that respects calendar arithmetic. Similar to `dateutil.relativedelta.relativedelta` from the `dateutil` package.
    

| Concept | Scalar Class | Array Class | pandas Data Type | Primary Creation Method |
| --- | --- | --- | --- | --- |
| Date times | `Timestamp` | `DatetimeIndex` | `datetime64[us]` or `datetime64[us, tz]` | `to_datetime` or `date_range` |
| Time deltas | `Timedelta` | `TimedeltaIndex` | `timedelta64[us]` | `to_timedelta` or `timedelta_range` |
| Time spans | `Period` | `PeriodIndex` | `period[freq]` | `Period` or `period_range` |
| Date offsets | `DateOffset` | `None` | `None` | `DateOffset` |

The default resolution for date times and time deltas is microsecond (“us”), though second (“s”), millisecond (“ms”), and nanosecond (“ns”) are also supported. The resolution can be changed using [`as_unit()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit "pandas.Series.dt.as_unit")
. Arithmetic keeps the resolution of its operands, see [Timedelta arithmetic](https://pandas.pydata.org/docs/user_guide/timedeltas.html#timedeltas-unit-preserving-arithmetic)
.

For time series data, it’s conventional to represent the time component in the index of a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 so manipulations can be performed with respect to the time element.

In \[19\]: pd.Series(range(3), index\=pd.date\_range("2000", freq\="D", periods\=3))
Out\[19\]: 
2000-01-01    0
2000-01-02    1
2000-01-03    2
Freq: D, dtype: int64

Copy to clipboard

However, [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 can directly also support the time component as data itself.

In \[20\]: pd.Series(pd.date\_range("2000", freq\="D", periods\=3))
Out\[20\]: 
0   2000-01-01
1   2000-01-02
2   2000-01-03
dtype: datetime64\[us\]

Copy to clipboard

[`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 have extended data type support and functionality for `datetime`, `timedelta` and `Period` data when passed into those constructors. `DateOffset` data however will be stored as `object` data.

In \[21\]: pd.Series(pd.period\_range("1/1/2011", freq\="M", periods\=3))
Out\[21\]: 
0    2011-01
1    2011-02
2    2011-03
dtype: period\[M\]

In \[22\]: pd.Series(\[pd.DateOffset(1), pd.DateOffset(2)\])
Out\[22\]: 
0         <DateOffset>
1    <2 \* DateOffsets>
dtype: object

In \[23\]: pd.Series(pd.date\_range("1/1/2011", freq\="ME", periods\=3))
Out\[23\]: 
0   2011-01-31
1   2011-02-28
2   2011-03-31
dtype: datetime64\[us\]

Copy to clipboard

Lastly, pandas represents null date times, time deltas, and time spans as `NaT` which is useful for representing missing or null date like values and behaves similar as `np.nan` does for float data.

In \[24\]: pd.Timestamp(pd.NaT)
Out\[24\]: NaT

In \[25\]: pd.Timedelta(pd.NaT)
Out\[25\]: NaT

In \[26\]: pd.Period(pd.NaT)
Out\[26\]: NaT

\# Equality acts as np.nan would
In \[27\]: pd.NaT \== pd.NaT
Out\[27\]: False

Copy to clipboard

Timestamps vs. time spans[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#timestamps-vs-time-spans "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Timestamped data is the most basic type of time series data that associates values with points in time. For pandas objects it means using the points in time.

In \[28\]: import datetime

In \[29\]: pd.Timestamp(datetime.datetime(2012, 5, 1))
Out\[29\]: Timestamp('2012-05-01 00:00:00')

In \[30\]: pd.Timestamp("2012-05-01")
Out\[30\]: Timestamp('2012-05-01 00:00:00')

In \[31\]: pd.Timestamp(2012, 5, 1)
Out\[31\]: Timestamp('2012-05-01 00:00:00')

Copy to clipboard

However, in many cases it is more natural to associate things like change variables with a time span instead. The span represented by `Period` can be specified explicitly, or inferred from datetime string format.

For example:

In \[32\]: pd.Period("2011-01")
Out\[32\]: Period('2011-01', 'M')

In \[33\]: pd.Period("2012-05", freq\="D")
Out\[33\]: Period('2012-05-01', 'D')

Copy to clipboard

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 and [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 can serve as an index. Lists of `Timestamp` and `Period` are automatically coerced to [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 and [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")
 respectively.

In \[34\]: dates \= \[\
   ....:    pd.Timestamp("2012-05-01"),\
   ....:    pd.Timestamp("2012-05-02"),\
   ....:    pd.Timestamp("2012-05-03"),\
   ....: \]
   ....: 

In \[35\]: ts \= pd.Series(np.random.randn(3), dates)

In \[36\]: type(ts.index)
Out\[36\]: pandas.DatetimeIndex

In \[37\]: ts.index
Out\[37\]: 
DatetimeIndex(\['2012-05-01', '2012-05-02', '2012-05-03'\],
              dtype='datetime64\[us\]', freq=None)

In \[38\]: ts
Out\[38\]: 
2012-05-01    0.469112
2012-05-02   -0.282863
2012-05-03   -1.509059
dtype: float64

In \[39\]: periods \= \[pd.Period("2012-01"), pd.Period("2012-02"), pd.Period("2012-03")\]

In \[40\]: ts \= pd.Series(np.random.randn(3), periods)

In \[41\]: type(ts.index)
Out\[41\]: pandas.PeriodIndex

In \[42\]: ts.index
Out\[42\]: PeriodIndex(\['2012-01', '2012-02', '2012-03'\], dtype='period\[M\]')

In \[43\]: ts
Out\[43\]: 
2012-01   -1.135632
2012-02    1.212112
2012-03   -0.173215
Freq: M, dtype: float64

Copy to clipboard

pandas allows you to capture both representations and convert between them. Under the hood, pandas represents timestamps using instances of `Timestamp` and sequences of timestamps using instances of `DatetimeIndex`. For regular time spans, pandas uses `Period` objects for scalar values and `PeriodIndex` for sequences of spans.

Converting to timestamps[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

To convert a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or list-like object of date-like objects e.g. strings, epochs, or a mixture, you can use the `to_datetime` function. When passed a `Series`, this returns a `Series` (with the same index), while a list-like is converted to a `DatetimeIndex`:

In \[44\]: pd.to\_datetime(pd.Series(\["Jul 31, 2009", "Jan 10, 2010", None\]))
Out\[44\]: 
0   2009-07-31
1   2010-01-10
2          NaT
dtype: datetime64\[us\]

In \[45\]: pd.to\_datetime(\["2005/11/23", "2010/12/31"\])
Out\[45\]: DatetimeIndex(\['2005-11-23', '2010-12-31'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

If you use dates which start with the day first (i.e. European style), you can pass the `dayfirst` flag:

In \[46\]: pd.to\_datetime(\["04-01-2012 10:00"\], dayfirst\=True)
Out\[46\]: DatetimeIndex(\['2012-01-04 10:00:00'\], dtype='datetime64\[us\]', freq=None)

In \[47\]: pd.to\_datetime(\["04-14-2012 10:00"\], dayfirst\=True)
Out\[47\]: DatetimeIndex(\['2012-04-14 10:00:00'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Warning

You see in the above example that `dayfirst` isn’t strict. If a date can’t be parsed with the day being first it will be parsed as if `dayfirst` were `False` and a warning will also be raised.

If you pass a single string to `to_datetime`, it returns a single `Timestamp`. `Timestamp` can also accept string input, but it doesn’t accept string parsing options like `dayfirst` or `format`, so use `to_datetime` if these are required.

In \[48\]: pd.to\_datetime("2010/11/12")
Out\[48\]: Timestamp('2010-11-12 00:00:00')

In \[49\]: pd.Timestamp("2010/11/12")
Out\[49\]: Timestamp('2010-11-12 00:00:00')

Copy to clipboard

You can also use the `DatetimeIndex` constructor directly:

In \[50\]: pd.DatetimeIndex(\["2018-01-01", "2018-01-03", "2018-01-05"\])
Out\[50\]: 
DatetimeIndex(\['2018-01-01', '2018-01-03', '2018-01-05'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

The string ‘infer’ can be passed in order to set the frequency of the index as the inferred frequency upon creation:

In \[51\]: pd.DatetimeIndex(\["2018-01-01", "2018-01-03", "2018-01-05"\], freq\="infer")
Out\[51\]: 
DatetimeIndex(\['2018-01-01', '2018-01-03', '2018-01-05'\],
              dtype='datetime64\[us\]', freq='2D')

Copy to clipboard

In most cases, parsing strings to datetimes (with any of [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
, [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
, or [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
) will produce objects with microsecond (“us”) unit. The exception to this rule is if your strings have nanosecond precision, in which case the result will have “ns” unit:

In \[52\]: pd.to\_datetime(\["2016-01-01 02:03:04"\]).unit
Out\[52\]: 'us'

In \[53\]: pd.to\_datetime(\["2016-01-01 02:03:04.123"\]).unit
Out\[53\]: 'us'

In \[54\]: pd.to\_datetime(\["2016-01-01 02:03:04.123456"\]).unit
Out\[54\]: 'us'

In \[55\]: pd.to\_datetime(\["2016-01-01 02:03:04.123456789"\]).unit
Out\[55\]: 'ns'

Copy to clipboard

Changed in version 3.0.0: Previously, [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
 and [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 would always parse strings to “ns” unit. During pandas 2.x, [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 could give any of “s”, “ms”, “us”, or “ns” depending on the specificity of the input string.

### Providing a format argument[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#providing-a-format-argument "Link to this heading")

In addition to the required datetime string, a `format` argument can be passed to ensure specific parsing. This could also potentially speed up the conversion considerably.

In \[56\]: pd.to\_datetime("2010/11/12", format\="%Y/%m/%d")
Out\[56\]: Timestamp('2010-11-12 00:00:00')

In \[57\]: pd.to\_datetime("12-11-2010 00:00", format\="%d\-%m-%Y %H:%M")
Out\[57\]: Timestamp('2010-11-12 00:00:00')

Copy to clipboard

For more information on the choices available when specifying the `format` option, see the Python [datetime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
.

### Assembling datetime from multiple DataFrame columns[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#assembling-datetime-from-multiple-dataframe-columns "Link to this heading")

You can also pass a `DataFrame` of integer or string columns to assemble into a `Series` of `Timestamps`.

In \[58\]: df \= pd.DataFrame(
   ....:    {"year": \[2015, 2016\], "month": \[2, 3\], "day": \[4, 5\], "hour": \[2, 3\]}
   ....: )
   ....: 

In \[59\]: pd.to\_datetime(df)
Out\[59\]: 
0   2015-02-04 02:00:00
1   2016-03-05 03:00:00
dtype: datetime64\[us\]

Copy to clipboard

You can pass only the columns that you need to assemble.

In \[60\]: pd.to\_datetime(df\[\["year", "month", "day"\]\])
Out\[60\]: 
0   2015-02-04
1   2016-03-05
dtype: datetime64\[us\]

Copy to clipboard

`pd.to_datetime` looks for standard designations of the datetime component in the column names, including:

*   required: `year`, `month`, `day`
    
*   optional: `hour`, `minute`, `second`, `millisecond`, `microsecond`, `nanosecond`
    

### Invalid data[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#invalid-data "Link to this heading")

The default behavior, `errors='raise'`, is to raise when unparsable:

In \[61\]: pd.to\_datetime(\['2009/07/31', 'asd'\], errors\='raise')
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[61\], line 1
\----> 1 pd.to\_datetime(\['2009/07/31', 'asd'\], errors\='raise')

File ~/work/pandas/pandas/pandas/core/tools/datetimes.py:1271, in to\_datetime(arg, errors, dayfirst, yearfirst, utc, format, exact, unit, origin, cache)
   1269         result \= \_convert\_and\_box\_cache(argc, cache\_array)
   1270     else:
\-> 1271         result \= convert\_listlike(argc, format)
   1272 else:
   1273     result \= convert\_listlike(np.array(\[arg\]), format)\[0\]

File ~/work/pandas/pandas/pandas/core/tools/datetimes.py:484, in \_convert\_listlike\_datetimes(arg, format, name, utc, unit, errors, dayfirst, yearfirst, exact)
    482 \# \`format\` could be inferred, or user didn't ask for mixed-format parsing.
    483 if format is not None and format != "mixed":
\--> 484     return \_array\_strptime\_with\_fallback(arg, name, utc, format, exact, errors)
    486 result, tz\_parsed \= objects\_to\_datetime64(
    487     arg,
    488     dayfirst\=dayfirst,
   (...)    491     errors\=errors,
    492 )
    494 if tz\_parsed is not None:
    495     \# We can take a shortcut since the datetime64 numpy array
    496     \# is in UTC

File ~/work/pandas/pandas/pandas/core/tools/datetimes.py:518, in \_array\_strptime\_with\_fallback(arg, name, utc, fmt, exact, errors)
    507 def \_array\_strptime\_with\_fallback(
    508     arg,
    509     name,
   (...)    513     errors: str,
    514 ) \-> Index:
    515     """
    516     Call array\_strptime, with fallback behavior depending on 'errors'.
    517     """
\--> 518     result, tz\_out \= array\_strptime(arg, fmt, exact\=exact, errors\=errors, utc\=utc)
    519     if tz\_out is not None:
    520         unit \= np.datetime\_data(result.dtype)\[0\]

File pandas/\_libs/tslibs/strptime.pyx:644, in pandas.\_libs.tslibs.strptime.array\_strptime()
\--> 644 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/strptime.pyx:561, in pandas.\_libs.tslibs.strptime.array\_strptime()
\--> 561 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/strptime.pyx:701, in pandas.\_libs.tslibs.strptime.\_parse\_with\_format()
\--> 701 'Could not get source, probably due dynamically evaluated source code.'
ValueError: time data "asd" doesn't match format "%Y/%m/%d". You might want to try:
    \- passing \`format\` if your strings have a consistent format;
    \- passing \`format\='ISO8601'\` if your strings are all ISO8601 but not necessarily in exactly the same format;
    \- passing \`format\='mixed'\`, and the format will be inferred for each element individually. You might want to use \`dayfirst\` alongside this.

Copy to clipboard

Pass `errors='coerce'` to convert unparsable data to `NaT` (not a time):

In \[62\]: pd.to\_datetime(\["2009/07/31", "asd"\], errors\="coerce")
Out\[62\]: DatetimeIndex(\['2009-07-31', 'NaT'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

### Epoch timestamps[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#epoch-timestamps "Link to this heading")

pandas supports converting integer or float epoch times to `Timestamp` and `DatetimeIndex`. The default unit is nanoseconds when no `unit` is specified. However, epochs are often stored in another `unit` which can be specified. These are computed from the starting point specified by the `origin` parameter.

In \[63\]: pd.to\_datetime(
   ....:    \[1349720105, 1349806505, 1349892905, 1349979305, 1350065705\], unit\="s"
   ....: )
   ....: 
Out\[63\]: 
DatetimeIndex(\['2012-10-08 18:15:05', '2012-10-09 18:15:05',\
               '2012-10-10 18:15:05', '2012-10-11 18:15:05',\
               '2012-10-12 18:15:05'\],
              dtype='datetime64\[us\]', freq=None)

In \[64\]: pd.to\_datetime(
   ....:    \[1349720105100, 1349720105200, 1349720105300, 1349720105400, 1349720105500\],
   ....:    unit\="ms",
   ....: )
   ....: 
Out\[64\]: 
DatetimeIndex(\['2012-10-08 18:15:05.100000', '2012-10-08 18:15:05.200000',\
               '2012-10-08 18:15:05.300000', '2012-10-08 18:15:05.400000',\
               '2012-10-08 18:15:05.500000'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Note

The `unit` parameter does not use the same strings as the `format` parameter that was discussed [above](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-converting-format)
. The available units are listed on the documentation for [`pandas.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
.

Constructing a [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 or [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 with an epoch timestamp with the `tz` argument specified will raise a ValueError. If you have epochs in wall time in another timezone, you can read the epochs as timezone-naive timestamps and then localize to the appropriate timezone:

In \[65\]: pd.Timestamp(1262347200000000000).tz\_localize("US/Pacific")
Out\[65\]: Timestamp('2010-01-01 12:00:00-0800', tz='US/Pacific')

In \[66\]: pd.DatetimeIndex(\[1262347200000000000\]).tz\_localize("US/Pacific")
Out\[66\]: 
DatetimeIndex(\['2010-01-01 12:00:00-08:00'\], dtype='datetime64\[ns, US/Pacific\]',
              freq=None)

Copy to clipboard

Note

Epoch times will be rounded to the nearest nanosecond.

Warning

Conversion of float epoch times can lead to inaccurate and unexpected results. [Python floats](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues "(in Python v3.15)")
 have about 15 digits precision in decimal. Rounding during conversion from float to high precision `Timestamp` is unavoidable. The only way to achieve exact precision is to use a fixed-width types (e.g. an int64).

In \[67\]: pd.to\_datetime(\[1490195805.433, 1490195805.433502912\], unit\="s")
Out\[67\]: 
DatetimeIndex(\['2017-03-22 15:16:45.433000088',\
               '2017-03-22 15:16:45.433502913'\],
              dtype='datetime64\[ns\]', freq=None)

In \[68\]: pd.to\_datetime(1490195805433502912, unit\="ns")
Out\[68\]: Timestamp('2017-03-22 15:16:45.433502912')

Copy to clipboard

See also

[Using the origin parameter](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-origin)

### From timestamps to epoch[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#from-timestamps-to-epoch "Link to this heading")

To invert the operation from above, namely, to convert from a `Timestamp` to a ‘unix’ epoch:

In \[69\]: stamps \= pd.date\_range("2012-10-08 18:15:05", periods\=4, freq\="D")

In \[70\]: stamps
Out\[70\]: 
DatetimeIndex(\['2012-10-08 18:15:05', '2012-10-09 18:15:05',\
               '2012-10-10 18:15:05', '2012-10-11 18:15:05'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

We subtract the epoch (midnight at January 1, 1970 UTC) and then floor divide by the “unit” (1 second).

In \[71\]: (stamps \- pd.Timestamp("1970-01-01")) // pd.Timedelta("1s")
Out\[71\]: Index(\[1349720105, 1349806505, 1349892905, 1349979305\], dtype='int64')

Copy to clipboard

Note

You may also see [`Timestamp.timestamp()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")
 used for this conversion. The explicit subtraction above is recommended because it is unambiguous about treating a timezone-naive value as UTC: [`Timestamp.timestamp()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")
 treats a naive `Timestamp` as UTC, which does _not_ match the standard library `datetime.datetime.timestamp`, where a naive value is interpreted as local time.

Another common way to perform this conversion is to convert directly to an integer dtype. Note that the exact integers this produces will depend on the specific unit or resolution of the datetime64 dtype:

In \[72\]: stamps.astype(np.int64)
Out\[72\]: 
Index(\[1349720105000000, 1349806505000000, 1349892905000000, 1349979305000000\],
      dtype='int64')

In \[73\]: stamps.as\_unit("s").astype(np.int64)
Out\[73\]: Index(\[1349720105, 1349806505, 1349892905, 1349979305\], dtype='int64')

In \[74\]: stamps.as\_unit("ns").astype(np.int64)
Out\[74\]: 
Index(\[1349720105000000000, 1349806505000000000, 1349892905000000000,\
       1349979305000000000\],
      dtype='int64')

Copy to clipboard

### Using the `origin` parameter[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#using-the-origin-parameter "Link to this heading")

Using the `origin` parameter, one can specify an alternative starting point for creation of a `DatetimeIndex`. For example, to use 1960-01-01 as the starting date:

In \[75\]: pd.to\_datetime(\[1, 2, 3\], unit\="D", origin\=pd.Timestamp("1960-01-01"))
Out\[75\]: 
DatetimeIndex(\['1960-01-02', '1960-01-03', '1960-01-04'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

The default is set at `origin='unix'`, which defaults to `1970-01-01 00:00:00`. Commonly called ‘unix epoch’ or POSIX time.

In \[76\]: pd.to\_datetime(\[1, 2, 3\], unit\="D")
Out\[76\]: 
DatetimeIndex(\['1970-01-02', '1970-01-03', '1970-01-04'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Generating ranges of timestamps[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#generating-ranges-of-timestamps "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

To generate an index with timestamps, you can use either the `DatetimeIndex` or `Index` constructor and pass in a list of datetime objects:

In \[77\]: dates \= \[\
   ....:    datetime.datetime(2012, 5, 1),\
   ....:    datetime.datetime(2012, 5, 2),\
   ....:    datetime.datetime(2012, 5, 3),\
   ....: \]
   ....: 

\# Note the frequency information
In \[78\]: index \= pd.DatetimeIndex(dates)

In \[79\]: index
Out\[79\]: 
DatetimeIndex(\['2012-05-01', '2012-05-02', '2012-05-03'\],
              dtype='datetime64\[us\]', freq=None)

\# Automatically converted to DatetimeIndex
In \[80\]: index \= pd.Index(dates)

In \[81\]: index
Out\[81\]: 
DatetimeIndex(\['2012-05-01', '2012-05-02', '2012-05-03'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

In practice this becomes very cumbersome because we often need a very long index with a large number of timestamps. If we need timestamps on a regular frequency, we can use the [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
 and [`bdate_range()`](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas.bdate_range "pandas.bdate_range")
 functions to create a `DatetimeIndex`. The default frequency for `date_range` is a **calendar day** while the default for `bdate_range` is a **business day**:

In \[82\]: start \= datetime.datetime(2011, 1, 1)

In \[83\]: end \= datetime.datetime(2012, 1, 1)

In \[84\]: index \= pd.date\_range(start, end)

In \[85\]: index
Out\[85\]: 
DatetimeIndex(\['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04',\
               '2011-01-05', '2011-01-06', '2011-01-07', '2011-01-08',\
               '2011-01-09', '2011-01-10',\
               ...\
               '2011-12-23', '2011-12-24', '2011-12-25', '2011-12-26',\
               '2011-12-27', '2011-12-28', '2011-12-29', '2011-12-30',\
               '2011-12-31', '2012-01-01'\],
              dtype='datetime64\[us\]', length=366, freq='D')

In \[86\]: index \= pd.bdate\_range(start, end)

In \[87\]: index
Out\[87\]: 
DatetimeIndex(\['2011-01-03', '2011-01-04', '2011-01-05', '2011-01-06',\
               '2011-01-07', '2011-01-10', '2011-01-11', '2011-01-12',\
               '2011-01-13', '2011-01-14',\
               ...\
               '2011-12-19', '2011-12-20', '2011-12-21', '2011-12-22',\
               '2011-12-23', '2011-12-26', '2011-12-27', '2011-12-28',\
               '2011-12-29', '2011-12-30'\],
              dtype='datetime64\[us\]', length=260, freq='B')

Copy to clipboard

Convenience functions like `date_range` and `bdate_range` can utilize a variety of [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
:

In \[88\]: pd.date\_range(start, periods\=1000, freq\="ME")
Out\[88\]: 
DatetimeIndex(\['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-30',\
               '2011-05-31', '2011-06-30', '2011-07-31', '2011-08-31',\
               '2011-09-30', '2011-10-31',\
               ...\
               '2093-07-31', '2093-08-31', '2093-09-30', '2093-10-31',\
               '2093-11-30', '2093-12-31', '2094-01-31', '2094-02-28',\
               '2094-03-31', '2094-04-30'\],
              dtype='datetime64\[us\]', length=1000, freq='ME')

In \[89\]: pd.bdate\_range(start, periods\=250, freq\="BQS")
Out\[89\]: 
DatetimeIndex(\['2011-01-03', '2011-04-01', '2011-07-01', '2011-10-03',\
               '2012-01-02', '2012-04-02', '2012-07-02', '2012-10-01',\
               '2013-01-01', '2013-04-01',\
               ...\
               '2071-01-01', '2071-04-01', '2071-07-01', '2071-10-01',\
               '2072-01-01', '2072-04-01', '2072-07-01', '2072-10-03',\
               '2073-01-02', '2073-04-03'\],
              dtype='datetime64\[us\]', length=250, freq='BQS-JAN')

Copy to clipboard

`date_range` and `bdate_range` make it easy to generate a range of dates using various combinations of parameters like `start`, `end`, `periods`, and `freq`. The start and end dates are strictly inclusive, so dates outside of those specified will not be generated:

In \[90\]: pd.date\_range(start, end, freq\="BME")
Out\[90\]: 
DatetimeIndex(\['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-29',\
               '2011-05-31', '2011-06-30', '2011-07-29', '2011-08-31',\
               '2011-09-30', '2011-10-31', '2011-11-30', '2011-12-30'\],
              dtype='datetime64\[us\]', freq='BME')

In \[91\]: pd.date\_range(start, end, freq\="W")
Out\[91\]: 
DatetimeIndex(\['2011-01-02', '2011-01-09', '2011-01-16', '2011-01-23',\
               '2011-01-30', '2011-02-06', '2011-02-13', '2011-02-20',\
               '2011-02-27', '2011-03-06', '2011-03-13', '2011-03-20',\
               '2011-03-27', '2011-04-03', '2011-04-10', '2011-04-17',\
               '2011-04-24', '2011-05-01', '2011-05-08', '2011-05-15',\
               '2011-05-22', '2011-05-29', '2011-06-05', '2011-06-12',\
               '2011-06-19', '2011-06-26', '2011-07-03', '2011-07-10',\
               '2011-07-17', '2011-07-24', '2011-07-31', '2011-08-07',\
               '2011-08-14', '2011-08-21', '2011-08-28', '2011-09-04',\
               '2011-09-11', '2011-09-18', '2011-09-25', '2011-10-02',\
               '2011-10-09', '2011-10-16', '2011-10-23', '2011-10-30',\
               '2011-11-06', '2011-11-13', '2011-11-20', '2011-11-27',\
               '2011-12-04', '2011-12-11', '2011-12-18', '2011-12-25',\
               '2012-01-01'\],
              dtype='datetime64\[us\]', freq='W-SUN')

In \[92\]: pd.bdate\_range(end\=end, periods\=20)
Out\[92\]: 
DatetimeIndex(\['2011-12-05', '2011-12-06', '2011-12-07', '2011-12-08',\
               '2011-12-09', '2011-12-12', '2011-12-13', '2011-12-14',\
               '2011-12-15', '2011-12-16', '2011-12-19', '2011-12-20',\
               '2011-12-21', '2011-12-22', '2011-12-23', '2011-12-26',\
               '2011-12-27', '2011-12-28', '2011-12-29', '2011-12-30'\],
              dtype='datetime64\[us\]', freq='B')

In \[93\]: pd.bdate\_range(start\=start, periods\=20)
Out\[93\]: 
DatetimeIndex(\['2011-01-03', '2011-01-04', '2011-01-05', '2011-01-06',\
               '2011-01-07', '2011-01-10', '2011-01-11', '2011-01-12',\
               '2011-01-13', '2011-01-14', '2011-01-17', '2011-01-18',\
               '2011-01-19', '2011-01-20', '2011-01-21', '2011-01-24',\
               '2011-01-25', '2011-01-26', '2011-01-27', '2011-01-28'\],
              dtype='datetime64\[us\]', freq='B')

Copy to clipboard

Specifying `start`, `end`, and `periods` will generate a range of evenly spaced dates from `start` to `end` inclusively, with `periods` number of elements in the resulting `DatetimeIndex`:

In \[94\]: pd.date\_range("2018-01-01", "2018-01-05", periods\=5)
Out\[94\]: 
DatetimeIndex(\['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',\
               '2018-01-05'\],
              dtype='datetime64\[us\]', freq=None)

In \[95\]: pd.date\_range("2018-01-01", "2018-01-05", periods\=10)
Out\[95\]: 
DatetimeIndex(\['2018-01-01 00:00:00', '2018-01-01 10:40:00',\
               '2018-01-01 21:20:00', '2018-01-02 08:00:00',\
               '2018-01-02 18:40:00', '2018-01-03 05:20:00',\
               '2018-01-03 16:00:00', '2018-01-04 02:40:00',\
               '2018-01-04 13:20:00', '2018-01-05 00:00:00'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

### Custom frequency ranges[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#custom-frequency-ranges "Link to this heading")

`bdate_range` can also generate a range of custom frequency dates by using the `weekmask` and `holidays` parameters. These parameters will only be used if a custom frequency string is passed.

In \[96\]: weekmask \= "Mon Wed Fri"

In \[97\]: holidays \= \[datetime.datetime(2011, 1, 5), datetime.datetime(2011, 3, 14)\]

In \[98\]: pd.bdate\_range(start, end, freq\="C", weekmask\=weekmask, holidays\=holidays)
Out\[98\]: 
DatetimeIndex(\['2011-01-03', '2011-01-07', '2011-01-10', '2011-01-12',\
               '2011-01-14', '2011-01-17', '2011-01-19', '2011-01-21',\
               '2011-01-24', '2011-01-26',\
               ...\
               '2011-12-09', '2011-12-12', '2011-12-14', '2011-12-16',\
               '2011-12-19', '2011-12-21', '2011-12-23', '2011-12-26',\
               '2011-12-28', '2011-12-30'\],
              dtype='datetime64\[us\]', length=154, freq='C')

In \[99\]: pd.bdate\_range(start, end, freq\="CBMS", weekmask\=weekmask)
Out\[99\]: 
DatetimeIndex(\['2011-01-03', '2011-02-02', '2011-03-02', '2011-04-01',\
               '2011-05-02', '2011-06-01', '2011-07-01', '2011-08-01',\
               '2011-09-02', '2011-10-03', '2011-11-02', '2011-12-02'\],
              dtype='datetime64\[us\]', freq='CBMS')

Copy to clipboard

See also

[Custom business days](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-custombusinessdays)

Timestamp limitations[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#timestamp-limitations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 uses a 64-bit integer to represent time, so the representable range depends on the chosen resolution (`unit`). For the default nanosecond resolution the span is limited to approximately 584 years; coarser resolutions such as second extend the range to roughly `+/- 2.9e11` years.

The class-level attributes [`Timestamp.min`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.min.html#pandas.Timestamp.min "pandas.Timestamp.min")
, [`Timestamp.max`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.max.html#pandas.Timestamp.max "pandas.Timestamp.max")
, and [`Timestamp.resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.resolution.html#pandas.Timestamp.resolution "pandas.Timestamp.resolution")
 default to nanosecond limits:

In \[100\]: pd.Timestamp.min
Out\[100\]: Timestamp('1677-09-21 00:12:43.145224193')

In \[101\]: pd.Timestamp.max
Out\[101\]: Timestamp('2262-04-11 23:47:16.854775807')

In \[102\]: pd.Timestamp.resolution
Out\[102\]: Timedelta('0 days 00:00:00.000000001')

Copy to clipboard

On a [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 _instance_, the same attributes reflect the bounds and step size of that instance’s resolution:

In \[103\]: ts \= pd.Timestamp("2262-04-12").as\_unit("s")

In \[104\]: ts.min
Out\[104\]: Timestamp('-292277022657-01-27 08:29:53')

In \[105\]: ts.max
Out\[105\]: Timestamp('292277026596-12-04 15:30:07')

In \[106\]: ts.resolution
Out\[106\]: Timedelta('0 days 00:00:01')

Copy to clipboard

Because [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 construction automatically picks a resolution wide enough to represent the input, a value outside the nanosecond range (such as `"3000-06-10"`) is parsed using a coarser unit rather than raising `OutOfBoundsDatetime`:

In \[107\]: far\_future \= pd.Timestamp("3000-06-10")

In \[108\]: far\_future
Out\[108\]: Timestamp('3000-06-10 00:00:00')

In \[109\]: far\_future.unit
Out\[109\]: 'us'

Copy to clipboard

Different resolutions can be converted to each other through [`Timestamp.as_unit()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "pandas.Timestamp.as_unit")
.

See also

[Representing out-of-bounds spans](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-oob)

Indexing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#indexing "Link to this heading")

-------------------------------------------------------------------------------------------------------

One of the main uses for `DatetimeIndex` is as an index for pandas objects. The `DatetimeIndex` class contains many time series related optimizations:

*   A large range of dates for various offsets are pre-computed and cached under the hood in order to make generating subsequent date ranges very fast (just have to grab a slice).
    
*   Fast shifting using the `shift` method on pandas objects.
    
*   Unioning of overlapping `DatetimeIndex` objects with the same frequency is very fast (important for fast data alignment).
    
*   Quick access to date fields via properties such as `year`, `month`, etc.
    
*   Regularization functions like `snap` and very fast `asof` logic.
    

`DatetimeIndex` objects have all the basic functionality of regular `Index` objects, and a smorgasbord of advanced time series specific methods for easy frequency processing.

See also

[Reindexing methods](https://pandas.pydata.org/docs/user_guide/basics.html#basics-reindexing)

Note

While pandas does not force you to have a sorted date index, some of these methods may have unexpected or incorrect behavior if the dates are unsorted.

`DatetimeIndex` can be used like a regular index and offers all of its intelligent functionality like selection, slicing, etc.

In \[110\]: rng \= pd.date\_range(start, end, freq\="BME")

In \[111\]: ts \= pd.Series(np.random.randn(len(rng)), index\=rng)

In \[112\]: ts.index
Out\[112\]: 
DatetimeIndex(\['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-29',\
               '2011-05-31', '2011-06-30', '2011-07-29', '2011-08-31',\
               '2011-09-30', '2011-10-31', '2011-11-30', '2011-12-30'\],
              dtype='datetime64\[us\]', freq='BME')

In \[113\]: ts\[:5\].index
Out\[113\]: 
DatetimeIndex(\['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-29',\
               '2011-05-31'\],
              dtype='datetime64\[us\]', freq='BME')

In \[114\]: ts\[::2\].index
Out\[114\]: 
DatetimeIndex(\['2011-01-31', '2011-03-31', '2011-05-31', '2011-07-29',\
               '2011-09-30', '2011-11-30'\],
              dtype='datetime64\[us\]', freq='2BME')

Copy to clipboard

### Partial string indexing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing "Link to this heading")

Dates and strings that parse to timestamps can be passed as indexing parameters:

In \[115\]: ts\["1/31/2011"\]
Out\[115\]: np.float64(0.11920871129693428)

In \[116\]: ts\[datetime.datetime(2011, 12, 25):\]
Out\[116\]: 
2011-12-30    0.56702
Freq: BME, dtype: float64

In \[117\]: ts\["10/31/2011":"12/31/2011"\]
Out\[117\]: 
2011-10-31    0.271860
2011-11-30   -0.424972
2011-12-30    0.567020
Freq: BME, dtype: float64

Copy to clipboard

To provide convenience for accessing longer time series, you can also pass in the year or year and month as strings:

In \[118\]: ts\["2011"\]
Out\[118\]: 
2011-01-31    0.119209
2011-02-28   -1.044236
2011-03-31   -0.861849
2011-04-29   -2.104569
2011-05-31   -0.494929
2011-06-30    1.071804
2011-07-29    0.721555
2011-08-31   -0.706771
2011-09-30   -1.039575
2011-10-31    0.271860
2011-11-30   -0.424972
2011-12-30    0.567020
Freq: BME, dtype: float64

In \[119\]: ts\["2011-6"\]
Out\[119\]: 
2011-06-30    1.071804
Freq: BME, dtype: float64

Copy to clipboard

This type of slicing will work on a `DataFrame` with a `DatetimeIndex` as well. Since the partial string selection is a form of label slicing, the endpoints **will be** included. This would include matching times on an included date:

Note

Indexing `DataFrame` rows with a _single_ string with getitem (e.g. `frame[dtstring]`) is no longer supported. Use `.loc` instead (e.g. `frame.loc[dtstring]`).

In \[120\]: dft \= pd.DataFrame(
   .....:    np.random.randn(100000, 1),
   .....:    columns\=\["A"\],
   .....:    index\=pd.date\_range("20130101", periods\=100000, freq\="min"),
   .....: )
   .....: 

In \[121\]: dft
Out\[121\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-03-11 10:35:00 -0.747967
2013-03-11 10:36:00 -0.034523
2013-03-11 10:37:00 -0.201754
2013-03-11 10:38:00 -1.509067
2013-03-11 10:39:00 -1.693043

\[100000 rows x 1 columns\]

In \[122\]: dft.loc\["2013"\]
Out\[122\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-03-11 10:35:00 -0.747967
2013-03-11 10:36:00 -0.034523
2013-03-11 10:37:00 -0.201754
2013-03-11 10:38:00 -1.509067
2013-03-11 10:39:00 -1.693043

\[100000 rows x 1 columns\]

Copy to clipboard

This starts on the very first time in the month, and includes the last date and time for the month:

In \[123\]: dft\["2013-1":"2013-2"\]
Out\[123\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-02-28 23:55:00  0.850929
2013-02-28 23:56:00  0.976712
2013-02-28 23:57:00 -2.693884
2013-02-28 23:58:00 -1.575535
2013-02-28 23:59:00 -1.573517

\[84960 rows x 1 columns\]

Copy to clipboard

This specifies a stop time **that includes all of the times on the last day**:

In \[124\]: dft\["2013-1":"2013-2-28"\]
Out\[124\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-02-28 23:55:00  0.850929
2013-02-28 23:56:00  0.976712
2013-02-28 23:57:00 -2.693884
2013-02-28 23:58:00 -1.575535
2013-02-28 23:59:00 -1.573517

\[84960 rows x 1 columns\]

Copy to clipboard

This specifies an **exact** stop time (and is not the same as the above):

In \[125\]: dft\["2013-1":"2013-2-28 00:00:00"\]
Out\[125\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-02-27 23:56:00  1.197749
2013-02-27 23:57:00  0.720521
2013-02-27 23:58:00 -0.072718
2013-02-27 23:59:00 -0.681192
2013-02-28 00:00:00 -0.557501

\[83521 rows x 1 columns\]

Copy to clipboard

We are stopping on the included end-point as it is part of the index:

In \[126\]: dft\["2013-1-15":"2013-1-15 12:30:00"\]
Out\[126\]: 
                            A
2013-01-15 00:00:00 -0.984810
2013-01-15 00:01:00  0.941451
2013-01-15 00:02:00  1.559365
2013-01-15 00:03:00  1.034374
2013-01-15 00:04:00 -1.480656
...                       ...
2013-01-15 12:26:00  0.371454
2013-01-15 12:27:00 -0.930806
2013-01-15 12:28:00 -0.069177
2013-01-15 12:29:00  0.066510
2013-01-15 12:30:00 -0.003945

\[751 rows x 1 columns\]

Copy to clipboard

`DatetimeIndex` partial string indexing also works on a `DataFrame` with a `MultiIndex`:

In \[127\]: dft2 \= pd.DataFrame(
   .....:    np.random.randn(20, 1),
   .....:    columns\=\["A"\],
   .....:    index\=pd.MultiIndex.from\_product(
   .....:        \[pd.date\_range("20130101", periods\=10, freq\="12h"), \["a", "b"\]\]
   .....:    ),
   .....: )
   .....: 

In \[128\]: dft2
Out\[128\]: 
                              A
2013-01-01 00:00:00 a -0.298694
                    b  0.823553
2013-01-01 12:00:00 a  0.943285
                    b -1.479399
2013-01-02 00:00:00 a -1.643342
...                         ...
2013-01-04 12:00:00 b  0.069036
2013-01-05 00:00:00 a  0.122297
                    b  1.422060
2013-01-05 12:00:00 a  0.370079
                    b  1.016331

\[20 rows x 1 columns\]

In \[129\]: dft2.loc\["2013-01-05"\]
Out\[129\]: 
                              A
2013-01-05 00:00:00 a  0.122297
                    b  1.422060
2013-01-05 12:00:00 a  0.370079
                    b  1.016331

In \[130\]: idx \= pd.IndexSlice

In \[131\]: dft2 \= dft2.swaplevel(0, 1).sort\_index()

In \[132\]: dft2.loc\[idx\[:, "2013-01-05"\], :\]
Out\[132\]: 
                              A
a 2013-01-05 00:00:00  0.122297
  2013-01-05 12:00:00  0.370079
b 2013-01-05 00:00:00  1.422060
  2013-01-05 12:00:00  1.016331

Copy to clipboard

Slicing with string indexing also honors UTC offset.

In \[133\]: df \= pd.DataFrame(\[0\], index\=pd.DatetimeIndex(\["2019-01-01"\], tz\="US/Pacific"))

In \[134\]: df
Out\[134\]: 
                           0
2019-01-01 00:00:00-08:00  0

In \[135\]: df\["2019-01-01 12:00:00+04:00":"2019-01-01 13:00:00+04:00"\]
Out\[135\]: 
                           0
2019-01-01 00:00:00-08:00  0

Copy to clipboard

### Slice vs. exact match[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#slice-vs-exact-match "Link to this heading")

The same string used as an indexing parameter can be treated either as a slice or as an exact match depending on the resolution of the index. If the string is less accurate than the index, it will be treated as a slice, otherwise as an exact match.

Consider a `Series` object with a minute resolution index:

In \[136\]: series\_minute \= pd.Series(
   .....:    \[1, 2, 3\],
   .....:    pd.DatetimeIndex(
   .....:        \["2011-12-31 23:59:00", "2012-01-01 00:00:00", "2012-01-01 00:02:00"\]
   .....:    ),
   .....: )
   .....: 

In \[137\]: series\_minute.index.resolution
Out\[137\]: 'minute'

Copy to clipboard

A timestamp string less accurate than a minute gives a `Series` object.

In \[138\]: series\_minute\["2011-12-31 23"\]
Out\[138\]: 
2011-12-31 23:59:00    1
dtype: int64

Copy to clipboard

A timestamp string with minute resolution (or more accurate), gives a scalar instead, i.e. it is not casted to a slice.

In \[139\]: series\_minute\["2011-12-31 23:59"\]
Out\[139\]: np.int64(1)

In \[140\]: series\_minute\["2011-12-31 23:59:00"\]
Out\[140\]: np.int64(1)

Copy to clipboard

If index resolution is second, then the minute-accurate timestamp gives a `Series`.

In \[141\]: series\_second \= pd.Series(
   .....:    \[1, 2, 3\],
   .....:    pd.DatetimeIndex(
   .....:        \["2011-12-31 23:59:59", "2012-01-01 00:00:00", "2012-01-01 00:00:01"\]
   .....:    ),
   .....: )
   .....: 

In \[142\]: series\_second.index.resolution
Out\[142\]: 'second'

In \[143\]: series\_second\["2011-12-31 23:59"\]
Out\[143\]: 
2011-12-31 23:59:59    1
dtype: int64

Copy to clipboard

If the timestamp string is treated as a slice, it can be used to index `DataFrame` with `.loc[]` as well.

In \[144\]: dft\_minute \= pd.DataFrame(
   .....:    {"a": \[1, 2, 3\], "b": \[4, 5, 6\]}, index\=series\_minute.index
   .....: )
   .....: 

In \[145\]: dft\_minute.loc\["2011-12-31 23"\]
Out\[145\]: 
                     a  b
2011-12-31 23:59:00  1  4

Copy to clipboard

Note

As [noted above](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-partialindexing)
, indexing `DataFrame` rows with a single string via `[]` is no longer supported; use `.loc` instead.

In \[146\]: dft\_minute.loc\["2011-12-31 23:59"\]
Out\[146\]: 
a    1
b    4
Name: 2011-12-31 23:59:00, dtype: int64

Copy to clipboard

Note also that `DatetimeIndex` resolution cannot be less precise than day.

In \[147\]: series\_monthly \= pd.Series(
   .....:    \[1, 2, 3\], pd.DatetimeIndex(\["2011-12", "2012-01", "2012-02"\])
   .....: )
   .....: 

In \[148\]: series\_monthly.index.resolution
Out\[148\]: 'day'

In \[149\]: series\_monthly\["2011-12"\]  \# returns Series
Out\[149\]: 
2011-12-01    1
dtype: int64

Copy to clipboard

### Exact indexing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#exact-indexing "Link to this heading")

As discussed in previous section, indexing a `DatetimeIndex` with a partial string depends on the “accuracy” of the period, in other words how specific the interval is in relation to the resolution of the index. In contrast, indexing with `Timestamp` or `datetime` objects is exact, because the objects have exact meaning. These also follow the semantics of _including both endpoints_.

These `Timestamp` and `datetime` objects have exact `hours, minutes,` and `seconds`, even though they were not explicitly specified (they are `0`).

In \[150\]: dft\[datetime.datetime(2013, 1, 1): datetime.datetime(2013, 2, 28)\]
Out\[150\]: 
                            A
2013-01-01 00:00:00  0.276232
2013-01-01 00:01:00 -1.087401
2013-01-01 00:02:00 -0.673690
2013-01-01 00:03:00  0.113648
2013-01-01 00:04:00 -1.478427
...                       ...
2013-02-27 23:56:00  1.197749
2013-02-27 23:57:00  0.720521
2013-02-27 23:58:00 -0.072718
2013-02-27 23:59:00 -0.681192
2013-02-28 00:00:00 -0.557501

\[83521 rows x 1 columns\]

Copy to clipboard

With no defaults.

In \[151\]: dft\[\
   .....:    datetime.datetime(2013, 1, 1, 10, 12, 0): datetime.datetime(\
   .....:        2013, 2, 28, 10, 12, 0\
   .....:    )\
   .....: \]
   .....: 
Out\[151\]: 
                            A
2013-01-01 10:12:00  0.565375
2013-01-01 10:13:00  0.068184
2013-01-01 10:14:00  0.788871
2013-01-01 10:15:00 -0.280343
2013-01-01 10:16:00  0.931536
...                       ...
2013-02-28 10:08:00  0.148098
2013-02-28 10:09:00 -0.388138
2013-02-28 10:10:00  0.139348
2013-02-28 10:11:00  0.085288
2013-02-28 10:12:00  0.950146

\[83521 rows x 1 columns\]

Copy to clipboard

### Non-inclusive slicing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#non-inclusive-slicing "Link to this heading")

As noted in the sections above, label-based slicing with a `DatetimeIndex` **includes both endpoints**. This differs from standard Python sequence slicing where the stop endpoint is excluded.

If you need to select data using open or half-open intervals (for example, `start < t < end` or `start <= t < end`), you can use boolean indexing:

In \[152\]: ts\_example \= pd.Series(
   .....:    range(5),
   .....:    index\=pd.date\_range("2000-01-01", periods\=5, freq\="D"),
   .....: )
   .....: 

In \[153\]: ts\_example
Out\[153\]: 
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
Freq: D, dtype: int64

Copy to clipboard

Select all entries strictly between `"2000-01-02"` and `"2000-01-04"` (excluding both endpoints):

In \[154\]: ts\_example\[(ts\_example.index \> "2000-01-02") & (ts\_example.index < "2000-01-04")\]
Out\[154\]: 
2000-01-03    2
Freq: D, dtype: int64

Copy to clipboard

Select entries with a half-open interval (include left, exclude right):

In \[155\]: ts\_example\[(ts\_example.index \>= "2000-01-02") & (ts\_example.index < "2000-01-04")\]
Out\[155\]: 
2000-01-02    1
2000-01-03    2
Freq: D, dtype: int64

Copy to clipboard

For large time series where boolean indexing may be less efficient, you can use [`get_slice_bound()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")
 together with `.iloc` to achieve non-inclusive slicing on a sorted index:

In \[156\]: lo \= ts\_example.index.get\_slice\_bound("2000-01-02", "right")

In \[157\]: hi \= ts\_example.index.get\_slice\_bound("2000-01-04", "left")

In \[158\]: ts\_example.iloc\[lo:hi\]
Out\[158\]: 
2000-01-03    2
Freq: D, dtype: int64

Copy to clipboard

Here, `side="right"` returns the position just past `"2000-01-02"`, and `side="left"` returns the position of `"2000-01-04"` itself. Since `.iloc` uses standard Python half-open slicing, the result excludes both endpoints.

### Selecting a time of day[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#selecting-a-time-of-day "Link to this heading")

Like [partial string indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-partialindexing)
, the methods [`at_time()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html#pandas.DataFrame.at_time "pandas.DataFrame.at_time")
 and [`between_time()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time "pandas.DataFrame.between_time")
 operate on the object’s index, selecting rows by their time of day regardless of the date. [`at_time()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html#pandas.DataFrame.at_time "pandas.DataFrame.at_time")
 selects all timestamps at a particular time:

In \[159\]: rng\_time \= pd.date\_range("2018-01-01", periods\=10, freq\="6h")

In \[160\]: ts\_time \= pd.Series(range(10), index\=rng\_time)

In \[161\]: ts\_time
Out\[161\]: 
2018-01-01 00:00:00    0
2018-01-01 06:00:00    1
2018-01-01 12:00:00    2
2018-01-01 18:00:00    3
2018-01-02 00:00:00    4
2018-01-02 06:00:00    5
2018-01-02 12:00:00    6
2018-01-02 18:00:00    7
2018-01-03 00:00:00    8
2018-01-03 06:00:00    9
Freq: 6h, dtype: int64

In \[162\]: ts\_time.at\_time("12:00")
Out\[162\]: 
2018-01-01 12:00:00    2
2018-01-02 12:00:00    6
Freq: 24h, dtype: int64

Copy to clipboard

[`between_time()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time "pandas.DataFrame.between_time")
 selects the rows whose time of day falls between two times, including both endpoints by default; the `inclusive` argument controls whether each endpoint is included:

In \[163\]: ts\_time.between\_time("00:00", "12:00")
Out\[163\]: 
2018-01-01 00:00:00    0
2018-01-01 06:00:00    1
2018-01-01 12:00:00    2
2018-01-02 00:00:00    4
2018-01-02 06:00:00    5
2018-01-02 12:00:00    6
2018-01-03 00:00:00    8
2018-01-03 06:00:00    9
dtype: int64

In \[164\]: ts\_time.between\_time("00:00", "12:00", inclusive\="left")
Out\[164\]: 
2018-01-01 00:00:00    0
2018-01-01 06:00:00    1
2018-01-02 00:00:00    4
2018-01-02 06:00:00    5
2018-01-03 00:00:00    8
2018-01-03 06:00:00    9
dtype: int64

Copy to clipboard

Both methods also accept `datetime.time` objects:

In \[165\]: import datetime

In \[166\]: ts\_time.at\_time(datetime.time(12, 0))
Out\[166\]: 
2018-01-01 12:00:00    2
2018-01-02 12:00:00    6
Freq: 24h, dtype: int64

Copy to clipboard

### Truncating & fancy indexing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#truncating-fancy-indexing "Link to this heading")

A [`truncate()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html#pandas.DataFrame.truncate "pandas.DataFrame.truncate")
 convenience function is provided that is similar to slicing. Note that `truncate` assumes a 0 value for any unspecified date component in a `DatetimeIndex` in contrast to slicing which returns any partially matching dates:

In \[167\]: rng2 \= pd.date\_range("2011-01-01", "2012-01-01", freq\="W")

In \[168\]: ts2 \= pd.Series(np.random.randn(len(rng2)), index\=rng2)

In \[169\]: ts2.truncate(before\="2011-11", after\="2011-12")
Out\[169\]: 
2011-11-06    0.437823
2011-11-13   -0.293083
2011-11-20   -0.059881
2011-11-27    1.252450
Freq: W-SUN, dtype: float64

In \[170\]: ts2\["2011-11":"2011-12"\]
Out\[170\]: 
2011-11-06    0.437823
2011-11-13   -0.293083
2011-11-20   -0.059881
2011-11-27    1.252450
2011-12-04    0.046611
2011-12-11    0.059478
2011-12-18   -0.286539
2011-12-25    0.841669
Freq: W-SUN, dtype: float64

Copy to clipboard

Even complicated fancy indexing that breaks the `DatetimeIndex` frequency regularity will result in a `DatetimeIndex`, although frequency is lost:

In \[171\]: ts2.iloc\[\[0, 2, 6\]\].index
Out\[171\]: 
DatetimeIndex(\['2011-01-02', '2011-01-16', '2011-02-13'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Time/date components[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-date-components "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

There are several time/date properties that one can access from `Timestamp` or a collection of timestamps like a `DatetimeIndex`.

 
| Property | Description |
| --- | --- |
| year | The year of the datetime |
| month | The month of the datetime |
| day | The days of the datetime |
| hour | The hour of the datetime |
| minute | The minutes of the datetime |
| second | The seconds of the datetime |
| microsecond | The microseconds of the datetime |
| nanosecond | The nanoseconds of the datetime |
| date | Returns datetime.date (does not contain timezone information) |
| time | Returns datetime.time (does not contain timezone information) |
| timetz | Returns datetime.time as local time with timezone information |
| dayofyear | The ordinal day of year |
| day\_of\_year | The ordinal day of year |
| dayofweek | The number of the day of the week with Monday=0, Sunday=6 |
| day\_of\_week | The number of the day of the week with Monday=0, Sunday=6 |
| weekday | The number of the day of the week with Monday=0, Sunday=6 |
| quarter | Quarter of the date: Jan-Mar = 1, Apr-Jun = 2, etc. |
| days\_in\_month | The number of days in the month of the datetime |
| is\_month\_start | Logical indicating if first day of month (defined by frequency) |
| is\_month\_end | Logical indicating if last day of month (defined by frequency) |
| is\_quarter\_start | Logical indicating if first day of quarter (defined by frequency) |
| is\_quarter\_end | Logical indicating if last day of quarter (defined by frequency) |
| is\_year\_start | Logical indicating if first day of year (defined by frequency) |
| is\_year\_end | Logical indicating if last day of year (defined by frequency) |
| is\_leap\_year | Logical indicating if the date belongs to a leap year |

Note

You can use `DatetimeIndex.isocalendar().week` to access week of year date information.

Furthermore, if you have a `Series` with datetimelike values, then you can access these properties via the `.dt` accessor, as detailed in the section on [.dt accessors](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dt-accessors)
.

You may obtain the year, week and day components of the ISO year from the ISO 8601 standard:

In \[172\]: idx \= pd.date\_range(start\="2019-12-29", freq\="D", periods\=4)

In \[173\]: idx.isocalendar()
Out\[173\]: 
            year  week  day
2019-12-29  2019    52    7
2019-12-30  2020     1    1
2019-12-31  2020     1    2
2020-01-01  2020     1    3

In \[174\]: idx.to\_series().dt.isocalendar()
Out\[174\]: 
            year  week  day
2019-12-29  2019    52    7
2019-12-30  2020     1    1
2019-12-31  2020     1    2
2020-01-01  2020     1    3

Copy to clipboard

DateOffset objects[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#dateoffset-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

In the preceding examples, frequency strings (e.g. `'D'`) were used to specify a frequency that defined:

*   how the date times in [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
     were spaced when using [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
    
*   the frequency of a [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
     or [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")
    

These frequency strings map to a [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 object and its subclasses. A [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 is similar to a [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 that represents a duration of time but follows specific calendar duration rules. For example, a [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 day will always increment `datetimes` by 24 hours, while a [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 day will increment `datetimes` to the same time the next day whether a day represents 23, 24 or 25 hours due to daylight savings time. However, all [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 subclasses that are an hour or smaller (`Hour`, `Minute`, `Second`, `Milli`, `Micro`, `Nano`) behave like [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 and respect absolute time.

The basic [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 acts similar to `dateutil.relativedelta` ([relativedelta documentation](https://dateutil.readthedocs.io/en/stable/relativedelta.html)
) that shifts a date time by the corresponding calendar duration specified. The arithmetic operator (`+`) can be used to perform the shift.

\# This particular day contains a day light savings time transition
In \[175\]: ts \= pd.Timestamp("2016-10-30 00:00:00", tz\="Europe/Helsinki")

\# Respects absolute time
In \[176\]: ts + pd.Timedelta(days\=1)
Out\[176\]: Timestamp('2016-10-30 23:00:00+0200', tz='Europe/Helsinki')

\# Respects calendar time
In \[177\]: ts + pd.DateOffset(days\=1)
Out\[177\]: Timestamp('2016-10-31 00:00:00+0200', tz='Europe/Helsinki')

In \[178\]: friday \= pd.Timestamp("2018-01-05")

In \[179\]: friday.day\_name()
Out\[179\]: 'Friday'

\# Add 2 business days (Friday --> Tuesday)
In \[180\]: two\_business\_days \= 2 \* pd.offsets.BDay()

In \[181\]: friday + two\_business\_days
Out\[181\]: Timestamp('2018-01-09 00:00:00')

In \[182\]: (friday + two\_business\_days).day\_name()
Out\[182\]: 'Tuesday'

Copy to clipboard

Most `DateOffsets` have associated frequencies strings, or offset aliases, that can be passed into `freq` keyword arguments. The available date offsets and associated frequency strings can be found below:

  
| Date Offset | Frequency String | Description |
| --- | --- | --- |
| [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset") | None | Generic offset class, defaults to absolute 24 hours |
| [`BDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BDay.html#pandas.tseries.offsets.BDay "pandas.tseries.offsets.BDay")<br> or [`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay") | `'B'` | business day (weekday) |
| [`CDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CDay.html#pandas.tseries.offsets.CDay "pandas.tseries.offsets.CDay")<br> or [`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "pandas.tseries.offsets.CustomBusinessDay") | `'C'` | custom business day |
| [`Week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas.tseries.offsets.Week "pandas.tseries.offsets.Week") | `'W'` | one week, optionally anchored on a day of the week (the anchor day is the last day of the weekly period) |
| [`WeekOfMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#pandas.tseries.offsets.WeekOfMonth "pandas.tseries.offsets.WeekOfMonth") | `'WOM'` | the x-th day of the y-th week of each month |
| [`LastWeekOfMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html#pandas.tseries.offsets.LastWeekOfMonth "pandas.tseries.offsets.LastWeekOfMonth") | `'LWOM'` | the x-th day of the last week of each month |
| [`MonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#pandas.tseries.offsets.MonthEnd "pandas.tseries.offsets.MonthEnd") | `'ME'` | calendar month end |
| [`MonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#pandas.tseries.offsets.MonthBegin "pandas.tseries.offsets.MonthBegin") | `'MS'` | calendar month begin |
| [`BMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthEnd.html#pandas.tseries.offsets.BMonthEnd "pandas.tseries.offsets.BMonthEnd")<br> or [`BusinessMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#pandas.tseries.offsets.BusinessMonthEnd "pandas.tseries.offsets.BusinessMonthEnd") | `'BME'` | business month end |
| [`BMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthBegin.html#pandas.tseries.offsets.BMonthBegin "pandas.tseries.offsets.BMonthBegin")<br> or [`BusinessMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#pandas.tseries.offsets.BusinessMonthBegin "pandas.tseries.offsets.BusinessMonthBegin") | `'BMS'` | business month begin |
| [`CBMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CBMonthEnd.html#pandas.tseries.offsets.CBMonthEnd "pandas.tseries.offsets.CBMonthEnd")<br> or [`CustomBusinessMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.html#pandas.tseries.offsets.CustomBusinessMonthEnd "pandas.tseries.offsets.CustomBusinessMonthEnd") | `'CBME'` | custom business month end |
| [`CBMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CBMonthBegin.html#pandas.tseries.offsets.CBMonthBegin "pandas.tseries.offsets.CBMonthBegin")<br> or [`CustomBusinessMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html#pandas.tseries.offsets.CustomBusinessMonthBegin "pandas.tseries.offsets.CustomBusinessMonthBegin") | `'CBMS'` | custom business month begin |
| [`SemiMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas.tseries.offsets.SemiMonthEnd "pandas.tseries.offsets.SemiMonthEnd") | `'SME'` | 15th (or other day\_of\_month) and calendar month end |
| [`SemiMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas.tseries.offsets.SemiMonthBegin "pandas.tseries.offsets.SemiMonthBegin") | `'SMS'` | 15th (or other day\_of\_month) and calendar month begin |
| [`QuarterEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterEnd.html#pandas.tseries.offsets.QuarterEnd "pandas.tseries.offsets.QuarterEnd") | `'QE'` | calendar quarter end |
| [`QuarterBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#pandas.tseries.offsets.QuarterBegin "pandas.tseries.offsets.QuarterBegin") | `'QS'` | calendar quarter begin |
| [`BQuarterEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.html#pandas.tseries.offsets.BQuarterEnd "pandas.tseries.offsets.BQuarterEnd") | `'BQE` | business quarter end |
| [`BQuarterBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.html#pandas.tseries.offsets.BQuarterBegin "pandas.tseries.offsets.BQuarterBegin") | `'BQS'` | business quarter begin |
| [`FY5253Quarter`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html#pandas.tseries.offsets.FY5253Quarter "pandas.tseries.offsets.FY5253Quarter") | `'REQ'` | retail (aka 52-53 week) quarter |
| [`HalfYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearEnd.html#pandas.tseries.offsets.HalfYearEnd "pandas.tseries.offsets.HalfYearEnd") | `'HYE'` | calendar half year end |
| [`HalfYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearBegin.html#pandas.tseries.offsets.HalfYearBegin "pandas.tseries.offsets.HalfYearBegin") | `'HYS'` | calendar half year begin |
| [`BHalfYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.html#pandas.tseries.offsets.BHalfYearEnd "pandas.tseries.offsets.BHalfYearEnd") | `'BHYE` | business half year end |
| [`BHalfYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.html#pandas.tseries.offsets.BHalfYearBegin "pandas.tseries.offsets.BHalfYearBegin") | `'BHYS'` | business half year begin |
| [`YearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearEnd.html#pandas.tseries.offsets.YearEnd "pandas.tseries.offsets.YearEnd") | `'YE'` | calendar year end |
| [`YearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#pandas.tseries.offsets.YearBegin "pandas.tseries.offsets.YearBegin") | `'YS'` or `'BYS'` | calendar year begin |
| [`BYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html#pandas.tseries.offsets.BYearEnd "pandas.tseries.offsets.BYearEnd") | `'BYE'` | business year end |
| [`BYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.html#pandas.tseries.offsets.BYearBegin "pandas.tseries.offsets.BYearBegin") | `'BYS'` | business year begin |
| [`FY5253`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#pandas.tseries.offsets.FY5253 "pandas.tseries.offsets.FY5253") | `'RE'` | retail (aka 52-53 week) year |
| [`Easter`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html#pandas.tseries.offsets.Easter "pandas.tseries.offsets.Easter") | None | Easter holiday |
| [`BusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas.tseries.offsets.BusinessHour "pandas.tseries.offsets.BusinessHour") | `'bh'` | business hour |
| [`CustomBusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas.tseries.offsets.CustomBusinessHour "pandas.tseries.offsets.CustomBusinessHour") | `'cbh'` | custom business hour |
| [`Day`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#pandas.tseries.offsets.Day "pandas.tseries.offsets.Day") | `'D'` | one calendar day |
| [`Hour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas.tseries.offsets.Hour "pandas.tseries.offsets.Hour") | `'h'` | one hour |
| [`Minute`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Minute.html#pandas.tseries.offsets.Minute "pandas.tseries.offsets.Minute") | `'min'` | one minute |
| [`Second`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas.tseries.offsets.Second "pandas.tseries.offsets.Second") | `'s'` | one second |
| [`Milli`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Milli.html#pandas.tseries.offsets.Milli "pandas.tseries.offsets.Milli") | `'ms'` | one millisecond |
| [`Micro`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Micro.html#pandas.tseries.offsets.Micro "pandas.tseries.offsets.Micro") | `'us'` | one microsecond |
| [`Nano`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Nano.html#pandas.tseries.offsets.Nano "pandas.tseries.offsets.Nano") | `'ns'` | one nanosecond |

`DateOffsets` additionally have `rollforward()` and `rollback()` methods for moving a date forward or backward respectively to a valid offset date relative to the offset. For example, business offsets will roll dates that land on the weekends (Saturday and Sunday) forward to Monday since business offsets operate on the weekdays.

In \[183\]: ts \= pd.Timestamp("2018-01-06 00:00:00")

In \[184\]: ts.day\_name()
Out\[184\]: 'Saturday'

\# BusinessHour's valid offset dates are Monday through Friday
In \[185\]: offset \= pd.offsets.BusinessHour(start\="09:00")

\# Bring the date to the closest offset date (Monday)
In \[186\]: offset.rollforward(ts)
Out\[186\]: Timestamp('2018-01-08 09:00:00')

\# Date is brought to the closest offset date first and then the hour is added
In \[187\]: ts + offset
Out\[187\]: Timestamp('2018-01-08 10:00:00')

Copy to clipboard

Both methods roll _conditionally_: a date that is already a valid offset date is returned unchanged, so `rollforward()` and `rollback()` give the same answer there. Use `is_on_offset()` to check whether a date is already valid, and add or subtract the offset to move unconditionally.

\# The last business day of July 2021, so already a valid BMonthEnd date
In \[188\]: ts \= pd.Timestamp("2021-07-30")

In \[189\]: offset \= pd.offsets.BMonthEnd()

In \[190\]: offset.is\_on\_offset(ts)
Out\[190\]: True

In \[191\]: offset.rollback(ts)
Out\[191\]: Timestamp('2021-07-30 00:00:00')

In \[192\]: offset.rollforward(ts)
Out\[192\]: Timestamp('2021-07-30 00:00:00')

\# Subtract the offset to always move to the previous business month end
In \[193\]: ts \- offset
Out\[193\]: Timestamp('2021-06-30 00:00:00')

Copy to clipboard

These operations preserve time (hour, minute, etc) information by default. To reset time to midnight, use `normalize()` before or after applying the operation (depending on whether you want the time information included in the operation).

In \[194\]: ts \= pd.Timestamp("2014-01-01 09:00")

In \[195\]: day \= pd.offsets.Day()

In \[196\]: day + ts
Out\[196\]: Timestamp('2014-01-02 09:00:00')

In \[197\]: (day + ts).normalize()
Out\[197\]: Timestamp('2014-01-02 00:00:00')

In \[198\]: ts \= pd.Timestamp("2014-01-01 22:00")

In \[199\]: hour \= pd.offsets.Hour()

In \[200\]: hour + ts
Out\[200\]: Timestamp('2014-01-01 23:00:00')

In \[201\]: (hour + ts).normalize()
Out\[201\]: Timestamp('2014-01-01 00:00:00')

In \[202\]: (hour + pd.Timestamp("2014-01-01 23:30")).normalize()
Out\[202\]: Timestamp('2014-01-02 00:00:00')

Copy to clipboard

### Parametric offsets[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#parametric-offsets "Link to this heading")

Some of the offsets can be “parameterized” when created to result in different behaviors. For example, the `Week` offset for generating weekly data accepts a `weekday` parameter which results in the generated dates always lying on a particular day of the week:

In \[203\]: d \= datetime.datetime(2008, 8, 18, 9, 0)

In \[204\]: d
Out\[204\]: datetime.datetime(2008, 8, 18, 9, 0)

In \[205\]: d + pd.offsets.Week()
Out\[205\]: Timestamp('2008-08-25 09:00:00')

In \[206\]: d + pd.offsets.Week(weekday\=4)
Out\[206\]: Timestamp('2008-08-22 09:00:00')

In \[207\]: (d + pd.offsets.Week(weekday\=4)).weekday()
Out\[207\]: 4

In \[208\]: d \- pd.offsets.Week()
Out\[208\]: Timestamp('2008-08-11 09:00:00')

Copy to clipboard

The `normalize` option will be effective for addition and subtraction.

In \[209\]: d + pd.offsets.Week(normalize\=True)
Out\[209\]: Timestamp('2008-08-25 00:00:00')

In \[210\]: d \- pd.offsets.Week(normalize\=True)
Out\[210\]: Timestamp('2008-08-11 00:00:00')

Copy to clipboard

Another example is parameterizing `YearEnd` with the specific ending month:

In \[211\]: d + pd.offsets.YearEnd()
Out\[211\]: Timestamp('2008-12-31 09:00:00')

In \[212\]: d + pd.offsets.YearEnd(month\=6)
Out\[212\]: Timestamp('2009-06-30 09:00:00')

Copy to clipboard

### Using offsets with `Series` / `DatetimeIndex`[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#using-offsets-with-series-datetimeindex "Link to this heading")

Offsets can be used with either a `Series` or `DatetimeIndex` to apply the offset to each element.

In \[213\]: rng \= pd.date\_range("2012-01-01", "2012-01-03")

In \[214\]: s \= pd.Series(rng)

In \[215\]: rng
Out\[215\]: 
DatetimeIndex(\['2012-01-01', '2012-01-02', '2012-01-03'\],
              dtype='datetime64\[us\]', freq='D')

In \[216\]: rng + pd.DateOffset(months\=2)
Out\[216\]: 
DatetimeIndex(\['2012-03-01', '2012-03-02', '2012-03-03'\],
              dtype='datetime64\[us\]', freq=None)

In \[217\]: s + pd.DateOffset(months\=2)
Out\[217\]: 
0   2012-03-01
1   2012-03-02
2   2012-03-03
dtype: datetime64\[us\]

In \[218\]: s \- pd.DateOffset(months\=2)
Out\[218\]: 
0   2011-11-01
1   2011-11-02
2   2011-11-03
dtype: datetime64\[us\]

Copy to clipboard

If the offset class maps directly to a `Timedelta` (`Hour`, `Minute`, `Second`, `Micro`, `Milli`, `Nano`) it can be used exactly like a `Timedelta` - see the [Timedelta section](https://pandas.pydata.org/docs/user_guide/timedeltas.html#timedeltas-operations)
 for more examples.

In \[219\]: s \- pd.offsets.Day(2)
Out\[219\]: 
0   2011-12-30
1   2011-12-31
2   2012-01-01
dtype: datetime64\[us\]

In \[220\]: td \= s \- pd.Series(pd.date\_range("2011-12-29", "2011-12-31"))

In \[221\]: td
Out\[221\]: 
0   3 days
1   3 days
2   3 days
dtype: timedelta64\[us\]

In \[222\]: td + pd.offsets.Minute(15)
Out\[222\]: 
0   3 days 00:15:00
1   3 days 00:15:00
2   3 days 00:15:00
dtype: timedelta64\[us\]

Copy to clipboard

Note that some offsets (such as `BQuarterEnd`) do not have a vectorized implementation. They can still be used but may calculate significantly slower and will show a `PerformanceWarning`

In \[223\]: rng + pd.offsets.BQuarterEnd()
Out\[223\]: 
DatetimeIndex(\['2012-03-30', '2012-03-30', '2012-03-30'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

### Custom business days[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#custom-business-days "Link to this heading")

The `CDay` or `CustomBusinessDay` class provides a parametric `BusinessDay` class which can be used to create customized business day calendars which account for local holidays and local weekend conventions.

As an interesting example, let’s look at Egypt where a Friday-Saturday weekend is observed.

In \[224\]: weekmask\_egypt \= "Sun Mon Tue Wed Thu"

\# They also observe International Workers' Day so let's
\# add that for a couple of years
In \[225\]: holidays \= \[\
   .....:    "2012-05-01",\
   .....:    datetime.datetime(2013, 5, 1),\
   .....:    np.datetime64("2014-05-01"),\
   .....: \]
   .....: 

In \[226\]: bday\_egypt \= pd.offsets.CustomBusinessDay(
   .....:    holidays\=holidays,
   .....:    weekmask\=weekmask\_egypt,
   .....: )
   .....: 

In \[227\]: dt \= datetime.datetime(2013, 4, 30)

In \[228\]: dt + 2 \* bday\_egypt
Out\[228\]: Timestamp('2013-05-05 00:00:00')

Copy to clipboard

Let’s map to the weekday names:

In \[229\]: dts \= pd.date\_range(dt, periods\=5, freq\=bday\_egypt)

In \[230\]: pd.Series(dts.day\_of\_week, dts).map(pd.Series("Mon Tue Wed Thu Fri Sat Sun".split()))
Out\[230\]: 
2013-04-30    Tue
2013-05-02    Thu
2013-05-05    Sun
2013-05-06    Mon
2013-05-07    Tue
Freq: C, dtype: str

Copy to clipboard

Holiday calendars can be used to provide the list of holidays. See the [holiday calendar](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-holiday)
 section for more information.

In \[231\]: from pandas.tseries.holiday import USFederalHolidayCalendar

In \[232\]: bday\_us \= pd.offsets.CustomBusinessDay(calendar\=USFederalHolidayCalendar())

\# Friday before MLK Day
In \[233\]: dt \= datetime.datetime(2014, 1, 17)

\# Tuesday after MLK Day (Monday is skipped because it's a holiday)
In \[234\]: dt + bday\_us
Out\[234\]: Timestamp('2014-01-21 00:00:00')

Copy to clipboard

Monthly offsets that respect a certain holiday calendar can be defined in the usual way.

In \[235\]: bmth\_us \= pd.offsets.CustomBusinessMonthBegin(calendar\=USFederalHolidayCalendar())

\# Skip new years
In \[236\]: dt \= datetime.datetime(2013, 12, 17)

In \[237\]: dt + bmth\_us
Out\[237\]: Timestamp('2014-01-02 00:00:00')

\# Define date index with custom offset
In \[238\]: pd.date\_range(start\="20100101", end\="20120101", freq\=bmth\_us)
Out\[238\]: 
DatetimeIndex(\['2010-01-04', '2010-02-01', '2010-03-01', '2010-04-01',\
               '2010-05-03', '2010-06-01', '2010-07-01', '2010-08-02',\
               '2010-09-01', '2010-10-01', '2010-11-01', '2010-12-01',\
               '2011-01-03', '2011-02-01', '2011-03-01', '2011-04-01',\
               '2011-05-02', '2011-06-01', '2011-07-01', '2011-08-01',\
               '2011-09-01', '2011-10-03', '2011-11-01', '2011-12-01'\],
              dtype='datetime64\[us\]', freq='CBMS')

Copy to clipboard

Note

The frequency string ‘C’ is used to indicate that a CustomBusinessDay DateOffset is used, it is important to note that since CustomBusinessDay is a parameterised type, instances of CustomBusinessDay may differ and this is not detectable from the ‘C’ frequency string. The user therefore needs to ensure that the ‘C’ frequency string is used consistently within the user’s application.

### Business hour[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#business-hour "Link to this heading")

The `BusinessHour` class provides a business hour representation on `BusinessDay`, allowing to use specific start and end times.

By default, `BusinessHour` uses 9:00 - 17:00 as business hours. Adding `BusinessHour` will increment `Timestamp` by hourly frequency. If target `Timestamp` is out of business hours, move to the next business hour then increment it. If the result exceeds the business hours end, the remaining hours are added to the next business day.

In \[239\]: bh \= pd.offsets.BusinessHour()

In \[240\]: bh
Out\[240\]: <BusinessHour: bh=09:00-17:00>

\# 2014-08-01 is Friday
In \[241\]: pd.Timestamp("2014-08-01 10:00").weekday()
Out\[241\]: 4

In \[242\]: pd.Timestamp("2014-08-01 10:00") + bh
Out\[242\]: Timestamp('2014-08-01 11:00:00')

\# Below example is the same as: pd.Timestamp('2014-08-01 09:00') + bh
In \[243\]: pd.Timestamp("2014-08-01 08:00") + bh
Out\[243\]: Timestamp('2014-08-01 10:00:00')

\# If the results is on the end time, move to the next business day
In \[244\]: pd.Timestamp("2014-08-01 16:00") + bh
Out\[244\]: Timestamp('2014-08-04 09:00:00')

\# Remainings are added to the next day
In \[245\]: pd.Timestamp("2014-08-01 16:30") + bh
Out\[245\]: Timestamp('2014-08-04 09:30:00')

\# Adding 2 business hours
In \[246\]: pd.Timestamp("2014-08-01 10:00") + pd.offsets.BusinessHour(2)
Out\[246\]: Timestamp('2014-08-01 12:00:00')

\# Subtracting 3 business hours
In \[247\]: pd.Timestamp("2014-08-01 10:00") + pd.offsets.BusinessHour(\-3)
Out\[247\]: Timestamp('2014-07-31 15:00:00')

Copy to clipboard

You can also specify `start` and `end` time by keywords. The argument must be a `str` with an `hour:minute` representation or a `datetime.time` instance. Specifying seconds, microseconds and nanoseconds as business hour results in `ValueError`.

In \[248\]: bh \= pd.offsets.BusinessHour(start\="11:00", end\=datetime.time(20, 0))

In \[249\]: bh
Out\[249\]: <BusinessHour: bh=11:00-20:00>

In \[250\]: pd.Timestamp("2014-08-01 13:00") + bh
Out\[250\]: Timestamp('2014-08-01 14:00:00')

In \[251\]: pd.Timestamp("2014-08-01 09:00") + bh
Out\[251\]: Timestamp('2014-08-01 12:00:00')

In \[252\]: pd.Timestamp("2014-08-01 18:00") + bh
Out\[252\]: Timestamp('2014-08-01 19:00:00')

Copy to clipboard

Passing `start` time later than `end` represents midnight business hour. In this case, business hour exceeds midnight and overlap to the next day. Valid business hours are distinguished by whether it started from valid `BusinessDay`.

In \[253\]: bh \= pd.offsets.BusinessHour(start\="17:00", end\="09:00")

In \[254\]: bh
Out\[254\]: <BusinessHour: bh=17:00-09:00>

In \[255\]: pd.Timestamp("2014-08-01 17:00") + bh
Out\[255\]: Timestamp('2014-08-01 18:00:00')

In \[256\]: pd.Timestamp("2014-08-01 23:00") + bh
Out\[256\]: Timestamp('2014-08-02 00:00:00')

\# Although 2014-08-02 is Saturday,
\# it is valid because it starts from 08-01 (Friday).
In \[257\]: pd.Timestamp("2014-08-02 04:00") + bh
Out\[257\]: Timestamp('2014-08-02 05:00:00')

\# Although 2014-08-04 is Monday,
\# it is out of business hours because it starts from 08-03 (Sunday).
In \[258\]: pd.Timestamp("2014-08-04 04:00") + bh
Out\[258\]: Timestamp('2014-08-04 18:00:00')

Copy to clipboard

Applying `BusinessHour.rollforward` and `rollback` to out of business hours results in the next business hour start or previous day’s end. Different from other offsets, `BusinessHour.rollforward` may output different results from `apply` by definition.

This is because one day’s business hour end is equal to next day’s business hour start. For example, under the default business hours (9:00 - 17:00), there is no gap (0 minutes) between `2014-08-01 17:00` and `2014-08-04 09:00`.

\# This adjusts a Timestamp to business hour edge
In \[259\]: pd.offsets.BusinessHour().rollback(pd.Timestamp("2014-08-02 15:00"))
Out\[259\]: Timestamp('2014-08-01 17:00:00')

In \[260\]: pd.offsets.BusinessHour().rollforward(pd.Timestamp("2014-08-02 15:00"))
Out\[260\]: Timestamp('2014-08-04 09:00:00')

\# It is the same as BusinessHour() + pd.Timestamp('2014-08-01 17:00').
\# And it is the same as BusinessHour() + pd.Timestamp('2014-08-04 09:00')
In \[261\]: pd.offsets.BusinessHour() + pd.Timestamp("2014-08-02 15:00")
Out\[261\]: Timestamp('2014-08-04 10:00:00')

\# BusinessDay results (for reference)
In \[262\]: pd.offsets.BusinessHour().rollforward(pd.Timestamp("2014-08-02"))
Out\[262\]: Timestamp('2014-08-04 09:00:00')

\# It is the same as BusinessDay() + pd.Timestamp('2014-08-01')
\# The result is the same as rollworward because BusinessDay never overlap.
In \[263\]: pd.offsets.BusinessHour() + pd.Timestamp("2014-08-02")
Out\[263\]: Timestamp('2014-08-04 10:00:00')

Copy to clipboard

`BusinessHour` regards Saturday and Sunday as holidays. To use arbitrary holidays, you can use `CustomBusinessHour` offset, as explained in the following subsection.

### Custom business hour[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#custom-business-hour "Link to this heading")

The `CustomBusinessHour` is a mixture of `BusinessHour` and `CustomBusinessDay` which allows you to specify arbitrary holidays. `CustomBusinessHour` works as the same as `BusinessHour` except that it skips specified custom holidays.

In \[264\]: from pandas.tseries.holiday import USFederalHolidayCalendar

In \[265\]: bhour\_us \= pd.offsets.CustomBusinessHour(calendar\=USFederalHolidayCalendar())

\# Friday before MLK Day
In \[266\]: dt \= datetime.datetime(2014, 1, 17, 15)

In \[267\]: dt + bhour\_us
Out\[267\]: Timestamp('2014-01-17 16:00:00')

\# Tuesday after MLK Day (Monday is skipped because it's a holiday)
In \[268\]: dt + bhour\_us \* 2
Out\[268\]: Timestamp('2014-01-21 09:00:00')

Copy to clipboard

You can use keyword arguments supported by either `BusinessHour` and `CustomBusinessDay`.

In \[269\]: bhour\_mon \= pd.offsets.CustomBusinessHour(start\="10:00", weekmask\="Tue Wed Thu Fri")

\# Monday is skipped because it's a holiday, business hour starts from 10:00
In \[270\]: dt + bhour\_mon \* 2
Out\[270\]: Timestamp('2014-01-21 10:00:00')

Copy to clipboard

### Offset aliases[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases "Link to this heading")

A number of string aliases are given to useful common time series frequencies. We will refer to these aliases as _offset aliases_.

 
| Alias | Description |
| --- | --- |
| B   | business day frequency |
| C   | custom business day frequency |
| D   | calendar day frequency |
| W   | weekly frequency (default anchored to Sunday, i.e. W-SUN) |
| ME  | month end frequency |
| SME | semi-month end frequency (15th and end of month) |
| BME | business month end frequency |
| CBME | custom business month end frequency |
| MS  | month start frequency |
| SMS | semi-month start frequency (1st and 15th) |
| BMS | business month start frequency |
| CBMS | custom business month start frequency |
| QE  | quarter end frequency |
| BQE | business quarter end frequency |
| QS  | quarter start frequency |
| BQS | business quarter start frequency |
| YE  | year end frequency |
| BYE | business year end frequency |
| YS  | year start frequency |
| BYS | business year start frequency |
| h   | hourly frequency |
| bh  | business hour frequency |
| cbh | custom business hour frequency |
| min | minutely frequency |
| s   | secondly frequency |
| ms  | milliseconds |
| us  | microseconds |
| ns  | nanoseconds |

Note

> When using the offset aliases above, it should be noted that functions such as [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
> , [`bdate_range()`](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas.bdate_range "pandas.bdate_range")
> , will only return timestamps that are in the interval defined by `start_date` and `end_date`. If the `start_date` does not correspond to the frequency, the returned timestamps will start at the next valid timestamp, same for `end_date`, the returned timestamps will stop at the previous valid timestamp.

For example, for the offset `MS`, if the `start_date` is not the first of the month, the returned timestamps will start with the first day of the next month. If `end_date` is not the first day of a month, the last returned timestamp will be the first day of the corresponding month.

In \[271\]: dates\_lst\_1 \= pd.date\_range("2020-01-06", "2020-04-03", freq\="MS")

In \[272\]: dates\_lst\_1
Out\[272\]: 
DatetimeIndex(\['2020-02-01', '2020-03-01', '2020-04-01'\],
              dtype='datetime64\[us\]', freq='MS')

In \[273\]: dates\_lst\_2 \= pd.date\_range("2020-01-01", "2020-04-01", freq\="MS")

In \[274\]: dates\_lst\_2
Out\[274\]: 
DatetimeIndex(\['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01'\],
              dtype='datetime64\[us\]', freq='MS')

Copy to clipboard

We can see in the above example [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
 and [`bdate_range()`](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas.bdate_range "pandas.bdate_range")
 will only return the valid timestamps between the `start_date` and `end_date`. If these are not valid timestamps for the given frequency it will roll to the next value for `start_date` (respectively previous for the `end_date`)

### Period aliases[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#period-aliases "Link to this heading")

A number of string aliases are given to useful common time series frequencies. We will refer to these aliases as _period aliases_.

 
| Alias | Description |
| --- | --- |
| B   | business day frequency |
| D   | calendar day frequency |
| W   | weekly frequency (default anchored to Sunday, i.e. W-SUN) |
| M   | monthly frequency |
| Q   | quarterly frequency |
| Y   | yearly frequency |
| h   | hourly frequency |
| min | minutely frequency |
| s   | secondly frequency |
| ms  | milliseconds |
| us  | microseconds |
| ns  | nanoseconds |

### Combining aliases[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#combining-aliases "Link to this heading")

As we have seen previously, the alias and the offset instance are fungible in most functions:

In \[275\]: pd.date\_range(start, periods\=5, freq\="B")
Out\[275\]: 
DatetimeIndex(\['2011-01-03', '2011-01-04', '2011-01-05', '2011-01-06',\
               '2011-01-07'\],
              dtype='datetime64\[us\]', freq='B')

In \[276\]: pd.date\_range(start, periods\=5, freq\=pd.offsets.BDay())
Out\[276\]: 
DatetimeIndex(\['2011-01-03', '2011-01-04', '2011-01-05', '2011-01-06',\
               '2011-01-07'\],
              dtype='datetime64\[us\]', freq='B')

Copy to clipboard

You can combine together day and intraday offsets:

In \[277\]: pd.date\_range(start, periods\=10, freq\="2h20min")
Out\[277\]: 
DatetimeIndex(\['2011-01-01 00:00:00', '2011-01-01 02:20:00',\
               '2011-01-01 04:40:00', '2011-01-01 07:00:00',\
               '2011-01-01 09:20:00', '2011-01-01 11:40:00',\
               '2011-01-01 14:00:00', '2011-01-01 16:20:00',\
               '2011-01-01 18:40:00', '2011-01-01 21:00:00'\],
              dtype='datetime64\[us\]', freq='140min')

In \[278\]: pd.date\_range(start, periods\=10, freq\="1D10us")
Out\[278\]: 
DatetimeIndex(\[       '2011-01-01 00:00:00', '2011-01-02 00:00:00.000010',\
               '2011-01-03 00:00:00.000020', '2011-01-04 00:00:00.000030',\
               '2011-01-05 00:00:00.000040', '2011-01-06 00:00:00.000050',\
               '2011-01-07 00:00:00.000060', '2011-01-08 00:00:00.000070',\
               '2011-01-09 00:00:00.000080', '2011-01-10 00:00:00.000090'\],
              dtype='datetime64\[us\]', freq='86400000010us')

Copy to clipboard

### Anchored offsets[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#anchored-offsets "Link to this heading")

For some frequencies you can specify an anchoring suffix:

 
| Alias | Description |
| --- | --- |
| W-SUN | weekly frequency, week ends on Sunday. Same as ‘W’ |
| W-MON | weekly frequency, week ends on Monday |
| W-TUE | weekly frequency, week ends on Tuesday |
| W-WED | weekly frequency, week ends on Wednesday |
| W-THU | weekly frequency, week ends on Thursday |
| W-FRI | weekly frequency, week ends on Friday |
| W-SAT | weekly frequency, week ends on Saturday |
| (B)QE-DEC | quarterly frequency, year ends in December. Same as ‘QE’ |
| (B)QE-JAN | quarterly frequency, year ends in January |
| (B)QE-FEB | quarterly frequency, year ends in February |
| (B)QE-MAR | quarterly frequency, year ends in March |
| (B)QE-APR | quarterly frequency, year ends in April |
| (B)QE-MAY | quarterly frequency, year ends in May |
| (B)QE-JUN | quarterly frequency, year ends in June |
| (B)QE-JUL | quarterly frequency, year ends in July |
| (B)QE-AUG | quarterly frequency, year ends in August |
| (B)QE-SEP | quarterly frequency, year ends in September |
| (B)QE-OCT | quarterly frequency, year ends in October |
| (B)QE-NOV | quarterly frequency, year ends in November |
| (B)QS-JAN | quarterly frequency, year starts in January. Same as ‘QS’ |
| (B)QS-FEB | quarterly frequency, year starts in February |
| (B)QS-MAR | quarterly frequency, year starts in March |
| (B)QS-APR | quarterly frequency, year starts in April |
| (B)QS-MAY | quarterly frequency, year starts in May |
| (B)QS-JUN | quarterly frequency, year starts in June |
| (B)QS-JUL | quarterly frequency, year starts in July |
| (B)QS-AUG | quarterly frequency, year starts in August |
| (B)QS-SEP | quarterly frequency, year starts in September |
| (B)QS-OCT | quarterly frequency, year starts in October |
| (B)QS-NOV | quarterly frequency, year starts in November |
| (B)QS-DEC | quarterly frequency, year starts in December |
| (B)YE-DEC | annual frequency, anchored end of December. Same as ‘YE’ |
| (B)YE-JAN | annual frequency, anchored end of January |
| (B)YE-FEB | annual frequency, anchored end of February |
| (B)YE-MAR | annual frequency, anchored end of March |
| (B)YE-APR | annual frequency, anchored end of April |
| (B)YE-MAY | annual frequency, anchored end of May |
| (B)YE-JUN | annual frequency, anchored end of June |
| (B)YE-JUL | annual frequency, anchored end of July |
| (B)YE-AUG | annual frequency, anchored end of August |
| (B)YE-SEP | annual frequency, anchored end of September |
| (B)YE-OCT | annual frequency, anchored end of October |
| (B)YE-NOV | annual frequency, anchored end of November |
| (B)YS-JAN | annual frequency, anchored start of January. Same as ‘YS’ |
| (B)YS-FEB | annual frequency, anchored start of February |
| (B)YS-MAR | annual frequency, anchored start of March |
| (B)YS-APR | annual frequency, anchored start of April |
| (B)YS-MAY | annual frequency, anchored start of May |
| (B)YS-JUN | annual frequency, anchored start of June |
| (B)YS-JUL | annual frequency, anchored start of July |
| (B)YS-AUG | annual frequency, anchored start of August |
| (B)YS-SEP | annual frequency, anchored start of September |
| (B)YS-OCT | annual frequency, anchored start of October |
| (B)YS-NOV | annual frequency, anchored start of November |
| (B)YS-DEC | annual frequency, anchored start of December |

These can be used as arguments to `date_range`, `bdate_range`, constructors for `DatetimeIndex`, as well as various other timeseries-related functions in pandas.

For a calendar step that is not anchored, such as yearly from an arbitrary date, pass a [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 like `freq=pd.DateOffset(years=1)`.

### Anchored offset semantics[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#anchored-offset-semantics "Link to this heading")

For those offsets that are anchored to the start or end of specific frequency (`MonthEnd`, `MonthBegin`, `WeekEnd`, etc), the following rules apply to rolling forward and backwards.

When `n` is not 0, if the given date is not on an anchor point, it snapped to the next(previous) anchor point, and moved `|n|-1` additional steps forwards or backwards.

In \[279\]: pd.Timestamp("2014-01-02") + pd.offsets.MonthBegin(n\=1)
Out\[279\]: Timestamp('2014-02-01 00:00:00')

In \[280\]: pd.Timestamp("2014-01-02") + pd.offsets.MonthEnd(n\=1)
Out\[280\]: Timestamp('2014-01-31 00:00:00')

In \[281\]: pd.Timestamp("2014-01-02") \- pd.offsets.MonthBegin(n\=1)
Out\[281\]: Timestamp('2014-01-01 00:00:00')

In \[282\]: pd.Timestamp("2014-01-02") \- pd.offsets.MonthEnd(n\=1)
Out\[282\]: Timestamp('2013-12-31 00:00:00')

In \[283\]: pd.Timestamp("2014-01-02") + pd.offsets.MonthBegin(n\=4)
Out\[283\]: Timestamp('2014-05-01 00:00:00')

In \[284\]: pd.Timestamp("2014-01-02") \- pd.offsets.MonthBegin(n\=4)
Out\[284\]: Timestamp('2013-10-01 00:00:00')

Copy to clipboard

If the given date _is_ on an anchor point, it is moved `|n|` points forwards or backwards.

In \[285\]: pd.Timestamp("2014-01-01") + pd.offsets.MonthBegin(n\=1)
Out\[285\]: Timestamp('2014-02-01 00:00:00')

In \[286\]: pd.Timestamp("2014-01-31") + pd.offsets.MonthEnd(n\=1)
Out\[286\]: Timestamp('2014-02-28 00:00:00')

In \[287\]: pd.Timestamp("2014-01-01") \- pd.offsets.MonthBegin(n\=1)
Out\[287\]: Timestamp('2013-12-01 00:00:00')

In \[288\]: pd.Timestamp("2014-01-31") \- pd.offsets.MonthEnd(n\=1)
Out\[288\]: Timestamp('2013-12-31 00:00:00')

In \[289\]: pd.Timestamp("2014-01-01") + pd.offsets.MonthBegin(n\=4)
Out\[289\]: Timestamp('2014-05-01 00:00:00')

In \[290\]: pd.Timestamp("2014-01-31") \- pd.offsets.MonthBegin(n\=4)
Out\[290\]: Timestamp('2013-10-01 00:00:00')

Copy to clipboard

For the case when `n=0`, the date is not moved if on an anchor point, otherwise it is rolled forward to the next anchor point.

In \[291\]: pd.Timestamp("2014-01-02") + pd.offsets.MonthBegin(n\=0)
Out\[291\]: Timestamp('2014-02-01 00:00:00')

In \[292\]: pd.Timestamp("2014-01-02") + pd.offsets.MonthEnd(n\=0)
Out\[292\]: Timestamp('2014-01-31 00:00:00')

In \[293\]: pd.Timestamp("2014-01-01") + pd.offsets.MonthBegin(n\=0)
Out\[293\]: Timestamp('2014-01-01 00:00:00')

In \[294\]: pd.Timestamp("2014-01-31") + pd.offsets.MonthEnd(n\=0)
Out\[294\]: Timestamp('2014-01-31 00:00:00')

Copy to clipboard

### Holidays / holiday calendars[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#holidays-holiday-calendars "Link to this heading")

Holidays and calendars provide a simple way to define holiday rules to be used with `CustomBusinessDay` or in other analysis that requires a predefined set of holidays. The `AbstractHolidayCalendar` class provides all the necessary methods to return a list of holidays and only `rules` need to be defined in a specific holiday calendar class. Furthermore, the `start_date` and `end_date` class attributes determine over what date range holidays are generated. These should be overwritten on the `AbstractHolidayCalendar` class to have the range apply to all calendar subclasses. `USFederalHolidayCalendar` is the only calendar that exists and primarily serves as an example for developing other calendars.

For holidays that occur on fixed dates (e.g., US Memorial Day or July 4th) an observance rule determines when that holiday is observed if it falls on a weekend or some other non-observed day. Defined observance rules are:

 
| Rule | Description |
| --- | --- |
| next\_workday | move to the next weekday, always advancing by at least one day |
| previous\_workday | move to the previous weekday, always moving back by at least one day |
| nearest\_workday | move Saturday to Friday and Sunday to Monday |
| before\_nearest\_workday | apply `nearest_workday` and then move to previous workday before that day |
| after\_nearest\_workday | apply `nearest_workday` and then move to next workday after that day |
| sunday\_to\_monday | move Sunday to following Monday |
| next\_monday\_or\_tuesday | move Saturday to Monday and Sunday/Monday to Tuesday |
| previous\_friday | move Saturday and Sunday to previous Friday |
| next\_monday | move Saturday and Sunday to following Monday |
| weekend\_to\_monday | same as `next_monday` |

An example of how holidays and holiday calendars are defined:

In \[295\]: from pandas.tseries.holiday import (
   .....:    Holiday,
   .....:    USMemorialDay,
   .....:    AbstractHolidayCalendar,
   .....:    nearest\_workday,
   .....:    MO,
   .....: )
   .....: 

In \[296\]: class ExampleCalendar(AbstractHolidayCalendar):
   .....:    rules \= \[\
   .....:        USMemorialDay,\
   .....:        Holiday("July 4th", month\=7, day\=4, observance\=nearest\_workday),\
   .....:        Holiday(\
   .....:            "Columbus Day",\
   .....:            month\=10,\
   .....:            day\=1,\
   .....:            offset\=pd.DateOffset(weekday\=MO(2)),\
   .....:        ),\
   .....:    \]
   .....: 

In \[297\]: cal \= ExampleCalendar()

In \[298\]: cal.holidays(datetime.datetime(2012, 1, 1), datetime.datetime(2012, 12, 31))
Out\[298\]: 
DatetimeIndex(\['2012-05-28', '2012-07-04', '2012-10-08'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

hint:

**weekday=MO(2)** is same as **2 \* Week(weekday=2)**

Using this calendar, creating an index or doing offset arithmetic skips weekends and holidays (i.e., Memorial Day/July 4th). For example, the below defines a custom business day offset using the `ExampleCalendar`. Like any other offset, it can be used to create a `DatetimeIndex` or added to `datetime` or `Timestamp` objects.

In \[299\]: pd.date\_range(
   .....:    start\="7/1/2012", end\="7/10/2012", freq\=pd.offsets.CDay(calendar\=cal)
   .....: ).to\_pydatetime()
   .....: 
Out\[299\]: 
array(\[datetime.datetime(2012, 7, 2, 0, 0),\
       datetime.datetime(2012, 7, 3, 0, 0),\
       datetime.datetime(2012, 7, 5, 0, 0),\
       datetime.datetime(2012, 7, 6, 0, 0),\
       datetime.datetime(2012, 7, 9, 0, 0),\
       datetime.datetime(2012, 7, 10, 0, 0)\], dtype=object)

In \[300\]: offset \= pd.offsets.CustomBusinessDay(calendar\=cal)

In \[301\]: datetime.datetime(2012, 5, 25) + offset
Out\[301\]: Timestamp('2012-05-29 00:00:00')

In \[302\]: datetime.datetime(2012, 7, 3) + offset
Out\[302\]: Timestamp('2012-07-05 00:00:00')

In \[303\]: datetime.datetime(2012, 7, 3) + 2 \* offset
Out\[303\]: Timestamp('2012-07-06 00:00:00')

In \[304\]: datetime.datetime(2012, 7, 6) + offset
Out\[304\]: Timestamp('2012-07-09 00:00:00')

Copy to clipboard

Ranges are defined by the `start_date` and `end_date` class attributes of `AbstractHolidayCalendar`. The defaults are shown below.

In \[305\]: AbstractHolidayCalendar.start\_date
Out\[305\]: Timestamp('1970-01-01 00:00:00')

In \[306\]: AbstractHolidayCalendar.end\_date
Out\[306\]: Timestamp('2200-12-31 00:00:00')

Copy to clipboard

These dates can be overwritten by setting the attributes as datetime/Timestamp/string.

In \[307\]: AbstractHolidayCalendar.start\_date \= datetime.datetime(2012, 1, 1)

In \[308\]: AbstractHolidayCalendar.end\_date \= datetime.datetime(2012, 12, 31)

In \[309\]: cal.holidays()
Out\[309\]: 
DatetimeIndex(\['2012-05-28', '2012-07-04', '2012-10-08'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Every calendar class is accessible by name using the `get_calendar` function which returns a holiday class instance. Any imported calendar class will automatically be available by this function. Also, `HolidayCalendarFactory` provides an easy interface to create calendars that are combinations of calendars or calendars with additional rules.

In \[310\]: from pandas.tseries.holiday import get\_calendar, HolidayCalendarFactory, USLaborDay

In \[311\]: cal \= get\_calendar("ExampleCalendar")

In \[312\]: cal.rules
Out\[312\]: 
\[Holiday: Memorial Day (month=5, day=31, offset=<DateOffset: weekday=MO(-1)>),\
 Holiday: July 4th (month=7, day=4, observance=<function nearest\_workday at 0x7fa243d21620>),\
 Holiday: Columbus Day (month=10, day=1, offset=<DateOffset: weekday=MO(+2)>)\]

In \[313\]: new\_cal \= HolidayCalendarFactory("NewExampleCalendar", cal, USLaborDay)

In \[314\]: new\_cal.rules
Out\[314\]: 
\[Holiday: Labor Day (month=9, day=1, offset=<DateOffset: weekday=MO(+1)>),\
 Holiday: Memorial Day (month=5, day=31, offset=<DateOffset: weekday=MO(-1)>),\
 Holiday: July 4th (month=7, day=4, observance=<function nearest\_workday at 0x7fa243d21620>),\
 Holiday: Columbus Day (month=10, day=1, offset=<DateOffset: weekday=MO(+2)>)\]

Copy to clipboard

Time Series-related instance methods[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-series-related-instance-methods "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Shifting / lagging[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#shifting-lagging "Link to this heading")

One may want to _shift_ or _lag_ the values in a time series back and forward in time. The method for this is [`shift()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")
, which is available on all of the pandas objects.

In \[315\]: ts \= pd.Series(range(len(rng)), index\=rng)

In \[316\]: ts \= ts\[:5\]

In \[317\]: ts.shift(1)
Out\[317\]: 
2012-01-01    NaN
2012-01-02    0.0
2012-01-03    1.0
Freq: D, dtype: float64

Copy to clipboard

The `shift` method accepts a `freq` argument which can accept a `DateOffset` class or other `timedelta`\-like object or also an [offset alias](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

When `freq` is specified, `shift` method changes all the dates in the index rather than changing the alignment of the data and the index:

In \[318\]: ts.shift(5, freq\="D")
Out\[318\]: 
2012-01-06    0
2012-01-07    1
2012-01-08    2
Freq: D, dtype: int64

In \[319\]: ts.shift(5, freq\=pd.offsets.BDay())
Out\[319\]: 
2012-01-06    0
2012-01-09    1
2012-01-10    2
dtype: int64

In \[320\]: ts.shift(5, freq\="BME")
Out\[320\]: 
2012-05-31    0
2012-05-31    1
2012-05-31    2
dtype: int64

Copy to clipboard

Note that with when `freq` is specified, the leading entry is no longer NaN because the data is not being realigned.

### Frequency conversion[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#frequency-conversion "Link to this heading")

The primary function for changing frequencies is the [`asfreq()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#pandas.Series.asfreq "pandas.Series.asfreq")
 method. For a `DatetimeIndex`, this is basically just a thin, but convenient wrapper around [`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")
 which generates a `date_range` and calls `reindex`.

In \[321\]: dr \= pd.date\_range("1/1/2010", periods\=3, freq\=3 \* pd.offsets.BDay())

In \[322\]: ts \= pd.Series(np.random.randn(3), index\=dr)

In \[323\]: ts
Out\[323\]: 
2010-01-01    1.494522
2010-01-06   -0.778425
2010-01-11   -0.253355
Freq: 3B, dtype: float64

In \[324\]: ts.asfreq(pd.offsets.BDay())
Out\[324\]: 
2010-01-01    1.494522
2010-01-04         NaN
2010-01-05         NaN
2010-01-06   -0.778425
2010-01-07         NaN
2010-01-08         NaN
2010-01-11   -0.253355
Freq: B, dtype: float64

Copy to clipboard

`asfreq` provides a further convenience so you can specify an interpolation method for any gaps that may appear after the frequency conversion.

In \[325\]: ts.asfreq(pd.offsets.BDay(), method\="pad")
Out\[325\]: 
2010-01-01    1.494522
2010-01-04    1.494522
2010-01-05    1.494522
2010-01-06   -0.778425
2010-01-07   -0.778425
2010-01-08   -0.778425
2010-01-11   -0.253355
Freq: B, dtype: float64

Copy to clipboard

### Filling forward / backward[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#filling-forward-backward "Link to this heading")

Related to `asfreq` and `reindex` is [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")
, which is documented in the [missing data section](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data-fillna)
.

### Converting to Python datetimes[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-python-datetimes "Link to this heading")

`DatetimeIndex` can be converted to an array of Python native [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
 objects using the `to_pydatetime` method.

Resampling[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling "Link to this heading")

-----------------------------------------------------------------------------------------------------------

pandas has a simple, powerful, and efficient functionality for performing resampling operations during frequency conversion (e.g., converting secondly data into 5-minutely data). This is extremely common in, but not limited to, financial applications.

[`resample()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")
 is a time-based groupby, followed by a reduction method on each of its groups. See some [cookbook examples](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook-resample)
 for some advanced strategies.

The `resample()` method can be used directly from `DataFrameGroupBy` objects, see the [groupby docs](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform-window-resample)
.

### Basics[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#basics "Link to this heading")

In \[326\]: rng \= pd.date\_range("1/1/2012", periods\=100, freq\="s")

In \[327\]: ts \= pd.Series(np.random.randint(0, 500, len(rng)), index\=rng)

In \[328\]: ts.resample("5Min").sum()
Out\[328\]: 
2012-01-01    25103
Freq: 5min, dtype: int64

Copy to clipboard

The `resample` function is very flexible and allows you to specify many different parameters to control the frequency conversion and resampling operation.

Any built-in method available via [GroupBy](https://pandas.pydata.org/docs/reference/groupby.html#api-groupby)
 is available as a method of the returned object, including `sum`, `mean`, `std`, `sem`, `max`, `min`, `median`, `first`, `last`, `ohlc`:

In \[329\]: ts.resample("5Min").mean()
Out\[329\]: 
2012-01-01    251.03
Freq: 5min, dtype: float64

In \[330\]: ts.resample("5Min").ohlc()
Out\[330\]: 
            open  high  low  close
2012-01-01   308   460    9    205

In \[331\]: ts.resample("5Min").max()
Out\[331\]: 
2012-01-01    460
Freq: 5min, dtype: int64

Copy to clipboard

For downsampling, `closed` can be set to ‘left’ or ‘right’ to specify which end of the interval is closed:

In \[332\]: ts.resample("5Min", closed\="right").mean()
Out\[332\]: 
2011-12-31 23:55:00    308.000000
2012-01-01 00:00:00    250.454545
Freq: 5min, dtype: float64

In \[333\]: ts.resample("5Min", closed\="left").mean()
Out\[333\]: 
2012-01-01    251.03
Freq: 5min, dtype: float64

Copy to clipboard

Parameters like `label` are used to manipulate the resulting labels. `label` specifies whether the result is labeled with the beginning or the end of the interval.

In \[334\]: ts.resample("5Min").mean()  \# by default label='left'
Out\[334\]: 
2012-01-01    251.03
Freq: 5min, dtype: float64

In \[335\]: ts.resample("5Min", label\="left").mean()
Out\[335\]: 
2012-01-01    251.03
Freq: 5min, dtype: float64

Copy to clipboard

Warning

The default values for `label` and `closed` is ‘**left**’ for all frequency offsets except for ‘ME’, ‘YE’, ‘QE’, ‘BME’, ‘BYE’, ‘BQE’, and ‘W’ which all have a default of ‘right’.

This might unintendedly lead to looking ahead, where the value for a later time is pulled back to a previous time as in the following example with the [`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")
 frequency:

In \[336\]: s \= pd.date\_range("2000-01-01", "2000-01-05").to\_series()

In \[337\]: s.iloc\[2\] \= pd.NaT

In \[338\]: s.dt.day\_name()
Out\[338\]: 
2000-01-01     Saturday
2000-01-02       Sunday
2000-01-03          NaN
2000-01-04      Tuesday
2000-01-05    Wednesday
Freq: D, dtype: str

\# default: label='left', closed='left'
In \[339\]: s.resample("B").last().dt.day\_name()
Out\[339\]: 
1999-12-31       Sunday
2000-01-03          NaN
2000-01-04      Tuesday
2000-01-05    Wednesday
Freq: B, dtype: str

Copy to clipboard

Notice how the value for Sunday got pulled back to the previous Friday. To get the behavior where the value for Sunday is pushed to Monday, use instead

In \[340\]: s.resample("B", label\="right", closed\="right").last().dt.day\_name()
Out\[340\]: 
2000-01-03       Sunday
2000-01-04      Tuesday
2000-01-05    Wednesday
2000-01-06          NaN
Freq: B, dtype: str

Copy to clipboard

The `axis` parameter can be set to 0 or 1 and allows you to resample the specified axis for a `DataFrame`.

`kind` can be set to ‘timestamp’ or ‘period’ to convert the resulting index to/from timestamp and time span representations. By default `resample` retains the input representation.

`convention` can be set to ‘start’ or ‘end’ when resampling period data (detail below). It specifies how low frequency periods are converted to higher frequency periods.

### Upsampling[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#upsampling "Link to this heading")

For upsampling, you can specify a way to upsample and the `limit` parameter to interpolate over the gaps that are created:

\# from secondly to every 250 milliseconds
In \[341\]: ts\[:2\].resample("250ms").asfreq()
Out\[341\]: 
2012-01-01 00:00:00.000    308.0
2012-01-01 00:00:00.250      NaN
2012-01-01 00:00:00.500      NaN
2012-01-01 00:00:00.750      NaN
2012-01-01 00:00:01.000    204.0
Freq: 250ms, dtype: float64

In \[342\]: ts\[:2\].resample("250ms").ffill()
Out\[342\]: 
2012-01-01 00:00:00.000    308
2012-01-01 00:00:00.250    308
2012-01-01 00:00:00.500    308
2012-01-01 00:00:00.750    308
2012-01-01 00:00:01.000    204
Freq: 250ms, dtype: int64

In \[343\]: ts\[:2\].resample("250ms").ffill(limit\=2)
Out\[343\]: 
2012-01-01 00:00:00.000    308.0
2012-01-01 00:00:00.250    308.0
2012-01-01 00:00:00.500    308.0
2012-01-01 00:00:00.750      NaN
2012-01-01 00:00:01.000    204.0
Freq: 250ms, dtype: float64

Copy to clipboard

### Sparse resampling[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#sparse-resampling "Link to this heading")

Sparse timeseries are the ones where you have a lot fewer points relative to the amount of time you are looking to resample. Naively upsampling a sparse series can potentially generate lots of intermediate values. When you don’t want to use a method to fill these values, e.g. `fill_method` is `None`, then intermediate values will be filled with `NaN`.

Since `resample` is a time-based groupby, the following is a method to efficiently resample only the groups that are not all `NaN`.

In \[344\]: rng \= pd.date\_range("2014-1-1", periods\=100, freq\="D") + pd.Timedelta("1s")

In \[345\]: ts \= pd.Series(range(100), index\=rng)

Copy to clipboard

If we want to resample to the full range of the series:

In \[346\]: ts.resample("3min").sum()
Out\[346\]: 
2014-01-01 00:00:00     0
2014-01-01 00:03:00     0
2014-01-01 00:06:00     0
2014-01-01 00:09:00     0
2014-01-01 00:12:00     0
                       ..
2014-04-09 23:48:00     0
2014-04-09 23:51:00     0
2014-04-09 23:54:00     0
2014-04-09 23:57:00     0
2014-04-10 00:00:00    99
Freq: 3min, Length: 47521, dtype: int64

Copy to clipboard

We can instead only resample those groups where we have points as follows:

In \[347\]: from functools import partial

In \[348\]: from pandas.tseries.frequencies import to\_offset

In \[349\]: def round(t, freq):
   .....:    freq \= to\_offset(freq)
   .....:    td \= pd.Timedelta(freq)
   .....:    return pd.Timestamp((t.value // td.value) \* td.value)
   .....: 

In \[350\]: ts.groupby(partial(round, freq\="3min")).sum()
Out\[350\]: 
2014-01-01     0
2014-01-02     1
2014-01-03     2
2014-01-04     3
2014-01-05     4
              ..
2014-04-06    95
2014-04-07    96
2014-04-08    97
2014-04-09    98
2014-04-10    99
Length: 100, dtype: int64

Copy to clipboard

### Aggregation[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#aggregation "Link to this heading")

The `resample()` method returns a `pandas.api.typing.Resampler` instance. Similar to the [aggregating API](https://pandas.pydata.org/docs/user_guide/basics.html#basics-aggregate)
, [groupby API](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-aggregate)
, and the [window API](https://pandas.pydata.org/docs/user_guide/window.html#window-overview)
, a `Resampler` can be selectively resampled.

Resampling a `DataFrame`, the default will be to act on all columns with the same function.

In \[351\]: df \= pd.DataFrame(
   .....:    np.random.randn(1000, 3),
   .....:    index\=pd.date\_range("1/1/2012", freq\="s", periods\=1000),
   .....:    columns\=\["A", "B", "C"\],
   .....: )
   .....: 

In \[352\]: r \= df.resample("3min")

In \[353\]: r.mean()
Out\[353\]: 
                            A         B         C
2012-01-01 00:00:00 -0.033823 -0.121514 -0.081447
2012-01-01 00:03:00  0.056909  0.146731 -0.024320
2012-01-01 00:06:00 -0.058837  0.047046 -0.052021
2012-01-01 00:09:00  0.063123 -0.026158 -0.066533
2012-01-01 00:12:00  0.186340 -0.003144  0.074752
2012-01-01 00:15:00 -0.085954 -0.016287 -0.050046

Copy to clipboard

We can select a specific column or columns using standard getitem.

In \[354\]: r\["A"\].mean()
Out\[354\]: 
2012-01-01 00:00:00   -0.033823
2012-01-01 00:03:00    0.056909
2012-01-01 00:06:00   -0.058837
2012-01-01 00:09:00    0.063123
2012-01-01 00:12:00    0.186340
2012-01-01 00:15:00   -0.085954
Freq: 3min, Name: A, dtype: float64

In \[355\]: r\[\["A", "B"\]\].mean()
Out\[355\]: 
                            A         B
2012-01-01 00:00:00 -0.033823 -0.121514
2012-01-01 00:03:00  0.056909  0.146731
2012-01-01 00:06:00 -0.058837  0.047046
2012-01-01 00:09:00  0.063123 -0.026158
2012-01-01 00:12:00  0.186340 -0.003144
2012-01-01 00:15:00 -0.085954 -0.016287

Copy to clipboard

You can pass a list or dict of functions to do aggregation with, outputting a `DataFrame`:

In \[356\]: r\["A"\].agg(\["sum", "mean", "std"\])
Out\[356\]: 
                           sum      mean       std
2012-01-01 00:00:00  -6.088060 -0.033823  1.043263
2012-01-01 00:03:00  10.243678  0.056909  1.058534
2012-01-01 00:06:00 -10.590584 -0.058837  0.949264
2012-01-01 00:09:00  11.362228  0.063123  1.028096
2012-01-01 00:12:00  33.541257  0.186340  0.884586
2012-01-01 00:15:00  -8.595393 -0.085954  1.035476

Copy to clipboard

On a resampled `DataFrame`, you can pass a list of functions to apply to each column, which produces an aggregated result with a hierarchical index:

In \[357\]: r.agg(\["sum", "mean"\])
Out\[357\]: 
                             A            ...          C          
                           sum      mean  ...        sum      mean
2012-01-01 00:00:00  -6.088060 -0.033823  ... -14.660515 -0.081447
2012-01-01 00:03:00  10.243678  0.056909  ...  -4.377642 -0.024320
2012-01-01 00:06:00 -10.590584 -0.058837  ...  -9.363825 -0.052021
2012-01-01 00:09:00  11.362228  0.063123  ... -11.975895 -0.066533
2012-01-01 00:12:00  33.541257  0.186340  ...  13.455299  0.074752
2012-01-01 00:15:00  -8.595393 -0.085954  ...  -5.004580 -0.050046

\[6 rows x 6 columns\]

Copy to clipboard

By passing a dict to `aggregate` you can apply a different aggregation to the columns of a `DataFrame`:

In \[358\]: r.agg({"A": "sum", "B": lambda x: np.std(x, ddof\=1)})
Out\[358\]: 
                             A         B
2012-01-01 00:00:00  -6.088060  1.001294
2012-01-01 00:03:00  10.243678  1.074597
2012-01-01 00:06:00 -10.590584  0.987309
2012-01-01 00:09:00  11.362228  0.944953
2012-01-01 00:12:00  33.541257  1.095025
2012-01-01 00:15:00  -8.595393  1.035312

Copy to clipboard

The function names can also be strings. In order for a string to be valid it must be implemented on the resampled object:

In \[359\]: r.agg({"A": "sum", "B": "std"})
Out\[359\]: 
                             A         B
2012-01-01 00:00:00  -6.088060  1.001294
2012-01-01 00:03:00  10.243678  1.074597
2012-01-01 00:06:00 -10.590584  0.987309
2012-01-01 00:09:00  11.362228  0.944953
2012-01-01 00:12:00  33.541257  1.095025
2012-01-01 00:15:00  -8.595393  1.035312

Copy to clipboard

Furthermore, you can also specify multiple aggregation functions for each column separately.

In \[360\]: r.agg({"A": \["sum", "std"\], "B": \["mean", "std"\]})
Out\[360\]: 
                             A                   B          
                           sum       std      mean       std
2012-01-01 00:00:00  -6.088060  1.043263 -0.121514  1.001294
2012-01-01 00:03:00  10.243678  1.058534  0.146731  1.074597
2012-01-01 00:06:00 -10.590584  0.949264  0.047046  0.987309
2012-01-01 00:09:00  11.362228  1.028096 -0.026158  0.944953
2012-01-01 00:12:00  33.541257  0.884586 -0.003144  1.095025
2012-01-01 00:15:00  -8.595393  1.035476 -0.016287  1.035312

Copy to clipboard

If a `DataFrame` does not have a datetimelike index, but instead you want to resample based on datetimelike column in the frame, it can passed to the `on` keyword.

In \[361\]: df \= pd.DataFrame(
   .....:    {"date": pd.date\_range("2015-01-01", freq\="W", periods\=5), "a": np.arange(5)},
   .....:    index\=pd.MultiIndex.from\_arrays(
   .....:        \[\[1, 2, 3, 4, 5\], pd.date\_range("2015-01-01", freq\="W", periods\=5)\],
   .....:        names\=\["v", "d"\],
   .....:    ),
   .....: )
   .....: 

In \[362\]: df
Out\[362\]: 
                   date  a
v d                       
1 2015-01-04 2015-01-04  0
2 2015-01-11 2015-01-11  1
3 2015-01-18 2015-01-18  2
4 2015-01-25 2015-01-25  3
5 2015-02-01 2015-02-01  4

In \[363\]: df.resample("MS", on\="date")\[\["a"\]\].sum()
Out\[363\]: 
            a
date         
2015-01-01  6
2015-02-01  4

Copy to clipboard

Similarly, if you instead want to resample by a datetimelike level of `MultiIndex`, its name or location can be passed to the `level` keyword.

In \[364\]: df.resample("MS", level\="d")\[\["a"\]\].sum()
Out\[364\]: 
            a
d            
2015-01-01  6
2015-02-01  4

Copy to clipboard

### Iterating through groups[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#iterating-through-groups "Link to this heading")

With the `Resampler` object in hand, iterating through the grouped data is very natural and functions similarly to [`itertools.groupby()`](https://docs.python.org/3/library/itertools.html#itertools.groupby "(in Python v3.15)")
:

In \[365\]: small \= pd.Series(
   .....:    range(6),
   .....:    index\=pd.to\_datetime(
   .....:        \[\
   .....:            "2017-01-01T00:00:00",\
   .....:            "2017-01-01T00:30:00",\
   .....:            "2017-01-01T00:31:00",\
   .....:            "2017-01-01T01:00:00",\
   .....:            "2017-01-01T03:00:00",\
   .....:            "2017-01-01T03:05:00",\
   .....:        \]
   .....:    ),
   .....: )
   .....: 

In \[366\]: resampled \= small.resample("h")

In \[367\]: for name, group in resampled:
   .....:    print("Group: ", name)
   .....:    print("-" \* 27)
   .....:    print(group, end\="\\n\\n")
   .....: 
Group:  2017-01-01 00:00:00
\---------------------------
2017\-01\-01 00:00:00    0
2017\-01\-01 00:30:00    1
2017\-01\-01 00:31:00    2
dtype: int64

Group:  2017-01-01 01:00:00
\---------------------------
2017\-01\-01 01:00:00    3
dtype: int64

Group:  2017-01-01 02:00:00
\---------------------------
Series(\[\], dtype: int64)

Group:  2017-01-01 03:00:00
\---------------------------
2017\-01\-01 03:00:00    4
2017\-01\-01 03:05:00    5
dtype: int64

Copy to clipboard

See [Iterating through groups](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-iterating-label)
 or `Resampler.__iter__` for more.

### Use `origin` or `offset` to adjust the start of the bins[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#use-origin-or-offset-to-adjust-the-start-of-the-bins "Link to this heading")

The bins of the grouping are adjusted based on the beginning of the day of the time series starting point. This works well with frequencies that are multiples of a day (like `30D`) or that divide a day evenly (like `90s` or `1min`). This can create inconsistencies with some frequencies that do not meet this criteria. To change this behavior you can specify a fixed Timestamp with the argument `origin`.

For example:

In \[368\]: start, end \= "2000-10-01 23:30:00", "2000-10-02 00:30:00"

In \[369\]: middle \= "2000-10-02 00:00:00"

In \[370\]: rng \= pd.date\_range(start, end, freq\="7min")

In \[371\]: ts \= pd.Series(np.arange(len(rng)) \* 3, index\=rng)

In \[372\]: ts
Out\[372\]: 
2000-10-01 23:30:00     0
2000-10-01 23:37:00     3
2000-10-01 23:44:00     6
2000-10-01 23:51:00     9
2000-10-01 23:58:00    12
2000-10-02 00:05:00    15
2000-10-02 00:12:00    18
2000-10-02 00:19:00    21
2000-10-02 00:26:00    24
Freq: 7min, dtype: int64

Copy to clipboard

Here we can see that, when using `origin` with its default value (`'start_day'`), the result after `'2000-10-02 00:00:00'` are not identical depending on the start of time series:

In \[373\]: ts.resample("17min", origin\="start\_day").sum()
Out\[373\]: 
2000-10-01 23:14:00     0
2000-10-01 23:31:00     9
2000-10-01 23:48:00    21
2000-10-02 00:05:00    54
2000-10-02 00:22:00    24
Freq: 17min, dtype: int64

In \[374\]: ts\[middle:end\].resample("17min", origin\="start\_day").sum()
Out\[374\]: 
2000-10-02 00:00:00    33
2000-10-02 00:17:00    45
Freq: 17min, dtype: int64

Copy to clipboard

Here we can see that, when setting `origin` to `'epoch'`, the result after `'2000-10-02 00:00:00'` are identical depending on the start of time series:

In \[375\]: ts.resample("17min", origin\="epoch").sum()
Out\[375\]: 
2000-10-01 23:18:00     0
2000-10-01 23:35:00    18
2000-10-01 23:52:00    27
2000-10-02 00:09:00    39
2000-10-02 00:26:00    24
Freq: 17min, dtype: int64

In \[376\]: ts\[middle:end\].resample("17min", origin\="epoch").sum()
Out\[376\]: 
2000-10-01 23:52:00    15
2000-10-02 00:09:00    39
2000-10-02 00:26:00    24
Freq: 17min, dtype: int64

Copy to clipboard

If needed you can use a custom timestamp for `origin`:

In \[377\]: ts.resample("17min", origin\="2001-01-01").sum()
Out\[377\]: 
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

In \[378\]: ts\[middle:end\].resample("17min", origin\=pd.Timestamp("2001-01-01")).sum()
Out\[378\]: 
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

Copy to clipboard

If needed you can just adjust the bins with an `offset` Timedelta that would be added to the default `origin`. Those two examples are equivalent for this time series:

In \[379\]: ts.resample("17min", origin\="start").sum()
Out\[379\]: 
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

In \[380\]: ts.resample("17min", offset\="23h30min").sum()
Out\[380\]: 
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

Copy to clipboard

Note the use of `'start'` for `origin` on the last example. In that case, `origin` will be set to the first value of the timeseries.

### Backward resample[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#backward-resample "Link to this heading")

Instead of adjusting the beginning of bins, sometimes we need to fix the end of the bins to make a backward resample with a given `freq`. The backward resample sets `closed` to `'right'` by default since the last value should be considered as the edge point for the last bin.

We can set `origin` to `'end'`. The value for a specific `Timestamp` index stands for the resample result from the current `Timestamp` minus `freq` to the current `Timestamp` with a right close.

In \[381\]: ts.resample('17min', origin\='end').sum()
Out\[381\]: 
2000-10-01 23:35:00     0
2000-10-01 23:52:00    18
2000-10-02 00:09:00    27
2000-10-02 00:26:00    63
Freq: 17min, dtype: int64

Copy to clipboard

Besides, in contrast with the `'start_day'` option, `end_day` is supported. This will set the origin as the ceiling midnight of the largest `Timestamp`.

In \[382\]: ts.resample('17min', origin\='end\_day').sum()
Out\[382\]: 
2000-10-01 23:38:00     3
2000-10-01 23:55:00    15
2000-10-02 00:12:00    45
2000-10-02 00:29:00    45
Freq: 17min, dtype: int64

Copy to clipboard

The above result uses `2000-10-02 00:29:00` as the last bin’s right edge since the following computation.

In \[383\]: ceil\_mid \= rng.max().ceil('D')

In \[384\]: freq \= pd.offsets.Minute(17)

In \[385\]: bin\_res \= ceil\_mid \- freq \* ((ceil\_mid \- rng.max()) // freq)

In \[386\]: bin\_res
Out\[386\]: Timestamp('2000-10-02 00:29:00')

Copy to clipboard

Time span representation[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-span-representation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Regular intervals of time are represented by `Period` objects in pandas while sequences of `Period` objects are collected in a `PeriodIndex`, which can be created with the convenience function `period_range`.

### Period[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#period "Link to this heading")

A `Period` represents a span of time (e.g., a day, a month, a quarter, etc). You can specify the span via `freq` keyword using a frequency alias like below. Because `freq` represents a span of `Period`, it cannot be negative like “-3D”.

In \[387\]: pd.Period("2012", freq\="Y-DEC")
Out\[387\]: Period('2012', 'Y-DEC')

In \[388\]: pd.Period("2012-1-1", freq\="D")
Out\[388\]: Period('2012-01-01', 'D')

In \[389\]: pd.Period("2012-1-1 19:00", freq\="h")
Out\[389\]: Period('2012-01-01 19:00', 'h')

In \[390\]: pd.Period("2012-1-1 19:00", freq\="5h")
Out\[390\]: Period('2012-01-01 19:00', '5h')

Copy to clipboard

Adding and subtracting integers from periods shifts the period by its own frequency. Arithmetic is not allowed between `Period` with different `freq` (span).

In \[391\]: p \= pd.Period("2012", freq\="Y-DEC")

In \[392\]: p + 1
Out\[392\]: Period('2013', 'Y-DEC')

In \[393\]: p \- 3
Out\[393\]: Period('2009', 'Y-DEC')

In \[394\]: p \= pd.Period("2012-01", freq\="2M")

In \[395\]: p + 2
Out\[395\]: Period('2012-05', '2M')

In \[396\]: p \- 1
Out\[396\]: Period('2011-11', '2M')

In \[397\]: p \== pd.Period("2012-01", freq\="3M")
Out\[397\]: False

Copy to clipboard

If `Period` freq is daily or higher (`D`, `h`, `min`, `s`, `ms`, `us`, and `ns`), `offsets` and `timedelta`\-like can be added if the result can have the same freq. Otherwise, `ValueError` will be raised.

In \[398\]: p \= pd.Period("2014-07-01 09:00", freq\="h")

In \[399\]: p + pd.offsets.Hour(2)
Out\[399\]: Period('2014-07-01 11:00', 'h')

In \[400\]: p + datetime.timedelta(minutes\=120)
Out\[400\]: Period('2014-07-01 11:00', 'h')

In \[401\]: p + np.timedelta64(7200, "s")
Out\[401\]: Period('2014-07-01 11:00', 'h')

Copy to clipboard

In \[402\]: p + pd.offsets.Minute(5)
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
File pandas/\_libs/tslibs/period.pyx:2241, in pandas.\_libs.tslibs.period.\_Period.\_add\_timedeltalike\_scalar()
\-> 2241 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/timedeltas.pyx:300, in pandas.\_libs.tslibs.timedeltas.delta\_to\_nanoseconds()
\--> 300 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/np\_datetime.pyx:827, in pandas.\_libs.tslibs.np\_datetime.convert\_reso()
\--> 827 'Could not get source, probably due dynamically evaluated source code.'
ValueError: Cannot losslessly convert units

The above exception was the direct cause of the following exception:

IncompatibleFrequency                     Traceback (most recent call last)
Cell In\[402\], line 1
\----> 1 p + pd.offsets.Minute(5)

File pandas/\_libs/tslibs/period.pyx:2262, in pandas.\_libs.tslibs.period.\_Period.\_\_add\_\_()
\-> 2262 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/period.pyx:2243, in pandas.\_libs.tslibs.period.\_Period.\_add\_timedeltalike\_scalar()
\-> 2243 'Could not get source, probably due dynamically evaluated source code.'
IncompatibleFrequency: Input cannot be converted to Period(freq=h)

Copy to clipboard

If `Period` has other frequencies, only the same `offsets` can be added. Otherwise, `ValueError` will be raised.

In \[403\]: p \= pd.Period("2014-07", freq\="M")

In \[404\]: p + pd.offsets.MonthEnd(3)
Out\[404\]: Period('2014-10', 'M')

Copy to clipboard

In \[405\]: p + pd.offsets.MonthBegin(3)
\---------------------------------------------------------------------------
IncompatibleFrequency                     Traceback (most recent call last)
Cell In\[405\], line 1
\----> 1 p + pd.offsets.MonthBegin(3)

File pandas/\_libs/tslibs/period.pyx:2264, in pandas.\_libs.tslibs.period.\_Period.\_\_add\_\_()
\-> 2264 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/period.pyx:2254, in pandas.\_libs.tslibs.period.\_Period.\_add\_offset()
\-> 2254 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/tslibs/period.pyx:2047, in pandas.\_libs.tslibs.period.PeriodMixin.\_require\_matching\_unit()
\-> 2047 'Could not get source, probably due dynamically evaluated source code.'
IncompatibleFrequency: Input has different freq=3MS from Period(freq=M)

Copy to clipboard

Taking the difference of `Period` instances with the same frequency will return the number of frequency units between them:

In \[406\]: pd.Period("2012", freq\="Y-DEC") \- pd.Period("2002", freq\="Y-DEC")
Out\[406\]: <10 \* YearEnds: month=12>

Copy to clipboard

### PeriodIndex and period\_range[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#periodindex-and-period-range "Link to this heading")

Regular sequences of `Period` objects can be collected in a `PeriodIndex`, which can be constructed using the `period_range` convenience function:

In \[407\]: prng \= pd.period\_range("1/1/2011", "1/1/2012", freq\="M")

In \[408\]: prng
Out\[408\]: 
PeriodIndex(\['2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06',\
             '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12',\
             '2012-01'\],
            dtype='period\[M\]')

Copy to clipboard

The `PeriodIndex` constructor can also be used directly:

In \[409\]: pd.PeriodIndex(\["2011-1", "2011-2", "2011-3"\], freq\="M")
Out\[409\]: PeriodIndex(\['2011-01', '2011-02', '2011-03'\], dtype='period\[M\]')

Copy to clipboard

Passing multiplied frequency outputs a sequence of `Period` which has multiplied span.

In \[410\]: pd.period\_range(start\="2014-01", freq\="3M", periods\=4)
Out\[410\]: PeriodIndex(\['2014-01', '2014-04', '2014-07', '2014-10'\], dtype='period\[3M\]')

Copy to clipboard

If `start` or `end` are `Period` objects, they will be used as anchor endpoints for a `PeriodIndex` with frequency matching that of the `PeriodIndex` constructor.

In \[411\]: pd.period\_range(
   .....:    start\=pd.Period("2017Q1", freq\="Q"), end\=pd.Period("2017Q2", freq\="Q"), freq\="M"
   .....: )
   .....: 
Out\[411\]: PeriodIndex(\['2017-03', '2017-04', '2017-05', '2017-06'\], dtype='period\[M\]')

Copy to clipboard

Just like `DatetimeIndex`, a `PeriodIndex` can also be used to index pandas objects:

In \[412\]: ps \= pd.Series(np.random.randn(len(prng)), prng)

In \[413\]: ps
Out\[413\]: 
2011-01   -2.916901
2011-02    0.514474
2011-03    1.346470
2011-04    0.816397
2011-05    2.258648
2011-06    0.494789
2011-07    0.301239
2011-08    0.464776
2011-09   -1.393581
2011-10    0.056780
2011-11    0.197035
2011-12    2.261385
2012-01   -0.329583
Freq: M, dtype: float64

Copy to clipboard

`PeriodIndex` supports addition and subtraction with the same rule as `Period`.

In \[414\]: idx \= pd.period\_range("2014-07-01 09:00", periods\=5, freq\="h")

In \[415\]: idx
Out\[415\]: 
PeriodIndex(\['2014-07-01 09:00', '2014-07-01 10:00', '2014-07-01 11:00',\
             '2014-07-01 12:00', '2014-07-01 13:00'\],
            dtype='period\[h\]')

In \[416\]: idx + pd.offsets.Hour(2)
Out\[416\]: 
PeriodIndex(\['2014-07-01 11:00', '2014-07-01 12:00', '2014-07-01 13:00',\
             '2014-07-01 14:00', '2014-07-01 15:00'\],
            dtype='period\[h\]')

In \[417\]: idx \= pd.period\_range("2014-07", periods\=5, freq\="M")

In \[418\]: idx
Out\[418\]: 
PeriodIndex(\['2014-07', '2014-08', '2014-09', '2014-10', '2014-11'\],
            dtype='period\[M\]')

In \[419\]: idx + pd.offsets.MonthEnd(3)
Out\[419\]: 
PeriodIndex(\['2014-10', '2014-11', '2014-12', '2015-01', '2015-02'\],
            dtype='period\[M\]')

Copy to clipboard

`PeriodIndex` has its own dtype named `period`, refer to [Period Dtypes](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-dtype)
.

### Period dtypes[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#period-dtypes "Link to this heading")

`PeriodIndex` has a custom `period` dtype. This is a pandas extension dtype similar to the [timezone aware dtype](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-timezone-series)
 (`datetime64[ns, tz]`).

The `period` dtype holds the `freq` attribute and is represented with `period[freq]` like `period[D]` or `period[M]`, using [frequency strings](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-aliases)
.

In \[420\]: pi \= pd.period\_range("2016-01-01", periods\=3, freq\="M")

In \[421\]: pi
Out\[421\]: PeriodIndex(\['2016-01', '2016-02', '2016-03'\], dtype='period\[M\]')

In \[422\]: pi.dtype
Out\[422\]: period\[M\]

Copy to clipboard

The `period` dtype can be used in `.astype(...)`. It allows one to change the `freq` of a `PeriodIndex` like `.asfreq()` and convert a `DatetimeIndex` to `PeriodIndex` like `to_period()`:

\# change monthly freq to daily freq
In \[423\]: pi.astype("period\[D\]")
Out\[423\]: PeriodIndex(\['2016-01-31', '2016-02-29', '2016-03-31'\], dtype='period\[D\]')

\# convert to DatetimeIndex
In \[424\]: pi.astype("datetime64\[ns\]")
Out\[424\]: 
DatetimeIndex(\['2016-01-01', '2016-02-01', '2016-03-01'\],
              dtype='datetime64\[ns\]', freq=None)

\# convert to PeriodIndex
In \[425\]: dti \= pd.date\_range("2011-01-01", freq\="ME", periods\=3)

In \[426\]: dti
Out\[426\]: 
DatetimeIndex(\['2011-01-31', '2011-02-28', '2011-03-31'\],
              dtype='datetime64\[us\]', freq='ME')

In \[427\]: dti.astype("period\[M\]")
Out\[427\]: PeriodIndex(\['2011-01', '2011-02', '2011-03'\], dtype='period\[M\]')

Copy to clipboard

### PeriodIndex partial string indexing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#periodindex-partial-string-indexing "Link to this heading")

PeriodIndex now supports partial string slicing with non-monotonic indexes.

You can pass in dates and strings to `Series` and `DataFrame` with `PeriodIndex`, in the same manner as `DatetimeIndex`. For details, refer to [DatetimeIndex Partial String Indexing](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-partialindexing)
.

In \[428\]: ps\["2011-01"\]
Out\[428\]: np.float64(-2.9169013294054507)

In \[429\]: ps\[datetime.datetime(2011, 12, 25):\]
Out\[429\]: 
2011-12    2.261385
2012-01   -0.329583
Freq: M, dtype: float64

In \[430\]: ps\["10/31/2011":"12/31/2011"\]
Out\[430\]: 
2011-10    0.056780
2011-11    0.197035
2011-12    2.261385
Freq: M, dtype: float64

Copy to clipboard

Passing a string representing a lower frequency than `PeriodIndex` returns partial sliced data.

In \[431\]: ps\["2011"\]
Out\[431\]: 
2011-01   -2.916901
2011-02    0.514474
2011-03    1.346470
2011-04    0.816397
2011-05    2.258648
2011-06    0.494789
2011-07    0.301239
2011-08    0.464776
2011-09   -1.393581
2011-10    0.056780
2011-11    0.197035
2011-12    2.261385
Freq: M, dtype: float64

In \[432\]: dfp \= pd.DataFrame(
   .....:    np.random.randn(600, 1),
   .....:    columns\=\["A"\],
   .....:    index\=pd.period\_range("2013-01-01 9:00", periods\=600, freq\="min"),
   .....: )
   .....: 

In \[433\]: dfp
Out\[433\]: 
                         A
2013-01-01 09:00 -0.538468
2013-01-01 09:01 -1.365819
2013-01-01 09:02 -0.969051
2013-01-01 09:03 -0.331152
2013-01-01 09:04 -0.245334
...                    ...
2013-01-01 18:55  0.522460
2013-01-01 18:56  0.118710
2013-01-01 18:57  0.167517
2013-01-01 18:58  0.922883
2013-01-01 18:59  1.721104

\[600 rows x 1 columns\]

In \[434\]: dfp.loc\["2013-01-01 10h"\]
Out\[434\]: 
                         A
2013-01-01 10:00 -0.308975
2013-01-01 10:01  0.542520
2013-01-01 10:02  1.061068
2013-01-01 10:03  0.754005
2013-01-01 10:04  0.352933
...                    ...
2013-01-01 10:55 -0.865621
2013-01-01 10:56 -1.167818
2013-01-01 10:57 -2.081748
2013-01-01 10:58 -0.527146
2013-01-01 10:59  0.802298

\[60 rows x 1 columns\]

Copy to clipboard

As with `DatetimeIndex`, the endpoints will be included in the result. The example below slices data starting from 10:00 to 11:59.

In \[435\]: dfp\["2013-01-01 10h":"2013-01-01 11h"\]
Out\[435\]: 
                         A
2013-01-01 10:00 -0.308975
2013-01-01 10:01  0.542520
2013-01-01 10:02  1.061068
2013-01-01 10:03  0.754005
2013-01-01 10:04  0.352933
...                    ...
2013-01-01 11:55 -0.590204
2013-01-01 11:56  1.539990
2013-01-01 11:57 -1.224826
2013-01-01 11:58  0.578798
2013-01-01 11:59 -0.685496

\[120 rows x 1 columns\]

Copy to clipboard

### Frequency conversion and resampling with PeriodIndex[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#frequency-conversion-and-resampling-with-periodindex "Link to this heading")

The frequency of `Period` and `PeriodIndex` can be converted via the `asfreq` method. Let’s start with the fiscal year 2011, ending in December:

In \[436\]: p \= pd.Period("2011", freq\="Y-DEC")

In \[437\]: p
Out\[437\]: Period('2011', 'Y-DEC')

Copy to clipboard

We can convert it to a monthly frequency. Using the `how` parameter, we can specify whether to return the starting or ending month:

In \[438\]: p.asfreq("M", how\="start")
Out\[438\]: Period('2011-01', 'M')

In \[439\]: p.asfreq("M", how\="end")
Out\[439\]: Period('2011-12', 'M')

Copy to clipboard

The shorthands ‘s’ and ‘e’ are provided for convenience:

In \[440\]: p.asfreq("M", "s")
Out\[440\]: Period('2011-01', 'M')

In \[441\]: p.asfreq("M", "e")
Out\[441\]: Period('2011-12', 'M')

Copy to clipboard

Converting to a “super-period” (e.g., annual frequency is a super-period of quarterly frequency) automatically returns the super-period that includes the input period:

In \[442\]: p \= pd.Period("2011-12", freq\="M")

In \[443\]: p.asfreq("Y-NOV")
Out\[443\]: Period('2012', 'Y-NOV')

Copy to clipboard

Note that since we converted to an annual frequency that ends the year in November, the monthly period of December 2011 is actually in the 2012 Y-NOV period.

Period conversions with anchored frequencies are particularly useful for working with various quarterly data common to economics, business, and other fields. Many organizations define quarters relative to the month in which their fiscal year starts and ends. Thus, first quarter of 2011 could start in 2010 or a few months into 2011. Via anchored frequencies, pandas works for all quarterly frequencies `Q-JAN` through `Q-DEC`.

`Q-DEC` define regular calendar quarters:

In \[444\]: p \= pd.Period("2012Q1", freq\="Q-DEC")

In \[445\]: p.asfreq("D", "s")
Out\[445\]: Period('2012-01-01', 'D')

In \[446\]: p.asfreq("D", "e")
Out\[446\]: Period('2012-03-31', 'D')

Copy to clipboard

`Q-MAR` defines fiscal year end in March:

In \[447\]: p \= pd.Period("2011Q4", freq\="Q-MAR")

In \[448\]: p.asfreq("D", "s")
Out\[448\]: Period('2011-01-01', 'D')

In \[449\]: p.asfreq("D", "e")
Out\[449\]: Period('2011-03-31', 'D')

Copy to clipboard

Converting between representations[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-between-representations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Timestamped data can be converted to PeriodIndex-ed data using `to_period` and vice-versa using `to_timestamp`:

In \[450\]: rng \= pd.date\_range("1/1/2012", periods\=5, freq\="ME")

In \[451\]: ts \= pd.Series(np.random.randn(len(rng)), index\=rng)

In \[452\]: ts
Out\[452\]: 
2012-01-31    1.931253
2012-02-29   -0.184594
2012-03-31    0.249656
2012-04-30   -0.978151
2012-05-31   -0.873389
Freq: ME, dtype: float64

In \[453\]: ps \= ts.to\_period()

In \[454\]: ps
Out\[454\]: 
2012-01    1.931253
2012-02   -0.184594
2012-03    0.249656
2012-04   -0.978151
2012-05   -0.873389
Freq: M, dtype: float64

In \[455\]: ps.to\_timestamp()
Out\[455\]: 
2012-01-01    1.931253
2012-02-01   -0.184594
2012-03-01    0.249656
2012-04-01   -0.978151
2012-05-01   -0.873389
Freq: MS, dtype: float64

Copy to clipboard

Remember that ‘s’ and ‘e’ can be used to return the timestamps at the start or end of the period:

In \[456\]: ps.to\_timestamp("D", how\="s")
Out\[456\]: 
2012-01-01    1.931253
2012-02-01   -0.184594
2012-03-01    0.249656
2012-04-01   -0.978151
2012-05-01   -0.873389
Freq: MS, dtype: float64

Copy to clipboard

Converting between period and timestamp enables some convenient arithmetic functions to be used. In the following example, we convert a quarterly frequency with year ending in November to 9am of the end of the month following the quarter end:

In \[457\]: prng \= pd.period\_range("1990Q1", "2000Q4", freq\="Q-NOV")

In \[458\]: ts \= pd.Series(np.random.randn(len(prng)), prng)

In \[459\]: ts.index \= (prng.asfreq("M", "e") + 1).asfreq("h", "s") + 9

In \[460\]: ts.head()
Out\[460\]: 
1990-03-01 09:00   -0.109291
1990-06-01 09:00   -0.637235
1990-09-01 09:00   -1.735925
1990-12-01 09:00    2.096946
1991-03-01 09:00   -1.039926
Freq: h, dtype: float64

Copy to clipboard

Representing out-of-bounds spans[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#representing-out-of-bounds-spans "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

If you have data that is outside of the `Timestamp` bounds, see [Timestamp limitations](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-timestamp-limits)
, then you can use a `PeriodIndex` and/or `Series` of `Periods` to do computations.

In \[461\]: span \= pd.period\_range("1215-01-01", "1381-01-01", freq\="D")

In \[462\]: span
Out\[462\]: 
PeriodIndex(\['1215-01-01', '1215-01-02', '1215-01-03', '1215-01-04',\
             '1215-01-05', '1215-01-06', '1215-01-07', '1215-01-08',\
             '1215-01-09', '1215-01-10',\
             ...\
             '1380-12-23', '1380-12-24', '1380-12-25', '1380-12-26',\
             '1380-12-27', '1380-12-28', '1380-12-29', '1380-12-30',\
             '1380-12-31', '1381-01-01'\],
            dtype='period\[D\]', length=60632)

Copy to clipboard

To convert from an `int64` based YYYYMMDD representation.

In \[463\]: s \= pd.Series(\[20121231, 20141130, 99991231\])

In \[464\]: s
Out\[464\]: 
0    20121231
1    20141130
2    99991231
dtype: int64

In \[465\]: def conv(x):
   .....:    return pd.Period(year\=x // 10000, month\=x // 100 % 100, day\=x % 100, freq\="D")
   .....: 

In \[466\]: s.apply(conv)
Out\[466\]: 
0    2012-12-31
1    2014-11-30
2    9999-12-31
dtype: period\[D\]

In \[467\]: s.apply(conv)\[2\]
Out\[467\]: Period('9999-12-31', 'D')

Copy to clipboard

These can easily be converted to a `PeriodIndex`:

In \[468\]: span \= pd.PeriodIndex(s.apply(conv))

In \[469\]: span
Out\[469\]: PeriodIndex(\['2012-12-31', '2014-11-30', '9999-12-31'\], dtype='period\[D\]')

Copy to clipboard

Time zone handling[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

pandas provides rich support for working with timestamps in different time zones using the `zoneinfo`, `pytz` and `dateutil` libraries or [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "(in Python v3.15)")
 objects from the standard library.

### Working with time zones[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#working-with-time-zones "Link to this heading")

By default, pandas objects are time zone unaware:

In \[470\]: rng \= pd.date\_range("3/6/2012 00:00", periods\=15, freq\="D")

In \[471\]: rng.tz is None
Out\[471\]: True

Copy to clipboard

To localize these dates to a time zone (assign a particular time zone to a naive date), you can use the `tz_localize` method or the `tz` keyword argument in [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")
, [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
, or [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
. You can either pass `zoneinfo`, `pytz` or `dateutil` time zone objects or Olson time zone database strings. Olson time zone strings will return `zoneinfo` time zone objects by default. To return `dateutil` time zone objects, append `dateutil/` before the string.

*   For `zoneinfo`, a list of available timezones are available from [`zoneinfo.available_timezones()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones "(in Python v3.15)")
    .
    
*   If `pytz` is installed (optional), you can find a list of common (and less common) time zones using `pytz.all_timezones`.
    
*   `dateutil` uses the OS time zones so there isn’t a fixed list available. For common zones, the names are the same as `zoneinfo`.
    

In \[472\]: import dateutil

In \[473\]: from zoneinfo import ZoneInfo

\# zoneinfo (default when using Olson strings)
In \[474\]: rng\_zi \= pd.date\_range("3/6/2012 00:00", periods\=3, freq\="D", tz\="Europe/London")

In \[475\]: rng\_zi.tz
Out\[475\]: zoneinfo.ZoneInfo(key='Europe/London')

\# dateutil
In \[476\]: rng\_dateutil \= pd.date\_range("3/6/2012 00:00", periods\=3, freq\="D")

In \[477\]: rng\_dateutil \= rng\_dateutil.tz\_localize("dateutil/Europe/London")

In \[478\]: rng\_dateutil.tz
Out\[478\]: tzfile('/usr/share/zoneinfo/Europe/London')

\# dateutil - utc special case
In \[479\]: rng\_utc \= pd.date\_range(
   .....:    "3/6/2012 00:00",
   .....:    periods\=3,
   .....:    freq\="D",
   .....:    tz\=dateutil.tz.tzutc(),
   .....: )
   .....: 

In \[480\]: rng\_utc.tz
Out\[480\]: tzutc()

Copy to clipboard

\# datetime.timezone
In \[481\]: rng\_utc \= pd.date\_range(
   .....:    "3/6/2012 00:00",
   .....:    periods\=3,
   .....:    freq\="D",
   .....:    tz\=datetime.timezone.utc,
   .....: )
   .....: 

In \[482\]: rng\_utc.tz
Out\[482\]: datetime.timezone.utc

Copy to clipboard

Note that the `UTC` time zone is a special case in `dateutil` and should be constructed explicitly as an instance of `dateutil.tz.tzutc`. You can also construct other time zones objects explicitly first.

\# zoneinfo
In \[483\]: tz\_zi \= ZoneInfo("Europe/London")

In \[484\]: rng\_zi \= pd.date\_range("3/6/2012 00:00", periods\=3, freq\="D")

In \[485\]: rng\_zi \= rng\_zi.tz\_localize(tz\_zi)

In \[486\]: rng\_zi.tz \== tz\_zi
Out\[486\]: True

\# dateutil
In \[487\]: tz\_dateutil \= dateutil.tz.gettz("Europe/London")

In \[488\]: rng\_dateutil \= pd.date\_range("3/6/2012 00:00", periods\=3, freq\="D", tz\=tz\_dateutil)

In \[489\]: rng\_dateutil.tz \== tz\_dateutil
Out\[489\]: True

Copy to clipboard

To convert a time zone aware pandas object from one time zone to another, you can use the `tz_convert` method.

In \[490\]: rng\_zi.tz\_convert("US/Eastern")
Out\[490\]: 
DatetimeIndex(\['2012-03-05 19:00:00-05:00', '2012-03-06 19:00:00-05:00',\
               '2012-03-07 19:00:00-05:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq=None)

Copy to clipboard

Warning

Be wary of conversions between time zone libraries. For some time zones, different libraries may have different definitions of the zone. This is more of a problem for unusual time zones than for ‘standard’ zones like `US/Eastern`.

Warning

Be aware that a time zone definition across versions of time zone libraries may not be considered equal. This may cause problems when working with stored data that is localized using one version and operated on with a different version. See [here](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5-notes)
 for how to handle such a situation.

Warning

Be aware that for times in the future, correct conversion between time zones (and UTC) cannot be guaranteed by any time zone library because a timezone’s offset from UTC may be changed by the respective government.

Under the hood, all timestamps are stored in UTC. Values from a time zone aware [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 or [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 will have their fields (day, hour, minute, etc.) localized to the time zone. However, timestamps with the same UTC value are still considered to be equal even if they are in different time zones:

In \[491\]: rng\_eastern \= rng\_utc.tz\_convert("US/Eastern")

In \[492\]: rng\_berlin \= rng\_utc.tz\_convert("Europe/Berlin")

In \[493\]: rng\_eastern\[2\]
Out\[493\]: Timestamp('2012-03-07 19:00:00-0500', tz='US/Eastern')

In \[494\]: rng\_berlin\[2\]
Out\[494\]: Timestamp('2012-03-08 01:00:00+0100', tz='Europe/Berlin')

In \[495\]: rng\_eastern\[2\] \== rng\_berlin\[2\]
Out\[495\]: True

Copy to clipboard

Operations between [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 in different time zones will yield UTC [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, aligning the data on the UTC timestamps:

In \[496\]: ts\_utc \= pd.Series(range(3), pd.date\_range("20130101", periods\=3, tz\="UTC"))

In \[497\]: eastern \= ts\_utc.tz\_convert("US/Eastern")

In \[498\]: berlin \= ts\_utc.tz\_convert("Europe/Berlin")

In \[499\]: result \= eastern + berlin

In \[500\]: result
Out\[500\]: 
2013-01-01 00:00:00+00:00    0
2013-01-02 00:00:00+00:00    2
2013-01-03 00:00:00+00:00    4
dtype: int64

In \[501\]: result.index
Out\[501\]: 
DatetimeIndex(\['2013-01-01 00:00:00+00:00', '2013-01-02 00:00:00+00:00',\
               '2013-01-03 00:00:00+00:00'\],
              dtype='datetime64\[us, UTC\]', freq=None)

Copy to clipboard

To remove time zone information, use `tz_localize(None)` or `tz_convert(None)`. `tz_localize(None)` will remove the time zone yielding the local time representation. `tz_convert(None)` will remove the time zone after converting to UTC time.

In \[502\]: didx \= pd.date\_range(start\="2014-08-01 09:00", freq\="h", periods\=3, tz\="US/Eastern")

In \[503\]: didx
Out\[503\]: 
DatetimeIndex(\['2014-08-01 09:00:00-04:00', '2014-08-01 10:00:00-04:00',\
               '2014-08-01 11:00:00-04:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq='h')

In \[504\]: didx.tz\_localize(None)
Out\[504\]: 
DatetimeIndex(\['2014-08-01 09:00:00', '2014-08-01 10:00:00',\
               '2014-08-01 11:00:00'\],
              dtype='datetime64\[us\]', freq=None)

In \[505\]: didx.tz\_convert(None)
Out\[505\]: 
DatetimeIndex(\['2014-08-01 13:00:00', '2014-08-01 14:00:00',\
               '2014-08-01 15:00:00'\],
              dtype='datetime64\[us\]', freq='h')

\# tz\_convert(None) is identical to tz\_convert('UTC').tz\_localize(None)
In \[506\]: didx.tz\_convert("UTC").tz\_localize(None)
Out\[506\]: 
DatetimeIndex(\['2014-08-01 13:00:00', '2014-08-01 14:00:00',\
               '2014-08-01 15:00:00'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

### Fold[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#fold "Link to this heading")

For ambiguous times, pandas supports explicitly specifying the keyword-only fold argument. Due to daylight saving time, one wall clock time can occur twice when shifting from summer to winter time; fold describes whether the datetime-like corresponds to the first (0) or the second time (1) the wall clock hits the ambiguous time. Fold is supported only for constructing from naive `datetime.datetime` (see [datetime documentation](https://docs.python.org/3/library/datetime.html)
 for details) or from [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 or for constructing from components (see below). Fold is supported with `zoneinfo` and `dateutil` timezones. We recommend using [`Timestamp.tz_localize()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")
 when localizing ambiguous datetimes if you need direct control over how they are handled.

In \[507\]: pd.Timestamp(
   .....:    datetime.datetime(2019, 10, 27, 1, 30, 0, 0),
   .....:    tz\="dateutil/Europe/London",
   .....:    fold\=0,
   .....: )
   .....: 
Out\[507\]: Timestamp('2019-10-27 01:30:00+0100', tz='dateutil//usr/share/zoneinfo/Europe/London')

In \[508\]: pd.Timestamp(
   .....:    year\=2019,
   .....:    month\=10,
   .....:    day\=27,
   .....:    hour\=1,
   .....:    minute\=30,
   .....:    tz\="dateutil/Europe/London",
   .....:    fold\=1,
   .....: )
   .....: 
Out\[508\]: Timestamp('2019-10-27 01:30:00+0000', tz='dateutil//usr/share/zoneinfo/Europe/London')

Copy to clipboard

### Ambiguous times when localizing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#ambiguous-times-when-localizing "Link to this heading")

`tz_localize` may not be able to determine the UTC offset of a timestamp because daylight savings time (DST) in a local time zone causes some times to occur twice within one day (“clocks fall back”). The following options are available:

*   `'raise'`: Raises a `ValueError` (the default behavior)
    
*   `'infer'`: Attempt to determine the correct offset based on the monotonicity of the timestamps
    
*   `'NaT'`: Replaces ambiguous times with `NaT`
    
*   `bool`: `True` represents a DST time, `False` represents non-DST time. An array-like of `bool` values is supported for a sequence of times.
    

In \[509\]: rng\_hourly \= pd.DatetimeIndex(
   .....:    \["11/06/2011 00:00", "11/06/2011 01:00", "11/06/2011 01:00", "11/06/2011 02:00"\]
   .....: )
   .....: 

Copy to clipboard

This will fail as there are ambiguous times (`'11/06/2011 01:00'`)

In \[510\]: rng\_hourly.tz\_localize('US/Eastern')
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[510\], line 1
\----> 1 rng\_hourly.tz\_localize('US/Eastern')

File ~/work/pandas/pandas/pandas/core/indexes/datetimes.py:1709, in DatetimeIndex.tz\_localize(self, tz, ambiguous, nonexistent)
   1568 """
   1569 Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index.
   1570 
   (...)   1706 dtype: datetime64\[ns, Europe/Warsaw\]
   1707 """  \# noqa: E501
   1708 freq \= self.\_freq
\-> 1709 arr \= self.\_data.tz\_localize(tz, ambiguous, nonexistent)
   1710 result \= type(self).\_simple\_new(arr, name\=self.name)
   1711 if timezones.is\_utc(arr.tz) or (len(arr) \== 1 and arr\[0\] is not NaT):
   1712     \# we can preserve freq
   1713     \# TODO: Also for fixed-offsets

File ~/work/pandas/pandas/pandas/core/arrays/\_mixins.py:82, in ravel\_compat.<locals>.method(self, \*args, \*\*kwargs)
     79 @wraps(meth)
     80 def method(self, \*args, \*\*kwargs):
     81     if self.ndim \== 1:
\---> 82         return meth(self, \*args, \*\*kwargs)
     84     flags \= self.\_ndarray.flags
     85     flat \= self.ravel("K")

File ~/work/pandas/pandas/pandas/core/arrays/datetimes.py:1115, in DatetimeArray.tz\_localize(self, tz, ambiguous, nonexistent)
   1112     tz \= timezones.maybe\_get\_tz(tz)
   1113     \# Convert to UTC
\-> 1115     new\_dates \= tzconversion.tz\_localize\_to\_utc(
   1116         self.asi8,
   1117         tz,
   1118         ambiguous\=ambiguous,
   1119         nonexistent\=nonexistent,
   1120         creso\=self.\_creso,
   1121     )
   1122 new\_dates\_dt64 \= new\_dates.view(f"M8\[{self.unit}\]")
   1123 dtype \= tz\_to\_dtype(tz, unit\=self.unit)

File pandas/\_libs/tslibs/tzconversion.pyx:441, in pandas.\_libs.tslibs.tzconversion.tz\_localize\_to\_utc()
\--> 441 'Could not get source, probably due dynamically evaluated source code.'
ValueError: Cannot infer dst time from 2011-11-06 01:00:00, try using the 'ambiguous' argument

Copy to clipboard

Handle these ambiguous times by specifying the following.

In \[511\]: rng\_hourly.tz\_localize("US/Eastern", ambiguous\="infer")
Out\[511\]: 
DatetimeIndex(\['2011-11-06 00:00:00-04:00', '2011-11-06 01:00:00-04:00',\
               '2011-11-06 01:00:00-05:00', '2011-11-06 02:00:00-05:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq=None)

In \[512\]: rng\_hourly.tz\_localize("US/Eastern", ambiguous\="NaT")
Out\[512\]: 
DatetimeIndex(\['2011-11-06 00:00:00-04:00', 'NaT', 'NaT',\
               '2011-11-06 02:00:00-05:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq=None)

In \[513\]: rng\_hourly.tz\_localize("US/Eastern", ambiguous\=\[True, True, False, False\])
Out\[513\]: 
DatetimeIndex(\['2011-11-06 00:00:00-04:00', '2011-11-06 01:00:00-04:00',\
               '2011-11-06 01:00:00-05:00', '2011-11-06 02:00:00-05:00'\],
              dtype='datetime64\[us, US/Eastern\]', freq=None)

Copy to clipboard

### Nonexistent times when localizing[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#nonexistent-times-when-localizing "Link to this heading")

A DST transition may also shift the local time ahead by 1 hour creating nonexistent local times (“clocks spring forward”). The behavior of localizing a timeseries with nonexistent times can be controlled by the `nonexistent` argument. The following options are available:

*   `'raise'`: Raises a `ValueError` (the default behavior)
    
*   `'NaT'`: Replaces nonexistent times with `NaT`
    
*   `'shift_forward'`: Shifts nonexistent times forward to the closest real time
    
*   `'shift_backward'`: Shifts nonexistent times backward to the closest real time
    
*   timedelta object: Shifts nonexistent times by the timedelta duration
    

In \[514\]: dti \= pd.date\_range(start\="2015-03-29 02:30:00", periods\=3, freq\="h")

\# 2:30 is a nonexistent time

Copy to clipboard

Localization of nonexistent times will raise an error by default.

In \[515\]: dti.tz\_localize('Europe/Warsaw')
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[515\], line 1
\----> 1 dti.tz\_localize('Europe/Warsaw')

File ~/work/pandas/pandas/pandas/core/indexes/datetimes.py:1709, in DatetimeIndex.tz\_localize(self, tz, ambiguous, nonexistent)
   1568 """
   1569 Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index.
   1570 
   (...)   1706 dtype: datetime64\[ns, Europe/Warsaw\]
   1707 """  \# noqa: E501
   1708 freq \= self.\_freq
\-> 1709 arr \= self.\_data.tz\_localize(tz, ambiguous, nonexistent)
   1710 result \= type(self).\_simple\_new(arr, name\=self.name)
   1711 if timezones.is\_utc(arr.tz) or (len(arr) \== 1 and arr\[0\] is not NaT):
   1712     \# we can preserve freq
   1713     \# TODO: Also for fixed-offsets

File ~/work/pandas/pandas/pandas/core/arrays/\_mixins.py:82, in ravel\_compat.<locals>.method(self, \*args, \*\*kwargs)
     79 @wraps(meth)
     80 def method(self, \*args, \*\*kwargs):
     81     if self.ndim \== 1:
\---> 82         return meth(self, \*args, \*\*kwargs)
     84     flags \= self.\_ndarray.flags
     85     flat \= self.ravel("K")

File ~/work/pandas/pandas/pandas/core/arrays/datetimes.py:1115, in DatetimeArray.tz\_localize(self, tz, ambiguous, nonexistent)
   1112     tz \= timezones.maybe\_get\_tz(tz)
   1113     \# Convert to UTC
\-> 1115     new\_dates \= tzconversion.tz\_localize\_to\_utc(
   1116         self.asi8,
   1117         tz,
   1118         ambiguous\=ambiguous,
   1119         nonexistent\=nonexistent,
   1120         creso\=self.\_creso,
   1121     )
   1122 new\_dates\_dt64 \= new\_dates.view(f"M8\[{self.unit}\]")
   1123 dtype \= tz\_to\_dtype(tz, unit\=self.unit)

File pandas/\_libs/tslibs/tzconversion.pyx:530, in pandas.\_libs.tslibs.tzconversion.tz\_localize\_to\_utc()
\--> 530 'Could not get source, probably due dynamically evaluated source code.'
ValueError: 2015-03-29 02:30:00 is a nonexistent time due to daylight savings time. Try using the 'nonexistent' argument.

Copy to clipboard

Transform nonexistent times to `NaT` or shift the times.

In \[516\]: dti
Out\[516\]: 
DatetimeIndex(\['2015-03-29 02:30:00', '2015-03-29 03:30:00',\
               '2015-03-29 04:30:00'\],
              dtype='datetime64\[us\]', freq='h')

In \[517\]: dti.tz\_localize("Europe/Warsaw", nonexistent\="shift\_forward")
Out\[517\]: 
DatetimeIndex(\['2015-03-29 03:00:00+02:00', '2015-03-29 03:30:00+02:00',\
               '2015-03-29 04:30:00+02:00'\],
              dtype='datetime64\[us, Europe/Warsaw\]', freq=None)

In \[518\]: dti.tz\_localize("Europe/Warsaw", nonexistent\="shift\_backward")
Out\[518\]: 
DatetimeIndex(\['2015-03-29 01:59:59.999999+01:00',\
                      '2015-03-29 03:30:00+02:00',\
                      '2015-03-29 04:30:00+02:00'\],
              dtype='datetime64\[us, Europe/Warsaw\]', freq=None)

In \[519\]: dti.tz\_localize("Europe/Warsaw", nonexistent\=pd.Timedelta(1, unit\="h"))
Out\[519\]: 
DatetimeIndex(\['2015-03-29 03:30:00+02:00', '2015-03-29 03:30:00+02:00',\
               '2015-03-29 04:30:00+02:00'\],
              dtype='datetime64\[us, Europe/Warsaw\]', freq=None)

In \[520\]: dti.tz\_localize("Europe/Warsaw", nonexistent\="NaT")
Out\[520\]: 
DatetimeIndex(\['NaT', '2015-03-29 03:30:00+02:00',\
               '2015-03-29 04:30:00+02:00'\],
              dtype='datetime64\[us, Europe/Warsaw\]', freq=None)

Copy to clipboard

### Time zone Series operations[#](https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-series-operations "Link to this heading")

A [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 with time zone **naive** values is represented with a dtype of `datetime64[us]`.

In \[521\]: s\_naive \= pd.Series(pd.date\_range("20130101", periods\=3))

In \[522\]: s\_naive
Out\[522\]: 
0   2013-01-01
1   2013-01-02
2   2013-01-03
dtype: datetime64\[us\]

Copy to clipboard

A [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 with a time zone **aware** values is represented with a dtype of `datetime64[us, tz]` where `tz` is the time zone

In \[523\]: s\_aware \= pd.Series(pd.date\_range("20130101", periods\=3, tz\="US/Eastern"))

In \[524\]: s\_aware
Out\[524\]: 
0   2013-01-01 00:00:00-05:00
1   2013-01-02 00:00:00-05:00
2   2013-01-03 00:00:00-05:00
dtype: datetime64\[us, US/Eastern\]

Copy to clipboard

Both of these [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 time zone information can be manipulated via the `.dt` accessor, see [the dt accessor section](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dt-accessors)
.

For example, to localize and convert a naive stamp to time zone aware.

In \[525\]: s\_naive.dt.tz\_localize("UTC").dt.tz\_convert("US/Eastern")
Out\[525\]: 
0   2012-12-31 19:00:00-05:00
1   2013-01-01 19:00:00-05:00
2   2013-01-02 19:00:00-05:00
dtype: datetime64\[us, US/Eastern\]

Copy to clipboard

Time zone information can also be manipulated using the `astype` method. This method can convert between different timezone-aware dtypes.

\# convert to a new time zone
In \[526\]: s\_aware.astype("datetime64\[us, CET\]")
Out\[526\]: 
0   2013-01-01 06:00:00+01:00
1   2013-01-02 06:00:00+01:00
2   2013-01-03 06:00:00+01:00
dtype: datetime64\[us, CET\]

Copy to clipboard

Note

Using [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 on a `Series`, returns a NumPy array of the data. NumPy does not currently support time zones (even though it is _printing_ in the local time zone!), therefore an object array of Timestamps is returned for time zone aware data:

In \[527\]: s\_naive.to\_numpy()
Out\[527\]: 
array(\['2013-01-01T00:00:00.000000', '2013-01-02T00:00:00.000000',\
       '2013-01-03T00:00:00.000000'\], dtype='datetime64\[us\]')

In \[528\]: s\_aware.to\_numpy()
Out\[528\]: 
array(\[Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'),\
       Timestamp('2013-01-02 00:00:00-0500', tz='US/Eastern'),\
       Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')\],
      dtype=object)

Copy to clipboard

This object-dtype default is significantly slower and more memory-intensive than a native `datetime64` array. For better performance, pass an explicit `dtype`:

In \[529\]: s\_aware.to\_numpy(dtype\="datetime64\[us\]")
Out\[529\]: 
array(\['2013-01-01T05:00:00.000000', '2013-01-02T05:00:00.000000',\
       '2013-01-03T05:00:00.000000'\], dtype='datetime64\[us\]')

Copy to clipboard

This converts to UTC and drops the timezone, returning a native `datetime64` array. If you need to preserve per-element timezone information (e.g. when converting back to a Series), use `dtype=object` explicitly:

In \[530\]: pd.Series(s\_aware.to\_numpy(dtype\=object))
Out\[530\]: 
0   2013-01-01 00:00:00-05:00
1   2013-01-02 00:00:00-05:00
2   2013-01-03 00:00:00-05:00
dtype: datetime64\[us, US/Eastern\]

Copy to clipboard

On this page