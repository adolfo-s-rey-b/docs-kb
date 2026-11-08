[Skip to content](https://lubridate.tidyverse.org/reference/lubridate-package.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Dates and times made easy with lubridate
========================================

Source: [`R/package.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/package.r)

`lubridate-package.Rd`

Lubridate provides tools that make it easier to parse and manipulate dates. These tools are grouped below by common purpose. More information about each function can be found in its help documentation.

Parsing dates[](https://lubridate.tidyverse.org/reference/lubridate-package.html#parsing-dates)

------------------------------------------------------------------------------------------------

Lubridate's parsing functions read strings into R as POSIXct date-time objects. Users should choose the function whose name models the order in which the year ('y'), month ('m') and day ('d') elements appear the string to be parsed: `[dmy()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[myd()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[ymd()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[ydm()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[dym()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[mdy()](https://lubridate.tidyverse.org/reference/ymd.html) `, `[ymd_hms()](https://lubridate.tidyverse.org/reference/ymd_hms.html) `). A very flexible and user friendly parser is provided by `[parse_date_time()](https://lubridate.tidyverse.org/reference/parse_date_time.html) `.

Lubridate can also parse partial dates from strings into [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 objects with the functions `[hm()](https://lubridate.tidyverse.org/reference/hms.html) `, `[hms()](https://lubridate.tidyverse.org/reference/hms.html) ` and `[ms()](https://lubridate.tidyverse.org/reference/hms.html) `.

Lubridate has an inbuilt very fast POSIX parser. Most of the `[strptime()](https://rdrr.io/r/base/strptime.html) ` formats and various extensions are supported for English locales. See `[parse_date_time()](https://lubridate.tidyverse.org/reference/parse_date_time.html) ` for more details.

Manipulating dates[](https://lubridate.tidyverse.org/reference/lubridate-package.html#manipulating-dates)

----------------------------------------------------------------------------------------------------------

Lubridate distinguishes between moments in time (known as `[instants()](https://lubridate.tidyverse.org/reference/is.instant.html) `) and spans of time (known as time spans, see [Timespan](https://lubridate.tidyverse.org/reference/Timespan-class.html)
). Time spans are further separated into [Duration](https://lubridate.tidyverse.org/reference/Duration-class.html)
, [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 and [Interval](https://lubridate.tidyverse.org/reference/Interval-class.html)
 objects.

Instants[](https://lubridate.tidyverse.org/reference/lubridate-package.html#instants)

--------------------------------------------------------------------------------------

Instants are specific moments of time. Date, POSIXct, and POSIXlt are the three object classes Base R recognizes as instants. `[is.Date()](https://lubridate.tidyverse.org/reference/date_utils.html) ` tests whether an object inherits from the Date class. `[is.POSIXt()](https://lubridate.tidyverse.org/reference/posix_utils.html) ` tests whether an object inherits from the POSIXlt or POSIXct classes. `[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) ` tests whether an object inherits from any of the three classes.

`[now()](https://lubridate.tidyverse.org/reference/now.html) ` returns the current system time as a POSIXct object. `[today()](https://lubridate.tidyverse.org/reference/now.html) ` returns the current system date. For convenience, 1970-01-01 00:00:00 is saved to [origin](https://lubridate.tidyverse.org/reference/origin.html)
. This is the instant from which POSIXct times are calculated. Try `unclass(now())` to see the numeric structure that underlies POSIXct objects. Each POSIXct object is saved as the number of seconds it occurred after 1970-01-01 00:00:00.

Conceptually, instants are a combination of measurements on different units (i.e, years, months, days, etc.). The individual values for these units can be extracted from an instant and set with the accessor functions `[second()](https://lubridate.tidyverse.org/reference/second.html) `, `[minute()](https://lubridate.tidyverse.org/reference/minute.html) `, `[hour()](https://lubridate.tidyverse.org/reference/hour.html) `, `[day()](https://lubridate.tidyverse.org/reference/day.html) `, `[yday()](https://lubridate.tidyverse.org/reference/day.html) `, `[mday()](https://lubridate.tidyverse.org/reference/day.html) `, `[wday()](https://lubridate.tidyverse.org/reference/day.html) `, `[week()](https://lubridate.tidyverse.org/reference/week.html) `, `[month()](https://lubridate.tidyverse.org/reference/month.html) `, `[year()](https://lubridate.tidyverse.org/reference/year.html) `, `[tz()](https://lubridate.tidyverse.org/reference/tz.html) `, and `[dst()](https://lubridate.tidyverse.org/reference/dst.html) `. Note: the accessor functions are named after the singular form of an element. They shouldn't be confused with the period helper functions that have the plural form of the units as a name (e.g, `[seconds()](https://lubridate.tidyverse.org/reference/period.html) `).

Rounding dates[](https://lubridate.tidyverse.org/reference/lubridate-package.html#rounding-dates)

--------------------------------------------------------------------------------------------------

Instants can be rounded to a convenient unit using the functions `[ceiling_date()](https://lubridate.tidyverse.org/reference/round_date.html) `, `[floor_date()](https://lubridate.tidyverse.org/reference/round_date.html) ` and `[round_date()](https://lubridate.tidyverse.org/reference/round_date.html) `.

Time zones[](https://lubridate.tidyverse.org/reference/lubridate-package.html#time-zones)

------------------------------------------------------------------------------------------

Lubridate provides two helper functions for working with time zones. `[with_tz()](https://lubridate.tidyverse.org/reference/with_tz.html) ` changes the time zone in which an instant is displayed. The clock time displayed for the instant changes, but the moment of time described remains the same. `[force_tz()](https://lubridate.tidyverse.org/reference/force_tz.html) ` changes only the time zone element of an instant. The clock time displayed remains the same, but the resulting instant describes a new moment of time.

Timespans[](https://lubridate.tidyverse.org/reference/lubridate-package.html#timespans)

----------------------------------------------------------------------------------------

A timespan is a length of time that may or may not be connected to a particular instant. For example, three months is a timespan. So is an hour and a half. Base R uses difftime class objects to record timespans. However, people are not always consistent in how they expect time to behave. Sometimes the passage of time is a monotone progression of instants that should be as mathematically reliable as the number line. On other occasions time must follow complex conventions and rules so that the clock times we see reflect what we expect to observe in terms of daylight, season, and congruence with the atomic clock. To better navigate the nuances of time, lubridate creates three additional timespan classes, each with its own specific and consistent behavior: [Interval](https://lubridate.tidyverse.org/reference/Interval-class.html)
, [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 and [Duration](https://lubridate.tidyverse.org/reference/Duration-class.html)
.

`[is.difftime()](https://lubridate.tidyverse.org/reference/is.difftime.html) ` tests whether an object inherits from the difftime class. `[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) ` tests whether an object inherits from any of the four timespan classes.

Durations[](https://lubridate.tidyverse.org/reference/lubridate-package.html#durations)

----------------------------------------------------------------------------------------

Durations measure the exact amount of time that occurs between two instants. This can create unexpected results in relation to clock times if a leap second, leap year, or change in daylight savings time (DST) occurs in the interval.

Functions for working with durations include `[is.duration()](https://lubridate.tidyverse.org/reference/duration.html) `, `[as.duration()](https://lubridate.tidyverse.org/reference/as.duration.html) ` and `[duration()](https://lubridate.tidyverse.org/reference/duration.html) `. `[dseconds()](https://lubridate.tidyverse.org/reference/duration.html) `, `[dminutes()](https://lubridate.tidyverse.org/reference/duration.html) `, `[dhours()](https://lubridate.tidyverse.org/reference/duration.html) `, `[ddays()](https://lubridate.tidyverse.org/reference/duration.html) `, `[dweeks()](https://lubridate.tidyverse.org/reference/duration.html) ` and `[dyears()](https://lubridate.tidyverse.org/reference/duration.html) ` convenient lengths.

Periods[](https://lubridate.tidyverse.org/reference/lubridate-package.html#periods)

------------------------------------------------------------------------------------

Periods measure the change in clock time that occurs between two instants. Periods provide robust predictions of clock time in the presence of leap seconds, leap years, and changes in DST.

Functions for working with periods include `[is.period()](https://lubridate.tidyverse.org/reference/period.html) `, `[as.period()](https://lubridate.tidyverse.org/reference/as.period.html) ` and `[period()](https://lubridate.tidyverse.org/reference/period.html) `. `[seconds()](https://lubridate.tidyverse.org/reference/period.html) `, `[minutes()](https://lubridate.tidyverse.org/reference/period.html) `, `[hours()](https://lubridate.tidyverse.org/reference/period.html) `, `[days()](https://lubridate.tidyverse.org/reference/period.html) `, `[weeks()](https://lubridate.tidyverse.org/reference/period.html) `, `[months()](https://rdrr.io/r/base/weekday.POSIXt.html) ` and `[years()](https://lubridate.tidyverse.org/reference/period.html) ` quickly create periods of convenient lengths.

Intervals[](https://lubridate.tidyverse.org/reference/lubridate-package.html#intervals)

----------------------------------------------------------------------------------------

Intervals are timespans that begin at a specific instant and end at a specific instant. Intervals retain complete information about a timespan. They provide the only reliable way to convert between periods and durations.

Functions for working with intervals include `[is.interval()](https://lubridate.tidyverse.org/reference/interval.html) `, `[as.interval()](https://lubridate.tidyverse.org/reference/as.interval.html) `, `[interval()](https://lubridate.tidyverse.org/reference/interval.html) `, `[int_shift()](https://lubridate.tidyverse.org/reference/interval.html) `, `[int_flip()](https://lubridate.tidyverse.org/reference/interval.html) `, `[int_aligns()](https://lubridate.tidyverse.org/reference/interval.html) `, `[int_overlaps()](https://lubridate.tidyverse.org/reference/interval.html) `, and `[%within%](https://lubridate.tidyverse.org/reference/within-interval.html) `. Intervals can also be manipulated with intersect, union, and setdiff().

Miscellaneous[](https://lubridate.tidyverse.org/reference/lubridate-package.html#miscellaneous)

------------------------------------------------------------------------------------------------

`[decimal_date()](https://lubridate.tidyverse.org/reference/decimal_date.html) ` converts an instant to a decimal of its year. `[leap_year()](https://lubridate.tidyverse.org/reference/leap_year.html) ` tests whether an instant occurs during a leap year. `[pretty_dates()](https://lubridate.tidyverse.org/reference/pretty_dates.html) ` provides a method of making pretty breaks for date-times. [lakers](https://lubridate.tidyverse.org/reference/lakers.html)
 is a data set that contains information about the Los Angeles Lakers 2008-2009 basketball season.

References[](https://lubridate.tidyverse.org/reference/lubridate-package.html#references)

------------------------------------------------------------------------------------------

Garrett Grolemund, Hadley Wickham (2011). Dates and Times Made Easy with lubridate. Journal of Statistical Software, 40(3), 1-25. [https://www.jstatsoft.org/v40/i03/](https://www.jstatsoft.org/v40/i03/)
.

See also[](https://lubridate.tidyverse.org/reference/lubridate-package.html#see-also)

--------------------------------------------------------------------------------------

Useful links:

*   [https://lubridate.tidyverse.org](https://lubridate.tidyverse.org/)
    
*   [https://github.com/tidyverse/lubridate](https://github.com/tidyverse/lubridate)
    
*   Report bugs at [https://github.com/tidyverse/lubridate/issues](https://github.com/tidyverse/lubridate/issues)
    

Author[](https://lubridate.tidyverse.org/reference/lubridate-package.html#author)

----------------------------------------------------------------------------------

**Maintainer**: Vitalie Spinu [spinuvit@gmail.com](mailto:spinuvit@gmail.com)

Authors:

*   Garrett Grolemund
    
*   Hadley Wickham
    

Other contributors:

*   Davis Vaughan \[contributor\]
    
*   Ian Lyttle \[contributor\]
    
*   Imanuel Costigan \[contributor\]
    
*   Jason Law \[contributor\]
    
*   Doug Mitarotonda \[contributor\]
    
*   Joseph Larmarange \[contributor\]
    
*   Jonathan Boiser \[contributor\]
    
*   Chel Hee Lee \[contributor\]