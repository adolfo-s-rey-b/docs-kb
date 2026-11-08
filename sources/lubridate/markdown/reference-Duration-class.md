[Skip to content](https://lubridate.tidyverse.org/reference/Duration-class.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Duration class
==============

Source: [`R/durations.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/durations.r)

`Duration-class.Rd`

Duration is an S4 class that extends the [Timespan](https://lubridate.tidyverse.org/reference/Timespan-class.html)
 class. Durations record the exact number of seconds in a time span. They measure the exact passage of time but do not always align with measurements made in larger units of time such as hours, months and years. This is because the exact length of larger time units can be affected by conventions such as leap years and Daylight Savings Time.

Details[](https://lubridate.tidyverse.org/reference/Duration-class.html#details)

---------------------------------------------------------------------------------

Durations provide a method for measuring generalized timespans when we wish to treat time as a mathematical quantity that increases in a uniform, monotone manner along a continuous number line. They allow exact comparisons with other durations. See [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 for an alternative way to measure timespans that better preserves clock times.

Durations class objects have one slot: .Data, a numeric object equal to the number of seconds in the duration.