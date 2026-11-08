[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas-periodindex "Link to this heading")

======================================================================================================================================

class pandas.PeriodIndex(_data\=None_, _freq\=None_, _dtype\=None_, _copy\=None_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L76-L1156)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "Link to this definition")

Immutable ndarray holding ordinal values indicating regular periods in time.

Index keys are boxed to Period objects which carries the metadata (eg, frequency information).

Parameters:

**data**array-like (1d int np.ndarray or PeriodArray), optional

Optional period-like data to construct index with.

**freq**str or period object, optional

One of pandas period strings or corresponding objects.

**dtype**str or PeriodDtype, default None

A dtype from which to extract a freq.

**copy**bool, default None

Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.

**name**str, default None

Name of the resulting PeriodIndex.

Attributes

|     |     |
| --- | --- |
| [`day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day") | The days of the period. |
| [`dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.dayofweek.html#pandas.PeriodIndex.dayofweek "pandas.PeriodIndex.dayofweek") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas.PeriodIndex.day_of_week "pandas.PeriodIndex.day_of_week") | The day of the week with Monday=0, Sunday=6. |
| [`dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.dayofyear.html#pandas.PeriodIndex.dayofyear "pandas.PeriodIndex.dayofyear") | (DEPRECATED) The ordinal day of the year. |
| [`day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year") | The ordinal day of the year. |
| [`days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas.PeriodIndex.days_in_month "pandas.PeriodIndex.days_in_month") | The number of days in the month. |
| [`daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.daysinmonth.html#pandas.PeriodIndex.daysinmonth "pandas.PeriodIndex.daysinmonth") | (DEPRECATED) The number of days in the month. |
| [`end_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#pandas.PeriodIndex.end_time "pandas.PeriodIndex.end_time") | Get the Timestamp for the end of the period. |
| [`freq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.freq.html#pandas.PeriodIndex.freq "pandas.PeriodIndex.freq") | Return the frequency object if it is set, otherwise None. |
| [`freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.freqstr.html#pandas.PeriodIndex.freqstr "pandas.PeriodIndex.freqstr") | Return the frequency object as a string if it's set, otherwise None. |
| [`hour`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.hour.html#pandas.PeriodIndex.hour "pandas.PeriodIndex.hour") | The hour of the period. |
| [`is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#pandas.PeriodIndex.is_leap_year "pandas.PeriodIndex.is_leap_year") | Logical indicating if the date belongs to a leap year. |
| [`minute`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas.PeriodIndex.minute "pandas.PeriodIndex.minute") | The minute of the period. |
| [`month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas.PeriodIndex.month "pandas.PeriodIndex.month") | The month as January=1, December=12. |
| [`quarter`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas.PeriodIndex.quarter "pandas.PeriodIndex.quarter") | The quarter of the date. |
| [`qyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas.PeriodIndex.qyear "pandas.PeriodIndex.qyear") | Fiscal year the Period lies in according to its starting-quarter. |
| [`second`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas.PeriodIndex.second "pandas.PeriodIndex.second") | The second of the period. |
| [`start_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#pandas.PeriodIndex.start_time "pandas.PeriodIndex.start_time") | Get the Timestamp for the start of the period. |
| [`week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.week.html#pandas.PeriodIndex.week "pandas.PeriodIndex.week") | The week ordinal of the year. |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekday.html#pandas.PeriodIndex.weekday "pandas.PeriodIndex.weekday") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekofyear.html#pandas.PeriodIndex.weekofyear "pandas.PeriodIndex.weekofyear") | The week ordinal of the year. |
| [`year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year") | The year of the period. |

Methods

|     |     |
| --- | --- |
| [`asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#pandas.PeriodIndex.asfreq "pandas.PeriodIndex.asfreq")<br>(\[freq, how\]) | Convert the PeriodIndex to the specified frequency freq. |
| [`strftime`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html#pandas.PeriodIndex.strftime "pandas.PeriodIndex.strftime")<br>(date\_format) | Convert to Index using specified date\_format. |
| [`to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")<br>(\[freq, how\]) | Cast to DatetimeIndex. |
| [`from_fields`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas.PeriodIndex.from_fields "pandas.PeriodIndex.from_fields")<br>(\*\[, year, quarter, month, day, ...\]) | Construct a PeriodIndex from fields (year, month, day, etc.). |
| [`from_ordinals`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas.PeriodIndex.from_ordinals "pandas.PeriodIndex.from_ordinals")<br>(ordinals, \*, freq\[, name\]) | Construct a PeriodIndex from ordinals. |

Raises:

ValueError

Passing the parameter data as a list without specifying either freq or dtype will raise a ValueError: “freq not specified and cannot be inferred”

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a period of time.

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

Index with datetime64 data.

[`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")

Index of timedelta64 data.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Create a fixed-frequency PeriodIndex.

Examples

\>>> idx \= pd.PeriodIndex(data\=\["2000Q1", "2002Q3"\], freq\="Q")
\>>> idx
PeriodIndex(\['2000Q1', '2002Q3'\], dtype='period\[Q-DEC\]')

Copy to clipboard

On this page