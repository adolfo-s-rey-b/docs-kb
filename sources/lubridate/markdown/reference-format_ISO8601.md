[Skip to content](https://lubridate.tidyverse.org/reference/format_ISO8601.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Format in ISO8601 character format
==================================

Source: [`R/format_ISO8601.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/format_ISO8601.r)

`format_ISO8601.Rd`

Format in ISO8601 character format

Usage[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#ref-usage)

---------------------------------------------------------------------------------

    format_ISO8601(x, usetz = FALSE, precision = NULL, ...)

Arguments[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#arguments)

-------------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#arg-x)

An object to convert to ISO8601 character format.

usetz[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#arg-usetz)

Include the time zone in the formatting. If `usetz` is `TRUE`, the time zone is included. If `usetz` is `"Z"`, the time is converted to "UTC" and the time zone is indicated with "Z" ISO8601 notation.

precision[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#arg-precision)

The amount of precision to represent with substrings of "ymdhms", as year, month, day, hour, minute, and second. (e.g. "ymd" is days precision, "ymdhm" is minute precision. When `NULL`, full precision for the object is shown.

...[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#arg--)

Additional arguments to methods.

Value[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#value)

-----------------------------------------------------------------------------

A character vector of ISO8601-formatted text.

References[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#references)

---------------------------------------------------------------------------------------

[https://en.wikipedia.org/wiki/ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601)

Examples[](https://lubridate.tidyverse.org/reference/format_ISO8601.html#ref-examples)

---------------------------------------------------------------------------------------

    format_ISO8601(as.Date("02-01-2018", format = "%m-%d-%Y"))
    #> [1] "2018-02-01"
    format_ISO8601(as.POSIXct("2018-02-01 03:04:05", tz = "America/New_York"), usetz = TRUE)
    #> [1] "2018-02-01T03:04:05-0500"
    format_ISO8601(as.POSIXct("2018-02-01 03:04:05", tz = "America/New_York"), precision = "ymdhm")
    #> [1] "2018-02-01T03:04"