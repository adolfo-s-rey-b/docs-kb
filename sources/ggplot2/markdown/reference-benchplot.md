[Skip to content](https://ggplot2.tidyverse.org/reference/benchplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Benchmark plot creation time. Broken down into construct, build, render and draw times.
=======================================================================================

Source: [`R/bench.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/bench.R)

`benchplot.Rd`

Benchmark plot creation time. Broken down into construct, build, render and draw times.

Usage[](https://ggplot2.tidyverse.org/reference/benchplot.html#ref-usage)

--------------------------------------------------------------------------

    benchplot(x)

Arguments[](https://ggplot2.tidyverse.org/reference/benchplot.html#arguments)

------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/benchplot.html#arg-x)

code to create ggplot2 plot

Examples[](https://ggplot2.tidyverse.org/reference/benchplot.html#ref-examples)

--------------------------------------------------------------------------------

    benchplot(ggplot(mtcars, aes(mpg, wt)) + geom_point())
    #>        step user.self sys.self elapsed
    #> 1 construct     0.005        0   0.005
    #> 2     build     0.027        0   0.027
    #> 3    render     0.039        0   0.039
    #> 4      draw     0.020        0   0.020
    #> 5     TOTAL     0.091        0   0.091
    benchplot(ggplot(mtcars, aes(mpg, wt)) + geom_point() + facet_grid(. ~ cyl))
    #>        step user.self sys.self elapsed
    #> 1 construct     0.005        0   0.005
    #> 2     build     0.027        0   0.028
    #> 3    render     0.091        0   0.092
    #> 4      draw     0.035        0   0.035
    #> 5     TOTAL     0.158        0   0.160
    
    # With tidy eval:
    p <- expr(ggplot(mtcars, aes(mpg, wt)) + geom_point())
    benchplot(!!p)
    
    #>        step user.self sys.self elapsed
    #> 1 construct     0.005        0   0.005
    #> 2     build     0.026        0   0.026
    #> 3    render     0.038        0   0.039
    #> 4      draw     0.019        0   0.019
    #> 5     TOTAL     0.088        0   0.089