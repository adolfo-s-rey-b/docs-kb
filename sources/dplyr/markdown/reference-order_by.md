[Skip to content](https://dplyr.tidyverse.org/reference/order_by.html#container)

![](https://dplyr.tidyverse.org/logo.png)

A helper function for ordering window function output
=====================================================

Source: [`R/order-by.R`](https://github.com/tidyverse/dplyr/blob/main/R/order-by.R)

`order_by.Rd`

This function makes it possible to control the ordering of window functions in R that don't have a specific ordering parameter. When translated to SQL it will modify the order clause of the OVER function.

Usage[](https://dplyr.tidyverse.org/reference/order_by.html#ref-usage)

-----------------------------------------------------------------------

    order_by(order_by, call)

Arguments[](https://dplyr.tidyverse.org/reference/order_by.html#arguments)

---------------------------------------------------------------------------

order\_by[](https://dplyr.tidyverse.org/reference/order_by.html#arg-order-by)

a vector to order\_by

call[](https://dplyr.tidyverse.org/reference/order_by.html#arg-call)

a function call to a window function, where the first argument is the vector being operated on

Details[](https://dplyr.tidyverse.org/reference/order_by.html#details)

-----------------------------------------------------------------------

This function works by changing the `call` to instead call `[with_order()](https://dplyr.tidyverse.org/reference/with_order.html) ` with the appropriate arguments.

Examples[](https://dplyr.tidyverse.org/reference/order_by.html#ref-examples)

-----------------------------------------------------------------------------

    order_by(10:1, cumsum(1:10))
    #>  [1] 55 54 52 49 45 40 34 27 19 10
    x <- 10:1
    y <- 1:10
    order_by(x, cumsum(y))
    #>  [1] 55 54 52 49 45 40 34 27 19 10
    
    df <- data.frame(year = 2000:2005, value = (0:5) ^ 2)
    scrambled <- df[sample(nrow(df)), ]
    
    wrong <- mutate(scrambled, running = cumsum(value))
    arrange(wrong, year)
    #>   year value running
    #> 1 2000     0       0
    #> 2 2001     1      26
    #> 3 2002     4      39
    #> 4 2003     9      35
    #> 5 2004    16      55
    #> 6 2005    25      25
    
    right <- mutate(scrambled, running = order_by(year, cumsum(value)))
    arrange(right, year)
    #>   year value running
    #> 1 2000     0       0
    #> 2 2001     1       1
    #> 3 2002     4       5
    #> 4 2003     9      14
    #> 5 2004    16      30
    #> 6 2005    25      55