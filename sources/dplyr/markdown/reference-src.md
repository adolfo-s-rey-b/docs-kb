[Skip to content](https://dplyr.tidyverse.org/reference/src.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Create a "src" object
=====================

Source: [`R/src.R`](https://github.com/tidyverse/dplyr/blob/main/R/src.R)

`src.Rd`

`src()` is the standard constructor for srcs and `is.src()` tests.

Usage[](https://dplyr.tidyverse.org/reference/src.html#ref-usage)

------------------------------------------------------------------

    src(subclass, ...)
    
    is.src(x)

Arguments[](https://dplyr.tidyverse.org/reference/src.html#arguments)

----------------------------------------------------------------------

subclass[](https://dplyr.tidyverse.org/reference/src.html#arg-subclass)

name of subclass. "src" is an abstract base class, so you must supply this value. `src_` is automatically prepended to the class name

...[](https://dplyr.tidyverse.org/reference/src.html#arg--)

fields used by object.

These dots are evaluated with [explicit splicing](https://rlang.r-lib.org/reference/list2.html)
.

x[](https://dplyr.tidyverse.org/reference/src.html#arg-x)

object to test for "src"-ness.