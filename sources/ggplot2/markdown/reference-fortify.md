[Skip to content](https://ggplot2.tidyverse.org/reference/fortify.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Fortify a model with data.
==========================

Source: [`R/fortify.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/fortify.R)

`fortify.Rd`

Rather than using this function, I now recommend using the broom package, which implements a much wider range of methods. `fortify()` may be deprecated in the future.

Usage[](https://ggplot2.tidyverse.org/reference/fortify.html#ref-usage)

------------------------------------------------------------------------

    fortify(model, data, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/fortify.html#arguments)

----------------------------------------------------------------------------

model[](https://ggplot2.tidyverse.org/reference/fortify.html#arg-model)

model or other R object to convert to data frame

data[](https://ggplot2.tidyverse.org/reference/fortify.html#arg-data)

original dataset, if needed

...[](https://ggplot2.tidyverse.org/reference/fortify.html#arg--)

Arguments passed to methods.

See also[](https://ggplot2.tidyverse.org/reference/fortify.html#see-also)

--------------------------------------------------------------------------

`[fortify.lm()](https://ggplot2.tidyverse.org/reference/fortify.lm.html) `

Other plotting automation topics: `[autolayer()](https://ggplot2.tidyverse.org/reference/autolayer.html) `, `[automatic_plotting](https://ggplot2.tidyverse.org/reference/automatic_plotting.html) `, `[autoplot()](https://ggplot2.tidyverse.org/reference/autoplot.html) `