[Skip to content](https://ggplot2.tidyverse.org/reference/autolayer.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Create a ggplot layer appropriate to a particular data type
===========================================================

Source: [`R/autolayer.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/autolayer.R)

`autolayer.Rd`

`autolayer()` uses ggplot2 to draw a particular layer for an object of a particular class in a single command. This defines the S3 generic that other classes and packages can extend.

Usage[](https://ggplot2.tidyverse.org/reference/autolayer.html#ref-usage)

--------------------------------------------------------------------------

    autolayer(object, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/autolayer.html#arguments)

------------------------------------------------------------------------------

object[](https://ggplot2.tidyverse.org/reference/autolayer.html#arg-object)

an object, whose class will determine the behaviour of autolayer

...[](https://ggplot2.tidyverse.org/reference/autolayer.html#arg--)

other arguments passed to specific methods

Value[](https://ggplot2.tidyverse.org/reference/autolayer.html#value)

----------------------------------------------------------------------

a ggplot layer

See also[](https://ggplot2.tidyverse.org/reference/autolayer.html#see-also)

----------------------------------------------------------------------------

Other plotting automation topics: `[automatic_plotting](https://ggplot2.tidyverse.org/reference/automatic_plotting.html) `, `[autoplot()](https://ggplot2.tidyverse.org/reference/autoplot.html) `, `[fortify()](https://ggplot2.tidyverse.org/reference/fortify.html) `