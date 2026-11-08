[Skip to content](https://ggplot2.tidyverse.org/reference/print.ggproto.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Format or print a ggproto object
================================

Source: [`R/ggproto.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/ggproto.R)

`print.ggproto.Rd`

If a ggproto object has a `$print` method, this will call that method. Otherwise, it will print out the members of the object, and optionally, the members of the inherited objects.

Usage[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#ref-usage)

------------------------------------------------------------------------------

    # S3 method for class 'ggproto'
    print(x, ..., flat = TRUE)
    
    # S3 method for class 'ggproto'
    format(x, ..., flat = TRUE)

Arguments[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#arguments)

----------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#arg-x)

A ggproto object to print.

...[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#arg--)

If the ggproto object has a `print` method, further arguments will be passed to it. Otherwise, these arguments are unused.

flat[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#arg-flat)

If `TRUE` (the default), show a flattened list of all local and inherited members. If `FALSE`, show the inheritance hierarchy.

Examples[](https://ggplot2.tidyverse.org/reference/print.ggproto.html#ref-examples)

------------------------------------------------------------------------------------

    Dog <- ggproto(
      print = function(self, n) {
        cat("Woof!\n")
      }
     )
    Dog
    #> Woof!
    cat(format(Dog), "\n")
    #> <ggproto object: Class gg>
    #>     print: function