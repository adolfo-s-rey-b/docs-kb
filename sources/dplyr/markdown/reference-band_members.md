[Skip to content](https://dplyr.tidyverse.org/reference/band_members.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Band membership
===============

Source: [`R/data-bands.R`](https://github.com/tidyverse/dplyr/blob/main/R/data-bands.R)

`band_members.Rd`

These data sets describe band members of the Beatles and Rolling Stones. They are toy data sets that can be displayed in their entirety on a slide (e.g. to demonstrate a join).

Usage[](https://dplyr.tidyverse.org/reference/band_members.html#ref-usage)

---------------------------------------------------------------------------

    band_members
    
    band_instruments
    
    band_instruments2

Format[](https://dplyr.tidyverse.org/reference/band_members.html#format)

-------------------------------------------------------------------------

Each is a tibble with two variables and three observations

Details[](https://dplyr.tidyverse.org/reference/band_members.html#details)

---------------------------------------------------------------------------

`band_instruments` and `band_instruments2` contain the same data but use different column names for the first column of the data set. `band_instruments` uses `name`, which matches the name of the key column of `band_members`; `band_instruments2` uses `artist`, which does not.

Examples[](https://dplyr.tidyverse.org/reference/band_members.html#ref-examples)

---------------------------------------------------------------------------------

    band_members
    #> # A tibble: 3 × 2
    #>   name  band   
    #>   <chr> <chr>  
    #> 1 Mick  Stones 
    #> 2 John  Beatles
    #> 3 Paul  Beatles
    band_instruments
    #> # A tibble: 3 × 2
    #>   name  plays 
    #>   <chr> <chr> 
    #> 1 John  guitar
    #> 2 Paul  bass  
    #> 3 Keith guitar
    band_instruments2
    #> # A tibble: 3 × 2
    #>   artist plays 
    #>   <chr>  <chr> 
    #> 1 John   guitar
    #> 2 Paul   bass  
    #> 3 Keith  guitar