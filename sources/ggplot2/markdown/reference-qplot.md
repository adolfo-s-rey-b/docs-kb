[Skip to content](https://ggplot2.tidyverse.org/reference/qplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Quick plot
==========

Source: [`R/quick-plot.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/quick-plot.R)

`qplot.Rd`

`qplot()` is now deprecated in order to encourage the users to learn `[ggplot()](https://ggplot2.tidyverse.org/reference/ggplot.html) ` as it makes it easier to create complex graphics.

Usage[](https://ggplot2.tidyverse.org/reference/qplot.html#ref-usage)

----------------------------------------------------------------------

    qplot(
      x,
      y,
      ...,
      data,
      facets = NULL,
      margins = FALSE,
      geom = "auto",
      xlim = c(NA, NA),
      ylim = c(NA, NA),
      log = "",
      main = NULL,
      xlab = NULL,
      ylab = NULL,
      asp = NA,
      stat = deprecated(),
      position = deprecated()
    )
    
    quickplot(
      x,
      y,
      ...,
      data,
      facets = NULL,
      margins = FALSE,
      geom = "auto",
      xlim = c(NA, NA),
      ylim = c(NA, NA),
      log = "",
      main = NULL,
      xlab = NULL,
      ylab = NULL,
      asp = NA,
      stat = deprecated(),
      position = deprecated()
    )

Arguments[](https://ggplot2.tidyverse.org/reference/qplot.html#arguments)

--------------------------------------------------------------------------

x, y, ...[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-x-y-)

Aesthetics passed into each layer

data[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-data)

Data frame to use (optional). If not specified, will create one, extracting vectors from the current environment.

facets[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-facets)

faceting formula to use. Picks `[facet_wrap()](https://ggplot2.tidyverse.org/reference/facet_wrap.html) ` or `[facet_grid()](https://ggplot2.tidyverse.org/reference/facet_grid.html) ` depending on whether the formula is one- or two-sided

margins[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-margins)

See `[facet_grid()](https://ggplot2.tidyverse.org/reference/facet_grid.html) `: display marginal facets?

geom[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-geom)

Character vector specifying geom(s) to draw. Defaults to "point" if x and y are specified, and "histogram" if only x is specified.

xlim, ylim[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-xlim-ylim)

X and y axis limits

log[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-log)

Which variables to log transform ("x", "y", or "xy")

main, xlab, ylab[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-main-xlab-ylab)

Character vector (or expression) giving plot title, x axis label, and y axis label respectively.

asp[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-asp)

The y/x aspect ratio

stat, position[](https://ggplot2.tidyverse.org/reference/qplot.html#arg-stat-position)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

Examples[](https://ggplot2.tidyverse.org/reference/qplot.html#ref-examples)

----------------------------------------------------------------------------

    # Use data from data.frame
    qplot(mpg, wt, data = mtcars)
    #> Warning: `qplot()` was deprecated in ggplot2 3.4.0.
    
    qplot(mpg, wt, data = mtcars, colour = cyl)
    
    qplot(mpg, wt, data = mtcars, size = cyl)
    
    qplot(mpg, wt, data = mtcars, facets = vs ~ am)
    
    
    # \donttest{
    set.seed(1)
    qplot(1:10, rnorm(10), colour = runif(10))
    
    qplot(1:10, letters[1:10])
    
    mod <- lm(mpg ~ wt, data = mtcars)
    qplot(resid(mod), fitted(mod))
    
    
    f <- function() {
       a <- 1:10
       b <- a ^ 2
       qplot(a, b)
    }
    f()
    
    
    # To set aesthetics, wrap in I()
    qplot(mpg, wt, data = mtcars, colour = I("red"))
    
    
    # qplot will attempt to guess what geom you want depending on the input
    # both x and y supplied = scatterplot
    qplot(mpg, wt, data = mtcars)
    
    # just x supplied = histogram
    qplot(mpg, data = mtcars)
    #> `stat_bin()` using `bins = 30`. Pick better value `binwidth`.
    
    # just y supplied = scatterplot, with x = seq_along(y)
    qplot(y = mpg, data = mtcars)
    
    
    # Use different geoms
    qplot(mpg, wt, data = mtcars, geom = "path")
    
    qplot(factor(cyl), wt, data = mtcars, geom = c("boxplot", "jitter"))
    
    qplot(mpg, data = mtcars, geom = "dotplot")
    #> Bin width defaults to 1/30 of the range of the data. Pick better value
    #> with `binwidth`.
    
    # }