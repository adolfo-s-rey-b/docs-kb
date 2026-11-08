[Skip to content](https://ggplot2.tidyverse.org/reference/economics.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

US economic time series
=======================

Source: [`R/data.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/data.R)

`economics.Rd`

This dataset was produced from US economic time series data available from [https://fred.stlouisfed.org/](https://fred.stlouisfed.org/)
. `economics` is in "wide" format, `economics_long` is in "long" format.

Usage[](https://ggplot2.tidyverse.org/reference/economics.html#ref-usage)

--------------------------------------------------------------------------

    economics
    
    economics_long

Format[](https://ggplot2.tidyverse.org/reference/economics.html#format)

------------------------------------------------------------------------

A data frame with 574 rows and 6 variables:

date

Month of data collection

pce

personal consumption expenditures, in billions of dollars, [https://fred.stlouisfed.org/series/PCE](https://fred.stlouisfed.org/series/PCE)

pop

total population, in thousands, [https://fred.stlouisfed.org/series/POP](https://fred.stlouisfed.org/series/POP)

psavert

personal savings rate, [https://fred.stlouisfed.org/series/PSAVERT/](https://fred.stlouisfed.org/series/PSAVERT/)

uempmed

median duration of unemployment, in weeks, [https://fred.stlouisfed.org/series/UEMPMED](https://fred.stlouisfed.org/series/UEMPMED)

unemploy

number of unemployed in thousands, [https://fred.stlouisfed.org/series/UNEMPLOY](https://fred.stlouisfed.org/series/UNEMPLOY)

An object of class `tbl_df` (inherits from `tbl`, `data.frame`) with 2870 rows and 4 columns.