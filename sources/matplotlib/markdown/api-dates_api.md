[Skip to main content](https://matplotlib.org/stable/api/dates_api.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

`matplotlib.dates`[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib-dates "Link to this heading")

================================================================================================================

Inheritance diagram of matplotlib.dates

Matplotlib provides sophisticated date plotting capabilities, standing on the shoulders of python [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 and the add-on module [dateutil](https://dateutil.readthedocs.io/)
.

By default, Matplotlib uses the units machinery described in [`units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
 to convert [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
, and [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 objects when plotted on an x- or y-axis. The user does not need to do anything for dates to be formatted, but dates often have strict formatting needs, so this module provides many tick locators and formatters. A basic example using [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 is:

import numpy as np

times \= np.arange(np.datetime64('2001-01-02'),
                  np.datetime64('2002-02-03'), np.timedelta64(75, 'm'))
y \= np.random.randn(len(times))

fig, ax \= plt.subplots()
ax.plot(times, y)

See also

*   [Date tick labels](https://matplotlib.org/stable/gallery/ticks/date.html)
    
*   [Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)
    
*   [Date converter demo](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html)
    

Matplotlib date format[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib-date-format "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Matplotlib represents dates using floating point numbers specifying the number of days since a default epoch of 1970-01-01 UTC; for example, 1970-01-01, 06:00 is the floating point number 0.25. The formatters and locators require the use of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 objects, so only dates between year 0001 and 9999 can be represented. Microsecond precision is achievable for (approximately) 70 years on either side of the epoch, and 20 microseconds for the rest of the allowable range of dates (year 0001 to 9999). The epoch can be changed at import time via [`dates.set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
 or `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`) to other dates if necessary; see [Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)
 for a discussion.

Note

Before Matplotlib 3.3, the epoch was 0000-12-31 which lost modern microsecond precision and also made the default axis limit of 0 an invalid datetime. In 3.3 the epoch was changed as above. To convert old ordinal floats to the new epoch, users can do:

new\_ordinal \= old\_ordinal + mdates.date2num(np.datetime64('0000-12-31'))

There are a number of helper functions to convert between [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 objects and Matplotlib dates:

|     |     |
| --- | --- |
| [`datestr2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.datestr2num "matplotlib.dates.datestr2num") | Convert a date string to a datenum using [`dateutil.parser.parse`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse "(in dateutil v3.9.0)")<br>. |
| [`date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num") | Convert datetime objects to Matplotlib dates. |
| [`num2date`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date") | Convert Matplotlib dates to [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")<br> objects. |
| [`num2timedelta`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2timedelta "matplotlib.dates.num2timedelta") | Convert number of days to a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")<br> object. |
| [`drange`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "matplotlib.dates.drange") | Return a sequence of equally spaced Matplotlib dates. |
| [`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch") | Set the epoch (origin for dates) for datetime calculations. |
| [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch") | Get the epoch used by [`dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")<br>. |

Note

Like Python's [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
, Matplotlib uses the Gregorian calendar for all conversions between dates and floating point numbers. This practice is not universal, and calendar differences can cause confusing differences between what Python and Matplotlib give as the number of days since 0001-01-01 and what other software and databases yield. For example, the US Naval Observatory uses a calendar that switches from Julian to Gregorian in October, 1582. Hence, using their calculator, the number of days between 0001-01-01 and 2006-04-01 is 732403, whereas using the Gregorian calendar via the datetime module we find:

In \[1\]: date(2006, 4, 1).toordinal() \- date(1, 1, 1).toordinal()
Out\[1\]: 732401

All the Matplotlib date converters, locators and formatters are timezone aware. If no explicit timezone is provided, `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`) is assumed, provided as a string. If you want to use a different timezone, pass the _tz_ keyword argument of [`num2date`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
 to any date tick locators or formatters you create. This can be either a [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
 instance or a string with the timezone name that can be parsed by [`gettz`](https://dateutil.readthedocs.io/en/stable/tz.html#dateutil.tz.gettz "(in dateutil v3.9.0)")
.

A wide range of specific and general purpose date tick locators and formatters are provided in this module. See [`matplotlib.ticker`](https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker "matplotlib.ticker")
 for general information on tick locators and formatters. These are described below.

The [dateutil](https://dateutil.readthedocs.io/)
 module provides additional code to handle date ticking, making it easy to place ticks on any kinds of dates. See examples below.

Date tick locators[#](https://matplotlib.org/stable/api/dates_api.html#date-tick-locators "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Most of the date tick locators can locate single or multiple ticks. For example:

\# import constants for the days of the week
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

\# tick on Mondays every week
loc \= WeekdayLocator(byweekday\=MO, tz\=tz)

\# tick on Mondays and Saturdays
loc \= WeekdayLocator(byweekday\=(MO, SA))

In addition, most of the constructors take an interval argument:

\# tick on Mondays every second week
loc \= WeekdayLocator(byweekday\=MO, interval\=2)

The rrule locator allows completely general date ticking:

\# tick every 5th easter
rule \= rrulewrapper(YEARLY, byeaster\=1, interval\=5)
loc \= RRuleLocator(rule)

The available date tick locators are:

*   [`MicrosecondLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator "matplotlib.dates.MicrosecondLocator")
    : Locate microseconds.
    
*   [`SecondLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.SecondLocator "matplotlib.dates.SecondLocator")
    : Locate seconds.
    
*   [`MinuteLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MinuteLocator "matplotlib.dates.MinuteLocator")
    : Locate minutes.
    
*   [`HourLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.HourLocator "matplotlib.dates.HourLocator")
    : Locate hours.
    
*   [`DayLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
    : Locate specified days of the month.
    
*   [`WeekdayLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.WeekdayLocator "matplotlib.dates.WeekdayLocator")
    : Locate days of the week, e.g., MO, TU.
    
*   [`MonthLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
    : Locate months, e.g., 7 for July.
    
*   [`YearLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "matplotlib.dates.YearLocator")
    : Locate years that are multiples of base.
    
*   [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
    : Locate using a [`rrulewrapper`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
    . [`rrulewrapper`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
     is a simple wrapper around [dateutil](https://dateutil.readthedocs.io/)
    's [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
     which allow almost arbitrary date tick specifications. See [rrule example](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html)
    .
    
*   [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
    : On autoscale, this class picks the best [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")
     (e.g., [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
    ) to set the view limits and the tick locations. If called with `interval_multiples=True` it will make ticks line up with sensible multiples of the tick intervals. For example, if the interval is 4 hours, it will pick hours 0, 4, 8, etc. as ticks. This behaviour is not guaranteed by default.
    

Date formatters[#](https://matplotlib.org/stable/api/dates_api.html#date-formatters "Link to this heading")

------------------------------------------------------------------------------------------------------------

The available date formatters are:

*   [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
    : attempts to figure out the best format to use. This is most useful when used with the [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
    .
    
*   [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
    : also attempts to figure out the best format to use, and to make the format as compact as possible while still having complete date information. This is most useful when used with the [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
    .
    
*   [`DateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
    : use [`strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
     format strings.
    

class matplotlib.dates.AutoDateFormatter(_locator_, _tz\=None_, _defaultfmt\='%Y-%m-%d'_, _\*_, _usetex\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L824-L940)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

A [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 which attempts to figure out the best format to use. This is most useful when used with the [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
.

[`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
 has a `.scaled` dictionary that maps tick scales (the interval in days between one major tick) to format strings; this dictionary defaults to

self.scaled \= {
    DAYS\_PER\_YEAR: rcParams\['date.autoformatter.year'\],
    DAYS\_PER\_MONTH: rcParams\['date.autoformatter.month'\],
    1: rcParams\['date.autoformatter.day'\],
    1 / HOURS\_PER\_DAY: rcParams\['date.autoformatter.hour'\],
    1 / MINUTES\_PER\_DAY: rcParams\['date.autoformatter.minute'\],
    1 / SEC\_PER\_DAY: rcParams\['date.autoformatter.second'\],
    1 / MUSECONDS\_PER\_DAY: rcParams\['date.autoformatter.microsecond'\],
}

The formatter uses the format string corresponding to the lowest key in the dictionary that is greater or equal to the current scale. Dictionary entries can be customized:

locator \= AutoDateLocator()
formatter \= AutoDateFormatter(locator)
formatter.scaled\[1/(24\*60)\] \= '%M:%S' \# only show min and sec

Custom callables can also be used instead of format strings. The following example shows how to use a custom format function to strip trailing zeros from decimal seconds and adds the date to the first ticklabel:

def my\_format\_function(x, pos\=None):
    x \= matplotlib.dates.num2date(x)
    if pos \== 0:
        fmt \= '%D %H:%M:%S.%f'
    else:
        fmt \= '%H:%M:%S.%f'
    label \= x.strftime(fmt)
    label \= label.rstrip("0")
    label \= label.rstrip(".")
    return label

formatter.scaled\[1/(24\*60)\] \= my\_format\_function

Autoformat the date labels.

Parameters:

**locator**[`ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Locator that this axis is using.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

**defaultfmt**str

The default format to use if none of the values in `self.scaled` are greater than the unit returned by `locator._get_unit()`.

**usetex**bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)

To enable/disable the use of TeX's math mode for rendering the results of the formatter. If any entries in `self.scaled` are set as functions, then it is up to the customized function to enable or disable TeX's math mode itself.

class matplotlib.dates.AutoDateLocator(_tz\=None_, _minticks\=5_, _maxticks\=None_, _interval\_multiples\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1216-L1446)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "Link to this definition")

Bases: [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")

On autoscale, this class picks the best [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")
 to set the view limits and the tick locations.

Attributes:

**intervald**dict

Mapping of tick frequencies to multiples allowed for that ticking. The default is

self.intervald \= {
    YEARLY  : \[1, 2, 4, 5, 10, 20, 40, 50, 100, 200, 400, 500,\
               1000, 2000, 4000, 5000, 10000\],
    MONTHLY : \[1, 2, 3, 4, 6\],
    DAILY   : \[1, 2, 3, 7, 14, 21\],
    HOURLY  : \[1, 2, 3, 4, 6, 12\],
    MINUTELY: \[1, 5, 10, 15, 30\],
    SECONDLY: \[1, 5, 10, 15, 30\],
    MICROSECONDLY: \[1, 2, 5, 10, 20, 50, 100, 200, 500,\
                    1000, 2000, 5000, 10000, 20000, 50000,\
                    100000, 200000, 500000, 1000000\],
}

where the keys are defined in [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
.

The interval is used to specify multiples that are appropriate for the frequency of ticking. For instance, every 7 days is sensible for daily ticks, but for minutes/seconds, 15 or 30 make sense.

When customizing, you should only modify the values for the existing keys. You should not add or delete entries.

Example for forcing ticks every 3 hours:

locator \= AutoDateLocator()
locator.intervald\[HOURLY\] \= \[3\]  \# only show every 3 hours

Parameters:

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

**minticks**int

The minimum number of ticks desired; controls whether ticks occur yearly, monthly, etc.

**maxticks**int

The maximum number of ticks desired; controls the interval between ticks (ticking every other, every 3, etc.). For fine-grained control, this can be a dictionary mapping individual rrule frequency constants (YEARLY, MONTHLY, etc.) to their own maximum number of ticks. This can be used to keep the number of ticks appropriate to the format chosen in [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
. Any frequency not specified in this dictionary is given a default value.

**interval\_multiples**bool, default: True

Whether ticks should be chosen to be multiple of the interval, locking them to 'nicer' locations. For example, this will force the ticks to be at hours 0, 6, 12, 18 when hourly ticking is done at 6 hour intervals.

get\_locator(_dmin_, _dmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1348-L1446)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator.get_locator "Link to this definition")

Pick the best locator based on a distance.

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1328-L1340)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator.nonsingular "Link to this definition")

Given the proposed upper and lower extent, adjust the range if it is too close to being singular (i.e. a range of ~0).

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1325-L1326)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.dates.ConciseDateConverter(_formats\=None_, _zero\_formats\=None_, _offset\_formats\=None_, _show\_offset\=True_, _\*_, _interval\_multiples\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1789-L1813)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "Link to this definition")

Bases: [`DateConverter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter "matplotlib.dates.DateConverter")

axisinfo(_unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1801-L1813)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter.axisinfo "Link to this definition")

Return the [`AxisInfo`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
 for _unit_.

_unit_ is a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
 instance or None. The _axis_ argument is required but not used.

class matplotlib.dates.ConciseDateFormatter(_locator_, _tz\=None_, _formats\=None_, _offset\_formats\=None_, _zero\_formats\=None_, _show\_offset\=True_, _\*_, _usetex\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L595-L821)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

A [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 which attempts to figure out the best format to use for the date, and to make it as compact as possible, but still be complete. This is most useful when used with the [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
:

\>>> locator \= AutoDateLocator()
\>>> formatter \= ConciseDateFormatter(locator)

Parameters:

**locator**[`ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Locator that this axis is using.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone, passed to [`dates.num2date`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
.

**formats**list of 6 strings, optional

Format strings for 6 levels of tick labelling: mostly years, months, days, hours, minutes, and seconds. Strings use the same format codes as [`strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
. Default is `['%Y', '%b', '%d', '%H:%M', '%H:%M', '%S.%f']`

**zero\_formats**list of 6 strings, optional

Format strings for tick labels that are "zeros" for a given tick level. For instance, if most ticks are months, ticks around 1 Jan 2005 will be labeled "Dec", "2005", "Feb". The default is `['', '%Y', '%b', '%b-%d', '%H:%M', '%H:%M']`

**offset\_formats**list of 6 strings, optional

Format strings for the 6 levels that is applied to the "offset" string found on the right side of an x-axis, or top of a y-axis. Combined with the tick labels this should completely specify the date. The default is:

\['', '%Y', '%Y-%b', '%Y-%b-%d', '%Y-%b-%d', '%Y-%b-%d %H:%M'\]

**show\_offset**bool, default: True

Whether to show the offset or not.

**usetex**bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)

To enable/disable the use of TeX's math mode for rendering the results of the formatter.

Examples

See [Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)

([`Source code`](https://matplotlib.org/stable/_downloads/d35cfd2538cb0601780e50ada2a98dba/dates_api-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c41e985a7a2bb0e0d3c34d89a8267079/dates_api-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/17e5a51e538bb9397dea9277dd9855ec/dates_api-1.png)
)

[![](https://matplotlib.org/stable/_images/api-dates_api-1.2x.png)](https://matplotlib.org/stable/_images/api-dates_api-1.2x.png)

Autoformat the date labels. The default format is used to form an initial string, and then redundant elements are removed.

format\_data\_short(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L820-L821)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter.format_data_short "Link to this definition")

Return a short string representation of _value_ for the mouseover tooltip (the coordinate display in the interactive figure window).

This should return concise, plain text (no mathtext / LaTeX). The precision is typically adapted to the current axis resolution so that neighbouring pixels produce distinguishable labels.

Defaults to [`Formatter.format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
; subclasses should override this to provide a plain-text representation that is independent of the current tick locations.

Note: The mouseover text can be customized by setting the `Axes.fmt_xdata` and `Axes.fmt_ydata` attributes.

format\_ticks(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L733-L815)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter.format_ticks "Link to this definition")

Return the tick label strings for all _values_.

This is the public API for generating tick labels. It calls `set_locs` to configure context-dependent formatting state before delegating to `__call__` for each individual value.

The output may contain mathtext or LaTeX markup.

Use this method (rather than `__call__`) whenever formatting a complete set of tick values, so that formatters which need to see all tick locations (e.g. to determine precision, offsets, or which date components to display) can work correctly.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L817-L818)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter.get_offset "Link to this definition")

property offset\_string[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter.offset_string "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use get\_offset() instead.

class matplotlib.dates.DateConverter(_\*_, _interval\_multiples\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1728-L1786)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter "Link to this definition")

Bases: [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")

Converter for [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")
 and [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 data, or for date/time data represented as it would be converted by [`date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
.

The 'unit' tag for such data is None or a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
 instance.

axisinfo(_unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1740-L1756)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter.axisinfo "Link to this definition")

Return the [`AxisInfo`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
 for _unit_.

_unit_ is a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
 instance or None. The _axis_ argument is required but not used.

static convert(_value_, _unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1758-L1766)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter.convert "Link to this definition")

If _value_ is not already a number or sequence of numbers, convert it with [`date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
.

The _unit_ and _axis_ arguments are not used.

static default\_units(_x_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1768-L1786)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter.default_units "Link to this definition")

Return the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
 instance of _x_ or of its first element, or None

class matplotlib.dates.DateFormatter(_fmt_, _tz\=None_, _\*_, _usetex\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L565-L592)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Format a tick (in days since the epoch) with a [`strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
 format string.

Parameters:

**fmt**str

[`strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
 format string

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

**usetex**bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)

To enable/disable the use of TeX's math mode for rendering the results of the formatter.

set\_tzinfo(_tz_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L591-L592)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter.set_tzinfo "Link to this definition")

class matplotlib.dates.DateLocator(_tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1064-L1137)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Determines the tick locations when plotting dates.

This class is subclassed by other Locators and is not meant to be used on its own.

Parameters:

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

datalim\_to\_dt()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1093-L1099)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator.datalim_to_dt "Link to this definition")

Convert axis data interval to datetime objects.

hms0d \= {'byhour': 0, 'byminute': 0, 'bysecond': 0}[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator.hms0d "Link to this definition")

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1121-L1137)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator.nonsingular "Link to this definition")

Given the proposed upper and lower extent, adjust the range if it is too close to being singular (i.e. a range of ~0).

set\_tzinfo(_tz_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1082-L1091)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator.set_tzinfo "Link to this definition")

Set timezone info.

Parameters:

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

viewlim\_to\_dt()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1101-L1106)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator.viewlim_to_dt "Link to this definition")

Convert the view interval to datetime objects.

class matplotlib.dates.DayLocator(_bymonthday\=None_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1555-L1580)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each day of the month. For example, 1, 15, 30.

Parameters:

**bymonthday**int or list of int, default: all days

Ticks will be placed on every day in _bymonthday_. Default is `bymonthday=range(1, 32)`, i.e., every day of the month.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.HourLocator(_byhour\=None_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1583-L1605)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.HourLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each hour.

Parameters:

**byhour**int or list of int, default: all hours

Ticks will be placed on every hour in _byhour_. Default is `byhour=range(24)`, i.e., every hour.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.MicrosecondLocator(_interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1657-L1725)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator "Link to this definition")

Bases: [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")

Make ticks on regular intervals of one or more microsecond(s).

Note

By default, Matplotlib uses a floating point representation of time in days since the epoch, so plotting data with microsecond time resolution does not work well for dates that are far (about 70 years) from the epoch (check with [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
).

If you want sub-microsecond resolution time plots, it is strongly recommended to use floating point seconds, not datetime-like time representation.

If you really must use datetime.datetime() or similar and still need microsecond precision, change the time origin via [`dates.set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
 to something closer to the dates being plotted. See [Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)
.

Parameters:

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1693-L1695)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator.set_axis "Link to this definition")

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1706-L1717)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.dates.MinuteLocator(_byminute\=None_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1608-L1630)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MinuteLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each minute.

Parameters:

**byminute**int or list of int, default: all minutes

Ticks will be placed on every minute in _byminute_. Default is `byminute=range(60)`, i.e., every minute.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.MonthLocator(_bymonth\=None_, _bymonthday\=1_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1499-L1523)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each month, e.g., 1, 3, 12.

Parameters:

**bymonth**int or list of int, default: all months

Ticks will be placed on every month in _bymonth_. Default is `range(1, 13)`, i.e. every month.

**bymonthday**int, default: 1

The day on which to place the ticks.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.RRuleLocator(_o_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1140-L1213)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "Link to this definition")

Bases: [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")

Parameters:

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

static get\_unit\_generic(_freq_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1192-L1210)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator.get_unit_generic "Link to this definition")

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1156-L1161)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.dates.SecondLocator(_bysecond\=None_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1633-L1654)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.SecondLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each second.

Parameters:

**bysecond**int or list of int, default: all seconds

Ticks will be placed on every second in _bysecond_. Default is `bysecond = range(60)`, i.e., every second.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.WeekdayLocator(_byweekday\=1_, _interval\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1526-L1552)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.WeekdayLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on occurrences of each weekday.

Parameters:

**byweekday**int, list of int, constant from [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
, or list of constants, default: 1 (Tuesday)

Ticks will be placed on every weekday in _byweekday_. Default is every Tuesday.

Elements of _byweekday_ (if a sequence) must be either integers or MO, TU, WE, TH, FR, SA, SU, the constants from [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
, which have been imported into the [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 namespace.

**interval**int, default: 1

The interval between each iteration. For example, if `interval=2`, mark every second occurrence.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

class matplotlib.dates.YearLocator(_base\=1_, _month\=1_, _day\=1_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L1449-L1496)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "Link to this definition")

Bases: [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")

Make ticks on a given day of each year that is a multiple of base.

Examples:

\# Tick every year on Jan 1st
locator \= YearLocator()

\# Tick every 5 years on July 4th
locator \= YearLocator(5, month\=7, day\=4)

Parameters:

**base**int, default: 1

Mark ticks every _base_ years.

**month**int, default: 1

The month on which to place the ticks, starting from 1. Default is January.

**day**int, default: 1

The day on which to place the ticks.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Ticks timezone. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

matplotlib.dates.date2num(_d_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L403-L452)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "Link to this definition")

Convert datetime objects to Matplotlib dates.

Parameters:

**d**[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 or [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 or sequences of these

Returns:

float or sequence of floats

Number of days since the epoch. See [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
 for the epoch, which can be changed by `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`) or [`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
. If the epoch is "1970-01-01T00:00:00" (default) then noon Jan 1 1970 ("1970-01-01T12:00:00") returns 0.5.

Notes

The Gregorian calendar is assumed; this is not universal practice. For details see the module docstring.

matplotlib.dates.datestr2num(_d_, _default\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L377-L400)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.datestr2num "Link to this definition")

Convert a date string to a datenum using [`dateutil.parser.parse`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse "(in dateutil v3.9.0)")
.

Parameters:

**d**str or sequence of str

The dates to convert.

**default**datetime.datetime, optional

The default date to use when fields are missing in _d_.

matplotlib.dates.drange(_dstart_, _dend_, _delta_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L508-L546)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "Link to this definition")

Return a sequence of equally spaced Matplotlib dates.

The dates start at _dstart_ and reach up to, but not including _dend_. They are spaced by _delta_.

Parameters:

**dstart, dend**[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")

The date limits.

**delta**[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")

Spacing of the dates.

Returns:

[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")

A list floats representing Matplotlib dates.

matplotlib.dates.get\_epoch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L295-L307)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "Link to this definition")

Get the epoch used by [`dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
.

Returns:

**epoch**str

String for the epoch (parsable by [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
).

matplotlib.dates.num2date(_x_, _tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L455-L482)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "Link to this definition")

Convert Matplotlib dates to [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 objects.

Parameters:

**x**float or sequence of floats

Number of days (fraction part represents hours, minutes, seconds) since the epoch. See [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
 for the epoch, which can be changed by `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`) or [`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
.

**tz**str or [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

Timezone of _x_. If a string, _tz_ is passed to [`dateutil.tz`](https://dateutil.readthedocs.io/en/stable/tz.html#module-dateutil.tz "(in dateutil v3.9.0)")
.

Returns:

[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 or sequence of [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")

Dates are returned in timezone _tz_.

If _x_ is a sequence, a sequence of [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 objects will be returned.

Notes

The Gregorian calendar is assumed; this is not universal practice. For details, see the module docstring.

matplotlib.dates.num2timedelta(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L489-L505)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2timedelta "Link to this definition")

Convert number of days to a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")
 object.

If _x_ is a sequence, a sequence of [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")
 objects will be returned.

Parameters:

**x**float, sequence of floats

Number of days. The fraction part represents hours, minutes, seconds.

Returns:

[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")
 or list\[[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")\
\]

class matplotlib.dates.relativedelta(_dt1\=None_, _dt2\=None_, _years\=0_, _months\=0_, _days\=0_, _leapdays\=0_, _weeks\=0_, _hours\=0_, _minutes\=0_, _seconds\=0_, _microseconds\=0_, _year\=None_, _month\=None_, _day\=None_, _weekday\=None_, _yearday\=None_, _nlyearday\=None_, _hour\=None_, _minute\=None_, _second\=None_, _microsecond\=None_)[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.relativedelta "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The relativedelta type is designed to be applied to an existing datetime and can replace specific components of that datetime, or represents an interval of time.

It is based on the specification of the excellent work done by M.-A. Lemburg in his [mx.DateTime](https://www.egenix.com/products/python/mxBase/mxDateTime/)
 extension. However, notice that this type does _NOT_ implement the same algorithm as his work. Do _NOT_ expect it to behave like mx.DateTime's counterpart.

There are two different ways to build a relativedelta instance. The first one is passing it two date/datetime classes:

relativedelta(datetime1, datetime2)

The second one is passing it any number of the following keyword arguments:

relativedelta(arg1\=x,arg2\=y,arg3\=z...)

year, month, day, hour, minute, second, microsecond:
    Absolute information (argument is singular); adding or subtracting a
    relativedelta with absolute information does not perform an arithmetic
    operation, but rather REPLACES the corresponding value in the
    original datetime with the value(s) in relativedelta.

years, months, weeks, days, hours, minutes, seconds, microseconds:
    Relative information, may be negative (argument is plural); adding
    or subtracting a relativedelta with relative information performs
    the corresponding arithmetic operation on the original datetime value
    with the information in the relativedelta.

weekday:
    One of the weekday instances (MO, TU, etc) available in the
    relativedelta module. These instances may receive a parameter N,
    specifying the Nth weekday, which could be positive or negative
    (like MO(+1) or MO(\-2)). Not specifying it is the same as specifying
    +1. You can also use an integer, where 0\=MO. This argument is always
    relative e.g. if the calculated date is already Monday, using MO(1)
    or MO(\-1) won't change the day. To effectively make it absolute, use
    it in combination with the day argument (e.g. day\=1, MO(1) for first
    Monday of the month).

leapdays:
    Will add given days to the date found, if year is a leap
    year, and the date found is post 28 of february.

yearday, nlyearday:
    Set the yearday or the non\-leap year day (jump leap days).
    These are converted to day/month/leapdays information.

There are relative and absolute forms of the keyword arguments. The plural is relative, and the singular is absolute. For each argument in the order below, the absolute form is applied first (by setting each attribute to that value) and then the relative form (by adding the value to the attribute).

The order of attributes considered when this relativedelta is added to a datetime is:

1.  Year
    
2.  Month
    
3.  Day
    
4.  Hours
    
5.  Minutes
    
6.  Seconds
    
7.  Microseconds
    

Finally, weekday is applied, using the rule described above.

For example

\>>> from datetime import datetime
\>>> from dateutil.relativedelta import relativedelta, MO
\>>> dt \= datetime(2018, 4, 9, 13, 37, 0)
\>>> delta \= relativedelta(hours\=25, day\=1, weekday\=MO(1))
\>>> dt + delta
datetime.datetime(2018, 4, 2, 14, 37)

First, the day is set to 1 (the first of the month), then 25 hours are added, to get to the 2nd day and 14th hour, finally the weekday is applied, but since the 2nd is already a Monday there is no effect.

normalized()[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.relativedelta.normalized "Link to this definition")

Return a version of this object represented entirely using integer values for the relative attributes.

\>>> relativedelta(days\=1.5, hours\=2).normalized()
relativedelta(days=+1, hours=+14)

Returns:

Returns a [`dateutil.relativedelta.relativedelta`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.relativedelta "dateutil.relativedelta.relativedelta")
 object.

property weeks[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.relativedelta.weeks "Link to this definition")

class matplotlib.dates.rrulewrapper(_freq_, _tzinfo\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L943-L1061)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A simple wrapper around a [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
 allowing flexible date tick specifications.

Parameters:

**freq**{YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY}

Tick frequency. These constants are defined in [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
, but they are accessible from [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 as well.

**tzinfo**[`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, optional

Time zone information. The default is None.

**\*\*kwargs**

Additional keyword arguments are passed to the [`dateutil.rrule`](https://dateutil.readthedocs.io/en/stable/rrule.html#module-dateutil.rrule "(in dateutil v3.9.0)")
.

set(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L965-L969)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper.set "Link to this definition")

Set parameters for an existing wrapper.

matplotlib.dates.set\_epoch(_epoch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/dates.py#L266-L292)
[#](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "Link to this definition")

Set the epoch (origin for dates) for datetime calculations.

The default epoch is `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`).

If microsecond accuracy is desired, the date being plotted needs to be within approximately 70 years of the epoch. Matplotlib internally represents dates as days since the epoch, so floating point dynamic range needs to be within a factor of 2^52.

[`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
 must be called before any dates are converted (i.e. near the import section) or a RuntimeError will be raised.

See also [Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)
.

Parameters:

**epoch**str

valid UTC date parsable by [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 (do not include timezone).

On this page