[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.to_datetime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.to_datetime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.to_datetime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.to_datetime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.to_datetime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.to_datetime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.to_datetime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.to_datetime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.to_datetime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.to_datetime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.to_datetime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.to_datetime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.to\_datetime[#](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas-to-datetime "Link to this heading")

=======================================================================================================================================

pandas.to\_datetime(_arg_, _errors\='raise'_, _dayfirst\=False_, _yearfirst\=False_, _utc\=False_, _format\=None_, _exact\=<no\_default>_, _unit\=None_, _origin\='unix'_, _cache\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/tools/datetimes.py#L834-L1280)
[#](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "Link to this definition")

Convert argument to datetime.

This function converts a scalar, array-like, [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
/dict-like to a pandas datetime object.

Parameters:

**arg**int, float, str, datetime, list, tuple, 1-d array, Series, DataFrame/dict-like

The object to convert to a datetime. If a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 is provided, the method expects minimally the following columns: `"year"`, `"month"`, `"day"`. The column “year” must be specified in 4-digit format.

**errors**{‘raise’, ‘coerce’}, default ‘raise’

*   If `'raise'`, then invalid parsing will raise an exception.
    
*   If `'coerce'`, then invalid parsing will be set as [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
    .
    

**dayfirst**bool, default False

Specify a date parse order if arg is str or is list-like. If `True`, parses dates with the day first, e.g. `"10/11/12"` is parsed as `2012-11-10`.

Warning

`dayfirst=True` is not strict, but will prefer to parse with day first.

**yearfirst**bool, default False

Specify a date parse order if arg is str or is list-like.

*   If `True` parses dates with the year first, e.g. `"10/11/12"` is parsed as `2010-11-12`.
    
*   If both dayfirst and yearfirst are `True`, yearfirst is preceded (same as `dateutil`).
    

Warning

`yearfirst=True` is not strict, but will prefer to parse with year first.

**utc**bool, default False

Control timezone-related parsing, localization and conversion.

*   If `True`, the function _always_ returns a timezone-aware UTC-localized [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
    , [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     or [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
    . To do this, timezone-naive inputs are _localized_ as UTC, while timezone-aware inputs are _converted_ to UTC.
    
*   If `False` (default), inputs will not be coerced to UTC. Timezone-naive inputs will remain naive, while timezone-aware ones will keep their time offsets. Limitations exist for mixed offsets (typically, daylight savings), see [Examples](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#to-datetime-tz-examples)
     section for details.
    

See also: pandas general documentation about [timezone conversion and localization](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-zone-handling)
.

**format**str, default None

The strftime to parse time, e.g. `"%d/%m/%Y"`. See [strftime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
 for more information on choices, though note that `"%f"` will parse all the way up to nanoseconds. You can also pass:

*   “ISO8601”, to parse any [ISO8601](https://en.wikipedia.org/wiki/ISO_8601)
     time string (not necessarily in exactly the same format);
    
*   “mixed”, to infer the format for each element individually. This is risky, and you should probably use it along with dayfirst.
    

Deprecated since version 3.1.0: Passing integer or float values together with `format` is deprecated; cast them to strings first. In a future version numeric values will be interpreted as epochs via `unit` instead, and `format` will only apply to string input.

Note

If a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 is passed, then format has no effect.

Note

When using `format`, any datetime components not present in the format string default to `1900-01-01 00:00:00`, consistent with Python’s [`datetime.datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "(in Python v3.15)")
 behavior. For example, `to_datetime(["1", "2"], format="%d")` returns dates in January 1900. The `origin` parameter does not affect string parsing via `format`; it only applies to numeric input interpreted through `unit`.

**exact**bool, default True

Control how format is used:

*   If `True`, require an exact format match.
    
*   If `False`, allow the format to match anywhere in the target string.
    

Cannot be used alongside `format='ISO8601'` or `format='mixed'`.

**unit**str, default ‘ns’

The unit of the numeric arg (Y, M, W, D, h, m, s, ms, us, ns, ps, fs, as). Specifies the unit of the input values when arg is numeric (int or float), interpreted relative to `origin`. For example, with `unit='ms'` and `origin='unix'`, the input values are treated as millisecond offsets from the Unix epoch (1970-01-01).

This does not truncate or round datetime-like inputs to the given unit. To change the resolution of the result, use [`Series.dt.as_unit()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit "pandas.Series.dt.as_unit")
. To truncate datetime values, use [`Series.dt.floor()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html#pandas.Series.dt.floor "pandas.Series.dt.floor")
 or [`Series.dt.normalize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#pandas.Series.dt.normalize "pandas.Series.dt.normalize")
.

Only applicable to numeric input; has no effect on datetime-like input or when `format` is specified.

**origin**scalar, default ‘unix’

Define the reference date. The numeric values would be parsed as number of units (defined by `unit`) since this reference date.

*   If `'unix'` (or POSIX) time; origin is set to 1970-01-01.
    
*   If `'julian'`, unit must be `'D'`, and origin is set to beginning of Julian Calendar. Julian day number `0` is assigned to the day starting at noon on January 1, 4713 BC.
    
*   If Timestamp convertible (Timestamp, dt.datetime, np.datetime64 or date string), origin is set to Timestamp identified by origin.
    
*   If a float or integer, origin is the difference (in units determined by the `unit` argument) relative to 1970-01-01.
    

Note

This parameter only affects numeric input used with `unit`. It does not affect string parsing via `format`. See the `format` parameter for how defaults are handled during string parsing.

**cache**bool, default True

If `True`, use a cache of unique, converted dates to apply the datetime conversion. May produce significant speed-up when parsing duplicate date strings, especially ones with timezone offsets. The cache is only used when there are at least 50 values. The presence of out-of-bounds values will render the cache unusable and may slow down parsing.

Returns:

datetime

If parsing succeeded. Return type depends on input (types in parenthesis correspond to fallback in case of unsuccessful timezone or out-of-range timestamp parsing):

*   scalar: [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
     (or [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    )
    
*   array-like: [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
     (or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     with [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
     dtype containing [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    )
    
*   Series: [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     of `datetime64` dtype (or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     of [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
     dtype containing [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    )
    
*   DataFrame: [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     of `datetime64` dtype (or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     of [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
     dtype containing [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    )
    

Raises:

ParserError

When parsing a date from string fails.

ValueError

When another datetime conversion error happens. For example when one of ‘year’, ‘month’, day’ columns is missing in a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, or when a Timezone-aware [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
 is found in an array-like of mixed time offsets, and `utc=False`, or when parsing datetimes with mixed time zones unless `utc=True`. If parsing datetimes with mixed time zones, please specify `utc=True`.

See also

[`DataFrame.astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")

Cast argument to a specified dtype.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

`convert_dtypes`

Convert dtypes.

Notes

Many input types are supported, and lead to different output types:

*   **scalars** can be int, float, str, datetime object (from stdlib [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.15)")
     module or [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "(in NumPy v2.5)")
    ). They are converted to [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
     when possible, otherwise they are converted to [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    . None/NaN/null scalars are converted to [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
    .
    
*   **array-like** can contain int, float, str, datetime objects. They are converted to [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
     when possible, otherwise they are converted to [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
     with [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
     dtype, containing [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    . None/NaN/null entries are converted to [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
     in both cases.
    
*   **Series** are converted to [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     with `datetime64` dtype when possible, otherwise they are converted to [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     with [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
     dtype, containing [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
    . None/NaN/null entries are converted to [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
     in both cases.
    
*   **DataFrame/dict-like** are converted to [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     with `datetime64` dtype. For each row a datetime is created from assembling the various dataframe columns. Column keys can be common abbreviations like \[‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’\]) or plurals of the same.
    

The following causes are responsible for [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
 objects being returned (possibly inside an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 or a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 with [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
 dtype) instead of a proper pandas designated type ([`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
, [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 with `datetime64` dtype):

*   when any input element is before [`Timestamp.min`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.min.html#pandas.Timestamp.min "pandas.Timestamp.min")
     or after [`Timestamp.max`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.max.html#pandas.Timestamp.max "pandas.Timestamp.max")
    , see [timestamp limitations](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-timestamp-limits)
    .
    
*   when `utc=False` (default) and the input is an array-like or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     containing mixed naive/aware datetime, or aware with mixed time offsets. Note that this happens in the (quite frequent) situation when the timezone has a daylight savings policy. In that case you may wish to use `utc=True`.
    

Examples

**Handling various input formats**

Assembling a datetime from multiple columns of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. The keys can be common abbreviations like \[‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’\]) or plurals of the same

\>>> df \= pd.DataFrame({"year": \[2015, 2016\], "month": \[2, 3\], "day": \[4, 5\]})
\>>> pd.to\_datetime(df)
0   2015-02-04
1   2016-03-05
dtype: datetime64\[us\]

Copy to clipboard

Using a unix epoch time

\>>> pd.to\_datetime(1490195805, unit\="s")
Timestamp('2017-03-22 15:16:45')
\>>> pd.to\_datetime(1490195805433502912, unit\="ns")
Timestamp('2017-03-22 15:16:45.433502912')

Copy to clipboard

Warning

For float arg, precision rounding might happen. To prevent unexpected behavior use a fixed-width exact type.

Using a non-unix epoch origin

\>>> pd.to\_datetime(\[1, 2, 3\], unit\="D", origin\=pd.Timestamp("1960-01-01"))
DatetimeIndex(\['1960-01-02', '1960-01-03', '1960-01-04'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

**Differences with strptime behavior**

`"%f"` will parse all the way up to nanoseconds.

\>>> pd.to\_datetime("2018-10-26 12:00:00.0000000011", format\="%Y-%m-%d %H:%M:%S.%f")
Timestamp('2018-10-26 12:00:00.000000001')

Copy to clipboard

**Non-convertible date/times**

Passing `errors='coerce'` will force an out-of-bounds date to [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
, in addition to forcing non-dates (or non-parseable dates) to [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
.

\>>> pd.to\_datetime("invalid for Ymd", format\="%Y%m%d", errors\="coerce")
NaT

Copy to clipboard

**Timezones and time offsets**

The default behaviour (`utc=False`) is as follows:

*   Timezone-naive inputs are converted to timezone-naive [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
    :
    

\>>> pd.to\_datetime(\["2018-10-26 12:00:00", "2018-10-26 13:00:15"\])
DatetimeIndex(\['2018-10-26 12:00:00', '2018-10-26 13:00:15'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

*   Timezone-aware inputs _with constant time offset_ are converted to timezone-aware [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
    :
    

\>>> pd.to\_datetime(\["2018-10-26 12:00 -0500", "2018-10-26 13:00 -0500"\])
DatetimeIndex(\['2018-10-26 12:00:00-05:00', '2018-10-26 13:00:00-05:00'\],
              dtype='datetime64\[us, UTC-05:00\]', freq=None)

Copy to clipboard

*   However, timezone-aware inputs _with mixed time offsets_ (for example issued from a timezone with daylight savings, such as Europe/Paris) are **not successfully converted** to a [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
    . Parsing datetimes with mixed time zones will raise a ValueError unless `utc=True`:
    

\>>> pd.to\_datetime(
...     \["2020-10-25 02:00 +0200", "2020-10-25 04:00 +0100"\]
... )
ValueError: Mixed timezones detected. Pass utc=True in to\_datetime
or tz='UTC' in DatetimeIndex to convert to a common timezone.

Copy to clipboard

*   To create a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     with mixed offsets and `object` dtype, please use [`Series.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")
     and `datetime.datetime.strptime()`:
    

\>>> import datetime as dt
\>>> ser \= pd.Series(\["2020-10-25 02:00 +0200", "2020-10-25 04:00 +0100"\])
\>>> ser.apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d %H:%M %z"))
0    2020-10-25 02:00:00+02:00
1    2020-10-25 04:00:00+01:00
dtype: object

Copy to clipboard

*   A mix of timezone-aware and timezone-naive inputs will also raise a ValueError unless `utc=True`:
    

\>>> from datetime import datetime
\>>> pd.to\_datetime(
...     \["2020-01-01 01:00:00-01:00", datetime(2020, 1, 1, 3, 0)\]
... )
ValueError: Mixed timezones detected. Pass utc=True in to\_datetime
or tz='UTC' in DatetimeIndex to convert to a common timezone.

Copy to clipboard

  

Setting `utc=True` solves most of the above issues:

*   Timezone-naive inputs are _localized_ as UTC
    

\>>> pd.to\_datetime(\["2018-10-26 12:00", "2018-10-26 13:00"\], utc\=True)
DatetimeIndex(\['2018-10-26 12:00:00+00:00', '2018-10-26 13:00:00+00:00'\],
              dtype='datetime64\[us, UTC\]', freq=None)

Copy to clipboard

*   Timezone-aware inputs are _converted_ to UTC (the output represents the exact same datetime, but viewed from the UTC time offset +00:00).
    

\>>> pd.to\_datetime(\["2018-10-26 12:00 -0530", "2018-10-26 12:00 -0500"\], utc\=True)
DatetimeIndex(\['2018-10-26 17:30:00+00:00', '2018-10-26 17:00:00+00:00'\],
              dtype='datetime64\[us, UTC\]', freq=None)

Copy to clipboard

*   Inputs can contain both string or datetime, the above rules still apply
    

\>>> pd.to\_datetime(\["2018-10-26 12:00", datetime(2020, 1, 1, 18)\], utc\=True)
DatetimeIndex(\['2018-10-26 12:00:00+00:00', '2020-01-01 18:00:00+00:00'\],
              dtype='datetime64\[us, UTC\]', freq=None)

Copy to clipboard

On this page