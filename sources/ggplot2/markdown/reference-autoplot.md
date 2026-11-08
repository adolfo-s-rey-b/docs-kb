[Skip to content](https://ggplot2.tidyverse.org/reference/autoplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Create a complete ggplot appropriate to a particular data type
==============================================================

Source: [`R/autoplot.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/autoplot.R)

`autoplot.Rd`

`autoplot()` uses ggplot2 to draw a particular plot for an object of a particular class in a single command. This defines the S3 generic that other classes and packages can extend.

Usage[](https://ggplot2.tidyverse.org/reference/autoplot.html#ref-usage)

-------------------------------------------------------------------------

    autoplot(object, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/autoplot.html#arguments)

-----------------------------------------------------------------------------

object[](https://ggplot2.tidyverse.org/reference/autoplot.html#arg-object)

an object, whose class will determine the behaviour of autoplot

...[](https://ggplot2.tidyverse.org/reference/autoplot.html#arg--)

other arguments passed to specific methods

Value[](https://ggplot2.tidyverse.org/reference/autoplot.html#value)

---------------------------------------------------------------------

a ggplot object

See also[](https://ggplot2.tidyverse.org/reference/autoplot.html#see-also)

---------------------------------------------------------------------------

Other plotting automation topics: `[autolayer()](https://ggplot2.tidyverse.org/reference/autolayer.html) `, `[automatic_plotting](https://ggplot2.tidyverse.org/reference/automatic_plotting.html) `, `[fortify()](https://ggplot2.tidyverse.org/reference/fortify.html) `