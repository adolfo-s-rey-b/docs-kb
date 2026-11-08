[Skip to content](https://lubridate.tidyverse.org/reference/pretty_dates.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Computes attractive axis breaks for date-time data
==================================================

Source: [`R/pretty.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/pretty.r)

`pretty_dates.Rd`

`pretty_dates()` identifies which unit of time the sub-intervals should be measured in to provide approximately n breaks, then chooses a "pretty" length for the sub-intervals and sets start and end points that 1) span the entire range of the data, and 2) allow the breaks to occur on important date-times (i.e. on the hour, on the first of the month, etc.)

Usage[](https://lubridate.tidyverse.org/reference/pretty_dates.html#ref-usage)

-------------------------------------------------------------------------------

    pretty_dates(x, n, ...)

Arguments[](https://lubridate.tidyverse.org/reference/pretty_dates.html#arguments)

-----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/pretty_dates.html#arg-x)

a vector of POSIXct, POSIXlt, Date, or chron date-time objects

n[](https://lubridate.tidyverse.org/reference/pretty_dates.html#arg-n)

integer value of the desired number of breaks

...[](https://lubridate.tidyverse.org/reference/pretty_dates.html#arg--)

additional arguments to pass to function

Value[](https://lubridate.tidyverse.org/reference/pretty_dates.html#value)

---------------------------------------------------------------------------

a vector of date-times that can be used as axis tick marks or bin breaks

Examples[](https://lubridate.tidyverse.org/reference/pretty_dates.html#ref-examples)

-------------------------------------------------------------------------------------

    x <- seq.Date(as.Date("2009-08-02"), by = "year", length.out = 2)
    pretty_dates(x, 12)
    #>  [1] "2009-08-01 UTC" "2009-09-01 UTC" "2009-10-01 UTC"
    #>  [4] "2009-11-01 UTC" "2009-12-01 UTC" "2010-01-01 UTC"
    #>  [7] "2010-02-01 UTC" "2010-03-01 UTC" "2010-04-01 UTC"
    #> [10] "2010-05-01 UTC" "2010-06-01 UTC" "2010-07-01 UTC"
    #> [13] "2010-08-01 UTC" "2010-09-01 UTC"