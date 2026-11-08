[Skip to content](https://lubridate.tidyverse.org/reference/month.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set months component of a date-time
=======================================

Source: [`R/accessors-month.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-month.r)

`month.Rd`

Date-time must be a POSIXct, POSIXlt, Date, Period, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/month.html#ref-usage)

------------------------------------------------------------------------

    month(x, label = FALSE, abbr = TRUE, locale = Sys.getlocale("LC_TIME"))
    
    month(x) <- value

Arguments[](https://lubridate.tidyverse.org/reference/month.html#arguments)

----------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/month.html#arg-x)

a date-time object

label[](https://lubridate.tidyverse.org/reference/month.html#arg-label)

logical. TRUE will display the month as a character string such as "January." FALSE will display the month as a number.

abbr[](https://lubridate.tidyverse.org/reference/month.html#arg-abbr)

logical. FALSE will display the month as a character string label, such as "January". TRUE will display an abbreviated version of the label, such as "Jan". abbr is disregarded if label = FALSE.

locale[](https://lubridate.tidyverse.org/reference/month.html#arg-locale)

for month, locale to use for month names. Default to current locale.

value[](https://lubridate.tidyverse.org/reference/month.html#arg-value)

a numeric object

Value[](https://lubridate.tidyverse.org/reference/month.html#value)

--------------------------------------------------------------------

If `label = FALSE`: month as number (1-12, 1 = January, 12 = December), otherwise as an ordered factor.

Examples[](https://lubridate.tidyverse.org/reference/month.html#ref-examples)

------------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    month(x)
    #> [1] 3
    month(x) <- 1
    month(x) <- 13
    month(x) > 3
    #> [1] FALSE
    
    month(ymd(080101))
    #> [1] 1
    month(ymd(080101), label = TRUE)
    #> [1] Jan
    #> 12 Levels: Jan < Feb < Mar < Apr < May < Jun < Jul < Aug < ... < Dec
    month(ymd(080101), label = TRUE, abbr = FALSE)
    #> [1] January
    #> 12 Levels: January < February < March < April < May < ... < December
    month(ymd(080101) + months(0:11), label = TRUE)
    #>  [1] Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    #> 12 Levels: Jan < Feb < Mar < Apr < May < Jun < Jul < Aug < ... < Dec