[Skip to content](https://lubridate.tidyverse.org/reference/index.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Package index
=============

Date/time parsing[](https://lubridate.tidyverse.org/reference/index.html#date-time-parsing)

--------------------------------------------------------------------------------------------

`[ymd()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[ydm()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[mdy()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[myd()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[dmy()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[dym()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[yq()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[ym()](https://lubridate.tidyverse.org/reference/ymd.html) ` `[my()](https://lubridate.tidyverse.org/reference/ymd.html) `

Parse dates with **y**ear, **m**onth, and **d**ay components

`[ymd_hms()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[ymd_hm()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[ymd_h()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[dmy_hms()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[dmy_hm()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[dmy_h()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[mdy_hms()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[mdy_hm()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[mdy_h()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[ydm_hms()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[ydm_hm()](https://lubridate.tidyverse.org/reference/ymd_hms.html) ` `[ydm_h()](https://lubridate.tidyverse.org/reference/ymd_hms.html) `

Parse date-times with **y**ear, **m**onth, and **d**ay, **h**our, **m**inute, and **s**econd components.

`[ms()](https://lubridate.tidyverse.org/reference/hms.html) ` `[hm()](https://lubridate.tidyverse.org/reference/hms.html) ` `[hms()](https://lubridate.tidyverse.org/reference/hms.html) `

Parse periods with **h**our, **m**inute, and **s**econd components

`[parse_date_time()](https://lubridate.tidyverse.org/reference/parse_date_time.html) ` `[parse_date_time2()](https://lubridate.tidyverse.org/reference/parse_date_time.html) ` `[fast_strptime()](https://lubridate.tidyverse.org/reference/parse_date_time.html) `

User friendly date-time parsing functions

`[guess_formats()](https://lubridate.tidyverse.org/reference/guess_formats.html) `

Guess possible date-times formats from a character vector

Setting, getting, and rounding[](https://lubridate.tidyverse.org/reference/index.html#setting-getting-and-rounding)

--------------------------------------------------------------------------------------------------------------------

`[year()](https://lubridate.tidyverse.org/reference/year.html) ` ``[`year<-`()](https://lubridate.tidyverse.org/reference/year.html) `` `[isoyear()](https://lubridate.tidyverse.org/reference/year.html) ` `[epiyear()](https://lubridate.tidyverse.org/reference/year.html) `

Get/set years component of a date-time

`[quarter()](https://lubridate.tidyverse.org/reference/quarter.html) ` `[semester()](https://lubridate.tidyverse.org/reference/quarter.html) `

Get the fiscal quarter and semester of a date-time

`[month()](https://lubridate.tidyverse.org/reference/month.html) ` ``[`month<-`()](https://lubridate.tidyverse.org/reference/month.html) ``

Get/set months component of a date-time

`[week()](https://lubridate.tidyverse.org/reference/week.html) ` ``[`week<-`()](https://lubridate.tidyverse.org/reference/week.html) `` `[isoweek()](https://lubridate.tidyverse.org/reference/week.html) ` `[epiweek()](https://lubridate.tidyverse.org/reference/week.html) `

Get/set weeks component of a date-time

`[day()](https://lubridate.tidyverse.org/reference/day.html) ` `[mday()](https://lubridate.tidyverse.org/reference/day.html) ` `[wday()](https://lubridate.tidyverse.org/reference/day.html) ` `[qday()](https://lubridate.tidyverse.org/reference/day.html) ` `[yday()](https://lubridate.tidyverse.org/reference/day.html) ` ``[`day<-`()](https://lubridate.tidyverse.org/reference/day.html) `` ``[`mday<-`()](https://lubridate.tidyverse.org/reference/day.html) `` ``[`qday<-`()](https://lubridate.tidyverse.org/reference/day.html) `` ``[`wday<-`()](https://lubridate.tidyverse.org/reference/day.html) `` ``[`yday<-`()](https://lubridate.tidyverse.org/reference/day.html) ``

Get/set days component of a date-time

`[hour()](https://lubridate.tidyverse.org/reference/hour.html) ` ``[`hour<-`()](https://lubridate.tidyverse.org/reference/hour.html) ``

Get/set hours component of a date-time

`[minute()](https://lubridate.tidyverse.org/reference/minute.html) ` ``[`minute<-`()](https://lubridate.tidyverse.org/reference/minute.html) ``

Get/set minutes component of a date-time

`[second()](https://lubridate.tidyverse.org/reference/second.html) ` ``[`second<-`()](https://lubridate.tidyverse.org/reference/second.html) ``

Get/set seconds component of a date-time

`[tz()](https://lubridate.tidyverse.org/reference/tz.html) ` ``[`tz<-`()](https://lubridate.tidyverse.org/reference/tz.html) ``

Get/set time zone component of a date-time

Date-time helpers[](https://lubridate.tidyverse.org/reference/index.html#date-time-helpers)

--------------------------------------------------------------------------------------------

`[as_date()](https://lubridate.tidyverse.org/reference/as_date.html) ` `[as_datetime()](https://lubridate.tidyverse.org/reference/as_date.html) `

Convert an object to a date or date-time

`[cyclic_encoding()](https://lubridate.tidyverse.org/reference/cyclic_encoding.html) `

Cyclic encoding of date-times

`[date()](https://lubridate.tidyverse.org/reference/date.html) ` ``[`date<-`()](https://lubridate.tidyverse.org/reference/date.html) ``

Get/set date component of a date-time

`[decimal_date()](https://lubridate.tidyverse.org/reference/decimal_date.html) `

Converts a date to a decimal of its year

`[is.Date()](https://lubridate.tidyverse.org/reference/date_utils.html) ` `[Date()](https://lubridate.tidyverse.org/reference/date_utils.html) ` `[NA_Date_](https://lubridate.tidyverse.org/reference/date_utils.html) `

Various date utilities

`[is.POSIXt()](https://lubridate.tidyverse.org/reference/posix_utils.html) ` `[is.POSIXlt()](https://lubridate.tidyverse.org/reference/posix_utils.html) ` `[is.POSIXct()](https://lubridate.tidyverse.org/reference/posix_utils.html) ` `[POSIXct()](https://lubridate.tidyverse.org/reference/posix_utils.html) ` `[NA_POSIXct_](https://lubridate.tidyverse.org/reference/posix_utils.html) `

Various POSIX utilities

`[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) ` `[is.timepoint()](https://lubridate.tidyverse.org/reference/is.instant.html) `

Is x a date-time object?

`[make_datetime()](https://lubridate.tidyverse.org/reference/make_datetime.html) ` `[make_date()](https://lubridate.tidyverse.org/reference/make_datetime.html) `

Efficient creation of date-times from numeric representations

`[now()](https://lubridate.tidyverse.org/reference/now.html) ` `[today()](https://lubridate.tidyverse.org/reference/now.html) `

The current day and time

`[origin](https://lubridate.tidyverse.org/reference/origin.html) `

1970-01-01 UTC

Durations[](https://lubridate.tidyverse.org/reference/index.html#durations)

----------------------------------------------------------------------------

A ‘duration’ is a timespan measured in seconds.

`[duration()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dseconds()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dminutes()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dhours()](https://lubridate.tidyverse.org/reference/duration.html) ` `[ddays()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dweeks()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dmonths()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dyears()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dmilliseconds()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dmicroseconds()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dnanoseconds()](https://lubridate.tidyverse.org/reference/duration.html) ` `[dpicoseconds()](https://lubridate.tidyverse.org/reference/duration.html) ` `[is.duration()](https://lubridate.tidyverse.org/reference/duration.html) `

Create a duration object.

`[is.difftime()](https://lubridate.tidyverse.org/reference/is.difftime.html) `

Is x a difftime object?

`[make_difftime()](https://lubridate.tidyverse.org/reference/make_difftime.html) `

Create a difftime object.

`[as.duration()](https://lubridate.tidyverse.org/reference/as.duration.html) `

Change an object to a duration

`[Duration-class](https://lubridate.tidyverse.org/reference/Duration-class.html) ` `[durations](https://lubridate.tidyverse.org/reference/Duration-class.html) `

Duration class

Periods[](https://lubridate.tidyverse.org/reference/index.html#periods)

------------------------------------------------------------------------

A ‘period’ is a timespan defined in civil time (human) units like years, months, and days.

`[period()](https://lubridate.tidyverse.org/reference/period.html) ` `[is.period()](https://lubridate.tidyverse.org/reference/period.html) ` `[seconds()](https://lubridate.tidyverse.org/reference/period.html) ` `[minutes()](https://lubridate.tidyverse.org/reference/period.html) ` `[hours()](https://lubridate.tidyverse.org/reference/period.html) ` `[days()](https://lubridate.tidyverse.org/reference/period.html) ` `[weeks()](https://lubridate.tidyverse.org/reference/period.html) ` `[years()](https://lubridate.tidyverse.org/reference/period.html) ` `[milliseconds()](https://lubridate.tidyverse.org/reference/period.html) ` `[microseconds()](https://lubridate.tidyverse.org/reference/period.html) ` `[nanoseconds()](https://lubridate.tidyverse.org/reference/period.html) ` `[picoseconds()](https://lubridate.tidyverse.org/reference/period.html) ` `[months(_<numeric>_)](https://lubridate.tidyverse.org/reference/period.html) `

Create or parse period objects

`[period_to_seconds()](https://lubridate.tidyverse.org/reference/period_to_seconds.html) ` `[seconds_to_period()](https://lubridate.tidyverse.org/reference/period_to_seconds.html) `

Contrive a period to/from a given number of seconds

`[as.period()](https://lubridate.tidyverse.org/reference/as.period.html) `

Change an object to a period

`[Period-class](https://lubridate.tidyverse.org/reference/Period-class.html) `

Period class

Intervals[](https://lubridate.tidyverse.org/reference/index.html#intervals)

----------------------------------------------------------------------------

An `interval` is a timespan defined by two date-times.

`[interval()](https://lubridate.tidyverse.org/reference/interval.html) ` ``[`%--%`](https://lubridate.tidyverse.org/reference/interval.html) `` `[is.interval()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_start()](https://lubridate.tidyverse.org/reference/interval.html) ` ``[`int_start<-`()](https://lubridate.tidyverse.org/reference/interval.html) `` `[int_end()](https://lubridate.tidyverse.org/reference/interval.html) ` ``[`int_end<-`()](https://lubridate.tidyverse.org/reference/interval.html) `` `[int_length()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_flip()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_shift()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_overlaps()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_standardize()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_aligns()](https://lubridate.tidyverse.org/reference/interval.html) ` `[int_diff()](https://lubridate.tidyverse.org/reference/interval.html) `

Utilities for creation and manipulation of `Interval` objects

`[as.interval()](https://lubridate.tidyverse.org/reference/as.interval.html) `

Change an object to an `interval`

``[`%within%`](https://lubridate.tidyverse.org/reference/within-interval.html) ``

Does a date (or interval) fall within an interval?

`[Interval-class](https://lubridate.tidyverse.org/reference/Interval-class.html) ` `[intervals](https://lubridate.tidyverse.org/reference/Interval-class.html) `

Interval class

Timespans[](https://lubridate.tidyverse.org/reference/index.html#timespans)

----------------------------------------------------------------------------

Timespans are the generic concept that underlies durations, periods, and intervals.

`[timespan](https://lubridate.tidyverse.org/reference/timespan.html) ` `[timespans](https://lubridate.tidyverse.org/reference/timespan.html) `

Description of time span classes in lubridate

`[time_length()](https://lubridate.tidyverse.org/reference/time_length.html) `

Compute the exact length of a time span

`[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) `

Is x a length of time?

Formatters[](https://lubridate.tidyverse.org/reference/index.html#formatters)

------------------------------------------------------------------------------

`[stamp()](https://lubridate.tidyverse.org/reference/stamp.html) ` `[stamp_date()](https://lubridate.tidyverse.org/reference/stamp.html) ` `[stamp_time()](https://lubridate.tidyverse.org/reference/stamp.html) `

Format dates and times based on human-friendly templates

`[format_ISO8601()](https://lubridate.tidyverse.org/reference/format_ISO8601.html) `

Format in ISO8601 character format

Other modification functions[](https://lubridate.tidyverse.org/reference/index.html#other-modification-functions)

------------------------------------------------------------------------------------------------------------------

`[update(_<POSIXt>_)](https://lubridate.tidyverse.org/reference/DateTimeUpdate.html) `

Changes the components of a date object

`[fit_to_timeline()](https://lubridate.tidyverse.org/reference/fit_to_timeline.html) `

Fit a POSIXlt date-time to the timeline

`[with_tz()](https://lubridate.tidyverse.org/reference/with_tz.html) `

Get date-time in a different time zone

`[force_tz()](https://lubridate.tidyverse.org/reference/force_tz.html) ` `[force_tzs()](https://lubridate.tidyverse.org/reference/force_tz.html) `

Replace time zone to create new date-time

`[round_date()](https://lubridate.tidyverse.org/reference/round_date.html) ` `[floor_date()](https://lubridate.tidyverse.org/reference/round_date.html) ` `[ceiling_date()](https://lubridate.tidyverse.org/reference/round_date.html) `

Round, floor and ceiling methods for date-time objects

`[pretty_dates()](https://lubridate.tidyverse.org/reference/pretty_dates.html) `

Computes attractive axis breaks for date-time data

`[rollbackward()](https://lubridate.tidyverse.org/reference/rollbackward.html) ` `[rollback()](https://lubridate.tidyverse.org/reference/rollbackward.html) ` `[rollforward()](https://lubridate.tidyverse.org/reference/rollbackward.html) `

Roll backward or forward a date the previous, current or next month

``[`%m+%`](https://lubridate.tidyverse.org/reference/mplus.html) `` `[add_with_rollback()](https://lubridate.tidyverse.org/reference/mplus.html) `

Add and subtract months to a date without exceeding the last day of the new month

`[local_time()](https://lubridate.tidyverse.org/reference/local_time.html) `

Get local time from a date-time vector.

Other date-time components[](https://lubridate.tidyverse.org/reference/index.html#other-date-time-components)

--------------------------------------------------------------------------------------------------------------

`[am()](https://lubridate.tidyverse.org/reference/am.html) ` `[pm()](https://lubridate.tidyverse.org/reference/am.html) `

Does date time occur in the am or pm?

`[days_in_month()](https://lubridate.tidyverse.org/reference/days_in_month.html) `

Get the number of days in the month of a date-time

`[dst()](https://lubridate.tidyverse.org/reference/dst.html) `

Get **d**aylight **s**avings **t**ime indicator of a date-time

`[leap_year()](https://lubridate.tidyverse.org/reference/leap_year.html) `

Is a year a leap year?

`[date_decimal()](https://lubridate.tidyverse.org/reference/date_decimal.html) `

Converts a decimal to a date

Data[](https://lubridate.tidyverse.org/reference/index.html#data)

------------------------------------------------------------------

`[lakers](https://lubridate.tidyverse.org/reference/lakers.html) `

Lakers 2008-2009 basketball data set