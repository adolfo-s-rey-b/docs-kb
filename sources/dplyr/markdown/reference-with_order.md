[Skip to content](https://dplyr.tidyverse.org/reference/with_order.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Run a function with one order, translating result back to original order
========================================================================

Source: [`R/order-by.R`](https://github.com/tidyverse/dplyr/blob/main/R/order-by.R)

`with_order.Rd`

This is used to power the ordering parameters of dplyr's window functions

Usage[](https://dplyr.tidyverse.org/reference/with_order.html#ref-usage)

-------------------------------------------------------------------------

    with_order(order_by, fun, x, ...)

Arguments[](https://dplyr.tidyverse.org/reference/with_order.html#arguments)

-----------------------------------------------------------------------------

order\_by[](https://dplyr.tidyverse.org/reference/with_order.html#arg-order-by)

vector to order by

fun[](https://dplyr.tidyverse.org/reference/with_order.html#arg-fun)

window function

x, ...[](https://dplyr.tidyverse.org/reference/with_order.html#arg-x-)

arguments to `f`