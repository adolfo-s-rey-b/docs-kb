[Skip to content](https://lubridate.tidyverse.org/reference/as.period.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Change an object to a period
============================

Source: [`R/coercion.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/coercion.r)

`as.period.Rd`

as.period changes Interval, Duration, difftime and numeric class objects to Period class objects with the specified units.

Usage[](https://lubridate.tidyverse.org/reference/as.period.html#ref-usage)

----------------------------------------------------------------------------

    as.period(x, unit, ...)

Arguments[](https://lubridate.tidyverse.org/reference/as.period.html#arguments)

--------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/as.period.html#arg-x)

an interval, difftime, or numeric object

unit[](https://lubridate.tidyverse.org/reference/as.period.html#arg-unit)

A character string that specifies which time units to build period in. unit is only implemented for the as.period.numeric method and the as.period.interval method. For as.period.interval, as.period will convert intervals to units no larger than the specified unit.

...[](https://lubridate.tidyverse.org/reference/as.period.html#arg--)

additional arguments to pass to as.period

Value[](https://lubridate.tidyverse.org/reference/as.period.html#value)

------------------------------------------------------------------------

a period object

Details[](https://lubridate.tidyverse.org/reference/as.period.html#details)

----------------------------------------------------------------------------

Users must specify which time units to measure the period in. The exact length of each time unit in a period will depend on when it occurs. See [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 and `[period()](https://lubridate.tidyverse.org/reference/period.html) `. The choice of units is not trivial; units that are normally equal may differ in length depending on when the time period occurs. For example, when a leap second occurs one minute is longer than 60 seconds.

Because periods do not have a fixed length, they can not be accurately converted to and from Duration objects. Duration objects measure time spans in exact numbers of seconds, see [Duration](https://lubridate.tidyverse.org/reference/Duration-class.html)
. Hence, a one to one mapping does not exist between durations and periods. When used with a Duration object, as.period provides an inexact estimate; the duration is broken into time units based on the most common lengths of time units, in seconds. Because the length of months are particularly variable, a period with a months unit can not be coerced from a duration object. For an exact transformation, first transform the duration to an interval with `[as.interval()](https://lubridate.tidyverse.org/reference/as.interval.html) `.

Coercing an interval to a period may cause surprising behavior if you request periods with small units. A leap year is 366 days long, but one year long. Such an interval will convert to 366 days when unit is set to days and 1 year when unit is set to years. Adding 366 days to a date will often give a different result than adding one year. Daylight savings is the one exception where this does not apply. Interval lengths are calculated on the UTC timeline, which does not use daylight savings. Hence, periods converted with seconds or minutes will not reflect the actual variation in seconds and minutes that occurs due to daylight savings. These periods will show the "naive" change in seconds and minutes that is suggested by the differences in clock time. See the examples below.

See also[](https://lubridate.tidyverse.org/reference/as.period.html#see-also)

------------------------------------------------------------------------------

[Period](https://lubridate.tidyverse.org/reference/Period-class.html)
, `[period()](https://lubridate.tidyverse.org/reference/period.html) `

Examples[](https://lubridate.tidyverse.org/reference/as.period.html#ref-examples)

----------------------------------------------------------------------------------

    span <- interval(ymd_hms("2009-01-01 00:00:00"), ymd_hms("2010-02-02 01:01:01")) # interval
    as.period(span)
    #> [1] "1y 1m 1d 1H 1M 1S"
    as.period(span, unit = "day")
    #> [1] "397d 1H 1M 1S"
    "397d 1H 1M 1S"
    #> [1] "397d 1H 1M 1S"
    leap <- interval(ymd("2016-01-01"), ymd("2017-01-01"))
    as.period(leap, unit = "days")
    #> [1] "366d 0H 0M 0S"
    as.period(leap, unit = "years")
    #> [1] "1y 0m 0d 0H 0M 0S"
    dst <- interval(
      ymd("2016-11-06", tz = "America/Chicago"),
      ymd("2016-11-07", tz = "America/Chicago")
    )
    # as.period(dst, unit = "seconds")
    as.period(dst, unit = "hours")
    #> [1] "25H 0M 0S"
    per <- period(hours = 10, minutes = 6)
    as.numeric(per, "hours")
    #> [1] 10.1
    as.numeric(per, "minutes")
    #> [1] 606