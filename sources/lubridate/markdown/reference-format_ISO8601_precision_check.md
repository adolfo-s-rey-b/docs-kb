[Skip to content](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Provide a format for ISO8601 dates and times with the requested precision.
==========================================================================

Source: [`R/format_ISO8601.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/format_ISO8601.r)

`format_ISO8601_precision_check.Rd`

Provide a format for ISO8601 dates and times with the requested precision.

Usage[](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#ref-usage)

-------------------------------------------------------------------------------------------------

    format_ISO8601_precision_check(precision, max_precision, usetz = FALSE)

Arguments[](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#arguments)

-----------------------------------------------------------------------------------------------------

precision[](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#arg-precision)

The amount of precision to represent with substrings of "ymdhms", as year, month, day, hour, minute, and second. (e.g. "ymd" is days precision, "ymdhm" is minute precision. When `NULL`, full precision for the object is shown.

max\_precision[](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#arg-max-precision)

The maximum precision allowed to be output.

usetz[](https://lubridate.tidyverse.org/reference/format_ISO8601_precision_check.html#arg-usetz)

Include the time zone in the formatting. If `usetz` is `TRUE`, the time zone is included. If `usetz` is `"Z"`, the time is converted to "UTC" and the time zone is indicated with "Z" ISO8601 notation.