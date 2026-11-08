[Skip to content](https://lubridate.tidyverse.org/reference/as.duration.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Change an object to a duration
==============================

Source: [`R/coercion.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/coercion.r)

`as.duration.Rd`

as.duration changes Interval, Period and numeric class objects to Duration objects. Numeric objects are changed to Duration objects with the seconds unit equal to the numeric value.

Usage[](https://lubridate.tidyverse.org/reference/as.duration.html#ref-usage)

------------------------------------------------------------------------------

    as.duration(x, ...)

Arguments[](https://lubridate.tidyverse.org/reference/as.duration.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/as.duration.html#arg-x)

Object to be coerced to a duration

...[](https://lubridate.tidyverse.org/reference/as.duration.html#arg--)

Parameters passed to other methods. Currently unused.

Value[](https://lubridate.tidyverse.org/reference/as.duration.html#value)

--------------------------------------------------------------------------

A duration object

Details[](https://lubridate.tidyverse.org/reference/as.duration.html#details)

------------------------------------------------------------------------------

Durations are exact time measurements, whereas periods are relative time measurements. See [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
. The length of a period depends on when it occurs. Hence, a one to one mapping does not exist between durations and periods. When used with a period object, as.duration provides an inexact estimate of the length of the period; each time unit is assigned its most common number of seconds. A period of one month is converted to 2628000 seconds (approximately 30.42 days). This ensures that 12 months will sum to 365 days, or one normal year. For an exact transformation, first transform the period to an interval with `[as.interval()](https://lubridate.tidyverse.org/reference/as.interval.html) `.

See also[](https://lubridate.tidyverse.org/reference/as.duration.html#see-also)

--------------------------------------------------------------------------------

[Duration](https://lubridate.tidyverse.org/reference/Duration-class.html)
, `[duration()](https://lubridate.tidyverse.org/reference/duration.html) `

Examples[](https://lubridate.tidyverse.org/reference/as.duration.html#ref-examples)

------------------------------------------------------------------------------------

    span <- interval(ymd("2009-01-01"), ymd("2009-08-01")) # interval
    as.duration(span)
    #> [1] "18316800s (~30.29 weeks)"
    as.duration(10) # numeric
    #> [1] "10s"
    dur <- duration(hours = 10, minutes = 6)
    as.numeric(dur, "hours")
    #> [1] 10.1
    as.numeric(dur, "minutes")
    #> [1] 606