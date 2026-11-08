[Skip to content](https://lubridate.tidyverse.org/reference/make_difftime.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Create a difftime object.
=========================

Source: [`R/difftimes.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/difftimes.r)

`make_difftime.Rd`

`make_difftime()` creates a difftime object with the specified number of units. Entries for different units are cumulative. difftime displays durations in various units, but these units are estimates given for convenience. The underlying object is always recorded as a fixed number of seconds.

Usage[](https://lubridate.tidyverse.org/reference/make_difftime.html#ref-usage)

--------------------------------------------------------------------------------

    make_difftime(num = NULL, units = "auto", ...)

Arguments[](https://lubridate.tidyverse.org/reference/make_difftime.html#arguments)

------------------------------------------------------------------------------------

num[](https://lubridate.tidyverse.org/reference/make_difftime.html#arg-num)

Optional number of seconds

units[](https://lubridate.tidyverse.org/reference/make_difftime.html#arg-units)

a character vector that lists the type of units to use for the display of the return value (see examples). If `units` is "auto" (the default) the display units are computed automatically. This might create undesirable effects when converting `difftime` objects to numeric values in data processing.

...[](https://lubridate.tidyverse.org/reference/make_difftime.html#arg--)

a list of time units to be included in the difftime and their amounts. Seconds, minutes, hours, days, and weeks are supported. Normally only one of `num` or `...` are present. If both are present, the `difftime` objects are concatenated.

Value[](https://lubridate.tidyverse.org/reference/make_difftime.html#value)

----------------------------------------------------------------------------

a difftime object

Details[](https://lubridate.tidyverse.org/reference/make_difftime.html#details)

--------------------------------------------------------------------------------

Conceptually, difftime objects are a type of duration. They measure the exact passage of time but do not always align with measurements made in larger units of time such as hours, months and years. This is because the length of larger time units can be affected by conventions such as leap years and Daylight Savings Time. lubridate provides a second class for measuring durations, the Duration class.

See also[](https://lubridate.tidyverse.org/reference/make_difftime.html#see-also)

----------------------------------------------------------------------------------

`[duration()](https://lubridate.tidyverse.org/reference/duration.html) `, `[as.duration()](https://lubridate.tidyverse.org/reference/as.duration.html) `

Examples[](https://lubridate.tidyverse.org/reference/make_difftime.html#ref-examples)

--------------------------------------------------------------------------------------

    make_difftime(1)
    #> Time difference of 1 secs
    make_difftime(60)
    #> Time difference of 1 mins
    make_difftime(3600)
    #> Time difference of 1 hours
    make_difftime(3600, units = "minute")
    #> Time difference of 60 mins
    # Time difference of 60 mins
    make_difftime(second = 90)
    #> Time difference of 1.5 mins
    # Time difference of 1.5 mins
    make_difftime(minute = 1.5)
    #> Time difference of 1.5 mins
    # Time difference of 1.5 mins
    make_difftime(second = 3, minute = 1.5, hour = 2, day = 6, week = 1)
    #> Time difference of 13.08441 days
    # Time difference of 13.08441 days
    make_difftime(hour = 1, minute = -60)
    #> Time difference of 0 secs
    # Time difference of 0 secs
    make_difftime(day = -1)
    #> Time difference of -1 days
    # Time difference of -1 days
    make_difftime(120, day = -1, units = "minute")
    #> Time differences in mins
    #> [1]     2 -1440
    # Time differences in mins