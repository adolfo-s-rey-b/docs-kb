[Skip to content](https://ggplot2.tidyverse.org/reference/hmisc.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

A selection of summary functions from Hmisc
===========================================

Source: [`R/stat-summary.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/stat-summary.R)

`hmisc.Rd`

These are wrappers around functions from Hmisc designed to make them easier to use with `[stat_summary()](https://ggplot2.tidyverse.org/reference/stat_summary.html) `. See the Hmisc documentation for more details:

*   `[Hmisc::smean.cl.boot()](https://rdrr.io/pkg/Hmisc/man/smean.sd.html) `
    
*   `[Hmisc::smean.cl.normal()](https://rdrr.io/pkg/Hmisc/man/smean.sd.html) `
    
*   `[Hmisc::smean.sdl()](https://rdrr.io/pkg/Hmisc/man/smean.sd.html) `
    
*   `[Hmisc::smedian.hilow()](https://rdrr.io/pkg/Hmisc/man/smean.sd.html) `
    

Usage[](https://ggplot2.tidyverse.org/reference/hmisc.html#ref-usage)

----------------------------------------------------------------------

    mean_cl_boot(x, ...)
    
    mean_cl_normal(x, ...)
    
    mean_sdl(x, ...)
    
    median_hilow(x, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/hmisc.html#arguments)

--------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/hmisc.html#arg-x)

a numeric vector

...[](https://ggplot2.tidyverse.org/reference/hmisc.html#arg--)

other arguments passed on to the respective Hmisc function.

Value[](https://ggplot2.tidyverse.org/reference/hmisc.html#value)

------------------------------------------------------------------

A data frame with columns `y`, `ymin`, and `ymax`.

Examples[](https://ggplot2.tidyverse.org/reference/hmisc.html#ref-examples)

----------------------------------------------------------------------------

    if (requireNamespace("Hmisc", quietly = TRUE)) {
    set.seed(1)
    x <- rnorm(100)
    mean_cl_boot(x)
    mean_cl_normal(x)
    mean_sdl(x)
    median_hilow(x)
    }
    #>           y      ymin     ymax
    #> 1 0.1139092 -1.671298 1.797468