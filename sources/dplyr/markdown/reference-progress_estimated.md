[Skip to content](https://dplyr.tidyverse.org/reference/progress_estimated.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Progress bar with estimated time.
=================================

Source: [`R/progress.R`](https://github.com/tidyverse/dplyr/blob/main/R/progress.R)

`progress_estimated.Rd`

[![[Deprecated]](https://dplyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

This progress bar has been deprecated since providing progress bars is not the responsibility of dplyr. Instead, you might try the more powerful [progress](https://github.com/r-lib/progress)
 package.

This reference class represents a text progress bar displayed estimated time remaining. When finished, it displays the total duration. The automatic progress bar can be disabled by setting option `dplyr.show_progress` to `FALSE`.

Usage[](https://dplyr.tidyverse.org/reference/progress_estimated.html#ref-usage)

---------------------------------------------------------------------------------

    progress_estimated(n, min_time = 0)

Arguments[](https://dplyr.tidyverse.org/reference/progress_estimated.html#arguments)

-------------------------------------------------------------------------------------

n[](https://dplyr.tidyverse.org/reference/progress_estimated.html#arg-n)

Total number of items

min\_time[](https://dplyr.tidyverse.org/reference/progress_estimated.html#arg-min-time)

Progress bar will wait until at least `min_time` seconds have elapsed before displaying any results.

Value[](https://dplyr.tidyverse.org/reference/progress_estimated.html#value)

-----------------------------------------------------------------------------

A ref class with methods `tick()`, `[print()](https://rdrr.io/r/base/print.html) `, `pause()`, and `[stop()](https://rdrr.io/r/base/stop.html) `.

Examples[](https://dplyr.tidyverse.org/reference/progress_estimated.html#ref-examples)

---------------------------------------------------------------------------------------

    p <- progress_estimated(3)
    #> Warning: `progress_estimated()` was deprecated in dplyr 1.0.0.
    p$tick()
    p$tick()
    p$tick()
    
    p <- progress_estimated(3)
    #> Warning: `progress_estimated()` was deprecated in dplyr 1.0.0.
    for (i in 1:3) p$pause(0.1)$tick()$print()
    
    p <- progress_estimated(3)
    #> Warning: `progress_estimated()` was deprecated in dplyr 1.0.0.
    p$tick()$print()$
     pause(1)$stop()
    
    # If min_time is set, progress bar not shown until that many
    # seconds have elapsed
    p <- progress_estimated(3, min_time = 3)
    #> Warning: `progress_estimated()` was deprecated in dplyr 1.0.0.
    for (i in 1:3) p$pause(0.1)$tick()$print()
    
    if (FALSE) { # \dontrun{
    p <- progress_estimated(10, min_time = 3)
    for (i in 1:10) p$pause(0.5)$tick()$print()
    } # }